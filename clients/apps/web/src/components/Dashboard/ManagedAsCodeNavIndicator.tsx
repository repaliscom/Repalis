'use client'

import { LockOutlined } from '@repalis/orbit/icons'
import { Tooltip, TooltipContent, TooltipTrigger } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'

export const ManagedAsCodeNavIndicator = () => (
  <Tooltip>
    <TooltipTrigger asChild>
      <Box
        as="span"
        display="inline-flex"
        color="text-tertiary"
        aria-label="Your catalog is managed in code"
      >
        <LockOutlined fontSize="inherit" />
      </Box>
    </TooltipTrigger>
    <TooltipContent side="top" align="center">
      Your catalog is managed in code
    </TooltipContent>
  </Tooltip>
)
