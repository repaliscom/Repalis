import {
  createExternalMembers,
  deleteExternalMembers,
  updateExternalMembers,
  listExternalMembers,
  getExternalMembers,
} from '@repalis/sdk/2026-10/services/customers/members'
import {
  updateExternalCustomers,
  getExternalCustomers,
  createCustomers,
} from '@repalis/sdk/2026-10/services/customers'
import { errors, type models, type RepalisCore } from '@repalis/sdk/2026-10'
import type { Organization } from 'better-auth/plugins/organization'
import {
  DEFAULT_BETTER_AUTH_CREATOR_ROLE,
  hasBetterAuthCreatorRole,
  mapBetterAuthRoleToRepalis,
  parseBetterAuthRoles,
} from './roles'
import type {
  BetterAuthOrganizationMemberMirror,
  BetterAuthOrganizationUser,
  RepalisMemberRole,
  RepalisNonOwnerMemberRole,
  RepalisOrganizationOptions,
  RepalisOrganizationRoleSyncOptions,
} from './types'

type RepalisOrganizationCustomerData = Parameters<
  NonNullable<RepalisOrganizationOptions['getTeamCustomerCreateParams']>
>[0]

export class RepalisOrganizationCustomerTypeError extends Error {
  constructor(externalCustomerId: string) {
    super(
      `Repalis customer with external ID "${externalCustomerId}" is not a team customer`,
    )
    this.name = 'RepalisOrganizationCustomerTypeError'
  }
}

export class RepalisOrganizationTeamCustomerNotFoundError extends Error {
  constructor(organizationId: string) {
    super(
      `Repalis team customer with external ID "${organizationId}" was not found`,
    )
    this.name = 'RepalisOrganizationTeamCustomerNotFoundError'
  }
}

export class RepalisOrganizationOwnerInvariantError extends Error {
  constructor(organizationId: string, detail: string) {
    super(
      `Cannot synchronize Repalis owner for organization "${organizationId}": ${detail}`,
    )
    this.name = 'RepalisOrganizationOwnerInvariantError'
  }
}

export class RepalisOrganizationMemberRoleMappingError extends Error {
  constructor(role: unknown) {
    super(
      `Repalis organization member role mapper returned ${JSON.stringify(role)}; expected "member" or "billing_manager"`,
    )
    this.name = 'RepalisOrganizationMemberRoleMappingError'
  }
}

const assertTeamCustomer = (
  customer: models.Customer,
  externalCustomerId: string,
) => {
  if (customer.type !== 'team') {
    throw new RepalisOrganizationCustomerTypeError(externalCustomerId)
  }
}

const isExternalIdConflict = (
  error: unknown,
  externalCustomerId: string,
): boolean =>
  error instanceof errors.HTTPValidationError &&
  error.statusCode === 422 &&
  Boolean(
    error.error.detail?.some(
      (detail) =>
        detail.type === 'value_error' &&
        detail.loc.length === 2 &&
        detail.loc[0] === 'body' &&
        detail.loc[1] === 'external_id' &&
        detail.input === externalCustomerId,
    ),
  )

const findTeamCustomer = async (
  client: RepalisCore,
  externalCustomerId: string,
): Promise<models.Customer | null> => {
  try {
    const customer = await getExternalCustomers(client)(externalCustomerId)
    assertTeamCustomer(customer, externalCustomerId)
    return customer
  } catch (error) {
    if (error instanceof errors.ResourceNotFound) {
      return null
    }
    throw error
  }
}

export const isTeamCustomerSynchronized = async (
  client: RepalisCore,
  externalCustomerId: string,
): Promise<boolean> =>
  (await findTeamCustomer(client, externalCustomerId)) !== null

export const ensureTeamCustomer = async (
  client: RepalisCore,
  organizationOptions: RepalisOrganizationOptions,
  data: RepalisOrganizationCustomerData,
) => {
  const existingCustomer = await findTeamCustomer(client, data.organization.id)

  if (existingCustomer) {
    return
  }

  const customParams = organizationOptions.getTeamCustomerCreateParams
    ? await organizationOptions.getTeamCustomerCreateParams(data)
    : {}

  try {
    await createCustomers(client)({
      ...customParams,
      external_id: data.organization.id,
      name: data.organization.name,
      owner: {
        external_id: data.owner.id,
        email: data.owner.email,
        name: data.owner.name,
      },
      type: 'team',
    })
  } catch (error) {
    if (!isExternalIdConflict(error, data.organization.id)) {
      throw error
    }

    const racedCustomer = await findTeamCustomer(client, data.organization.id)
    if (!racedCustomer) {
      throw error
    }
  }
}

