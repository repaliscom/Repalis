import { mkdir, readFile, writeFile } from 'node:fs/promises'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { gzipSync } from 'node:zlib'

import { build, version } from 'esbuild'

const clients = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const [label, outputDirectory, clientFactory = 'createRepalisCore'] =
  process.argv.slice(2)
if (!label || !outputDirectory) {
  throw new Error(
    'Usage: node scripts/measure-adapter-bundles.mjs <label> <output-directory> [createRepalisCore|createRepalis]',
  )
}
if (!['createRepalisCore', 'createRepalis'].includes(clientFactory)) {
  throw new Error('Client factory must be createRepalisCore or createRepalis')
}

const entries = {
  'adapter-utils': ['adapter-utils', 'src/index.ts'],
  'better-auth': ['better-auth', 'src/index.ts'],
  'better-auth/client': ['better-auth', 'src/client.ts'],
  nextjs: ['nextjs', 'src/index.ts'],
  'nuxt/module': ['nuxt', 'src/module.ts'],
  'nuxt/runtime': ['nuxt', 'src/runtime/server/index.ts'],
  'tanstack-start': ['tanstack-start', 'src/index.ts'],
}
const measurements = {}
await mkdir(outputDirectory, { recursive: true })
for (const [name, [adapter, entry]] of Object.entries(entries)) {
  const directory = resolve(clients, 'adapters', adapter)
  const variants = name === 'better-auth' ? [false, true] : [false]
  for (const configured of variants) {
    const key = configured ? `${name}/with-client` : name
    const result = await build({
      stdin: {
        contents: `export * from './${entry}';${name === 'nuxt/module' ? `export { default } from './${entry}';` : ''}${configured ? `import { ${clientFactory} } from '@repalis/sdk/2026-04'; export const client = ${clientFactory}({accessToken: process.env.REPALIS_ACCESS_TOKEN});` : ''}`,
        resolveDir: directory,
        sourcefile: 'bundle-entry.ts',
        loader: 'ts',
      },
      bundle: true,
      minify: true,
      treeShaking: true,
      platform: 'node',
      target: 'node22',
      format: 'esm',
      write: false,
      metafile: true,
      alias: {
        '@repalis/adapter-utils': resolve(
          clients,
          'adapters/adapter-utils/src/index.ts',
        ),
      },
      external: [
        'next',
        'next/*',
        '@tanstack/*',
        '@nuxt/*',
        'nuxt',
        'nuxt/*',
        'h3',
        'better-auth',
        'better-auth/*',
        'zod',
        'zod/*',
      ],
    })
    const bytes = result.outputFiles[0].contents
    measurements[key] = {
      minifiedBytes: bytes.length,
      gzipBytes: gzipSync(bytes, { level: 9 }).length,
    }
    const filename = key.replaceAll('/', '-')
    await writeFile(resolve(outputDirectory, `${label}-${filename}.mjs`), bytes)
    await writeFile(
      resolve(outputDirectory, `${label}-${filename}.meta.json`),
      JSON.stringify(result.metafile, null, 2),
    )
  }
}
const sdk = JSON.parse(
  await readFile(
    resolve(clients, 'adapters/nextjs/node_modules/@repalis/sdk/package.json'),
    'utf8',
  ),
)
const report = {
  label,
  node: process.version,
  esbuild: version,
  sdk: sdk.version,
  clientFactory,
  measurements,
}
await writeFile(
  resolve(outputDirectory, `${label}.json`),
  `${JSON.stringify(report, null, 2)}\n`,
)
console.log(JSON.stringify(report, null, 2))
