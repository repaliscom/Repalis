import {
  getPaymentDisplayStatus,
  PaymentStatusDisplayColor,
  PaymentStatusDisplayTitle,
} from '@/utils/payment'
import { schemas } from '@repalis/client'
import { Status } from '@repalis/orbit'

const PaymentStatus = ({ payment }: { payment: schemas['Payment'] }) => {
  const status = getPaymentDisplayStatus(payment)
  return (
    <Status
      color={PaymentStatusDisplayColor[status]}
      status={PaymentStatusDisplayTitle[status]}
    />
  )
}

export default PaymentStatus