export const updateTeamCustomer = async (
  client: RepalisCore,
  organization: Organization & Record<string, unknown>,
) => {
  const updatedCustomer = await updateExternalCustomers(client)(
    organization.id,
    { name: organization.name },
  )
  assertTeamCustomer(updatedCustomer, organization.id)
}

const findMember = async (
  client: RepalisCore,
  organizationId: string,
  externalMemberId: string,
): Promise<models.Member | null> => {
  try {
    return await getExternalMembers(client)(organizationId, externalMemberId)
  } catch (error) {
    if (error instanceof errors.ResourceNotFound) {
      return null
    }
    throw error
  }
}

type MemberRoleData = Pick<
  BetterAuthOrganizationMemberMirror,
  'role' | 'user' | 'userId'
>

const ensureMemberRecord = async (
  client: RepalisCore,
  organizationId: string,
  member: MemberRoleData,
  role: RepalisNonOwnerMemberRole,
): Promise<void> => {
  const existingMember = await findMember(client, organizationId, member.userId)

  if (existingMember) {
    return
  }

  await createExternalMembers(client)(organizationId, {
    external_id: member.userId,
    email: member.user.email,
    name: member.user.name,
    role,
  })
}

const resolveNonOwnerRole = async (
  options: RepalisOrganizationRoleSyncOptions,
  organizationId: string,
  member: MemberRoleData,
): Promise<RepalisNonOwnerMemberRole> => {
  if (!options.mapBetterAuthRoleToRepalisRole) {
    const role = mapBetterAuthRoleToRepalis(
      { role: member.role, isCanonicalOwner: false },
      options,
    )
    if (role === 'owner') {
      throw new RepalisOrganizationMemberRoleMappingError(role)
    }
    return role
  }

  const role = await options.mapBetterAuthRoleToRepalisRole({
    role: member.role,
    roles: parseBetterAuthRoles(member.role),
    organizationId,
    user: member.user,
  })
  if (role !== 'member' && role !== 'billing_manager') {
    throw new RepalisOrganizationMemberRoleMappingError(role)
  }
  return role
}

export const byEarliestMembership = (
  left: Pick<BetterAuthOrganizationMemberMirror, 'id' | 'createdAt'>,
  right: Pick<BetterAuthOrganizationMemberMirror, 'id' | 'createdAt'>,
): number => {
  const createdAtDifference =
    left.createdAt.getTime() - right.createdAt.getTime()
  if (createdAtDifference !== 0) return createdAtDifference
  if (left.id < right.id) return -1
  if (left.id > right.id) return 1
  return 0
}

const updateMemberRole = async (
  client: RepalisCore,
  organizationId: string,
  externalMemberId: string,
  role: RepalisMemberRole,
) => {
  await updateExternalMembers(client)(organizationId, externalMemberId, {
    role,
  })
}

const getCurrentRepalisOwner = async (
  client: RepalisCore,
  organizationId: string,
): Promise<models.Member> => {
  const customer = await findTeamCustomer(client, organizationId)
  if (!customer) {
    throw new RepalisOrganizationTeamCustomerNotFoundError(organizationId)
  }

  const ownerPage = await listExternalMembers(client)(organizationId, {
    role: 'owner',
    limit: 100,
  })

  const repalisOwners = ownerPage.items
  if (repalisOwners.length !== 1) {
    throw new RepalisOrganizationOwnerInvariantError(
      organizationId,
      `Repalis returned ${repalisOwners.length} owners`,
    )
  }

  const currentOwner = repalisOwners[0]
  if (!currentOwner?.external_id) {
    throw new RepalisOrganizationOwnerInvariantError(
      organizationId,
      'the current Repalis owner has no external ID',
    )
  }
  return currentOwner
}

