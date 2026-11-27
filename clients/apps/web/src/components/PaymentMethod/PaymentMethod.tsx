import { isCardPayment, isKrCardPayment } from '@/utils/payment'
import { schemas } from '@repalis/client'
import { Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import CreditCardBrandIcon from '../CreditCardBrandIcon'
import { getPaymentMethodTypeLabel } from '../PaymentMethodDisplay'

const PaymentMethod = ({ payment }: { payment: schemas['Payment'] }) => {
  const metadata =
    isCardPayment(payment) || isKrCardPayment(payment)
      ? payment.method_metadata
      : null

  if (metadata?.last4) {
    return (
      <Box alignItems="center" columnGap="xs">
        <CreditCardBrandIcon
          height="1.5em"
          brand={metadata.brand ?? 'unknown'}
        />
        <Text>{`•••• ${metadata.last4}`}</Text>
      </Box>
    )
  }
  return <Text>{getPaymentMethodTypeLabel(payment.method)}</Text>
}

export default PaymentMethod
