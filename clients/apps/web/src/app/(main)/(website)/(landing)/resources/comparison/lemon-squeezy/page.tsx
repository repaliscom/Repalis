import { RepalisVsLemonSqueezyPage } from '@/components/Landing/comparison/RepalisLemonSqueezyPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Repalis vs Lemon Squeezy',
  description:
    'Repalis vs Lemon Squeezy: compare two Merchant of Record platforms for developers, including open-source billing, usage-based pricing and transaction fees.',
  keywords:
    'repalis vs lemon squeezy, lemon squeezy alternative, merchant of record, saas billing, digital products',
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
  return <RepalisVsLemonSqueezyPage />
}
