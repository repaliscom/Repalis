'use client'

import { schemas } from '@repalis/client'
import { Alert } from '@repalis/orbit/Alert'

export const PastDueSubscriptionCallout = ({
  subscription,
}: {
  subscription: schemas['OrganizationSubscription']
}) => {
  if (subscription.status !== 'past_due') {
    return null
  }

  return (
    <Alert
      variant="warning"
      title="Renewal payment failed"
      description="We couldn't process your latest subscription renewal. Update your default payment method to retry the payment and keep your plan active."
    />
  )
}
