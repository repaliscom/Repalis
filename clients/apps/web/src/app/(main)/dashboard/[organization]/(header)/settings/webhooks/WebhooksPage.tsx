'use client'

import { DashboardBody } from '@/components/Layout/DashboardLayout'
import { useModal } from '@/components/Modal/useModal'
import NewWebhookModal from '@/components/Settings/Webhook/NewWebhookModal'
import WebhookSettings from '@/components/Settings/Webhook/WebhookSettings'
import { useIsManagedAsCode } from '@/hooks/permissions'
import { schemas } from '@repalis/client'
import { Button, InlineModal } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import { ArrowUpRight } from '@repalis/orbit/icons'

export default function ClientPage({
  organization: org,
}: {
  organization: schemas['Organization']
}) {
  const { isShown, show, hide } = useModal()
  const managedAsCode = useIsManagedAsCode(org.id)

  return (
    <DashboardBody
      wrapperClassName="max-w-(--breakpoint-md)!"
      title="Webhooks"
      header={
        <Box alignItems="center" columnGap="s">
          <a
            href="/docs/integrate/webhooks/endpoints"
            target="_blank"
            rel="noopener noreferrer"
          >
            <Button variant="ghost" className="gap-x-2" asChild>
              <span>Documentation</span>
              <ArrowUpRight className="h-4 w-4" />
            </Button>
          </a>
          {!managedAsCode && <Button onClick={show}>Add Endpoint</Button>}
        </Box>
      }
    >
      <WebhookSettings org={org} />
      <InlineModal
        isShown={isShown}
        hide={hide}
        modalContent={<NewWebhookModal hide={hide} organization={org} />}
      />
    </DashboardBody>
  )
}
