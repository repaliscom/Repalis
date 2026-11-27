import {
  Button,
  Footer,
  Intro,
  Text,
  WrapperRepalis,
} from '../components/foundation'
import type { schemas } from '../types'

export function OrganizationOffboarded({
  email,
  organization_name,
  account_url,
}: schemas['OrganizationOffboardedProps']) {
  return (
    <WrapperRepalis
      preview={`${organization_name} has been offboarded from Repalis`}
    >
      <Intro headline={`${organization_name} has been offboarded`}>
        Your organization{' '}
        <Text as="span" weight="bold">
          {organization_name}
        </Text>{' '}
        has been offboarded from Repalis. New payments, including checkouts and
        subscription renewals, are now disabled.
      </Intro>
      <Text>
        Your remaining balance is available to withdraw. You can request a
        payout from your dashboard at any time.
      </Text>
      <Button href={account_url}>Withdraw your balance</Button>
      <Text>
        If you have any questions, just reply to this email and our team will
        help.
      </Text>
      <Footer email={email} />
    </WrapperRepalis>
  )
}

OrganizationOffboarded.PreviewProps = {
  email: 'admin@example.com',
  organization_name: 'Acme Inc.',
  account_url: 'https://repalis.com/dashboard/acme-inc/finance/account',
}

export default OrganizationOffboarded
