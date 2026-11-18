import { IntegratePage } from '@/components/Landing/integrate/IntegratePage'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Integrate Repalis',
  description:
    'Integrate Repalis with the TypeScript and Python SDKs, the REST API, the CLI or the MCP server. One billing stack, whichever surface you work from.',
  keywords:
    'repalis sdk, repalis api, repalis cli, repalis mcp, billing api, usage billing sdk, webhooks',
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
  return <IntegratePage />
}
