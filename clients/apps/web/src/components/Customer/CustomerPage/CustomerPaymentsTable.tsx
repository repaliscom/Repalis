'use client'

import PaymentMethod from '@/components/PaymentMethod/PaymentMethod'
import PaymentStatus from '@/components/PaymentStatus/PaymentStatus'
import { paymentDeclineReasonColumns } from '@/components/PaymentStatus/paymentDeclineReasonColumns'
import { usePayments } from '@/hooks/queries/payments'
import { schemas } from '@repalis/client'
import { formatCurrency } from '@repalis/currency'
import { Button, DataTable, Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import FormattedDateTime from '@repalis/ui/components/atoms/FormattedDateTime'
import Link from 'next/link'

interface CustomerPaymentsTableProps {
  organization: schemas['Organization']
  customer: schemas['Customer']
}

export const CustomerPaymentsTable = ({
  organization,
  customer,
}: CustomerPaymentsTableProps) => {
  const { data: payments, isLoading } = usePayments(customer.organization_id, {
    customer_id: customer.id,
    limit: 10,
    sorting: ['-created_at'],
  })

  return (
    <Box flexDirection="column" rowGap="l">
      <Text variant="heading-xxs" as="h3">
        Recent Payments
      </Text>
      <DataTable
        data={payments?.items ?? []}
        columns={[
          {
            header: 'Created At',
            accessorKey: 'created_at',
            cell: ({ row: { original } }) => (
              <FormattedDateTime
                dateStyle="medium"
                resolution="time"
                datetime={original.created_at}
              />
            ),
          },
          {
            header: 'Amount',
            accessorKey: 'amount',
            cell: ({ row: { original } }) =>
              formatCurrency('compact')(original.amount, original.currency),
          },
          {
            header: 'Method',
            accessorKey: 'method',
            cell: ({ row: { original } }) => (
              <PaymentMethod payment={original} />
            ),
          },
          {
            header: 'Status',
            accessorKey: 'status',
            cell: ({ row: { original } }) => (
              <PaymentStatus payment={original} />
            ),
          },
          ...paymentDeclineReasonColumns(payments?.items ?? []),
          {
            header: '',
            accessorKey: 'action',
            cell: ({ row: { original } }) =>
              original.order_id ? (
                <Box justifyContent="end">
                  <Link
                    href={`/dashboard/${organization.slug}/sales/${original.order_id}`}
                  >
                    <Button variant="secondary" size="sm">
                      View Order
                    </Button>
                  </Link>
                </Box>
              ) : null,
          },
        ]}
        isLoading={isLoading}
        className="text-sm"
      />
    </Box>
  )
}
