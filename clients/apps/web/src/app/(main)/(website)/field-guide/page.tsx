import FieldGuideReader from '@/components/FieldGuide/Reader'
import { Metadata } from 'next'

const title = 'Agent-first Billing: A Field Guide'
const description =
  'How we’re building the most ambitious metering and billing engine for AI software: billing as code, events, meters, local-first checks, guardrails, credits, entitlements and agents. Now in early access.'
const image = {
  url: 'https://repalis.com/assets/field-guide/og.jpg',
  width: 1200,
  height: 630,
  alt: title,
}

export const metadata: Metadata = {
  title,
  description,
  keywords:
    'agent-first billing, usage-based billing, metering, ai billing, credits, entitlements, billing as code, repalis',
  alternates: {
    canonical: 'https://repalis.com/field-guide',
  },
  openGraph: {
    title,
    description,
    url: 'https://repalis.com/field-guide',
    siteName: 'Repalis',
    type: 'website',
    images: [image],
  },
  twitter: {
    card: 'summary_large_image',
    title,
    description,
    images: [image],
  },
}

export default function Page() {
  return <FieldGuideReader />
}
