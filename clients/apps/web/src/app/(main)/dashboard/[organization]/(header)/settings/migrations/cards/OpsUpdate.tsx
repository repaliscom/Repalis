'use client'

import { schemas } from '@repalis/client'
import { Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import FormattedDateTime from '@repalis/ui/components/atoms/FormattedDateTime'

export function OpsUpdate({ step }: { step: schemas['PanTransferStep'] }) {
  if (!step.note && !step.expected_at) {
    return null
  }

  return (
    <Box flexDirection="column" rowGap="xs">
      {/* Prose wraps on its own; a pasted link does not. */}
      {step.note && (
        <Box overflowX="auto" maxWidth="100%">
          <Text variant="caption">{step.note}</Text>
        </Box>
      )}
      {step.expected_at && (
        <Text variant="caption" color="muted">
          Expected by <FormattedDateTime datetime={step.expected_at} />
        </Text>
      )}
    </Box>
  )
}
