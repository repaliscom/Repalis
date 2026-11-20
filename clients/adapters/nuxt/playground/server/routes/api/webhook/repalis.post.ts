export default defineEventHandler((event) => {
  const {
    private: { repalisWebhookSecret },
  } = useRuntimeConfig()

  const webhooksHandler = Webhooks({
    webhookSecret: repalisWebhookSecret,
    onPayload: async () => {
      // Handle the payload
      // No need to return an acknowledge response
    },
  })

  return webhooksHandler(event)
})
