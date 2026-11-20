'use client'

import { useDisputes } from '@/hooks/queries/disputes'
import {
  DisputeStatusDisplayColor,
  DisputeStatusDisplayTitle,
} from '@/utils/dispute'
import { schemas } from '@repalis/client'
import { formatCurrency } from '@repalis/currency'
import { DataTable, type DataTableColumnDef, Status } from '@repalis/orbit'
import FormattedDateTime from '@repalis/ui/components/atoms/FormattedDateTime'
import { OrderSection } from './OrderSection'

export const OrderDisputesTable = ({
  organization,
  order,
}: {
  organization: schemas['Organization']
  order: schemas['Order']
}) => {
  const { data: disputes, isLoading } = useDisputes(organization.id, {
    order_id: order.id,
  })

  if (!disputes || disputes.items.length === 0) {
    return null
  }

  return (
    <OrderSection title="Disputes">
      <DataTable
        isLoading={isLoading}
        columns={
          [
            {
              accessorKey: 'created_at',
              header: 'Created At',
              cell: ({ row }) => (
                <FormattedDateTime
                  dateStyle="long"
                  datetime={row.original.created_at}
                />
              ),
            },
            {
              accessorKey: 'amount',
              header: 'Amount',
              cell: ({ row }) =>
                formatCurrency('standard')(
                  row.original.amount,
                  row.original.currency,
                ),
            },
            {
              accessorKey: 'status',
              header: 'Status',
              cell: ({ row }) => (
                <Status
                  color={DisputeStatusDisplayColor[row.original.status]}
                  status={DisputeStatusDisplayTitle[row.original.status]}
                />
              ),
            },
          ] satisfies DataTableColumnDef<schemas['Dispute']>[]
        }
        data={disputes.items}
      />
    </OrderSection>
  )
}
