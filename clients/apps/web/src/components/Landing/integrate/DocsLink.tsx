import { Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import { ArrowRight } from '@repalis/orbit/icons'
export const DocsLink = ({ href, label }: { href: string; label: string }) => (
  <a href={href}>
    <Box
      alignItems="center"
      columnGap="xs"
      color={{ base: 'text-primary', hover: 'text-secondary' }}
      transitionProperty="colors"
      transitionDuration="fast"
    >
      <Text variant="body" color="inherit">
        {label}
      </Text>
      <ArrowRight size={16} />
    </Box>
  </a>
)
