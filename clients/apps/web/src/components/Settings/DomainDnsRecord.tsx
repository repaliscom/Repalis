import { toast } from '@/components/Toast/use-toast'
import { schemas } from '@repalis/client'
import { Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import CopyToClipboardInput from '@repalis/ui/components/atoms/CopyToClipboardInput'

export const DomainDnsRecord = ({
  domain,
}: {
  domain: schemas['OrganizationDomain']
}) => (
  <Box flexDirection="column" rowGap="s">
    <Text variant="label">Name</Text>
    <CopyToClipboardInput
      value={domain.verification_record_name}
      ariaLabel="TXT record name"
      onCopy={() => toast({ title: 'Copied to clipboard' })}
      variant="mono"
    />
    <Text variant="label">Value</Text>
    <CopyToClipboardInput
      value={domain.verification_record_value ?? ''}
      ariaLabel="TXT record value"
      onCopy={() => toast({ title: 'Copied to clipboard' })}
      variant="mono"
    />
  </Box>
)
