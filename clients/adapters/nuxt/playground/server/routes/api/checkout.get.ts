export default defineEventHandler((event) => {
  const {
    private: { repalisAccessToken, polarCheckoutSuccessUrl, polarServer },
  } = useRuntimeConfig()

  const checkoutHandler = Checkout({
    accessToken: repalisAccessToken,
    successUrl: polarCheckoutSuccessUrl,
    environment: polarServer as 'sandbox' | 'production',
  })

  return checkoutHandler(event)
})
