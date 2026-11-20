import {
  CheckoutStatusDisplayColor,
  CheckoutStatusDisplayTitle,
} from '@/utils/checkout'
import { schemas } from '@repalis/client'
import { Status } from '@repalis/orbit'

const CheckoutStatus = ({
  checkout: { status },
}: {
  checkout: schemas['Checkout']
}) => {
  return (
    <Status
      color={CheckoutStatusDisplayColor[status]}
      status={CheckoutStatusDisplayTitle[status]}
    />
  )
}

export default CheckoutStatus
