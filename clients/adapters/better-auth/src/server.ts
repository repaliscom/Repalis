import type { AuthContext, BetterAuthPlugin } from 'better-auth'
import {
  onAfterUserCreate,
  onBeforeUserDelete,
  onUserDelete,
  onUserUpdate,
} from './hooks/customer'
import { installOrganizationHooks } from './organization/hooks'
import { createOrganizationLifecycleHooks } from './organization/lifecycle'
import type { RepalisEndpoints, RepalisOptions } from './types'

export interface RepalisBetterAuthPlugin {
  id: 'repalis'
  endpoints: RepalisEndpoints
  hooks: ReturnType<typeof createOrganizationLifecycleHooks>
  init: (ctx: AuthContext) => {
    options: {
      databaseHooks: {
        user: {
          create: {
            after: ReturnType<typeof onAfterUserCreate>
          }
          update: {
            after: ReturnType<typeof onUserUpdate>
          }
          delete: {
            before: ReturnType<typeof onBeforeUserDelete>
            after: ReturnType<typeof onUserDelete>
          }
        }
      }
    }
  }
}

export const repalis = <O extends RepalisOptions>(
  options: O,
): RepalisBetterAuthPlugin => {
  const plugins = options.use.reduce<RepalisEndpoints>((endpoints, use) => {
    Object.assign(endpoints, use(options.client, options))
    return endpoints
  }, {} as RepalisEndpoints)

  return {
    id: 'repalis',
    endpoints: plugins,
    hooks: createOrganizationLifecycleHooks(options),
    init(ctx) {
      installOrganizationHooks(ctx, options)

      return {
        options: {
          databaseHooks: {
            user: {
              create: {
                after: onAfterUserCreate(options),
              },
              update: {
                after: onUserUpdate(options, ctx),
              },
              delete: {
                before: onBeforeUserDelete(options, ctx),
                after: onUserDelete(options),
              },
            },
          },
        },
      }
    },
  } satisfies BetterAuthPlugin
}
