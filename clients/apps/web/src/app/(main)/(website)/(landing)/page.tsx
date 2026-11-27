import { Metadata } from 'next'
import LandingPage from '../../../../components/Landing/LandingPage'
export const metadata: Metadata = {
  title: 'Repalis — Developer Monetization Platform & Merchant of Record',
  description:
    'Repalis is the Merchant of Record for developers: global payments, subscriptions, digital products, and billing infrastructure with tax handled for you.',
  keywords:
    'monetization, merchant of record, saas, digital products, platform, developer, open source, funding, open source, economy',
  openGraph: {
    siteName: 'Repalis',
    type: 'website',
    images: [
      {
        url: 'https://repalis.com/assets/brand/repalis_og.jpg',
        width: 1200,
        height: 630,
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    images: [
      {
        url: 'https://repalis.com/assets/brand/repalis_og.jpg',
        width: 1200,
        height: 630,
        alt: 'Repalis',
      },
    ],
  },
}

export default function Page() {
  return <LandingPage />
}
