'use client'

import { MasterDetailLayoutContent } from '@/components/Layout/MasterDetailLayout'
import { schemas } from '@repalis/client'
import { Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import { PropsWithChildren } from 'react'
import { CustomerHeader } from './CustomerHeader'
import { CustomerSubnav } from './CustomerSubnav'

interface CustomerPageShellProps extends PropsWithChildren {
  organization: schemas['Organization']
  customer: schemas['Customer']
}

export const CustomerPageShell = ({
  organization,
  customer,
  children,
}: CustomerPageShellProps) => {
  const hasName = (customer.name?.length ?? 0) > 0
  const showBillingName =
    hasName &&
    !!customer.billing_name &&
    customer.name?.toLocaleLowerCase() !==
      customer.billing_name.toLocaleLowerCase()

  return (
    <MasterDetailLayoutContent
      header={
        <>
          <Box flexDirection="column">
            <Text variant="heading-xs" as="h1">
              {hasName ? customer.name : (customer.billing_name ?? '—')}
              {showBillingName && (
                <Text as="span" variant="body" color="muted">
                  {' '}
                  {customer.billing_name}
                </Text>
              )}
            </Text>
            {(customer.email || customer.type === 'individual') && (
              <Text variant="heading-xs" color="muted">
                {customer.email ?? '—'}
              </Text>
            )}
          </Box>

          <CustomerHeader organization={organization} customer={customer} />
        </>
      }
    >
      <Box flexDirection="column" rowGap="3xl">
        <CustomerSubnav organization={organization} customer={customer} />
        {children}
      </Box>
    </MasterDetailLayoutContent>
  )
}
