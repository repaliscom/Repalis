import { CookieConsent } from '@/components/Privacy/CookieConsent'
import { CONFIG } from '@/utils/config'
import { headers } from 'next/headers'
import { Metadata } from 'next/types'
import { RepalisThemeProvider } from '../providers'

export async function generateMetadata(): Promise<Metadata> {
  const baseMetadata: Metadata = {
    title: {
      template: '%s | Repalis',
      default: 'Repalis — Merchant of Record & Developer Monetization',
    },
    description:
      'Repalis is the developer-first Merchant of Record: global payments, subscriptions, digital products, and billing infrastructure.',
    openGraph: {
      images: 'https://repalis.com/assets/brand/repalis_og.jpg',
      type: 'website',
      siteName: 'Repalis',
      title: 'Repalis — Merchant of Record & Developer Monetization',
      description:
        'Create digital products and SaaS billing with flexible pricing models and seamless payment processing.',
      locale: 'en_US',
    },
    twitter: {
      images: 'https://repalis.com/assets/brand/repalis_og.jpg',
      card: 'summary_large_image',
      title: 'Repalis — Merchant of Record & Developer Monetization',
      description:
        'Create digital products and SaaS billing with flexible pricing models and seamless payment processing.',
    },
    metadataBase: new URL('https://repalis.com/'),
    alternates: {
      canonical: 'https://repalis.com/',
    },
  }

  if (CONFIG.IS_SANDBOX) {
    return {
      ...baseMetadata,
      robots: {
        index: false,
        follow: false,
        googleBot: {
          index: false,
          follow: false,
        },
      },
    }
  }

  return {
    ...baseMetadata,
    robots: {
      index: true,
      follow: true,
      googleBot: {
        index: true,
        follow: true,
        'max-video-preview': -1,
        'max-image-preview': 'large',
        'max-snippet': -1,
      },
    },
  }
}

export default async function MainLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const headersList = await headers()
  const countryCode = headersList.get('x-vercel-ip-country')

  return (
    <RepalisThemeProvider>
      <link
        rel="preload"
        href="/fonts/PPNeueMontreal-VariableUpright.woff2"
        as="font"
        type="font/woff2"
        crossOrigin=""
      />
      <link
        rel="preload"
        href="/fonts/GeistMono-Variable.woff2"
        as="font"
        type="font/woff2"
        crossOrigin=""
      />
      <div className="dark:bg-repalis-950 h-full bg-white dark:text-white">
        {children}
        <CookieConsent countryCode={countryCode} />
      </div>
    </RepalisThemeProvider>
  )
}
