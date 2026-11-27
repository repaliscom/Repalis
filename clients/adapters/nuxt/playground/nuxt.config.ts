export default defineNuxtConfig({
  modules: ['../src/module'],
  repalis: {},
  devtools: { enabled: true },
  compatibilityDate: '2025-02-25',
  runtimeConfig: {
    private: {
      repalisAccessToken: '',
      repalisServer: '',
      repalisCheckoutSuccessUrl: '',
      repalisWebhookSecret: '',
    },
  },
})
