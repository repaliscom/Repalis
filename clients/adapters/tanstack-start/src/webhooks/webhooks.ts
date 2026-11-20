import {
  type WebhooksConfig,
  handleWebhookPayload,
} from '@repalis/adapter-utils'
import { webhooks } from '@repalis/sdk/2026-10'
import type { StartRouteHandler } from '../types'

export {
  EntitlementStrategy,
  Entitlements,
  type EntitlementContext,
  type EntitlementHandler,
  type EntitlementProperties,
} from '@repalis/adapter-utils'

export const Webhooks = <TPath extends string = string>({
  webhookSecret,
  entitlements,
  onPayload,
  ...eventHandlers
}: WebhooksConfig): StartRouteHandler<TPath> => {
  return async ({ request }) => {
    const requestBody = await request.text()

    const webhookHeaders = {
      'webhook-id': request.headers.get('webhook-id') ?? '',
      'webhook-timestamp': request.headers.get('webhook-timestamp') ?? '',
      'webhook-signature': request.headers.get('webhook-signature') ?? '',
    }

    let webhookPayload: webhooks.WebhookPayload
    try {
      webhookPayload = await webhooks.validateEvent(
        requestBody,
        webhookHeaders,
        webhookSecret,
      )
    } catch (error) {
      if (error instanceof webhooks.RepalisWebhookVerificationError) {
        return Response.json({ received: false }, { status: 403 })
      }

      if (error instanceof webhooks.RepalisWebhookUnknownTypeError) {
        return Response.json(
          { received: error.eventType !== null },
          { status: error.eventType !== null ? 200 : 400 },
        )
      }

      if (error instanceof webhooks.RepalisWebhookError) {
        return Response.json({ received: false }, { status: 400 })
      }

      throw error
    }

    await handleWebhookPayload(webhookPayload, {
      webhookSecret,
      entitlements,
      onPayload,
      ...eventHandlers,
    })

    return Response.json({ received: true })
  }
}
