import type { models } from '@repalis/sdk/2026-10'
import type { User } from 'better-auth'
import type { Member, Organization } from 'better-auth/plugins/organization'

export type RepalisMemberRole = models.MemberRole
export type RepalisNonOwnerMemberRole = Exclude<RepalisMemberRole, 'owner'>

export type BetterAuthOrganizationUser = User & Record<string, unknown>

export interface BetterAuthRoleMappingInput {
  /**
   * Better Auth's raw role value. Multiple roles are comma-separated.
   */
  role: string
  /**
   * Whether this member was selected as Repalis's sole owner.
   */
  isCanonicalOwner: boolean
}

export interface BetterAuthRoleMappingOptions {
  /**
   * Better Auth role used to identify organization owners.
   *
   * @default "owner"
   */
  creatorRole?: string
  /**
   * Better Auth roles that can manage billing in Repalis.
   *
   * @default ["admin"]
   */
  billingManagerRoles?: readonly string[]
}

export interface RepalisOrganizationMemberRoleInput {
  /** Better Auth's raw, potentially comma-separated role value. */
  role: string
  /** Parsed and de-duplicated Better Auth roles. */
  roles: ReadonlySet<string>
  organizationId: string
  user: BetterAuthOrganizationUser
}

export type BetterAuthOrganizationMemberMirror = Pick<
  Member,
  'id' | 'organizationId' | 'userId' | 'role' | 'createdAt'
> & {
  user: BetterAuthOrganizationUser
}

export interface RepalisOrganizationRoleSyncOptions extends BetterAuthRoleMappingOptions {
  mapBetterAuthRoleToRepalisRole?: (
    data: RepalisOrganizationMemberRoleInput,
  ) => RepalisNonOwnerMemberRole | Promise<RepalisNonOwnerMemberRole>
}

export type RepalisOrganizationCustomerCreateParams = Omit<
  models.CustomerTeamCreate,
  'external_id' | 'name' | 'owner' | 'type'
>

export interface SelectSeatProductsForMemberInput {
  organization: Organization & Record<string, unknown>
  member: Member & Record<string, unknown>
  user: BetterAuthOrganizationUser
  products: models.Product[]
}

export type SelectSeatProductsForMember = (
  input: SelectSeatProductsForMemberInput,
) => readonly string[] | Promise<readonly string[]>

/**
 * Experimental Better Auth organization synchronization options.
 *
 * Existing organization billing data is not migrated. Applications that
 * already handle organization billing should not enable this integration.
 *
 * @experimental
 */
export interface RepalisOrganizationOptions {
  /**
   * Enable Better Auth organization to Repalis team-customer synchronization.
   */
  enabled: boolean
  /**
   * Add optional Repalis customer fields such as metadata or billing details.
   * Identity fields are always supplied by the integration and cannot be
   * overridden by this callback.
   */
  getTeamCustomerCreateParams?: (data: {
    organization: Organization & Record<string, unknown>
    owner: User & Record<string, unknown>
  }) => Promise<RepalisOrganizationCustomerCreateParams>
  /**
   * Map non-canonical Better Auth members to a Repalis billing role.
   *
   * Ownership is intentionally not exposed: the adapter alone selects Repalis's
   * single canonical owner. Return `member` or `billing_manager` only.
   */
  mapBetterAuthRoleToRepalisRole?: (
    data: RepalisOrganizationMemberRoleInput,
  ) => RepalisNonOwnerMemberRole | Promise<RepalisNonOwnerMemberRole>
  /**
   * Automatically synchronize recurring seat-based subscriptions with the
   * Better Auth organization roster.
   *
   * @default false
   */
  syncSeats?: boolean
  /**
   * Select the recurring seat-based products assigned to each member when
   * `syncSeats` is enabled.
   *
   * When omitted, every organization member receives every candidate
   * recurring seat-based product.
   */
  selectSeatProductsForMember?: SelectSeatProductsForMember
}
