import { commands } from '@repalis/cli-commands'
import { Command, GlobalFlag } from 'effect/cli'
import { Help } from '@/utils/help'
import { Output } from '@/utils/output'
import { agent } from '@/commands/agent'
import { auth } from '@/commands/auth'
import { config } from '@/commands/config'
import { repalis } from '@/commands/home'
import { update } from '@/commands/update'
import { webhook } from '@/commands/webhook'

// Add new preview commands in this array, e.g [config, newFeature]
const previews = [config].map((command) =>
  command.pipe(Command.withDescription(`${command.description} (preview)`)),
)

interface ProgramOptions {
  readonly preview: boolean
}

export const program = ({ preview }: ProgramOptions) =>
  repalis.pipe(
    Command.withSubcommands([
      {
        group: 'CLI COMMANDS',
        commands: [auth, agent, webhook, update, ...(preview ? previews : [])],
      },
      { group: 'API RESOURCES', commands },
    ]),
    Command.withGlobalFlags([Output]),
  )

const sharedBuiltIns = [
  GlobalFlag.Version,
  GlobalFlag.Completions,
  GlobalFlag.LogLevel,
]

export const builtIns = [Help, ...sharedBuiltIns]

export const referenceBuiltIns = [GlobalFlag.Help, ...sharedBuiltIns]
