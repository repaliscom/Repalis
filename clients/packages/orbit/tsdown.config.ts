import { defineConfig, type UserConfig } from 'tsdown'

export const options: UserConfig = {
  entry: ['./src/index.ts', './src/tokens/tokens.stylex.ts'],
  format: ['cjs', 'esm'],
  minify: true,
  dts: process.env.REPALIS_SKIP_DTS === '1' ? false : { sourcemap: false },
  fixedExtension: false,
  deps: { dts: { neverBundle: true } },
}

export default defineConfig(options)
