import type { models, Repalis } from '../../sdk'
import type { MemberIdentifier } from './utils'

export type IngestedEvent = {
  name: string
  timestamp: Date
  metadata?: models.EventMetadataInput | undefined
}

export const ingestEvents = async (
  sdk: Repalis,
  identifier: MemberIdentifier,
  events: readonly IngestedEvent[],
) => {
  const { inserted } = await sdk.events.ingest({
    events: events.map(({ name, timestamp, metadata }) => ({
      ...identifier,
      name,
      timestamp: timestamp.toISOString(),
      ...(metadata !== undefined ? { metadata } : {}),
    })),
  })

  return inserted
}
