# =============================================================================
# Vercel — Sandbox frontend (sandbox.repalis.com)
# =============================================================================




module "vercel" {
  source = "../modules/vercel"

  name     = "repalis-sandbox"
  git_repo = "repaliscom/Repalis"

  preview_deployments_disabled = true

  domains = [
    {
      name = "sandbox.repalis.com"
      dns = {
        zone_id = "22bcd1b07ec25452aab472486bc8df94"
        content = "50b537f2e43aa1b6.vercel-dns-016.com"
        proxied = true
      }
    },
  ]

  config = {
    next_public_api_url                             = "https://sandbox-api.repalis.com"
    next_public_backoffice_url                      = "https://${local.private_backoffice_hostname}"
    next_public_sentry_dsn                          = var.next_public_sentry_dsn
    next_public_posthog_token                       = var.next_public_posthog_token
    next_public_apple_domain_association            = var.next_public_apple_domain_association
    next_public_checkout_embed_script_src           = "https://cdn.jsdelivr.net/npm/@repalis/checkout@0.1/dist/embed.global.js"
    next_public_stripe_payment_method_configuration = var.next_public_stripe_payment_method_configuration
    s3_public_images_bucket_protocol                = "https"
    s3_public_images_bucket_hostname                = "repalis-public-sandbox-files.s3.amazonaws.com"
    s3_public_images_bucket_port                    = null
    s3_public_images_bucket_pathname                = "/product_media/**"
    s3_upload_origins                               = "https://repalis-sandbox-files.s3.amazonaws.com https://repalis-public-sandbox-files.s3.amazonaws.com"
    repalis_checkout_embed_script_allowed_origins     = "https://repalis.com,https://sandbox.repalis.com"
    enable_experimental_corepack                    = "1"
  }

  secrets = {
    pydantic_ai_gateway_api_key = var.pydantic_ai_gateway_api_key
    mintlify_assistant_api_key  = var.mintlify_assistant_api_key
    gram_api_key                = var.gram_api_key
    sentry_auth_token           = var.sentry_auth_token
  }

  # Environment-specific or target-varies-by-env.
  environment_variables = [
    { key = "NEXT_PUBLIC_FRONTEND_BASE_URL", value = "https://sandbox.repalis.com" },
    { key = "NEXT_PUBLIC_ENVIRONMENT", value = "sandbox" },
    { key = "REPALIS_AUTH_COOKIE_KEY", value = "repalis_sandbox_session" },
    { key = "NEXT_PUBLIC_PRODUCT_LINK_BASE_URL", value = "https://sandbox.repalis.com/api/checkout?price=" },
    { key = "NEXT_PUBLIC_STRIPE_KEY", value = var.stripe_publishable_key, target = ["production", "development"] },
    { key = "NEXT_PUBLIC_STRIPE_KEY", value = var.stripe_publishable_key_preview, target = ["preview"], sensitive = true },
    { key = "MCP_OAUTH2_CLIENT_ID", value = var.mcp_oauth2_client_id, target = ["production", "preview", "development"] },
    { key = "MCP_OAUTH2_CLIENT_SECRET", value = var.mcp_oauth2_client_secret, target = ["production", "preview", "development"] },
  ]
}

