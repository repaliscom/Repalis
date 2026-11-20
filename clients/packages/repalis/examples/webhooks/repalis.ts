import { RuntimeSDK } from '@repalis/repalis'
import config from './repalis.config'

export const repalis = RuntimeSDK(config, {
  accessToken: process.env.REPALIS_ACCESS_TOKEN ?? '',
  environment: 'sandbox',
})
