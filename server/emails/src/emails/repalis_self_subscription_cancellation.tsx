import { Footer, Intro, Text, WrapperRepalis } from '../components/foundation'
import { formatDate } from '../utils/formatters'
import type { schemas } from '../types'

export function RepalisSelfSubscriptionCancellation({
  email,
  product_name,
  ends_at,
}: schemas['RepalisSelfSubscriptionCancellationProps']) {
  const endDate = ends_at ? formatDate(ends_at) : null

  return (
    <WrapperRepalis
      preview={`Your ${product_name} subscription has been canceled`}
    >
      <Intro headline="Your subscription has been canceled">
        Your{' '}
        <Text as="span" weight="medium">
          {product_name}
        </Text>{' '}
        subscription has been canceled.{' '}
        {endDate
          ? `You'll keep full access until ${endDate}.`
          : "You'll keep full access until the end of your current billing period."}
      </Intro>
      <Text>
        If you change your mind, you can resubscribe anytime from your billing
        settings.
      </Text>
      <Footer email={email} />
    </WrapperRepalis>
  )
}

RepalisSelfSubscriptionCancellation.PreviewProps = {
  email: 'john@example.com',
  product_name: 'Repalis Pro',
  ends_at: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString(),
} satisfies schemas['RepalisSelfSubscriptionCancellationProps']

export default RepalisSelfSubscriptionCancellation
