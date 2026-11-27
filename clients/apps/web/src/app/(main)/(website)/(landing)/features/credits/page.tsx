import { CreditsPage } from '@/components/Landing/features/CreditsPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Credits & Prepaid Balances',
  description:
    'Prepaid usage for your API. Issue credits, draw down balances, and let metered pricing handle the overage.',
  keywords:
    'prepaid billing, api credits, usage credits, wallet, prepay, metered billing',
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
  return <CreditsPage />
}
