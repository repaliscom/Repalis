import { RepalisVsStripePage } from '@/components/Landing/comparison/RepalisStripePage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Repalis vs Stripe',
  description:
    'Repalis vs Stripe: Repalis is a Merchant of Record that handles payments, subscriptions, usage-based billing and global sales tax for you, while Stripe leaves tax and compliance to you.',
  keywords:
    'repalis vs stripe, stripe alternative, merchant of record, saas billing, usage-based billing, payment infrastructure',
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
  return <RepalisVsStripePage />
}
