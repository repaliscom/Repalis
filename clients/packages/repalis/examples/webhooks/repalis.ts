import { RuntimeSDK } from '@repalis/repalis'
import config from './repalis.config'

export const polar = RuntimeSDK(config, {
  accessToken: process.env.POLAR_ACCESS_TOKEN ?? '',
  environment: 'sandbox',
})
