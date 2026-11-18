import { Box, type BoxProps } from '@polar-sh/orbit/Box'

export const LoadingBox = (props: BoxProps) => (
  <Box
    display="block"
    {...props}
    // oxlint-disable-next-line polar/no-classname-box
    className="dark:bg-repalis-700 animate-pulse bg-gray-100"
  />
)
