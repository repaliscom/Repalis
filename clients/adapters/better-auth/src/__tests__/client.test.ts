import type { BetterAuthClientPlugin } from 'better-auth'
import { describe, expect, it } from 'vitest'
import { repalisClient } from '../client'

describe('repalisClient', () => {
  it('should create a client plugin with correct id', () => {
    const plugin = repalisClient()

    expect(plugin.id).toBe('repalis-client')
  })

  it('should satisfy BetterAuthClientPlugin interface', () => {
    const plugin = repalisClient()

    // Check that it has the required properties for BetterAuthClientPlugin
    expect(plugin).toHaveProperty('id')
    expect(plugin).toHaveProperty('$InferServerPlugin')
    expect(typeof plugin.id).toBe('string')
    expect(typeof plugin.$InferServerPlugin).toBe('object')
  })

  it('should have consistent plugin id across multiple calls', () => {
    const plugin1 = repalisClient()
    const plugin2 = repalisClient()

    expect(plugin1.id).toBe(plugin2.id)
    expect(plugin1.id).toBe('repalis-client')
  })

  it('should be a function that returns a plugin object', () => {
    expect(typeof repalisClient).toBe('function')

    const plugin = repalisClient()
    expect(typeof plugin).toBe('object')
    expect(plugin).not.toBe(null)
  })

  it('should have proper type inference marker', () => {
    const plugin = repalisClient()

    // The $InferServerPlugin should be an empty object used for type inference
    expect(plugin.$InferServerPlugin).toEqual({})
  })

  it('should conform to BetterAuthClientPlugin type structure', () => {
    const plugin = repalisClient()

    // Type assertion to ensure it matches the expected interface
    const clientPlugin: BetterAuthClientPlugin = plugin

    expect(clientPlugin.id).toBe('repalis-client')
    expect(clientPlugin).toHaveProperty('$InferServerPlugin')
  })
})
