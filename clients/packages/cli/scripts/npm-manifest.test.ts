import { describe, expect, test } from 'vitest'
import {
  binaryName,
  findTarget,
  mainManifest,
  placeholderBinary,
  platformDirectory,
  platformManifest,
  platformPackageName,
  targets,
} from './npm-manifest.ts'

describe('npm platform packages', () => {
  test('names packages after the npm platform and architecture', () => {
    const windows = findTarget('bun-windows-x64')
    expect(platformPackageName(windows)).toBe('@repalis/cli-windows-x64')
    expect(platformDirectory(windows)).toBe('cli-windows-x64')
    expect(binaryName(windows.os)).toBe('polar.exe')

    const linux = findTarget('bun-linux-arm64')
    expect(platformPackageName(linux)).toBe('@repalis/cli-linux-arm64')
    expect(binaryName(linux.os)).toBe('polar')
  })

  test('rejects unknown Bun targets', () => {
    expect(() => findTarget('bun-freebsd-x64')).toThrow(/Unknown target/)
    expect(() => findTarget(undefined)).toThrow(/Unknown target/)
  })

  test('restricts each platform package to its platform', () => {
    expect(platformManifest(findTarget('bun-darwin-arm64'), '1.4.0')).toEqual(
      expect.objectContaining({
        name: '@repalis/cli-darwin-arm64',
        version: '1.4.0',
        os: ['darwin'],
        cpu: ['arm64'],
      }),
    )
    expect(platformManifest(findTarget('bun-windows-x64'), '1.4.0')).toEqual(
      expect.objectContaining({ os: ['win32'], cpu: ['x64'] }),
    )
  })
})

describe('npm main package', () => {
  const binaries = Object.fromEntries(
    targets.map((target) => [platformPackageName(target), '1.4.0']),
  )

  test('points the command at the placeholder swapped in by postinstall', () => {
    const manifest = mainManifest('1.4.0', binaries)

    expect(manifest.name).toBe('@repalis/cli')
    expect(manifest.bin).toEqual({ polar: 'bin/polar.exe' })
    expect(manifest.scripts).toEqual({ postinstall: 'node ./postinstall.mjs' })
    expect(Object.keys(manifest.optionalDependencies)).toEqual([
      '@repalis/cli-darwin-arm64',
      '@repalis/cli-darwin-x64',
      '@repalis/cli-linux-arm64',
      '@repalis/cli-linux-x64',
      '@repalis/cli-windows-x64',
    ])
    expect(Object.values(manifest.optionalDependencies)).toEqual(
      Array(5).fill('1.4.0'),
    )
  })

  test('refuses platform packages from another version', () => {
    expect(() =>
      mainManifest('1.4.0', {
        ...binaries,
        '@repalis/cli-linux-x64': '1.3.9',
      }),
    ).toThrow(/does not match @polar-sh\/cli@1.4.0/)
  })

  test('refuses unrelated packages and empty releases', () => {
    expect(() => mainManifest('1.4.0', { '@repalis/sdk': '1.4.0' })).toThrow(
      /not a @polar-sh\/cli platform package/,
    )
    expect(() => mainManifest('1.4.0', {})).toThrow(/No platform packages/)
  })

  test('placeholder explains that postinstall did not run', () => {
    expect(placeholderBinary()).toMatch(/postinstall script was not run/)
    expect(placeholderBinary()).toMatch(/exit 1\n$/)
  })
})
