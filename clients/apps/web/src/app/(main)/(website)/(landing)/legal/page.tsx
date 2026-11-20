import {
  FeatureChapter,
  SectionTitle,
} from '@/components/Landing/features/FeatureChapter'
import { Grid, Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import { ArrowRight } from '@repalis/orbit/icons'
import { Metadata } from 'next'
import Link from 'next/link'

export const metadata: Metadata = {
  title: 'Legal',
  description: 'Legal documents',
  keywords:
    'legal, privacy, tos, terms of service, merchant of record, saas, digital products, platform, developer, open source, funding, open source, economy',
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

interface LegalDocument {
  title: string
  description: string
  href: string
}

interface LegalGroup {
  title: string
  documents: LegalDocument[]
}

const GROUPS: LegalGroup[] = [
  {
    title: 'Terms',
    documents: [
      {
        title: 'Master Services Terms',
        description: 'Core contractual terms for using Repalis as a platform.',
        href: '/legal/master-services-terms',
      },
      {
        title: 'Acceptable Use Policy',
        description: 'Rules and restrictions for using Repalis services.',
        href: '/legal/acceptable-use-policy',
      },
      {
        title: 'Checkout Buyer Terms',
        description: 'Terms that apply to buyers purchasing through checkout.',
        href: '/legal/checkout-buyer-terms',
      },
    ],
  },
  {
    title: 'Privacy',
    documents: [
      {
        title: 'Privacy Policy',
        description: 'How Repalis collects, uses, and protects personal data.',
        href: '/legal/privacy-policy',
      },
      {
        title: 'Data Processing Addendum',
        description: 'Data protection terms governing processing activities.',
        href: '/legal/data-processing-addendum',
      },
    ],
  },
  {
    title: 'Partners',
    documents: [
      {
        title: 'Sub-processors',
        description:
          'Third-party service providers and affiliates supporting the delivery and operation of the Repalis platform.',
        href: '/legal/sub-processors',
      },
      {
        title: 'Payment Processor Partners',
        description: 'Information about payment partners used by Repalis.',
        href: '/legal/payment-processor-partners',
      },
    ],
  },
]

const DocumentRow = ({ title, description, href }: LegalDocument) => (
  <Link href={href} prefetch>
    <Box
      alignItems="start"
      justifyContent="between"
      columnGap="2xl"
      paddingVertical="xl"
      borderTopWidth={1}
      borderStyle="solid"
      borderColor="border-primary"
      color={{ base: 'text-primary', hover: 'text-secondary' }}
      transitionProperty="colors"
      transitionDuration="fast"
    >
      <Box flexDirection="column">
        <Text variant="heading-xxs" as="h3" color="inherit">
          {title}
        </Text>
        <Text variant="heading-xxs" as="p" color="muted" wrap="pretty">
          {description}
        </Text>
      </Box>
      <Box flexShrink={0} paddingTop="xs">
        <ArrowRight size={16} />
      </Box>
    </Box>
  </Link>
)

export default function Legal() {
  return (
    <Box width="100%" flexDirection="column">
      <Box
        as="section"
        width="100%"
        paddingTop={{ base: 'm', md: '3xl' }}
        paddingBottom={{ base: '3xl', md: '5xl' }}
      >
        <Grid
          templateColumns={{ base: '1fr', lg: 'repeat(2, 1fr)' }}
          gap={{ base: '2xl', lg: 'l' }}
        >
          <Box flexDirection="column">
            <Text variant="heading-m" as="h1" wrap="balance">
              Legal
            </Text>
            <Text variant="heading-m" as="p" color="muted" wrap="balance">
              The terms and policies behind Repalis
            </Text>
          </Box>
        </Grid>
      </Box>

      {GROUPS.map((group) => (
        <FeatureChapter
          key={group.title}
          aside={<SectionTitle>{group.title}</SectionTitle>}
          content={
            <Box flexDirection="column">
              {group.documents.map((document) => (
                <DocumentRow key={document.href} {...document} />
              ))}
            </Box>
          }
        />
      ))}
    </Box>
  )
}
