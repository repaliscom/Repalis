import { vi } from 'vitest'
import type { createMockRepalisClient } from './mocks'

type MockRepalisClient = ReturnType<typeof createMockRepalisClient>

vi.mock('@repalis/sdk/2026-10/services/checkouts', () => ({
  createCheckouts: (client: MockRepalisClient) => client.checkouts.create,
  clientUpdateCheckouts: (client: MockRepalisClient) =>
    client.checkouts.clientUpdate,
}))

vi.mock('@repalis/sdk/2026-10/services/customer_sessions', () => ({
  createCustomerSessions: (client: MockRepalisClient) =>
    client.customerSessions.create,
}))

vi.mock('@repalis/sdk/2026-10/services/customers', () => ({
  listCustomers: (client: MockRepalisClient) => client.customers.list,
  createCustomers: (client: MockRepalisClient) => client.customers.create,
  deleteCustomers: (client: MockRepalisClient) => client.customers.delete,
  updateCustomers: (client: MockRepalisClient) => client.customers.update,
  getExternalCustomers: (client: MockRepalisClient) =>
    client.customers.getExternal,
  updateExternalCustomers: (client: MockRepalisClient) =>
    client.customers.updateExternal,
  getStateExternalCustomers: (client: MockRepalisClient) =>
    client.customers.getStateExternal,
}))

vi.mock('@repalis/sdk/2026-10/services/products', () => ({
  getProducts: (client: MockRepalisClient) => client.products.get,
}))

vi.mock('@repalis/sdk/2026-10/services/subscriptions', () => ({
  listSubscriptions: (client: MockRepalisClient) => client.subscriptions.list,
  getSubscriptions: (client: MockRepalisClient) => client.subscriptions.get,
  updateSubscriptions: (client: MockRepalisClient) => client.subscriptions.update,
}))

vi.mock('@repalis/sdk/2026-10/services/customer_seats', () => ({
  listSeatsCustomerSeats: (client: MockRepalisClient) =>
    client.customerSeats.listSeats,
  assignSeatCustomerSeats: (client: MockRepalisClient) =>
    client.customerSeats.assignSeat,
  revokeSeatCustomerSeats: (client: MockRepalisClient) =>
    client.customerSeats.revokeSeat,
}))

vi.mock('@repalis/sdk/2026-10/services/events', () => ({
  ingestEvents: (client: MockRepalisClient) => client.events.ingest,
}))

vi.mock('@repalis/sdk/2026-10/services/customers/members', () => ({
  listExternalMembers: (client: MockRepalisClient) =>
    client.customers.members.listExternal,
  createExternalMembers: (client: MockRepalisClient) =>
    client.customers.members.createExternal,
  getExternalMembers: (client: MockRepalisClient) =>
    client.customers.members.getExternal,
  deleteExternalMembers: (client: MockRepalisClient) =>
    client.customers.members.deleteExternal,
  updateExternalMembers: (client: MockRepalisClient) =>
    client.customers.members.updateExternal,
}))

vi.mock(
  '@repalis/sdk/2026-10/services/customer_portal/benefit_grants',
  () => ({
    listBenefitGrants: (client: MockRepalisClient) =>
      client.customerPortal.benefitGrants.list,
  }),
)

vi.mock('@repalis/sdk/2026-10/services/customer_portal/subscriptions', () => ({
  listSubscriptions: (client: MockRepalisClient) =>
    client.customerPortal.subscriptions.list,
}))

vi.mock('@repalis/sdk/2026-10/services/customer_portal/orders', () => ({
  listOrders: (client: MockRepalisClient) => client.customerPortal.orders.list,
}))

vi.mock(
  '@repalis/sdk/2026-10/services/customer_portal/customer_meters',
  () => ({
    listCustomerMeters: (client: MockRepalisClient) =>
      client.customerPortal.customerMeters.list,
  }),
)
