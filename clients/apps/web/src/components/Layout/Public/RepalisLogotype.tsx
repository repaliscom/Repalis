'use client'

import LogoIcon from '@/components/Brand/logos/LogoIcon'
import LogoType from '@/components/Brand/logos/LogoType'

import {
  LOGO_MARK_HORIZONTAL_PATH,
  LOGO_MARK_PATH,
  LOGO_WORDMARK_PATH,
} from '@/components/Brand/logos/paths'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@repalis/ui/components/ui/dropdown-menu'
import { ArrowDown, Clipboard } from '@repalis/orbit/icons'
import Link from 'next/link'
import { MouseEventHandler, useCallback, useRef, useState } from 'react'
import { twMerge } from 'tailwind-merge'
import { useOutsideClick } from '@/utils/useOutsideClick'

export const RepalisLogotype = ({
  logoVariant = 'icon',
  size,
  className,
  logoClassName,
  href,
}: {
  logoVariant?: 'icon' | 'logotype'
  size?: number
  className?: string
  logoClassName?: string
  href?: string
}) => {
  const RepalisLogotypeRef = useRef<HTMLDivElement>(null)

  const [RepalisLogotypeOpen, setRepalisLogotypeOpen] = useState(false)

  useOutsideClick([RepalisLogotypeRef], () => setRepalisLogotypeOpen(false))

  const handleTriggerClick: MouseEventHandler<HTMLElement> = useCallback(
    (e) => {
      e.preventDefault()
      e.stopPropagation()
      setRepalisLogotypeOpen(true)
    },
    [],
  )

  const handleCopyLogoToClipboard = useCallback(() => {
    navigator.clipboard.writeText(
      logoVariant === 'icon' ? RepalisIconSVGString : RepalisLogoSVGString,
    )
    setRepalisLogotypeOpen(false)
  }, [logoVariant])

  const LogoComponent =
    logoVariant === 'logotype' ? (
      <LogoType
        className={twMerge(
          '-ml-2 text-black md:ml-0 dark:text-white',
          logoClassName,
        )}
        width={size ?? 100}
      />
    ) : (
      <LogoIcon
        className={twMerge('text-black dark:text-white', logoClassName)}
        size={size ?? 42}
      />
    )

  return (
    <div className={twMerge('relative flex flex-row items-center', className)}>
      <DropdownMenu open={RepalisLogotypeOpen}>
        <DropdownMenuTrigger
          className={href ? 'cursor-pointer' : ''}
          onContextMenu={handleTriggerClick}
        >
          {href ? (
            <Link href={href}>{LogoComponent}</Link>
          ) : (
            <div>{LogoComponent}</div>
          )}
        </DropdownMenuTrigger>
        <DropdownMenuContent ref={RepalisLogotypeRef} align="start">
          <DropdownMenuItem
            className="flex flex-row gap-x-3"
            onClick={handleCopyLogoToClipboard}
          >
            <Clipboard className="h-3 w-3" />
            <span>Copy Logo as SVG</span>
          </DropdownMenuItem>
          <DropdownMenuItem
            className="flex flex-row gap-x-3"
            onClick={() => setRepalisLogotypeOpen(false)}
          >
            <ArrowDown className="h-3 w-3" />
            <Link href="/assets/brand/repalis_brand.zip">
              Download Branding Assets
            </Link>
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  )
}

const RepalisIconSVGString = `<svg width="120" height="96" viewBox="0 0 120 96" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="${LOGO_MARK_PATH}" fill="white"/></svg>`

const RepalisLogoSVGString = `<svg width="372" height="81" viewBox="0 0 372 81" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="${LOGO_MARK_HORIZONTAL_PATH}" fill="white"/><path d="${LOGO_WORDMARK_PATH}" fill="white"/></svg>`
