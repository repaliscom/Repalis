import { vi } from 'vitest'
import type { RepalisOptions } from '../../types'
import { createMockRepalisClient } from './mocks'

export const createTestRepalisOptions = (
  overrides: Partial<RepalisOptions> = {},
): RepalisOptions => ({
  client: createMockRepalisClient(),
  createCustomerOnSignUp: true,
  use: [] as any,
  ...overrides,
})

export { createMockRepalisClient }

export const mockApiError = (status: number, message: string) => {
  const error = new Error(message) as any
  error.status = status
  error.response = {
    status,
    data: { error: { message } },
  }
  return error
}

export const mockApiResponse = <T>(data: T) => Promise.resolve({ data })

export const createMockMiddleware = (): ReturnType<typeof vi.fn> => {
  const middleware = vi.fn()
  middleware.mockImplementation((context, next) => next())
  return middleware
}