/** Transfer ownership only when the current Repalis owner is no longer a Better Auth owner. */
const syncOwnerTransfer = async (
  client: RepalisCore,
  options: RepalisOrganizationRoleSyncOptions,
  data: {
    organizationId: string
    members: readonly BetterAuthOrganizationMemberMirror[]
  },
) => {
  const creatorRole = options.creatorRole ?? DEFAULT_BETTER_AUTH_CREATOR_ROLE
  const ownerCandidates = data.members
    .filter((member) => hasBetterAuthCreatorRole(member.role, creatorRole))
    .sort(byEarliestMembership)
  const fallbackOwner = ownerCandidates[0]
  if (!fallbackOwner) {
    throw new RepalisOrganizationOwnerInvariantError(
      data.organizationId,
      `Better Auth has no member with creator role "${creatorRole}"`,
    )
  }

  const currentOwner = await getCurrentRepalisOwner(client, data.organizationId)

  const retainedOwner = ownerCandidates.find(
    (candidate) => candidate.userId === currentOwner.external_id,
  )

  if (retainedOwner) {
    return { canonicalOwner: retainedOwner, currentOwner, transferred: false }
  }

  const successor = await findMember(
    client,
    data.organizationId,
    fallbackOwner.userId,
  )
  if (!successor) {
    throw new RepalisOrganizationOwnerInvariantError(
      data.organizationId,
      `successor "${fallbackOwner.userId}" is not a Repalis member`,
    )
  }
  await updateMemberRole(
    client,
    data.organizationId,
    fallbackOwner.userId,
    'owner',
  )

  // Repalis automatically demotes the previous owner to billing manager. If the
  // previous owner remains in Better Auth and maps to `member`, apply that
  // explicit role as part of this transfer.
  const previousOwner = data.members.find(
    (member) => member.userId === currentOwner.external_id,
  )

  if (previousOwner) {
    const previousOwnerRole = await resolveNonOwnerRole(
      options,
      data.organizationId,
      previousOwner,
    )

    if (previousOwnerRole !== 'billing_manager') {
      await updateMemberRole(
        client,
        data.organizationId,
        previousOwner.userId,
        previousOwnerRole,
      )
    }
  }

  return { canonicalOwner: fallbackOwner, currentOwner, transferred: true }
}

export const ensureMemberMirror = async (
  client: RepalisCore,
  options: RepalisOrganizationRoleSyncOptions,
  data: {
    organizationId: string
    user: BetterAuthOrganizationUser
    betterAuthRole: string
  },
) => {
  const customer = await findTeamCustomer(client, data.organizationId)
  if (!customer) {
    throw new RepalisOrganizationTeamCustomerNotFoundError(data.organizationId)
  }

  const member = {
    role: data.betterAuthRole,
    userId: data.user.id,
    user: data.user,
  }
  const role = await resolveNonOwnerRole(options, data.organizationId, member)
  await ensureMemberRecord(client, data.organizationId, member, role)
}

export const updateMemberRoleMirror = async (
  client: RepalisCore,
  options: RepalisOrganizationRoleSyncOptions,
  data: {
    organizationId: string
    user: BetterAuthOrganizationUser
    betterAuthRole: string
    members: readonly BetterAuthOrganizationMemberMirror[]
  },
) => {
  const ownership = await syncOwnerTransfer(client, options, {
    organizationId: data.organizationId,
    members: data.members,
  })

  if (
    data.user.id === ownership.canonicalOwner.userId ||
    (ownership.transferred &&
      data.user.id === ownership.currentOwner.external_id)
  ) {
    return
  }

  const member = {
    role: data.betterAuthRole,
    userId: data.user.id,
    user: data.user,
  }

  const role = await resolveNonOwnerRole(options, data.organizationId, member)

  await updateMemberRole(client, data.organizationId, data.user.id, role)
}

export const updateMemberMirror = async (
  client: RepalisCore,
  data: {
    organizationId: string
    user: BetterAuthOrganizationUser
  },
) => {
  await updateExternalMembers(client)(data.organizationId, data.user.id, {
    email: data.user.email,
    name: data.user.name,
  })
}

export const promoteMemberMirrorToOwner = async (
  client: RepalisCore,
  data: {
    organizationId: string
    externalMemberId: string
  },
) => {
  const repalisSuccessor = await findMember(
    client,
    data.organizationId,
    data.externalMemberId,
  )
  if (!repalisSuccessor) {
    throw new RepalisOrganizationOwnerInvariantError(
      data.organizationId,
      `successor "${data.externalMemberId}" is not a Repalis member`,
    )
  }
  await updateMemberRole(
    client,
    data.organizationId,
    data.externalMemberId,
    'owner',
  )
}

export const removeMemberMirror = async (
  client: RepalisCore,
  data: {
    organizationId: string
    externalMemberId: string
  },
) => {
  try {
    await deleteExternalMembers(client)(
      data.organizationId,
      data.externalMemberId,
    )
  } catch (error) {
    if (error instanceof errors.ResourceNotFound) return

    throw error
  }
}
