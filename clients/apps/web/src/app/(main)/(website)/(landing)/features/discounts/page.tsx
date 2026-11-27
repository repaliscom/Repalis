import { DiscountsPage } from '@/components/Landing/features/DiscountsPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Discounts & Coupons',
  description:
    'Coupons, promo codes, and recurring discounts. Apply automatically at checkout, prefill via URL, or via the API.',
  keywords:
    'discounts, coupons, promo codes, percentage discount, fixed amount discount, recurring discount',
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
  return <DiscountsPage />
}
