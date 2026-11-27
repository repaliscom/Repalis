import { BrandPage } from '@/components/Brand/BrandPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Brand',
  alternates: {
    canonical: 'https://repalis.com/brand',
  },
  description:
    'The Repalis brand system: logo, color, typography, illustration, voice and marketing.',
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
  return <BrandPage />
}
