import {
  updateExternalCustomers,
  createCustomers,
  deleteExternalCustomers,
  updateCustomers,
  listCustomers,
} from '@repalis/sdk/2026-10/services/customers'
import type { AuthContext, GenericEndpointContext, User } from 'better-auth'
import { APIError } from 'better-auth/api'
import {
  synchronizeUserDeletionMemberships,
  synchronizeUserOrganizationProfiles,
} from '../organization/lifecycle'
import type { RepalisOptions } from '../types'

const isAnonymousUser = (user: Partial<User>) =>
  'isAnonymous' in user && user.isAnonymous === true

export const onAfterUserCreate =
  (options: RepalisOptions) =>
  async (user: User, context: GenericEndpointContext | null) => {
    if (!context || !options.createCustomerOnSignUp || isAnonymousUser(user)) {
      return
    }

    try {
      const existingCustomers = await listCustomers(options.client)({
        email: user.email,
      })
      const existingCustomer = existingCustomers.items.find(
        (c) => c.type === 'individual',
      )

      if (existingCustomer) {
        if (existingCustomer.external_id === user.id) {
          return
        }
        if (existingCustomer.external_id !== null) {
          throw new APIError('CONFLICT', {
            message: 'Repalis customer is already linked to a different user',
          })
        }
        await updateCustomers(options.client)(existingCustomer.id, {
          external_id: user.id,
        })
        return
      }

      if (existingCustomers.items.some((c) => c.type === 'team')) {
        throw new APIError('CONFLICT', {
          message: 'A team customer with this email already exists',
        })
      }

      const params = options.getCustomerCreateParams
        ? await options.getCustomerCreateParams({ user })
        : {}

      await createCustomers(options.client)({
        ...params,
        email: user.email,
        name: user.name,
        external_id: user.id,
      })
    } catch (e: unknown) {
      if (e instanceof APIError) {
        throw e
      }
      throw new APIError('INTERNAL_SERVER_ERROR', {
        message: `Repalis customer creation failed. Error: ${e instanceof Error ? e.message : e}`,
      })
    }
  }

export const onUserUpdate =
  (options: RepalisOptions, initContext?: AuthContext) =>
  async (user: User, context: GenericEndpointContext | null) => {
    // Preserve the existing personal-customer behavior, including its
    // best-effort error handling, independently from organization support.
    if (context && options.createCustomerOnSignUp) {
      try {
        if (!isAnonymousUser(user)) {
          await updateExternalCustomers(options.client)(user.id, {
            email: user.email,
            name: user.name,
          })
        }
      } catch (e: unknown) {
        if (e instanceof Error) {
          context.context.logger.error(
            `Repalis customer update failed. Error: ${e.message}`,
          )
        } else {
          context.context.logger.error(
            `Repalis customer update failed. Error: ${e}`,
          )
        }
      }
    }

    if (!options.experimental_organizationSync?.enabled) {
      return
    }

    const authContext = context?.context ?? initContext

    if (!authContext) {
      throw new Error(
        'Repalis organization profile synchronization requires a Better Auth context',
      )
    }

    await synchronizeUserOrganizationProfiles(
      authContext,
      options.client,
      user,
      options.experimental_organizationSync,
    )
  }

/**
 * Membership rows are still queryable here. Better Auth may cascade them
 * before the user `after` hook runs, so organization cleanup cannot move later.
 */
export const onBeforeUserDelete =
  (options: RepalisOptions, initContext?: AuthContext) =>
  async (user: User, context: GenericEndpointContext | null) => {
    if (!options.experimental_organizationSync?.enabled) {
      return
    }
    const authContext = context?.context ?? initContext
    if (!authContext) {
      throw new Error(
        'Repalis organization member deletion requires a Better Auth context',
      )
    }
    await synchronizeUserDeletionMemberships(
      authContext,
      options.client,
      user,
      options.experimental_organizationSync,
    )
  }

export const onUserDelete =
  (options: RepalisOptions) =>
  async (user: User, context: GenericEndpointContext | null) => {
    if (context && options.createCustomerOnSignUp) {
      try {
        if (isAnonymousUser(user)) {
          return
        }

        await deleteExternalCustomers(options.client)(user.id)
      } catch (e: unknown) {
        if (e instanceof Error) {
          context?.context.logger.error(
            `Repalis customer delete failed. Error: ${e.message}`,
          )
          return
        }
        context?.context.logger.error(
          `Repalis customer delete failed. Error: ${e}`,
        )
      }
    }
  }
