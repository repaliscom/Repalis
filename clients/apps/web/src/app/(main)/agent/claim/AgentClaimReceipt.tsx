import ProductPriceLabel from '@/components/Products/ProductPriceLabel'
import { schemas } from '@repalis/client'
import { Text } from '@repalis/orbit'
import { Box } from '@repalis/orbit/Box'

const AgentClaimReceipt = ({
  claim: { organization, products },
}: {
  claim: schemas['AgentClaim']
}) => {
  if (!organization) return null
  return (
    <Box
      flexDirection="column"
      rowGap="xl"
      paddingTop="xl"
      borderTopWidth={1}
      borderStyle="solid"
      borderColor="border-secondary"
    >
      <Box flexDirection="column" rowGap="xs">
        <Text variant="caption" color="muted">
          Your organization
        </Text>
        <Text>{organization.name}</Text>
      </Box>
      {products.length > 0 && (
        <Box flexDirection="column" rowGap="xs">
          <Text variant="caption" color="muted">
            Products
          </Text>
          {products.map((product) => (
            <Box key={product.id} justifyContent="between" alignItems="center">
              <Text>{product.name}</Text>
              <Text>
                <ProductPriceLabel
                  product={product}
                  currency={product.prices[0]?.price_currency ?? 'usd'}
                />
              </Text>
            </Box>
          ))}
        </Box>
      )}
    </Box>
  )
}

export default AgentClaimReceipt
