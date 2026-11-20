import { ArrowOutwardOutlined } from '@repalis/orbit/icons'
import { Grid, Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import Link from 'next/link'
import { PropsWithChildren } from 'react'
import { RepalisLogotype } from '../Layout/Public/RepalisLogotype'
import { CookiePreferencesButton } from '../Privacy/CookiePreferencesButton'

const Footer = () => {
  return (
    <Box
      as="footer"
      width="100%"
      maxWidth="80rem"
      flexDirection="column"
      marginTop={{ base: 'none', md: '2xl' }}
      paddingHorizontal={{ base: 'xl', md: 'none' }}
      paddingVertical={{ base: '4xl', md: '5xl' }}
      borderTopWidth={1}
      borderStyle="solid"
      borderColor="border-primary"
    >
      <Grid
        width="100%"
        templateColumns={{ base: '1fr', lg: 'repeat(2, 1fr)' }}
        gap={{ base: '3xl', lg: 'l' }}
      >
        <Box
          flexDirection="column"
          justifyContent="between"
          alignItems="start"
          rowGap="3xl"
        >
          <RepalisLogotype
            className="ml-2 md:ml-0"
            logoVariant="logotype"
            size={120}
          />
          <Box flexDirection="column" rowGap="xl">
            <Link
              href="/signup"
              className="w-fit border-b border-current pb-0.5"
            >
              <Box
                as="span"
                display="inline-flex"
                alignItems="center"
                columnGap="s"
                color="text-primary"
              >
                <Text as="span" variant="body" color="inherit">
                  Get Started
                </Text>
                <ArrowOutwardOutlined fontSize="inherit" />
              </Box>
            </Link>
            <Text variant="body" color="muted">
              &copy; Repalis {new Date().getFullYear()}
            </Text>
          </Box>
        </Box>

        <Grid
          templateColumns={{ base: '1fr', sm: 'repeat(2, 1fr)' }}
          columnGap="l"
          rowGap="3xl"
        >
          <FooterSection title="Features">
            <FooterLink href="/features/usage-billing">
              Usage Billing
            </FooterLink>
            <FooterLink href="/features/subscriptions">
              Subscriptions
            </FooterLink>
            <FooterLink href="/features/seats">Seats</FooterLink>
            <FooterLink href="/features/credits">Credits</FooterLink>
            <FooterLink href="/features/trials">Trials</FooterLink>
            <FooterLink href="/features/discounts">Discounts</FooterLink>
            <FooterLink href="/features/cost-insights">
              Cost Insights
            </FooterLink>
            <FooterLink href="/features/finance">Finance</FooterLink>
            <FooterLink href="/features/merchant-of-record">
              Merchant of Record
            </FooterLink>
          </FooterSection>

          <FooterSection title="Resources">
            <FooterLink href="/integrate">Integrate</FooterLink>
            <FooterLink href="/resources/why">Why Repalis</FooterLink>
            <FooterLink href="/resources/merchant-of-record">
              Merchant of Record
            </FooterLink>
            <FooterLink href="/resources/pricing">Pricing</FooterLink>
            <FooterLink href="/downloads">Downloads</FooterLink>
          </FooterSection>

          <FooterSection title="Company">
            <FooterLink href="/company">About Repalis</FooterLink>
            <FooterLink href="https://github.com/repaliscom/Repalis">
              GitHub
            </FooterLink>
            <FooterLink href="https://x.com/repalis">X / Twitter</FooterLink>
            <FooterLink href="/brand">
              Brand Assets
            </FooterLink>
            <FooterLink href="/legal">Legal</FooterLink>
            <CookiePreferencesButton />
          </FooterSection>

          <FooterSection title="Support">
            <FooterLink href="https://repalis.com/docs">Docs</FooterLink>
            <FooterLink href="mailto:contact@repalis.com">Contact</FooterLink>
            <FooterLink href="https://status.repalis.com">
              Service Status
            </FooterLink>
          </FooterSection>
        </Grid>
      </Grid>
    </Box>
  )
}

export default Footer

const FooterSection = ({
  title,
  children,
}: PropsWithChildren<{ title: string }>) => (
  <Box flexDirection="column" rowGap="m">
    <Text as="h3" variant="body" color="muted">
      {title}
    </Text>
    <Box flexDirection="column" rowGap="xs">
      {children}
    </Box>
  </Box>
)

const FooterLink = ({
  href,
  children,
}: PropsWithChildren<{ href: string }>) => (
  <Link href={href}>
    <Box
      as="span"
      display="inline-flex"
      alignItems="center"
      columnGap="xs"
      color={{ base: 'text-primary', hover: 'text-secondary' }}
      transitionProperty="colors"
      transitionDuration="fast"
    >
      <Text as="span" variant="body" color="inherit">
        {children}
      </Text>
    </Box>
  </Link>
)
