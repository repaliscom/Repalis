'use client'

import { Alert } from '@repalis/orbit'

export function AUPBlocker({ categories }: { categories: string[] }) {
  return (
    <Alert
      variant="warning"
      title={`Not supported: ${categories.join(', ')}`}
      description={
        <>
          Repalis is a Merchant of Record for digital products only. Physical
          goods, human services, and marketplaces are not permitted under our{' '}
          <a
            href="https://repalis.com/legal/acceptable-use-policy"
            className="underline"
            target="_blank"
            rel="noopener noreferrer"
          >
            Acceptable Use Policy
          </a>
          .
        </>
      }
    />
  )
}
