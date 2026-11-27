import { Footer, Intro, Text, WrapperRepalis } from '../components/foundation'
import type { schemas } from '../types'

export function RepalisSelfSubscriptionConfirmation({
  email,
  product_name,
}: schemas['RepalisSelfSubscriptionConfirmationProps']) {
  return (
    <WrapperRepalis preview="We're happy to have you selling on Repalis!">
      <Intro headline="Thanks for choosing Repalis!">
        You're now subscribed to{' '}
        <Text as="span" weight="medium">
          {product_name}
        </Text>
        . Your invoice is attached for your records.
      </Intro>
      <Footer email={email} />
    </WrapperRepalis>
  )
}

RepalisSelfSubscriptionConfirmation.PreviewProps = {
  email: 'john@example.com',
  product_name: 'Repalis Pro',
} satisfies schemas['RepalisSelfSubscriptionConfirmationProps']

export default RepalisSelfSubscriptionConfirmation
