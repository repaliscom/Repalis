import { Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import { ArrowRight } from '@repalis/orbit/icons'
import Link from 'next/link'

export const WidgetLink = ({ href }: { href: string }) => (
  <Link href={href} className="hover:opacity-60">
    <Box alignItems="center" columnGap="xs" color="text-secondary">
      <Text color="muted">View all</Text>
      <ArrowRight className="h-3.5 w-3.5" />
    </Box>
  </Link>
)
