import { FinancePage } from '@/components/Landing/features/FinancePage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Finance & Payouts',
  description:
    'Live balance, transactions ledger, transparent fees, and manual payouts. All visible.',
  keywords:
    'finance, payouts, transactions, ledger, balance, fees, stripe connect, multi-currency',
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
  return <FinancePage />
}
