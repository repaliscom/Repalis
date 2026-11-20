import { OrderStatus } from '@/components/Orders/OrderStatus'
import { ContextCard } from '@/components/Shared/ContextCard'
import { DetailRow } from '@/components/Shared/DetailRow'
import { schemas } from '@repalis/client'
import { formatCurrency } from '@repalis/currency'
import { Button, Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import FormattedDateTime from '@repalis/ui/components/atoms/FormattedDateTime'
import Link from 'next/link'

const format = formatCurrency('accounting')

export const DisputeOrderContextCard = ({
  organization,
  order,
}: {
  organization: schemas['Organization']
  order: schemas['Order']
}) => (
  <ContextCard>
    <Text variant="heading-xxs" as="h3">
      Order
    </Text>
    <Box flexDirection="column">
      <DetailRow label="Product" value={order.product?.name ?? '—'} />
      <DetailRow
        label="Status"
        value={<OrderStatus size="small" status={order.status} />}
      />
      <DetailRow
        label="Amount"
        value={format(order.total_amount, order.currency)}
      />
      <DetailRow
        label="Date"
        value={<FormattedDateTime datetime={order.created_at} />}
      />
    </Box>
    <Button className="w-full" size="default" variant="secondary" asChild>
      <Link href={`/dashboard/${organization.slug}/sales/${order.id}`}>
        View order
      </Link>
    </Button>
  </ContextCard>
)
