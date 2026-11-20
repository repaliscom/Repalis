import { Button, Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'

export const WidgetError = ({
  title,
  onRetry,
}: {
  title: string
  onRetry: () => void
}) => (
  <Box
    flex={1}
    flexDirection="column"
    justifyContent="end"
    alignItems="start"
    rowGap="s"
    paddingBottom="xl"
  >
    <Text>{title}</Text>
    <Button variant="secondary" size="sm" onClick={onRetry}>
      Retry
    </Button>
  </Box>
)
