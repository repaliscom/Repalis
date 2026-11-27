import { NextRequest } from 'next/server'
import { afterEach, describe, expect, it, vi } from 'vitest'
import { Checkout } from './checkout/checkout'
import { CustomerPortal } from './customerPortal/customerPortal'

afterEach(() => vi.unstubAllGlobals())

describe('SDK transport', () => {
  it('creates a checkout through the core client with sandbox authentication', async () => {
    const fetch = vi
      .fn()
      .mockResolvedValue(
        Response.json({ url: 'https://sandbox.repalis.com/checkout/123' }),
      )
    vi.stubGlobal('fetch', fetch)

    const response = await Checkout({
      accessToken: 'test-token',
      environment: 'sandbox',
    })(new NextRequest('https://example.com/checkout?products=product-123'))

    const [url, init] = fetch.mock.calls[0]!
    expect(url).toBe('https://sandbox-api.repalis.com/v1/checkouts/')
    expect(init.method).toBe('POST')
    expect(new Headers(init.headers).get('Authorization')).toBe(
      'Bearer test-token',
    )
    expect(JSON.parse(init.body)).toEqual({ products: ['product-123'] })
    expect(response.headers.get('location')).toBe(
      'https://sandbox.repalis.com/checkout/123',
    )
  })

  it('creates a portal session using the external customer ID', async () => {
    const fetch = vi
      .fn()
      .mockResolvedValue(
        Response.json({ customer_portal_url: 'https://repalis.com/portal/123' }),
      )
    vi.stubGlobal('fetch', fetch)

    const response = await CustomerPortal({
      accessToken: 'test-token',
      getExternalCustomerId: async () => 'user-123',
      returnUrl: 'https://example.com/account',
    })(new NextRequest('https://example.com/portal'))

    const [url, init] = fetch.mock.calls[0]!
    expect(url).toBe('https://api.repalis.com/v1/customer-sessions/')
    expect(JSON.parse(init.body)).toEqual({
      external_customer_id: 'user-123',
      return_url: 'https://example.com/account',
    })
    expect(response.headers.get('location')).toBe('https://repalis.com/portal/123')
  })
})
