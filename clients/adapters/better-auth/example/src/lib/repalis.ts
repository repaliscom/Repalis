import { createRepalisCore } from '@repalis/sdk/2026-10'

export const repalisSDK = createRepalisCore({
  accessToken: process.env['REPALIS_ACCESS_TOKEN'] as string,
  environment: 'sandbox',
})
