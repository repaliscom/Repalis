'use client'

import { m, useReducedMotion } from 'motion/react'
import { LOGO_ICON_VIEWBOX, LOGO_MARK_PATH } from './paths'

const LogoLoader = ({
  size = 29,
  className,
}: {
  size?: number
  className?: string
}) => {
  const reducedMotion = useReducedMotion()

  const svgProps = {
    width: size,
    height: size,
    viewBox: LOGO_ICON_VIEWBOX,
    fill: 'none',
    xmlns: 'http://www.w3.org/2000/svg',
    className,
    role: 'status',
    'aria-label': 'Loading',
  }

  return (
    <m.svg
      {...svgProps}
      animate={
        reducedMotion
          ? { opacity: [1, 0.4, 1] }
          : { opacity: [1, 0.35, 1], scale: [1, 0.96, 1] }
      }
      transition={{ duration: 1.6, ease: 'easeInOut', repeat: Infinity }}
    >
      <path d={LOGO_MARK_PATH} fill="currentColor" />
    </m.svg>
  )
}

export default LogoLoader
