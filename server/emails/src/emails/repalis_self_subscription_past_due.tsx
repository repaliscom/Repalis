import { Footer, Intro, Text, WrapperRepalis } from '../components/foundation'
import type { schemas } from '../types'

export function RepalisSelfSubscriptionPastDue({
  email,
  product_name,
}: schemas['PolarSelfSubscriptionPastDueProps']) {
  return (
    <WrapperRepalis
      preview={`Action needed: we couldn't process your payment for ${product_name}`}
    >
      <Intro headline="We couldn&rsquo;t process your payment">
        We tried to charge your payment method for your{' '}
        <Text as="span" weight="medium">
          {product_name}
        </Text>{' '}
        subscription, but it didn&rsquo;t go through. This can happen for a
        number of reasons, like an expired card or a temporary bank hold.
      </Intro>
      <Text>
        Please update your payment method in your billing settings to keep your
        subscription active. We&rsquo;ll automatically retry the payment.
      </Text>
      <Footer email={email} />
    </WrapperRepalis>
  )
}

RepalisSelfSubscriptionPastDue.PreviewProps = {
  email: 'john@example.com',
  product_name: 'Repalis Pro',
} satisfies schemas['PolarSelfSubscriptionPastDueProps']

export default RepalisSelfSubscriptionPastDue
