import { defineConfig } from 'tsdown'

export default defineConfig([
  {
    entry: ['src/index.ts'],
    format: ['cjs', 'esm'],
    minify: true,
    dts: process.env.REPALIS_SKIP_DTS === '1' ? false : { sourcemap: false },
    fixedExtension: false,
    deps: { dts: { neverBundle: true } },
  },
])
