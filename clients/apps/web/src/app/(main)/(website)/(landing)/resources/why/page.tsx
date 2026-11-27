import { WhyRepalisPage } from '@/components/Landing/resources/WhyRepalisPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Why Repalis is the best way to monetize your software',
  description: 'Learn why Repalis is the best way to monetize your software',
  keywords:
    'monetize, monetization, switch, migration, payment infrastructure, saas, monetization, developer tools',
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
  return <WhyRepalisPage />
}
