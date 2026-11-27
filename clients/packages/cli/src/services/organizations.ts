import { Context, Effect, Layer } from 'effect'
import {
  AuthError,
  orgCommand,
  type ActiveOrganization,
  type OrganizationSelection,
  type RepalisEnvironment,
} from '@/schemas/Auth'
import { Auth } from '@/services/auth'
import { CLIConfig } from '@/services/config'
import { Repalis } from '@/services/repalis'

export class Organizations extends Context.Service<
  Organizations,
  {
    list: (
      environment: RepalisEnvironment,
    ) => Effect.Effect<ActiveOrganization[], AuthError>
    listAll: Effect.Effect<ActiveOrganization[], AuthError>
    selected: Effect.Effect<OrganizationSelection | undefined, AuthError>
    select: (selection: OrganizationSelection) => Effect.Effect<void, AuthError>
    resolve: (
      id?: string,
      environment?: RepalisEnvironment,
    ) => Effect.Effect<ActiveOrganization, AuthError>
  }
>()('Organizations') {}

const isUuid = (value: string) =>
  /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(value)

export const layer = Layer.effect(
  Organizations,
  Effect.gen(function* () {
    const repalis = yield* Repalis
    const auth = yield* Auth
    const config = yield* CLIConfig
    const list = (environment: RepalisEnvironment) =>
      Effect.gen(function* () {
        const organizations: ActiveOrganization[] = []
        let page = 1
        while (true) {
          const response = yield* repalis.use(
            (client) => client.organizations.list({ page, limit: 100 }),
            environment,
          )
          organizations.push(
            ...response.items.map(({ id, name, slug }) => ({
              id,
              name,
              slug,
              environment,
            })),
          )
          if (page >= response.pagination.max_page) break
          page++
        }
        return organizations
      })
    const listAll = Effect.gen(function* () {
      const organizations: ActiveOrganization[] = []
      for (const environment of yield* auth.environments) {
        organizations.push(...(yield* list(environment)))
      }
      return organizations
    })
    const get = (id: string, environment: RepalisEnvironment) =>
      Effect.map(
        repalis.use((client) => client.organizations.get(id), environment, {
          organizationId: id,
        }),
        (organization) => ({
          id: organization.id,
          name: organization.name,
          slug: organization.slug,
          environment,
        }),
      )
    const getBySlug = (slug: string, environment: RepalisEnvironment) =>
      Effect.gen(function* () {
        const response = yield* repalis.use(
          (client) => client.organizations.list({ slug, limit: 1 }),
          environment,
        )
        const organization = response.items[0]
        if (organization === undefined) {
          return yield* new AuthError({
            message: `No organization with the slug ${slug} in ${environment}.`,
          })
        }
        return {
          id: organization.id,
          name: organization.name,
          slug: organization.slug,
          environment,
        }
      })
    const find = (reference: string, environment?: RepalisEnvironment) =>
      Effect.gen(function* () {
        const lookup = isUuid(reference) ? get : getBySlug
        if (environment !== undefined)
          return yield* lookup(reference, environment)
        const available = yield* auth.environments
        if (available.length === 0) {
          return yield* new AuthError({
            message:
              'Not logged in. Run repalis auth login or set REPALIS_ACCESS_TOKEN.',
          })
        }
        if (available.length === 1)
          return yield* lookup(reference, available[0]!)
        const matches: ActiveOrganization[] = []
        for (const environment of available) {
          const found = yield* lookup(reference, environment).pipe(
            Effect.orElseSucceed(() => undefined),
          )
          if (found === undefined) continue
          if (isUuid(reference)) return found
          matches.push(found)
        }
        if (matches.length === 1) return matches[0]!
        if (matches.length > 1) {
          return yield* new AuthError({
            message: `${reference} is an organization in ${matches.map((match) => match.environment).join(' and ')}. Pass its ID instead; repalis auth list shows it.`,
          })
        }
        return yield* new AuthError({
          message: `Organization ${reference} is missing or inaccessible in ${available.join(' and ')}. Check --org or run repalis auth list.`,
        })
      })
    return Organizations.of({
      list,
      listAll,
      selected: Effect.gen(function* () {
        if (yield* auth.override) return undefined
        return yield* config.getActiveOrganization
      }),
      select: (selection) =>
        Effect.gen(function* () {
          if (yield* auth.override)
            return yield* new AuthError({
              message: 'Unset REPALIS_ACCESS_TOKEN to manage saved sessions.',
            })
          yield* auth.resolve(selection.environment)
          yield* config.setActiveOrganization(selection)
        }),
      resolve: (id, environment) =>
        Effect.gen(function* () {
          if (id !== undefined) {
            if (id.trim() === '') {
              return yield* new AuthError({
                message: 'The organization is empty. Pass its ID or slug.',
              })
            }
            return yield* find(id, environment)
          }
          if (yield* auth.override) {
            const organizations = yield* listAll
            if (organizations.length === 1) return organizations[0]!
            return yield* new AuthError({
              message:
                'REPALIS_ACCESS_TOKEN has no unique active organization. Supply --org <id> for an accessible organization.',
            })
          }
          const selection = yield* config.getActiveOrganization
          if (!selection) {
            return yield* new AuthError({
              message: `No active organization. Run repalis auth list to see yours, then ${orgCommand} <id> or pass --org <id>.`,
            })
          }
          return yield* get(selection.id, selection.environment).pipe(
            Effect.mapError((error) =>
              error.statusCode === 404
                ? new AuthError({
                    statusCode: 404,
                    message: `The selected organization is missing or inaccessible in ${selection.environment}. Run ${orgCommand} to pick another one.`,
                  })
                : error,
            ),
          )
        }),
    })
  }),
)
