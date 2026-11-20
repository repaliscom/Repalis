locals {
  environment = var.backend_config.environment == null ? var.environment : var.backend_config.environment

  google_secrets = {
    REPALIS_GOOGLE_CLIENT_ID            = var.google_secrets.client_id
    REPALIS_GOOGLE_CLIENT_SECRET        = var.google_secrets.client_secret
    REPALIS_GOOGLE_SERVICE_ACCOUNT_JSON = var.google_secrets.service_account_json
  }

  backoffice_google_secrets = {
    REPALIS_BACKOFFICE_GOOGLE_CLIENT_ID     = var.google_secrets.backoffice_client_id
    REPALIS_BACKOFFICE_GOOGLE_CLIENT_SECRET = var.google_secrets.backoffice_client_secret
    REPALIS_BACKOFFICE_GOOGLE_HOSTED_DOMAIN = var.google_secrets.backoffice_hosted_domain
  }

  pydantic_ai_gateway_secrets = {
    REPALIS_PYDANTIC_AI_GATEWAY_API_KEY = var.pydantic_ai_gateway_secrets.api_key
  }

  backend_environment_variables = merge(
    {
      REPALIS_USER_SESSION_COOKIE_DOMAIN           = var.backend_config.user_session_cookie_domain
      REPALIS_AUTHENTICATION_SESSION_COOKIE_DOMAIN = var.backend_config.authentication_session_cookie_domain
      REPALIS_OAUTH2_SESSION_STATE_COOKIE_DOMAIN   = var.backend_config.oauth2_session_state_cookie_domain
      REPALIS_BASE_URL                             = var.backend_config.base_url
      REPALIS_EMAIL_SENDER                         = var.backend_config.email_sender
      REPALIS_EMAIL_FROM_NAME                      = var.backend_config.email_from_name
      REPALIS_EMAIL_FROM_DOMAIN                    = var.backend_config.email_from_domain
      REPALIS_ENV                                  = local.environment
      REPALIS_FRONTEND_BASE_URL                    = var.backend_config.frontend_base_url
      REPALIS_CHECKOUT_BASE_URL                    = var.backend_config.checkout_base_url
      REPALIS_LOG_LEVEL                            = var.backend_config.log_level
      REPALIS_TESTING                              = var.backend_config.testing
      REPALIS_INVOICES_ADDITIONAL_INFO             = var.backend_config.invoices_additional_info
      REPALIS_INVOICES_VAT_NUMBERS                 = var.backend_config.invoices_vat_numbers
      REPALIS_STRIPE_PUBLISHABLE_KEY               = var.backend_secrets.stripe_publishable_key
      REPALIS_LOGO_DEV_PUBLISHABLE_KEY             = var.backend_secrets.logo_dev_publishable_key
      REPALIS_TAX_PROCESSORS                       = var.backend_config.tax_processors
      REPALIS_TAX_RECORD_PROCESSOR                 = var.backend_config.tax_record_processor
      REPALIS_CUSTOMER_PORTAL_URL_OVERRIDES        = var.backend_config.customer_portal_url_overrides
    },
    { for name, value in {
      REPALIS_DATABASE_STATEMENT_CACHE_SIZE               = var.backend_config.database_statement_cache_size
      REPALIS_DATABASE_PREPARED_STATEMENT_CACHE_SIZE      = var.backend_config.database_prepared_statement_cache_size
      REPALIS_ORGANIZATION_ACCESS_TOKEN_CACHE_TTL_SECONDS = var.backend_config.organization_access_token_cache_ttl_seconds
    } : name => tostring(value) if value != null },
    var.backend_config.backoffice_host != null ? {
      REPALIS_BACKOFFICE_HOST = var.backend_config.backoffice_host
    } : {},
    var.backend_config.plain_default_tier_external_id != "" ? {
      REPALIS_PLAIN_DEFAULT_TIER_EXTERNAL_ID = var.backend_config.plain_default_tier_external_id
    } : {},
    var.backend_config.linear_team_id != "" ? {
      REPALIS_LINEAR_TEAM_ID = var.backend_config.linear_team_id
    } : {},
    var.backend_config.linear_payout_amount_mismatch_template_id != "" ? {
      REPALIS_LINEAR_PAYOUT_AMOUNT_MISMATCH_TEMPLATE_ID = var.backend_config.linear_payout_amount_mismatch_template_id
    } : {},
    var.backend_config.merchant_migration_destination_stripe_account_id != "" ? {
      REPALIS_MERCHANT_MIGRATION_DESTINATION_STRIPE_ACCOUNT_ID = var.backend_config.merchant_migration_destination_stripe_account_id
    } : {},
    var.backend_config.customer_meter_units_from_reducer ? {
      REPALIS_CUSTOMER_METER_UNITS_FROM_REDUCER = "true"
    } : {},
  )

  backend_secrets = merge(
    {
      REPALIS_MCP_OAUTH2_CLIENT_ID  = var.backend_secrets.mcp_oauth2_client_id
      REPALIS_DISCORD_BOT_TOKEN     = var.backend_secrets.discord_bot_token
      REPALIS_DISCORD_CLIENT_ID     = var.backend_secrets.discord_client_id
      REPALIS_DISCORD_CLIENT_SECRET = var.backend_secrets.discord_client_secret
      REPALIS_DISCORD_PROXY_URL     = var.backend_secrets.discord_proxy_url
      REPALIS_RESEND_API_KEY        = var.backend_secrets.resend_api_key
      REPALIS_RESEND_WEBHOOK_SECRET = var.backend_secrets.resend_webhook_secret
      REPALIS_FIRECRAWL_API_KEY     = var.backend_secrets.firecrawl_api_key
      REPALIS_LINEAR_API_KEY        = var.backend_secrets.linear_api_key
      REPALIS_SENTRY_DSN            = var.backend_secrets.sentry_dsn
      REPALIS_NUMERAL_API_KEY       = var.backend_secrets.numeral_api_key
      REPALIS_TURNSTILE_SECRET      = var.backend_secrets.turnstile_secret
    },
    var.backend_secrets.resend_active_users_segment_id != "" ? {
      REPALIS_RESEND_ACTIVE_USERS_SEGMENT_ID = var.backend_secrets.resend_active_users_segment_id
    } : {},
    var.backend_config.user_session_cookie_key != "" ? {
      REPALIS_USER_SESSION_COOKIE_KEY = var.backend_config.user_session_cookie_key
    } : {},
    var.backend_config.auth_cookie_key != "" ? {
      REPALIS_AUTH_COOKIE_KEY = var.backend_config.auth_cookie_key
    } : {},
  )

  backend_production_environment_variables = var.environment == "production" ? {
    REPALIS_CHECKOUT_LINK_HOST = var.backend_config.checkout_link_host
  } : {}

  backend_production_secrets = var.environment == "production" ? {
    REPALIS_POSTHOG_PROJECT_API_KEY        = var.backend_secrets.posthog_project_api_key
    REPALIS_PLAIN_REQUEST_SIGNING_SECRET   = var.backend_secrets.plain_request_signing_secret
    REPALIS_PLAIN_TOKEN                    = var.backend_secrets.plain_token
    REPALIS_PLAIN_CHAT_SECRET              = var.backend_secrets.plain_chat_secret
    REPALIS_APP_REVIEW_EMAIL               = var.backend_secrets.app_review_email
    REPALIS_APP_REVIEW_OTP_CODE            = var.backend_secrets.app_review_otp_code
    REPALIS_CHARGEBACK_STOP_WEBHOOK_SECRET = var.backend_secrets.chargeback_stop_webhook_secret
  } : {}

  aws_s3_environment_variables = {
    REPALIS_AWS_REGION                       = var.aws_s3_config.region
    REPALIS_AWS_SIGNATURE_VERSION            = var.aws_s3_config.signature_version
    REPALIS_S3_FILES_BUCKET_NAME             = "repalis-${var.environment}-files"
    REPALIS_S3_FILES_PRESIGN_TTL             = var.aws_s3_config.files_presign_ttl
    REPALIS_S3_FILES_PUBLIC_BUCKET_NAME      = var.aws_s3_config.files_public_bucket_name
    REPALIS_S3_CUSTOMER_INVOICES_BUCKET_NAME = var.aws_s3_config.customer_invoices_bucket_name
    REPALIS_S3_CUSTOMER_RECEIPTS_BUCKET_NAME = var.aws_s3_config.customer_receipts_bucket_name
    REPALIS_S3_PAYOUT_INVOICES_BUCKET_NAME   = var.aws_s3_config.payout_invoices_bucket_name
    REPALIS_S3_LOGS_BUCKET_NAME              = var.aws_s3_config.logs_bucket_name
  }

  aws_s3_secrets = {
    for key, value in {
      REPALIS_AWS_ACCESS_KEY_ID        = var.aws_s3_secrets.access_key_id
      REPALIS_AWS_SECRET_ACCESS_KEY    = var.aws_s3_secrets.secret_access_key
      REPALIS_S3_FILES_DOWNLOAD_SALT   = var.aws_s3_secrets.files_download_salt
      REPALIS_S3_FILES_DOWNLOAD_SECRET = var.aws_s3_secrets.files_download_secret
    } : key => value if value != null
  }

  secrets_kms_environment_variables = {
    REPALIS_AWS_KMS_KEY_ID                 = var.aws_kms_config.key_id
    REPALIS_AWS_JWKS_KMS_KEY_ID            = var.aws_kms_config.jwks_key_id
    REPALIS_AWS_JWKS_KMS_PUBLISHED_KEY_IDS = jsonencode(var.aws_kms_config.jwks_published_key_ids)
    REPALIS_AWS_HASH_SECRET_ARN            = var.hash_secret_arn
  }

  secrets_kms_render_environment_variables = {
    AWS_ROLE_ARN = var.aws_kms_config.role_arn
  }

  worker_sqs_environment_variables = var.worker_sqs_config != null ? {
    REPALIS_WORKER_SQS_ENABLED      = var.worker_sqs_config.enabled
    REPALIS_WORKER_SQS_ACTORS       = var.worker_sqs_config.actors
    REPALIS_WORKER_SQS_QUEUE_PREFIX = var.worker_sqs_config.queue_prefix
  } : {}

  github_secrets = {
    REPALIS_GITHUB_CLIENT_ID                           = var.github_secrets.client_id
    REPALIS_GITHUB_CLIENT_SECRET                       = var.github_secrets.client_secret
    REPALIS_GITHUB_REPOSITORY_BENEFITS_APP_IDENTIFIER  = var.github_secrets.repository_benefits_app_identifier
    REPALIS_GITHUB_REPOSITORY_BENEFITS_APP_NAMESPACE   = var.github_secrets.repository_benefits_app_namespace
    REPALIS_GITHUB_REPOSITORY_BENEFITS_APP_PRIVATE_KEY = var.github_secrets.repository_benefits_app_private_key
    REPALIS_GITHUB_REPOSITORY_BENEFITS_CLIENT_ID       = var.github_secrets.repository_benefits_client_id
    REPALIS_GITHUB_REPOSITORY_BENEFITS_CLIENT_SECRET   = var.github_secrets.repository_benefits_client_secret
  }

  stripe_secrets = {
    REPALIS_STRIPE_CONNECT_WEBHOOK_SECRET      = var.stripe_secrets.connect_webhook_secret
    REPALIS_STRIPE_SECRET_KEY                  = var.stripe_secrets.secret_key
    REPALIS_STRIPE_WEBHOOK_SECRET              = var.stripe_secrets.webhook_secret
    REPALIS_STRIPE_ACCOUNT_RISK_WEBHOOK_SECRET = var.stripe_secrets.account_risk_webhook_secret
  }

  logfire_secrets = var.logfire_config != null ? {
    REPALIS_LOGFIRE_TOKEN = var.logfire_config.token
  } : {}

  apple_secrets = {
    REPALIS_APPLE_CLIENT_ID = var.apple_secrets.client_id
    REPALIS_APPLE_TEAM_ID   = var.apple_secrets.team_id
    REPALIS_APPLE_KEY_ID    = var.apple_secrets.key_id
    REPALIS_APPLE_KEY_VALUE = var.apple_secrets.key_value
  }

  prometheus_environment_variables = var.prometheus_config != null ? merge(
    {
      REPALIS_GRAFANA_CLOUD_PROMETHEUS_WRITE_URL      = "${var.prometheus_config.url}/api/prom/push"
      REPALIS_GRAFANA_CLOUD_PROMETHEUS_WRITE_USERNAME = var.prometheus_config.username
      REPALIS_GRAFANA_CLOUD_PROMETHEUS_WRITE_INTERVAL = var.prometheus_config.interval
    },
    var.prometheus_config.query_key != null ? {
      REPALIS_GRAFANA_CLOUD_PROMETHEUS_QUERY_URL  = "${var.prometheus_config.url}/api/prom"
      REPALIS_GRAFANA_CLOUD_PROMETHEUS_QUERY_USER = var.prometheus_config.username
    } : {},
  ) : {}

  prometheus_secrets = var.prometheus_config != null ? merge(
    {
      REPALIS_GRAFANA_CLOUD_PROMETHEUS_WRITE_PASSWORD = var.prometheus_config.password
    },
    var.prometheus_config.query_key != null ? {
      REPALIS_GRAFANA_CLOUD_PROMETHEUS_QUERY_KEY = var.prometheus_config.query_key
    } : {},
  ) : {}

  slo_report_environment_variables = try(var.slo_report_config.slack_channel, null) != null ? {
    REPALIS_SLACK_CHANNEL = var.slo_report_config.slack_channel
  } : {}

  slo_report_secrets = var.slo_report_config != null ? {
    REPALIS_SLACK_BOT_TOKEN = var.slo_report_config.slack_bot_token
  } : {}

  tinybird_environment_variables = var.tinybird_config != null ? {
    REPALIS_TINYBIRD_API_URL             = var.tinybird_config.api_url
    REPALIS_TINYBIRD_CLICKHOUSE_URL      = var.tinybird_config.clickhouse_url
    REPALIS_TINYBIRD_CLICKHOUSE_USERNAME = var.tinybird_config.clickhouse_username
    REPALIS_TINYBIRD_WORKSPACE           = var.tinybird_config.workspace
  } : {}

  tinybird_secrets = var.tinybird_config != null ? {
    REPALIS_TINYBIRD_API_TOKEN        = var.tinybird_config.api_token
    REPALIS_TINYBIRD_READ_TOKEN       = var.tinybird_config.read_token
    REPALIS_TINYBIRD_CLICKHOUSE_TOKEN = var.tinybird_config.clickhouse_token
  } : {}

  repalis_self_environment_variables = var.repalis_self_config != null ? {
    REPALIS_REPALIS_ORGANIZATION_ID  = var.repalis_self_config.organization_id
    REPALIS_REPALIS_API_URL          = var.repalis_self_config.api_url
    REPALIS_REPALIS_SCALE_PRODUCT_ID = var.repalis_self_config.scale_product_id
  } : {}

  repalis_self_secrets = var.repalis_self_config != null ? {
    REPALIS_REPALIS_ACCESS_TOKEN   = var.repalis_self_config.access_token
    REPALIS_REPALIS_WEBHOOK_SECRET = var.repalis_self_config.webhook_secret
  } : {}

  environment_groups = {
    google              = local.google_secrets
    backoffice_google   = local.backoffice_google_secrets
    pydantic_ai_gateway = local.pydantic_ai_gateway_secrets
    backend = merge(
      local.backend_environment_variables,
      local.backend_secrets,
    )
    backend_production = var.environment == "production" ? merge(local.backend_production_environment_variables, local.backend_production_secrets) : null
    aws_s3             = merge(local.aws_s3_environment_variables, local.aws_s3_secrets)
    secrets_kms        = merge(local.secrets_kms_environment_variables, local.secrets_kms_render_environment_variables)
    worker_sqs         = var.worker_sqs_config != null ? local.worker_sqs_environment_variables : null
    github             = local.github_secrets
    stripe             = local.stripe_secrets
    logfire            = var.logfire_config != null ? local.logfire_secrets : null
    apple              = local.apple_secrets
    prometheus         = var.prometheus_config != null ? merge(local.prometheus_environment_variables, local.prometheus_secrets) : null
    slo_report         = var.slo_report_config != null ? merge(local.slo_report_environment_variables, local.slo_report_secrets) : null
    tinybird           = var.tinybird_config != null ? merge(local.tinybird_environment_variables, local.tinybird_secrets) : null
    repalis_self         = var.repalis_self_config != null ? merge(local.repalis_self_environment_variables, local.repalis_self_secrets) : null
  }

  environment_variables = merge(
    local.backend_environment_variables,
    local.backend_production_environment_variables,
    local.aws_s3_environment_variables,
    local.secrets_kms_environment_variables,
    local.worker_sqs_environment_variables,
    local.prometheus_environment_variables,
    local.slo_report_environment_variables,
    local.tinybird_environment_variables,
    local.repalis_self_environment_variables,
  )

  secret_environment_variables = merge(
    local.google_secrets,
    local.backoffice_google_secrets,
    local.pydantic_ai_gateway_secrets,
    local.backend_secrets,
    local.backend_production_secrets,
    local.aws_s3_secrets,
    local.github_secrets,
    local.stripe_secrets,
    local.logfire_secrets,
    local.apple_secrets,
    local.prometheus_secrets,
    local.slo_report_secrets,
    local.tinybird_secrets,
    local.repalis_self_secrets,
  )
}
