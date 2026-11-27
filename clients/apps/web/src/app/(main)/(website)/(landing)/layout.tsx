import { HomepageAgentSignupHint } from '@/components/Auth/AgentSignupHint'
import { PropsWithChildren } from 'react'
import LandingLayout from '../../../../components/Landing/LandingLayout'

export const dynamic = 'force-static'
export const dynamicParams = false

const jsonLd = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'Organization',
      '@id': 'https://repalis.com/#organization',
      name: 'Repalis',
      url: 'https://repalis.com/',
      logo: {
        '@type': 'ImageObject',
        url: 'https://repalis.com/assets/brand/app-icon.png',
      },
      description:
        'Repalis is a developer-first monetization platform and Merchant of Record for software companies — handling payments, digital products, subscriptions, and global billing infrastructure.',
      sameAs: ['https://github.com/repaliscom/Repalis', 'https://x.com/repalis'],
      contactPoint: {
        '@type': 'ContactPoint',
        contactType: 'customer support',
        email: 'contact@repalis.com',
        url: 'https://repalis.com',
      },
      address: {
        '@type': 'PostalAddress',
        streetAddress: 'Gwalior, Madhya Pradesh',
        addressLocality: 'Gwalior',
        addressRegion: 'MP',
        postalCode: '474001',
        addressCountry: 'IN',
      },
    },
    {
      '@type': 'WebSite',
      '@id': 'https://repalis.com/#website',
      name: 'Repalis',
      url: 'https://repalis.com/',
      publisher: {
        '@id': 'https://repalis.com/#organization',
      },
    },
  ],
}

export default function Layout({ children }: PropsWithChildren) {
  return (
    <>
      <HomepageAgentSignupHint />
      <script
        type="application/ld+json"
        // oxlint-disable-next-line react/no-danger
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(jsonLd).replace(/</g, '\\u003c'),
        }}
      />
      <LandingLayout>{children}</LandingLayout>
    </>
  )
}
