import { afterEach, expect, test, vi } from 'vitest'
import { Effect, Redacted } from 'effect'
import type { Repalis as RepalisSDK } from '@repalis/sdk/2026-10'
import { AuthError, type RepalisEnvironment } from '@/schemas/Auth'
import { UsedEnvironments } from '@/services/api'
import { Auth, type Credential } from '@/services/auth'
import { make } from '@/services/repalis'
import {
  fakeAuth,
  keyringCredential,
  overrideCredential,
} from '@/utils/test-utils/services'

type Resolve = (
  environment: RepalisEnvironment,
  rejected?: Redacted.Redacted<string>,
) => Effect.Effect<Credential, AuthError>

const repalisWith = (resolve: Resolve) =>
  Effect.runPromise(
    make.pipe(
      Effect.provideService(Auth, Auth.of({ ...fakeAuth().auth, resolve })),
    ),
  )

afterEach(() => {
  vi.unstubAllGlobals()
  vi.restoreAllMocks()
})

test('notes the environment even when there is no saved session', async () => {
  const used = new Set<RepalisEnvironment>()
  const repalis = await repalisWith(() =>
    Effect.fail(new AuthError({ message: 'Not logged in to production.' })),
  )
  await Effect.runPromise(
    repalis
      .use(() => Promise.resolve('unreachable'), 'production')
      .pipe(Effect.provideService(UsedEnvironments, used), Effect.flip),
  )
  expect([...used]).toEqual(['production'])
})

test('retries a rejected saved token with refreshed credentials in the same environment', async () => {
  const saved = keyringCredential('saved-token')
  const resolve = vi
    .fn<Resolve>()
    .mockReturnValueOnce(Effect.succeed(saved))
    .mockReturnValueOnce(Effect.succeed(keyringCredential('refreshed-token')))
  const repalis = await repalisWith(resolve)
  const organization = { id: 'org-1', name: 'First', slug: 'first' }
  const fetch = vi
    .fn<typeof globalThis.fetch>()
    .mockResolvedValueOnce(
      Response.json({ detail: 'Unauthorized' }, { status: 401 }),
    )
    .mockResolvedValueOnce(Response.json(organization))
  vi.stubGlobal('fetch', fetch)

  expect(
    await Effect.runPromise(
      repalis.use((client) => client.organizations.get('org-1'), 'production'),
    ),
  ).toEqual(organization)
  expect(resolve.mock.calls).toEqual([
    ['production'],
    ['production', saved.accessToken],
  ])
  expect(
    fetch.mock.calls.map(([, init]) =>
      new Headers(init?.headers).get('Authorization'),
    ),
  ).toEqual(['Bearer saved-token', 'Bearer refreshed-token'])
  expect(fetch.mock.calls.map(([url]) => url)).toEqual([
    'https://api.repalis.com/v1/organizations/org-1',
    'https://api.repalis.com/v1/organizations/org-1',
  ])
})

test.each([
  {
    credential: overrideCredential(),
    status: 401,
    attempts: 1,
    message: 'Authentication rejected',
  },
  {
    credential: keyringCredential(),
    status: 403,
    attempts: 1,
    message: 'Access denied',
  },
  {
    credential: keyringCredential(),
    status: 404,
    attempts: 1,
    message:
      'Not found in sandbox. Check the ID, or run repalis auth org to switch if it belongs to another organization.',
  },
  {
    credential: keyringCredential(),
    status: 401,
    attempts: 2,
    message: 'Authentication rejected',
  },
])(
  'bounds retries for $credential.source credentials on HTTP $status',
  async ({ credential, status, attempts, message }) => {
    const resolve = vi.fn<Resolve>(() => Effect.succeed(credential))
    const repalis = await repalisWith(resolve)
    const request = vi
      .fn<(client: RepalisSDK) => Promise<string>>()
      .mockRejectedValue({ statusCode: status })

    await expect(Effect.runPromise(repalis.use(request))).rejects.toMatchObject({
      message: expect.stringContaining(message),
      statusCode: status,
    })
    expect(request).toHaveBeenCalledTimes(attempts)
    expect(resolve).toHaveBeenCalledTimes(attempts)
  },
)

test('passes the one-second request timeout to the SDK', async () => {
  const timeout = vi.spyOn(AbortSignal, 'timeout')
  vi.stubGlobal(
    'fetch',
    vi.fn().mockResolvedValue(Response.json({ id: 'customer-1' })),
  )
  const repalis = await repalisWith(() => Effect.succeed(overrideCredential()))
  await Effect.runPromise(
    repalis.use((client) => client.customers.get('customer-1'), 'sandbox', {
      timeout: 1,
    }),
  )
  expect(timeout).toHaveBeenCalledWith(1000)
})

test('preserves refresh failures without retrying the API request', async () => {
  const error = new AuthError({ message: 'Unable to refresh saved session.' })
  const repalis = await repalisWith((_environment, rejected) =>
    rejected ? Effect.fail(error) : Effect.succeed(keyringCredential()),
  )
  const request = vi
    .fn<(client: RepalisSDK) => Promise<string>>()
    .mockRejectedValue({ statusCode: 401 })

  expect(await Effect.runPromise(repalis.use(request).pipe(Effect.flip))).toBe(
    error,
  )
  expect(request).toHaveBeenCalledTimes(1)
})

