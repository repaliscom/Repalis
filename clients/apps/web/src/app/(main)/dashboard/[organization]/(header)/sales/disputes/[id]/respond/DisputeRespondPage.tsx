'use client'

import { DashboardBody } from '@/components/Layout/DashboardLayout'
import { useDispute } from '@/hooks/queries/disputes'
import { schemas } from '@repalis/client'
import { Button, Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import { LoaderCircle as Loader2 } from '@repalis/orbit/icons'
import Link from 'next/link'
import { DisputeRespondView } from './DisputeRespondView'

interface Props {
  organization: schemas['Organization']
  disputeId: string
}

const DisputeRespondPage = ({ organization, disputeId }: Props) => {
  const { data: dispute, isLoading } = useDispute(disputeId)

  if (isLoading) {
    return (
      <DashboardBody>
        <Box alignItems="center" justifyContent="center" paddingVertical="3xl">
          <Loader2 className="dark:text-repalis-400 h-5 w-5 animate-spin text-gray-500" />
        </Box>
      </DashboardBody>
    )
  }

  if (!dispute || dispute.customer.organization_id !== organization.id) {
    return (
      <DashboardBody>
        <Box
          flexDirection="column"
          alignItems="center"
          justifyContent="center"
          paddingVertical="3xl"
          rowGap="s"
          textAlign="center"
        >
          <Text variant="label">Dispute not found</Text>
          <Text color="muted">
            This dispute does not exist or you do not have access to it.
          </Text>
        </Box>
      </DashboardBody>
    )
  }

  if (dispute.status !== 'needs_response') {
    return (
      <DashboardBody>
        <Box
          flexDirection="column"
          alignItems="center"
          justifyContent="center"
          paddingVertical="3xl"
          rowGap="m"
          textAlign="center"
        >
          <Box flexDirection="column" rowGap="s">
            <Text variant="label">This dispute is no longer open</Text>
            <Text color="muted">
              It is not awaiting a response, so it can no longer be countered.
            </Text>
          </Box>
          <Link
            href={`/dashboard/${organization.slug}/sales/disputes/${dispute.id}`}
          >
            <Button variant="secondary">Back to dispute</Button>
          </Link>
        </Box>
      </DashboardBody>
    )
  }

  return <DisputeRespondView organization={organization} dispute={dispute} />
}

export default DisputeRespondPage
