import { StartupProgramPage } from '@/components/Landing/startup-program/StartupProgramPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Repalis Startup Program',
  description:
    'Scale-tier pricing for a full year, free. For AI and SaaS startups building on Repalis.',
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
  return <StartupProgramPage />
}
