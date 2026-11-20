import { RepalisEmbedCheckout } from '@repalis/checkout/embed'
import type { RepalisEmbedCheckout as RepalisEmbedCheckoutType } from '@repalis/checkout/embed'
import type { BetterAuthClientPlugin } from 'better-auth'
import type { BetterFetch, BetterFetchOption } from 'better-auth/client'
import type { CheckoutParams } from './plugins/checkout'
import type { polar } from './server'

export type { RepalisEmbedCheckoutType as RepalisEmbedCheckout }

export const repalisClient = () => {
  return {
    id: 'repalis-client',
    $InferServerPlugin: {} as ReturnType<typeof polar>,
    getActions: ($fetch: BetterFetch) => {
      return {
        checkoutEmbed: async (
          data: Omit<CheckoutParams, 'redirect' | 'embed_origin'>,
          fetchOptions?: BetterFetchOption,
        ): Promise<RepalisEmbedCheckoutType> => {
          const res = await $fetch('/checkout', {
            method: 'POST',
            body: {
              ...data,
              redirect: false,
              embed_origin: window.location.origin,
            },
            ...fetchOptions,
          })

          if (res.error) {
            throw new Error(res.error.message)
          }

          const checkout = res.data as { url: string }

          const theme =
            (new URL(checkout.url).searchParams.get('theme') as
              | 'light'
              | 'dark'
              | undefined) ?? 'light'

          return await RepalisEmbedCheckout.create(checkout.url, { theme })
        },
      }
    },
  } satisfies BetterAuthClientPlugin
}
