import { LOGO_ICON_VIEWBOX, LOGO_MARK_PATH } from '@/components/Brand/logos/paths'
import { Box } from '@repalis/orbit/Box'

const SIZE = 96

export const HeroMark = () => (
  <Box
    display={{ base: 'none', lg: 'block' }}
    color="text-primary"
    opacity={0.15}
  >
    <svg
      width={SIZE}
      height={SIZE}
      viewBox={LOGO_ICON_VIEWBOX}
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      aria-hidden="true"
    >
      <path d={LOGO_MARK_PATH} fill="currentColor" />
    </svg>
  </Box>
)
