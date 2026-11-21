'use client'

import { m, useReducedMotion, type Variants } from 'motion/react'
import { useId } from 'react'
import {
  LOGO_ICON_VIEWBOX,
  LOGO_MARK_ARC_PATH,
  LOGO_MARK_ARC_STROKE_WIDTH,
  LOGO_MARK_ARC_STROKES,
  LOGO_MARK_HUB,
  LOGO_MARK_RAYS_PATH,
  LOGO_MARK_HORIZONTAL_ARC_PATH,
  LOGO_MARK_HORIZONTAL_ARC_STROKE_WIDTH,
  LOGO_MARK_HORIZONTAL_ARC_STROKES,
  LOGO_MARK_HORIZONTAL_HUB,
  LOGO_MARK_HORIZONTAL_RAYS_PATH,
  LOGO_TYPE_VIEWBOX,
  LOGO_WORDMARK_PATH,
} from './paths'
import { LOGO_REVEAL_ARC, LOGO_REVEAL_EASE, LOGO_REVEAL_RAYS } from './timing'

const EASE_FADE = [0.4, 0, 0.6, 1] as const

const rays: Variants = {
  hidden: { r: 0 },
  visible: (radius: number) => ({
    r: radius,
    transition: { ...LOGO_REVEAL_RAYS, ease: LOGO_REVEAL_EASE },
  }),
}

const arc: Variants = {
  hidden: { pathLength: 0 },
  visible: {
    pathLength: 1,
    transition: { ...LOGO_REVEAL_ARC, ease: LOGO_REVEAL_EASE },
  },
}

const wordmark: Variants = {
  hidden: { opacity: 0, x: -40 },
  visible: {
    opacity: 1,
    x: 0,
    transition: {
      x: { duration: 1.1, delay: 0.08, ease: LOGO_REVEAL_EASE },
      opacity: { duration: 0.55, delay: 0.3, ease: EASE_FADE },
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
  const id = useId()
  const reducedMotion = useReducedMotion()

  const isIcon = variant === 'icon'
  const hub = isIcon ? LOGO_MARK_HUB : LOGO_MARK_HORIZONTAL_HUB
  const arcStrokes = isIcon
    ? LOGO_MARK_ARC_STROKES
    : LOGO_MARK_HORIZONTAL_ARC_STROKES
  const arcStrokeWidth = isIcon
    ? LOGO_MARK_ARC_STROKE_WIDTH
    : LOGO_MARK_HORIZONTAL_ARC_STROKE_WIDTH
  const raysPath = isIcon
    ? LOGO_MARK_RAYS_PATH
    : LOGO_MARK_HORIZONTAL_RAYS_PATH
  const arcPath = isIcon
    ? LOGO_MARK_ARC_PATH
    : LOGO_MARK_HORIZONTAL_ARC_PATH

  return (
    <m.svg
      width={size}
      height={isIcon ? size : undefined}
      viewBox={isIcon ? LOGO_ICON_VIEWBOX : LOGO_TYPE_VIEWBOX}
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={className}
      role="img"
      aria-label="Repalis"
      initial={reducedMotion ? 'visible' : 'hidden'}
      whileInView="visible"
      viewport={{ once: true, amount: 0.6 }}
    >
      <mask id={`${id}-rays`}>
        <m.circle
          cx={hub.cx}
          cy={hub.cy}
          fill="white"
          custom={hub.r}
          variants={rays}
        />
      </mask>
      <mask id={`${id}-arc`}>
        {arcStrokes.map((d) => (
          <m.path
            key={d}
            d={d}
            stroke="white"
            strokeWidth={arcStrokeWidth}
            strokeLinecap="round"
            variants={arc}
          />
        ))}
      </mask>
      <path d={raysPath} fill="currentColor" mask={`url(#${id}-rays)`} />
      <path d={arcPath} fill="currentColor" mask={`url(#${id}-arc)`} />
      {!isIcon ? (
        <m.path
          d={LOGO_WORDMARK_PATH}
          fill="currentColor"
          variants={wordmark}
        />
      ) : null}
    </m.svg>
  )
}

export default LogoReveal