test.each([
  { organizationId: 'org-1', header: 'org-1' },
  { organizationId: undefined, header: null },
])(
  'sends Repalis-Organization only for a scoped request ($organizationId)',
  async ({ organizationId, header }) => {
    const fetch = vi
      .fn<typeof globalThis.fetch>()
      .mockResolvedValue(Response.json({ id: 'org-1' }))
    vi.stubGlobal('fetch', fetch)
    const repalis = await repalisWith(() => Effect.succeed(overrideCredential()))
    await Effect.runPromise(
      repalis.use((client) => client.organizations.get('org-1'), 'sandbox', {
        organizationId,
      }),
    )
    expect(
      new Headers(fetch.mock.calls[0]![1]?.headers).get('Repalis-Organization'),
    ).toBe(header)
  },
)

test.each([
  {
    name: 'a parsed error body',
    rejection: {
      statusCode: 409,
      error: { error: 'ProductNotDeletable', detail: 'Archive it instead.' },
    },
    message: 'Archive it instead.',
  },
  {
    name: 'a raw error body',
    rejection: {
      statusCode: 409,
      error: '{"error":"ProductNotDeletable","detail":"Archive it instead."}',
    },
    message: 'Archive it instead.',
  },
  {
    name: 'validation errors',
    rejection: {
      statusCode: 422,
      error: {
        detail: [
          { loc: ['body', 'prices'], msg: 'Field required', type: 'missing' },
          {
            loc: ['body', 'config', 'body'],
            msg: 'Too long',
            type: 'too_long',
          },
          {
            loc: ['body', 'prices', 0, 'price_amount'],
            msg: 'Input should be a valid integer',
            type: 'int_type',
          },
        ],
      },
    },
    message:
      'The request is invalid:\n    prices: Field required\n    config.body: Too long\n    prices.0.price_amount: Input should be a valid integer',
  },
  {
    name: 'a JSON list passed to a repeatable ID flag',
    rejection: {
      statusCode: 422,
      error: {
        detail: [
          {
            loc: ['body', 'benefits', 0],
            msg: 'Input should be a valid UUID, invalid character: found `[` at 1',
            type: 'uuid_parsing',
          },
          {
            loc: ['body', 'percentage', 'custom_products', 0],
            msg: 'Input should be a valid UUID, invalid character: found `[` at 1',
            type: 'uuid_parsing',
          },
          {
            loc: ['body', 'products', 0],
            msg: 'Input should be a valid UUID, invalid length',
            type: 'uuid_parsing',
          },
        ],
      },
    },
    message:
      'The request is invalid:\n    benefits.0: Input should be a valid UUID, invalid character: found `[` at 1. Repeat --benefits once per ID instead of passing a list, e.g. --benefits <id> --benefits <id>\n    percentage.custom_products.0: Input should be a valid UUID, invalid character: found `[` at 1. Repeat --custom-products once per ID instead of passing a list, e.g. --custom-products <id> --custom-products <id>\n    products.0: Input should be a valid UUID, invalid length',
  },
  {
    name: 'a body without detail',
    rejection: { statusCode: 422, error: 'Unprocessable Entity' },
    message: 'The Repalis API rejected the request (422).',
  },
  {
    name: 'a server error',
    rejection: { statusCode: 503 },
    message:
      'The Repalis API returned an error (503). It may be having issues, try again shortly.',
  },
  {
    name: 'a network failure',
    rejection: new TypeError('fetch failed'),
    message:
      'Repalis API request failed (TypeError). Check your connection and try again.',
  },
])('surfaces the API message for $name', async ({ rejection, message }) => {
  const repalis = await repalisWith(() => Effect.succeed(overrideCredential()))
  const request = vi
    .fn<(client: RepalisSDK) => Promise<string>>()
    .mockRejectedValue(rejection)

  await expect(Effect.runPromise(repalis.use(request))).rejects.toMatchObject({
    message,
  })
})

const notAccessible = {
  error: 'RequestedOrganizationNotAccessible',
  detail: 'The requested organization is not accessible.',
}

test('explains an inaccessible organization in a parsed error body', async () => {
  const repalis = await repalisWith(() => Effect.succeed(overrideCredential()))
  const request = vi
    .fn<(client: RepalisSDK) => Promise<string>>()
    .mockRejectedValue({ statusCode: 403, error: notAccessible })

  await expect(
    Effect.runPromise(
      repalis.use(request, 'sandbox', { organizationId: 'org-2' }),
    ),
  ).rejects.toMatchObject({
    message:
      'Organization org-2 is not accessible with this credential. Check --org or run repalis auth org.',
    statusCode: 403,
  })
})

test('explains an inaccessible organization in a raw API response', async () => {
  vi.stubGlobal(
    'fetch',
    vi.fn().mockResolvedValue(Response.json(notAccessible, { status: 403 })),
  )
  const repalis = await repalisWith(() => Effect.succeed(overrideCredential()))
  await expect(
    Effect.runPromise(
      repalis.use((client) => client.products.list(), 'sandbox', {
        organizationId: 'org-2',
      }),
    ),
  ).rejects.toThrow('Organization org-2 is not accessible')
})
