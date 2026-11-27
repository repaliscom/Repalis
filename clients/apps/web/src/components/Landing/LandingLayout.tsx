'use client'

import { RepalisLogotype } from '@/components/Layout/Public/RepalisLogotype'
import Footer from '@/components/Organization/Footer'
import { usePostHog } from '@/hooks/posthog'
import { Modal } from '@repalis/orbit'
import {
  Sidebar,
  SidebarContent,
  SidebarHeader,
  SidebarProvider,
  SidebarTrigger,
  useSidebar,
} from '@repalis/ui/components/atoms/Sidebar'
import Link from 'next/link'
import { PropsWithChildren } from 'react'
import { AuthModal } from '../Auth/AuthModal'
import { useModal } from '../Modal/useModal'
import { LandingPageDesktopNavigation } from './DesktopNav'
import { NavLink } from './NavLink'

export default function Layout({ children }: PropsWithChildren) {
  return (
    <>
      <div className="sticky top-0 z-30 flex w-full flex-col">
        <LandingPageDesktopNavigation />
      </div>
      <div className="dark:bg-repalis-950 relative flex flex-col overflow-x-clip bg-white px-0 md:w-full md:flex-1 md:items-center md:px-12">
        <div className="flex flex-col gap-y-2 md:w-full md:max-w-7xl">
          <SidebarProvider className="absolute inset-0 flex flex-col items-start md:hidden">
            <LandingPageTopbar />
            <LandingPageMobileNavigation />
          </SidebarProvider>
          <div className="dark:bg-repalis-950 relative flex flex-col px-6 pt-32 md:w-full md:px-0 md:pt-0">
            {children}
          </div>
        </div>
        <LandingPageFooter />
      </div>
    </>
  )
}

interface NavigationItem {
  title: string
  href: string
  isActive?: (pathname: string) => boolean
  target?: '_blank'
}

const mobileNavigationItems: NavigationItem[] = [
  {
    title: 'Overview',
    href: '/',
    isActive: (pathname) => pathname === '/',
  },
  {
    title: 'Integrate',
    href: '/integrate',
  },
  {
    title: 'Documentation',
    href: 'https://repalis.com/docs',
    target: '_blank',
  },
  {
    title: 'Pricing',
    href: '/#pricing',
  },
  {
    title: 'Blog',
    href: '/blog',
  },
  {
    title: 'Company',
    href: '/company',
  },
  {
    title: 'Open Source',
    href: 'https://github.com/repaliscom',
    target: '_blank',
  },
  {
    title: 'Repalis on X',
    href: 'https://x.com/repalis',
    target: '_blank',
  },
]

const LandingPageMobileNavigation = () => {
  const sidebar = useSidebar()

  const posthog = usePostHog()
  const { isShown: isModalShown, hide: hideModal, show: showModal } = useModal()

  const onLoginClick = () => {
    posthog.capture('global:user:login:click')
    sidebar.toggleSidebar()
    showModal()
  }

  return (
    <>
      <Sidebar className="md:hidden">
        <SidebarHeader className="p-4">
          <Link href="/">
            <RepalisLogotype logoVariant="icon" />
          </Link>
        </SidebarHeader>
        <SidebarContent className="flex flex-col gap-y-6 px-6 py-2">
          <div className="flex flex-col gap-y-1">
            {mobileNavigationItems.map((item) => {
              return (
                <NavLink
                  key={item.title}
                  className="text-xl tracking-tight"
                  isActive={item.isActive}
                  target={item.target}
                  href={item.href}
                  onClick={sidebar.toggleSidebar}
                >
                  {item.title}
                </NavLink>
              )
            })}
          </div>
          <NavLink
            href="#"
            onClick={onLoginClick}
            className="text-xl tracking-tight"
          >
            Login
          </NavLink>
        </SidebarContent>
      </Sidebar>
      <Modal
        title="Sign in"
        isShown={isModalShown}
        hide={hideModal}
        modalContent={<AuthModal />}
        className="lg:w-full lg:max-w-[480px]"
      />
    </>
  )
}

const LandingPageTopbar = () => {
  return (
    <div className="z-30 flex w-full flex-row items-center justify-between px-6 py-6 md:hidden md:px-12">
      <RepalisLogotype
        className="mt-1 ml-2 md:hidden"
        logoVariant="logotype"
        size={100}
      />
      <SidebarTrigger className="md:hidden" />
    </div>
  )
}

const LandingPageFooter = () => {
  return (
    <div className="relative flex w-full flex-col items-center">
      <Footer />
    </div>
  )
}
