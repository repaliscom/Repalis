export default defineEventHandler((event) => {
  const {
    private: { repalisAccessToken, repalisServer },
  } = useRuntimeConfig()

  const customerPortalHandler = CustomerPortal({
    accessToken: repalisAccessToken,
    environment: repalisServer as 'sandbox' | 'production',
    getCustomerId: () => {
      return Promise.resolve('9d89909b-216d-475e-8005-053dba7cff07')
    },
  })

  return customerPortalHandler(event)
})
