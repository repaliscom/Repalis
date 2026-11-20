import { createRepalisCore } from '@repalis/sdk/2026-10'

export const polarSDK = createRepalisCore({
  accessToken: process.env['REPALIS_ACCESS_TOKEN'] as string,
  environment: 'sandbox',
})
