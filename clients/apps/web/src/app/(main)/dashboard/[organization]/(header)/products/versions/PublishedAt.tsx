'use client'

import { schemas } from '@repalis/client'
import { Tooltip, TooltipContent, TooltipTrigger } from '@repalis/orbit'
import FormattedDateTime from '@repalis/ui/components/atoms/FormattedDateTime'
import RepalisTimeAgo from '@repalis/ui/components/atoms/RepalisTimeAgo'
import { useState } from 'react'

const WEEK_MS = 7 * 24 * 60 * 60 * 1000

const publishedAt = (catalog: schemas['Catalog']) =>
  catalog.published_at ?? catalog.created_at

export const PublishedAt = ({ catalog }: { catalog: schemas['Catalog'] }) => {
  const [now] = useState(() => Date.now())
  const datetime = publishedAt(catalog)

  if (now - new Date(datetime).getTime() >= WEEK_MS) {
    return <FormattedDateTime datetime={datetime} />
  }

  return (
    <Tooltip delayDuration={150}>
      <TooltipTrigger asChild>
        <span>
          <RepalisTimeAgo date={new Date(datetime)} />
        </span>
      </TooltipTrigger>
      <TooltipContent>
        <FormattedDateTime datetime={datetime} resolution="time" />
      </TooltipContent>
    </Tooltip>
  )
}
