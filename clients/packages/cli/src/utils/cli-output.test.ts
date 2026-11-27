import { CliError } from 'effect/cli'
import { describe, expect, test } from 'vitest'
import { formatter } from '@/utils/cli-output'
import { stripAnsi } from '@/utils/test-utils/cli'

const unknown = (subcommand: string, parent: string[]) =>
  stripAnsi(
    formatter.formatErrors([
      new CliError.UnknownSubcommand({ subcommand, parent, suggestions: [] }),
    ]),
  )

describe('formatErrors', () => {
  test.each([
    ['listen', 'webhook listen'],
    ['trigger', 'webhook trigger'],
  ])('suggests the webhook command for repalis %s', (subcommand, moved) => {
    expect(unknown(subcommand, ['repalis'])).toContain(
      `Did you mean this?\n    ${moved}`,
    )
  })

  test.each([
    [['repalis'], 'login', 'auth login'],
    [['repalis'], 'whoami', 'auth whoami'],
    [['repalis', 'auth'], 'status', 'auth whoami'],
    [['repalis', 'webhooks'], 'list', 'webhooks list_webhook_endpoints'],
    [['repalis', 'webhooks'], 'listen', 'webhook listen'],
  ])('suggests the real command for %j %s', (parent, subcommand, intended) => {
    expect(unknown(subcommand, parent)).toContain(
      `Did you mean this?\n    ${intended}`,
    )
  })

  test('leaves other unknown subcommands alone', () => {
    expect(unknown('listen', ['repalis', 'config'])).not.toContain('Did you mean')
    expect(unknown('nope', ['repalis'])).not.toContain('Did you mean')
  })
})
