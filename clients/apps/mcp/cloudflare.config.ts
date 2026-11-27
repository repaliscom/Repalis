import { bindings, defineConfig } from 'cf/config'
import * as entrypoint from './src/index.ts' with { type: 'cf-worker' }

const REPALIS_SERVERS = {
  'repalis-mcp': 'https://api.repalis.com',
  'repalis-sandbox': 'https://sandbox-api.repalis.com',
}

const LOCAL_REPALIS_SERVERS = {
  'repalis-local': process.env.REPALIS_LOCAL_API_URL ?? 'http://127.0.0.1:8000',
}

export default defineConfig(({ mode }) => ({
  worker: {
    name: 'repalis-mcp',
    compatibilityDate: '2026-10-01',
    compatibilityFlags: ['nodejs_compat'],
    entrypoint,
    env: {
      LOADER: bindings.workerLoader(),
      MINTLIFY_SEARCH_KEY: bindings.secret(),
      MCP_ANALYTICS_SECRET: bindings.secret(),
      POSTHOG_PROJECT_KEY: bindings.text(
        mode === 'development'
          ? (process.env.POSTHOG_PROJECT_KEY ?? '')
          : 'phc_H2ajVAY4cy0uQpcgN5fzpv8JC3yP8VZOjx2EXiFBbgz',
      ),
      REPALIS_SERVERS: bindings.json(
        mode === 'development'
          ? { ...REPALIS_SERVERS, ...LOCAL_REPALIS_SERVERS }
          : REPALIS_SERVERS,
      ),
    },
    observability: {
      enabled: true,
    },
  },
}))
