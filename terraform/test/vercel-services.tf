# =============================================================================
# Vercel Services — full-stack test deployment
# =============================================================================

locals {
  # Vercel's Postgres and Redis integrations own REPALIS_POSTGRES_URL_NON_POOLING
  # and REPALIS_REDIS_URL. They are intentionally not duplicated here.
  vercel_services_environment_variables = {
    SENTRY_ORG = {
      value     = "repalis"
      sensitive = false
    }
    SENTRY_PROJECT = {
      value     = "dashboard"
      sensitive = false
    }
    NEXT_PUBLIC_ENVIRONMENT = {
      value     = "test"
      sensitive = false
    }
    NEXT_PUBLIC_BACKOFFICE_URL = {
      value     = "/api/backoffice"
      sensitive = false
    }
    NEXT_PUBLIC_SANDBOX_FRONTEND_BASE_URL = {
      value     = "https://sandbox.repalis.com"
      sensitive = false
    }
    NEXT_PUBLIC_SENTRY_DSN = {
      value     = var.next_public_sentry_dsn
      sensitive = false
    }
    NEXT_PUBLIC_POSTHOG_TOKEN = {
      value     = var.next_public_posthog_token
      sensitive = false
    }
    NEXT_PUBLIC_APPLE_DOMAIN_ASSOCIATION = {
      value     = var.next_public_apple_domain_association
      sensitive = false
    }
    NEXT_PUBLIC_CHECKOUT_EMBED_SCRIPT_SRC = {
      value     = "https://cdn.jsdelivr.net/npm/@repalis/checkout@0.1/dist/embed.global.js"
      sensitive = false
    }
    NEXT_PUBLIC_STRIPE_PAYMENT_METHOD_CONFIGURATION = {
      value     = var.next_public_stripe_payment_method_configuration
      sensitive = false
    }
    NEXT_PUBLIC_TURNSTILE_SITE_KEY = {
      value     = "1x00000000000000000000AA"
      sensitive = false
    }
    next_public_stripe_key_production = {
      key       = "NEXT_PUBLIC_STRIPE_KEY"
      value     = var.stripe_publishable_key
      target    = ["production"]
      sensitive = false
    }
    next_public_stripe_key_preview = {
      key       = "NEXT_PUBLIC_STRIPE_KEY"
      value     = var.stripe_publishable_key_preview
      target    = ["preview"]
      sensitive = false
    }
    S3_PUBLIC_IMAGES_BUCKET_PROTOCOL = {
      value     = "https"
      sensitive = false
    }
    S3_PUBLIC_IMAGES_BUCKET_HOSTNAME = {
      value     = "repalis-test-public-files.s3.amazonaws.com"
      sensitive = false
    }
    S3_PUBLIC_IMAGES_BUCKET_PATHNAME = {
      value     = "/product_media/**"
      sensitive = false
    }
    S3_UPLOAD_ORIGINS = {
      value     = "https://repalis-test-files.s3.amazonaws.com https://repalis-test-files.s3.us-east-2.amazonaws.com https://repalis-test-public-files.s3.amazonaws.com https://repalis-test-public-files.s3.us-east-2.amazonaws.com"
      sensitive = false
    }
    REPALIS_CHECKOUT_EMBED_SCRIPT_ALLOWED_ORIGINS = {
      value     = "https://repalis.com,https://sandbox.repalis.com,https://test.repalis.com"
      sensitive = false
    }
    ENABLE_EXPERIMENTAL_COREPACK = {
      value     = "1"
      sensitive = false
    }
    PYDANTIC_AI_GATEWAY_API_KEY = {
      value = var.pydantic_ai_gateway_api_key
    }
    MINTLIFY_ASSISTANT_API_KEY = {
      value = var.mintlify_assistant_api_key
    }
    GRAM_API_KEY = {
      value = var.gram_api_key
    }
    SENTRY_AUTH_TOKEN = {
      value = var.sentry_auth_token
    }
    MCP_OAUTH2_CLIENT_ID = {
      value = var.mcp_oauth2_client_id
    }
    MCP_OAUTH2_CLIENT_SECRET = {
      value = var.mcp_oauth2_client_secret
    }
    REPALIS_ENV = {
      value     = "test"
      sensitive = false
    }
    REPALIS_TESTING = {
      value     = "0"
      sensitive = false
    }
    REPALIS_LOG_LEVEL = {
      value     = "INFO"
      sensitive = false
    }
    REPALIS_CORS_ORIGINS = {
      value     = "[\"https://github.com\", \"https://repalis.com/docs\"]"
      sensitive = false
    }
    REPALIS_DATABASE_POOL_SIZE = {
      value     = "5"
      sensitive = false
    }
    REPALIS_USER_SESSION_COOKIE_KEY = {
      value     = "repalis_test_session"
      sensitive = false
    }
    REPALIS_AUTH_COOKIE_KEY = {
      value     = "repalis_test_session"
      sensitive = false
    }
    REPALIS_EMAIL_SENDER = {
      value     = "resend"
      sensitive = false
    }
    REPALIS_EMAIL_FROM_NAME = {
      value     = "[TEST] Repalis"
      sensitive = false
    }
    REPALIS_EMAIL_FROM_DOMAIN = {
      value     = "notifications.test.repalis.com"
      sensitive = false
    }
    # This service reaches AWS with static keys, not the assumed role the
    # hash_secret module grants, so it stays on the environment variable.
    REPALIS_SECRET = {
      value = var.backend_secret
    }
    REPALIS_SENTRY_DSN = {
      value = var.backend_sentry_dsn
    }
    REPALIS_TAX_PROCESSORS = {
      value     = "[\"numeral\",\"stripe\"]"
      sensitive = false
    }
    REPALIS_TAX_RECORD_PROCESSOR = {
      value     = "numeral"
      sensitive = false
    }
    REPALIS_CUSTOMER_PORTAL_URL_OVERRIDES = {
      value     = var.customer_portal_url_overrides
      sensitive = false
    }
    REPALIS_PLAIN_DEFAULT_TIER_EXTERNAL_ID = {
      value     = var.plain_default_tier_external_id
      sensitive = false
    }
    REPALIS_TURNSTILE_SECRET = {
      value = "1x0000000000000000000000000000000AA"
    }
    REPALIS_FIRECRAWL_API_KEY = {
      value = var.firecrawl_api_key
    }
    REPALIS_LOGO_DEV_PUBLISHABLE_KEY = {
      value     = var.backend_logo_dev_publishable_key
      sensitive = false
    }
    REPALIS_DISCORD_BOT_TOKEN = {
      value = var.backend_discord_bot_token
    }
    REPALIS_DISCORD_CLIENT_ID = {
      value = var.backend_discord_client_id
    }
    REPALIS_DISCORD_CLIENT_SECRET = {
      value = var.backend_discord_client_secret
    }
    REPALIS_DISCORD_PROXY_URL = {
      value = var.backend_discord_proxy_url
    }
    REPALIS_RESEND_API_KEY = {
      value = var.backend_resend_api_key
    }
    REPALIS_RESEND_ACTIVE_USERS_SEGMENT_ID = var.resend_active_users_segment_id != "" ? {
      value     = var.resend_active_users_segment_id
      sensitive = false
    } : null
    REPALIS_RESEND_WEBHOOK_SECRET = {
      value = var.backend_resend_webhook_secret
    }
    REPALIS_NUMERAL_API_KEY = {
      value = var.numeral_api_key
    }
    REPALIS_GOOGLE_CLIENT_ID = {
      value = var.google_client_id
    }
    REPALIS_GOOGLE_CLIENT_SECRET = {
      value = var.google_client_secret
    }
    REPALIS_GOOGLE_SERVICE_ACCOUNT_JSON = {
      value = var.google_service_account_json
    }
    REPALIS_PYDANTIC_AI_GATEWAY_API_KEY = {
      value = var.pydantic_ai_gateway_api_key
    }
    REPALIS_GITHUB_CLIENT_ID = {
      value = var.github_client_id
    }
    REPALIS_GITHUB_CLIENT_SECRET = {
      value = var.github_client_secret
    }
    REPALIS_GITHUB_REPOSITORY_BENEFITS_APP_IDENTIFIER = {
      value = var.github_repository_benefits_app_identifier
    }
    REPALIS_GITHUB_REPOSITORY_BENEFITS_APP_NAMESPACE = {
      value = var.github_repository_benefits_app_namespace
    }
    REPALIS_GITHUB_REPOSITORY_BENEFITS_APP_PRIVATE_KEY = {
      value = var.github_repository_benefits_app_private_key
    }
    REPALIS_GITHUB_REPOSITORY_BENEFITS_CLIENT_ID = {
      value = var.github_repository_benefits_client_id
    }
    REPALIS_GITHUB_REPOSITORY_BENEFITS_CLIENT_SECRET = {
      value = var.github_repository_benefits_client_secret
    }
    REPALIS_STRIPE_PUBLISHABLE_KEY = {
      value     = var.stripe_publishable_key
      sensitive = false
    }
    REPALIS_STRIPE_CONNECT_WEBHOOK_SECRET = {
      value = var.stripe_connect_webhook_secret
    }
    REPALIS_STRIPE_SECRET_KEY = {
      value = var.stripe_secret_key
    }
    REPALIS_STRIPE_WEBHOOK_SECRET = {
      value = var.stripe_webhook_secret
    }
    REPALIS_STRIPE_ACCOUNT_RISK_WEBHOOK_SECRET = {
      value = var.stripe_account_risk_webhook_secret
    }
    REPALIS_APPLE_CLIENT_ID = {
      value = var.apple_client_id
    }
    REPALIS_APPLE_TEAM_ID = {
      value = var.apple_team_id
    }
    REPALIS_APPLE_KEY_ID = {
      value = var.apple_key_id
    }
    REPALIS_APPLE_KEY_VALUE = {
      value = var.apple_key_value
    }
    REPALIS_AWS_REGION = {
      value     = "us-east-2"
      sensitive = false
    }
    REPALIS_AWS_SIGNATURE_VERSION = {
      value     = "v4"
      sensitive = false
    }
    REPALIS_AWS_ACCESS_KEY_ID = {
      value = var.aws_access_key_id
    }
    REPALIS_AWS_SECRET_ACCESS_KEY = {
      value = var.aws_secret_access_key
    }
    AWS_ACCESS_KEY_ID = {
      value = var.aws_access_key_id
    }
    AWS_SECRET_ACCESS_KEY = {
      value = var.aws_secret_access_key
    }
    REPALIS_S3_FILES_BUCKET_NAME = {
      value     = local.files_bucket_name
      sensitive = false
    }
    REPALIS_S3_FILES_PRESIGN_TTL = {
      value     = "600"
      sensitive = false
    }
    REPALIS_S3_FILES_PUBLIC_BUCKET_NAME = {
      value     = local.files_public_bucket_name
      sensitive = false
    }
    REPALIS_S3_CUSTOMER_INVOICES_BUCKET_NAME = {
      value     = "repalis-test-customer-invoices"
      sensitive = false
    }
    REPALIS_S3_CUSTOMER_RECEIPTS_BUCKET_NAME = {
      value     = "repalis-test-customer-receipts"
      sensitive = false
    }
    REPALIS_S3_PAYOUT_INVOICES_BUCKET_NAME = {
      value     = "repalis-test-payout-invoices"
      sensitive = false
    }
    REPALIS_S3_LOGS_BUCKET_NAME = {
      value     = "repalis-test-logs"
      sensitive = false
    }
    REPALIS_S3_FILES_DOWNLOAD_SALT = {
      value = var.s3_files_download_salt
    }
    REPALIS_S3_FILES_DOWNLOAD_SECRET = {
      value = var.s3_files_download_secret
    }
    REPALIS_LOGFIRE_TOKEN = {
      value = var.logfire_token
    }
    REPALIS_GRAFANA_CLOUD_PROMETHEUS_WRITE_URL = {
      value     = "${var.grafana_cloud_prometheus_url}/api/prom/push"
      sensitive = false
    }
    REPALIS_GRAFANA_CLOUD_PROMETHEUS_WRITE_USERNAME = {
      value = var.grafana_cloud_prometheus_username
    }
    REPALIS_GRAFANA_CLOUD_PROMETHEUS_WRITE_PASSWORD = {
      value = var.grafana_cloud_prometheus_password
    }
    REPALIS_GRAFANA_CLOUD_PROMETHEUS_WRITE_INTERVAL = {
      value     = "60"
      sensitive = false
    }
    REPALIS_REPALIS_ACCESS_TOKEN = {
      value = var.repalis_access_token
    }
    REPALIS_REPALIS_WEBHOOK_SECRET = {
      value = var.repalis_webhook_secret
    }
    REPALIS_REPALIS_ORGANIZATION_ID = {
      value     = var.repalis_organization_id
      sensitive = false
    }
    REPALIS_REPALIS_SCALE_PRODUCT_ID = {
      value     = var.repalis_scale_product_id
      sensitive = false
    }
    REPALIS_REPALIS_API_URL = {
      value     = "https://test-api.repalis.com"
      sensitive = false
    }
    REPALIS_TINYBIRD_API_URL = {
      value     = "https://api.us-east.aws.tinybird.co"
      sensitive = false
    }
    REPALIS_TINYBIRD_CLICKHOUSE_URL = {
      value     = "https://clickhouse.us-east.aws.tinybird.co"
      sensitive = false
    }
    REPALIS_TINYBIRD_API_TOKEN = {
      value = var.tinybird_api_token
    }
    REPALIS_TINYBIRD_READ_TOKEN = {
      value = var.tinybird_read_token
    }
    REPALIS_TINYBIRD_CLICKHOUSE_USERNAME = {
      value = var.tinybird_clickhouse_username
    }
    REPALIS_TINYBIRD_CLICKHOUSE_TOKEN = {
      value = var.tinybird_clickhouse_token
    }
    REPALIS_TINYBIRD_WORKSPACE = {
      value = var.tinybird_workspace
    }
  }
}

module "vercel_services" {
  source = "../modules/vercel_services"

  name     = "repalis-test-services"
  git_repo = "repaliscom/Repalis"

  preview_deployments_disabled = true

  resource_config = {
    function_default_regions = ["cle1"]
  }

  environment_variables = { for name, config in local.vercel_services_environment_variables : name => config if config != null }
}
