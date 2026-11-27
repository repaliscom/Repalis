import { EventIngestionPage } from '@/components/Landing/features/EventIngestionPage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Event Ingestion',
  description:
    'Send an event when usage happens. One API call or an SDK strategy for LLMs, streams and storage, and every token is ready to meter and bill.',
  keywords:
    'event ingestion, usage events, llm token billing, metered billing, usage billing api, ai billing',
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
  return <EventIngestionPage />
}
