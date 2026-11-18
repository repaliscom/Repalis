import { PolarVsPaddlePage } from '@/components/Landing/comparison/PolarPaddlePage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Repalis vs Paddle',
  description:
    'Repalis vs Paddle: compare two Merchant of Record platforms for SaaS and digital products, including billing models, usage-based pricing and transaction fees.',
  keywords:
    'repalis vs paddle, paddle alternative, merchant of record, saas billing, subscriptions, usage-based billing',
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
  return <PolarVsPaddlePage />
}
