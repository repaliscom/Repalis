import { vi } from 'vitest'

export const evaluate = vi.fn<
  () => Promise<{
    result?: string
    error?: string
    errorName?: string
    status?: number
    body?: unknown
    requests?: number
    calls?: Array<{ method: string; url: string; status: number }>
  }>
>()
export const get = vi.fn<
  (
    _name: string | null,
    _getCode: () => WorkerLoaderWorkerCode,
  ) => { getEntrypoint: () => { evaluate: typeof evaluate } }
>(() => ({ getEntrypoint: () => ({ evaluate }) }))
export const env = {
  REPALIS_SERVERS: {
    'repalis-mcp': 'https://api.repalis.test',
    'repalis-sandbox': 'https://sandbox-api.repalis.test',
  },
  LOADER: { get },
  MINTLIFY_SEARCH_KEY: 'mint_dsc_test',
  MCP_ANALYTICS_SECRET: 'analytics-secret-test',
  POSTHOG_PROJECT_KEY: '',
}
export const waitUntil = vi.fn<(promise: Promise<unknown>) => void>()
export const exports = {
  RepalisApiOutbound: vi.fn(() => ({ fetch: vi.fn() })),
}
export class WorkerEntrypoint {
  constructor(public ctx: { props: unknown }) {}
}
