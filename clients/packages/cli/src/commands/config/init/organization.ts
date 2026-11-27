import { Effect } from 'effect'
import { announceAuthorization } from '@/commands/auth'
import { AuthError, loginCommand, type RepalisEnvironment } from '@/schemas/Auth'
import { Auth } from '@/services/auth'
import { Organizations } from '@/services/organizations'
import { select } from '@/utils/prompt'

type EnvironmentFlags = Record<RepalisEnvironment, boolean>

const chosenEnvironment = (flags: EnvironmentFlags) => {
  const chosen = (Object.keys(flags) as RepalisEnvironment[]).filter(
    (environment) => flags[environment],
  )
  if (chosen.length > 1) {
    return Effect.fail(
      new AuthError({ message: 'Pass only one environment flag.' }),
    )
  }
  return Effect.succeed(chosen[0])
}

const pickEnvironment = select<RepalisEnvironment>(
  {
    message: 'Which environment do you want to set up?',
    choices: [
      { title: 'Sandbox', value: 'sandbox', description: 'sandbox.repalis.com' },
      { title: 'Production', value: 'production', description: 'repalis.com' },
    ],
  },
  (environment) => environment,
)

const pickOrganization = (environment: RepalisEnvironment, prompt: boolean) =>
  Effect.gen(function* () {
    const items = yield* (yield* Organizations).list(environment)
    if (items.length === 1) return items[0]!
    if (items.length === 0) {
      return yield* new AuthError({
        message: `No organizations in ${environment} yet. Create one in the dashboard, then run repalis config init again.`,
      })
    }
    if (!prompt) {
      return yield* new AuthError({
        message: `Pass --org <slug> to choose one of ${items.map((item) => item.slug).join(', ')}.`,
      })
    }
    return yield* select(
      {
        message: `Which ${environment} organization do you want to set up?`,
        choices: items.map((item) => ({
          value: item,
          title: item.name,
          description: item.slug,
        })),
      },
      (item) => item.name,
    )
  })

const notLoggedIn = (environment?: RepalisEnvironment) =>
  new AuthError({
    message:
      environment === undefined
        ? `Not logged in. Run ${loginCommand('sandbox')} or ${loginCommand('production')} first.`
        : `Not logged in to ${environment}. Run ${loginCommand(environment)} first.`,
  })

const login = (environment: RepalisEnvironment) =>
  Effect.gen(function* () {
    yield* (yield* Auth).login(
      environment,
      false,
      announceAuthorization(environment),
    )
    return environment
  })

const ensureSession = (environment: RepalisEnvironment, prompt: boolean) =>
  Effect.gen(function* () {
    const auth = yield* Auth
    if (yield* auth.override) return
    if ((yield* auth.environments).includes(environment)) return
    if (!prompt) return yield* notLoggedIn(environment)
    yield* login(environment)
  })

export const resolveOrganization = (
  flags: EnvironmentFlags,
  reference: string | undefined,
  prompt: boolean,
) =>
  Effect.gen(function* () {
    const organizations = yield* Organizations
    const environment = yield* chosenEnvironment(flags)
    if (environment !== undefined) {
      yield* ensureSession(environment, prompt)
      return reference === undefined
        ? yield* pickOrganization(environment, prompt)
        : yield* organizations.resolve(reference, environment)
    }
    if (reference !== undefined) return yield* organizations.resolve(reference)
    const auth = yield* Auth
    if ((yield* auth.environments).length === 0 && !(yield* auth.override)) {
      if (!prompt) return yield* notLoggedIn()
      return yield* pickOrganization(
        yield* login(yield* pickEnvironment),
        prompt,
      )
    }
    return yield* organizations.resolve()
  })
