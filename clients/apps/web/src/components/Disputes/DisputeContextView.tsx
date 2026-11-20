import { schemas } from '@repalis/client'
import { Box } from '@repalis/orbit/Box'
import { DisputeCustomerContextCard } from './DisputeCustomerContextCard'
import { DisputeOrderContextCard } from './DisputeOrderContextCard'

export const DisputeContextView = ({
  organization,
  order,
}: {
  organization: schemas['Organization']
  order: schemas['Order']
}) => (
  <Box flexDirection="column" rowGap="s">
    <DisputeOrderContextCard organization={organization} order={order} />
    <DisputeCustomerContextCard
      organization={organization}
      customer={order.customer}
    />
  </Box>
)
