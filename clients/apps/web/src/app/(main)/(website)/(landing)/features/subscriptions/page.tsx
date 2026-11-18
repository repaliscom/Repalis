import { SubscriptionsPage } from '@/components/Landing/features/SubscriptionsPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Subscriptions',
  description:
    'Recurring revenue on autopilot. Renewals, proration, dunning, and customer self-service — all handled.',
  keywords:
    'subscriptions, recurring billing, saas billing, proration, dunning, renewal, customer portal',
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
  return <SubscriptionsPage />
}
