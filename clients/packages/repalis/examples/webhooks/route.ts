import { repalis } from './repalis'

// Next.js App Router: app/api/repalis/webhooks/route.ts
export const POST = repalis.webhooks.app

export const typeErrors = () => [
  // @ts-expect-error 'sales' is a Slack notification, it has no handler
  repalis.webhooks.sales,
]
