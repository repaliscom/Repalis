import {
  type WebhooksConfig,
  handleWebhookPayload,
} from '@repalis/adapter-utils'
import { webhooks } from '@repalis/sdk/2026-10'
import { type NextRequest, NextResponse } from 'next/server'

export {
  type EntitlementContext,
  type EntitlementHandler,
  type EntitlementProperties,
  EntitlementStrategy,
  Entitlements,
} from '@repalis/adapter-utils'

export const Webhooks = ({
  webhookSecret,
  entitlements,
  onPayload,
  ...eventHandlers
}: WebhooksConfig) => {
  return async (request: NextRequest) => {
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
        return NextResponse.json({ received: false }, { status: 403 })
      }

      if (error instanceof webhooks.RepalisWebhookUnknownTypeError) {
        return NextResponse.json(
          { received: error.eventType !== null },
          { status: error.eventType !== null ? 200 : 400 },
        )
      }

      if (error instanceof webhooks.RepalisWebhookError) {
        return NextResponse.json({ received: false }, { status: 400 })
      }

      throw error
    }

    await handleWebhookPayload(webhookPayload, {
      webhookSecret,
      entitlements,
      onPayload,
      ...eventHandlers,
    })

    return NextResponse.json({ received: true })
  }
}
