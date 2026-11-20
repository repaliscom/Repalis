export default defineEventHandler((event) => {
  const {
    private: { repalisAccessToken, repalisCheckoutSuccessUrl, repalisServer },
  } = useRuntimeConfig()

  const checkoutHandler = Checkout({
    accessToken: repalisAccessToken,
    successUrl: repalisCheckoutSuccessUrl,
    environment: repalisServer as 'sandbox' | 'production',
  })

  return checkoutHandler(event)
})
