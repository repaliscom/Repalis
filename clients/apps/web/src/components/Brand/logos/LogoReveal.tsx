'use client'

import { m, useReducedMotion, type Variants } from 'motion/react'
import {
  LOGO_ICON_VIEWBOX,
  LOGO_MARK_HORIZONTAL_PATH,
  LOGO_MARK_PATH,
  LOGO_TYPE_VIEWBOX,
  LOGO_WORDMARK_PATH,
} from './paths'
import { LOGO_REVEAL_EASE } from './timing'

const EASE_FADE = [0.4, 0, 0.6, 1] as const

const markVariants: Variants = {
  hidden: { opacity: 0, y: 8 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.7, ease: LOGO_REVEAL_EASE },
  },
}

const wordmarkVariants: Variants = {
  hidden: { opacity: 0, x: -20 },
  visible: {
    opacity: 1,
    x: 0,
    transition: {
      x: { duration: 0.8, delay: 0.12, ease: LOGO_REVEAL_EASE },
      opacity: { duration: 0.6, delay: 0.18, ease: EASE_FADE },
    },
  },
}

const LogoReveal = ({
  variant = 'logotype',
  size,
  className,
}: {
  variant?: 'icon' | 'logotype'
  size?: number
  className?: string
}) => {
  const reducedMotion = useReducedMotion()

  return (
    <m.svg
      width={size}
      height={variant === 'icon' ? size : undefined}
      viewBox={variant === 'icon' ? LOGO_ICON_VIEWBOX : LOGO_TYPE_VIEWBOX}
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={className}
      role="img"
      aria-label="Repalis"
      initial={reducedMotion ? 'visible' : 'hidden'}
      whileInView="visible"
      viewport={{ once: true, amount: 0.6 }}
    >
      <m.path
        d={variant === 'icon' ? LOGO_MARK_PATH : LOGO_MARK_HORIZONTAL_PATH}
        fill="currentColor"
        variants={markVariants}
      />
      {variant === 'logotype' ? (
        <m.path
          d={LOGO_WORDMARK_PATH}
          fill="currentColor"
          variants={wordmarkVariants}
        />
      ) : null}
    </m.svg>
  )
}

export default LogoReveal
