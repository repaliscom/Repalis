import { Footer, Intro, Text, WrapperRepalis } from '../components/foundation'
import type { schemas } from '../types'

export function RepalisSelfSubscriptionCycled({
  email,
  product_name,
}: schemas['RepalisSelfSubscriptionCycledProps']) {
  return (
    <WrapperRepalis preview={`Your ${product_name} subscription renewed`}>
      <Intro headline={`${product_name} renewed`}>
        Your{' '}
        <Text as="span" weight="medium">
          {product_name}
        </Text>{' '}
        subscription renewed for another cycle. The latest invoice is attached.
      </Intro>
      <Footer email={email} />
    </WrapperRepalis>
  )
}

RepalisSelfSubscriptionCycled.PreviewProps = {
  email: 'john@example.com',
  product_name: 'Repalis Pro',
} satisfies schemas['RepalisSelfSubscriptionCycledProps']

export default RepalisSelfSubscriptionCycled
