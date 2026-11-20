import type { RepalisCore } from '@repalis/sdk/2026-10'

import type { UnionToIntersection, User } from 'better-auth'
import type { RepalisOrganizationOptions } from './organization/types'
import type { checkout } from './plugins/checkout'
import type { portal } from './plugins/portal'
import type { usage } from './plugins/usage'
import type { webhooks } from './plugins/webhooks'

export type Product = {
  /**
   * Product Id from Repalis Product
   */
  productId: string
  /**
   * Easily identifiable slug for the product
   */
  slug: string
}

export type PolarPlugin = (
  client: RepalisCore,
  options?: RepalisOptions,
) => ReturnType<
  | ReturnType<typeof checkout>
  | ReturnType<typeof usage>
  | ReturnType<typeof portal>
  | ReturnType<typeof webhooks>
>

export type PolarPlugins = [PolarPlugin, ...PolarPlugin[]]

export type PolarEndpoints = UnionToIntersection<ReturnType<PolarPlugin>>

export interface RepalisOptions {
  /**
   * Polar core client created with createRepalisCore
   */
  client: RepalisCore
  /**
   * Create a Repalis customer after the user is inserted, with external_id set to user.id
   */
  createCustomerOnSignUp?: boolean
  /**
   * Additional metadata for new customers, evaluated after user creation.
   * The user ID, email, and name cannot be overridden.
   */
  getCustomerCreateParams?: (
    data: {
      user: Partial<User>
    },
    request?: Request,
  ) => Promise<{
    metadata?: Record<string, string | number | boolean>
  }>
  /**
   * EXPERIMENTAL: Mirror Better Auth organizations to Repalis team customers.
   *
   * Do not enable this for applications that already handle organization
   * billing. Existing billing data is not migrated and can become inconsistent
   * with the newly synchronized Polar team customer.
   *
   * Organization support is disabled when omitted.
   */
  experimental_organizationSync?: RepalisOrganizationOptions
  /**
   * Use Polar plugins
   */
  use: PolarPlugins
}
