import GetStartedButton from '@/components/Auth/GetStartedButton'
import { Button, Grid, Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'
import { BackdropPanel } from './Backdrop'
import { SurfaceCards } from './SurfaceCards'
import { McpSession } from './McpSession'

const DOCS_HREF = '/docs/integrate/sdk/introduction'

export const IntegrateHero = () => (
  <Box
    as="section"
    width="100%"
    paddingTop={{ base: 'm', md: '3xl' }}
    paddingBottom={{ base: '3xl', md: '5xl' }}
    flexDirection="column"
    rowGap={{ base: '4xl', md: '5xl' }}
  >
    <Grid
      templateColumns={{ base: '1fr', lg: 'repeat(2, 1fr)' }}
      gap={{ base: '3xl', lg: 'l' }}
    >
      <Box
        flexDirection="column"
        justifyContent="between"
        alignItems="start"
        rowGap="3xl"
      >
        <Box flexDirection="column" rowGap="s">
          <Text variant="heading-m" as="h1" wrap="balance">
            Integrate Repalis
          </Text>
          <Text variant="heading-m" as="p" color="muted" wrap="balance">
            From one prompt to production billing
          </Text>
        </Box>
        <Box alignItems="center" columnGap="m">
          <GetStartedButton size="lg" text="Get Started" />
          <a href={DOCS_HREF}>
            <Button size="lg" variant="secondary">
              Documentation
            </Button>
          </a>
        </Box>
      </Box>
      <BackdropPanel
        src="/assets/landing/company/Repalis_Flow_03_No_Logo.jpg"
        aside="MCP"
      >
        <McpSession />
      </BackdropPanel>
    </Grid>
    <SurfaceCards />
  </Box>
)
