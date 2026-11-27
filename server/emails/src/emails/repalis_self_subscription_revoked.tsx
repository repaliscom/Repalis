import { Footer, Intro, Text, WrapperRepalis } from '../components/foundation'
import type { schemas } from '../types'

export function RepalisSelfSubscriptionRevoked({
  email,
  product_name,
}: schemas['RepalisSelfSubscriptionRevokedProps']) {
  return (
    <WrapperRepalis preview={`Your ${product_name} subscription has ended`}>
      <Intro headline={`Your ${product_name} subscription has ended`}>
        Your{' '}
        <Text as="span" weight="medium">
          {product_name}
        </Text>{' '}
        subscription has ended, and the associated benefits are no longer
        active.
      </Intro>
      <Text>
        You can resubscribe anytime from your billing settings. If this
        wasn&rsquo;t expected, please get in touch and we&rsquo;ll help sort it
        out.
      </Text>
      <Footer email={email} />
    </WrapperRepalis>
  )
}

RepalisSelfSubscriptionRevoked.PreviewProps = {
  email: 'john@example.com',
  product_name: 'Repalis Pro',
} satisfies schemas['RepalisSelfSubscriptionRevokedProps']

export default RepalisSelfSubscriptionRevoked
