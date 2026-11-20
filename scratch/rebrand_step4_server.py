import os
import re

def replace_in_file(path, replacements):
    if not os.path.exists(path):
        return 0
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    orig = content
    for pattern, repl in replacements:
        if isinstance(pattern, str):
            content = content.replace(pattern, repl)
        else:
            content = pattern.sub(repl, content)
    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return 1
    return 0

# Core server replacements
core_replacements = [
    # Custom HTTP Headers & OpenAPI extensions
    ("x-polar-allowed-subjects", "x-repalis-allowed-subjects"),
    ("x-polar-pagination", "x-repalis-pagination"),
    ("x-polar-environment", "x-repalis-environment"),
    ("x-polar-client-version", "x-repalis-client-version"),
    ("x-polar-triggered", "x-repalis-triggered"),
    ("x-polar-probe", "x-repalis-probe"),
    ('VERSION_HEADER = "Polar-Version"', 'VERSION_HEADER = "Repalis-Version"'),
    ('ORGANIZATION_HEADER = "Polar-Organization"', 'ORGANIZATION_HEADER = "Repalis-Organization"'),
    ('Polar-Organization header', 'Repalis-Organization header'),
    ('Polar-Organization', 'Repalis-Organization'),
    ('Polar-Version', 'Repalis-Version'),
    
    # S3 Metadata Headers
    ("polar-organization-id", "repalis-organization-id"),
    ("polar-name", "repalis-name"),
    ("polar-size", "repalis-size"),
    ("polar-sha256-base64", "repalis-sha256-base64"),
    ("polar-sha256-hex", "repalis-sha256-hex"),
    ("polar-id", "repalis-id"),
    
    # External Event Source
    ('polar = "polar"', 'repalis = "repalis"'),
    ("ExternalEventSource.polar", "ExternalEventSource.repalis"),
    ('source: Mapped[Literal[ExternalEventSource.polar]]', 'source: Mapped[Literal[ExternalEventSource.repalis]]'),
    ('"polymorphic_identity": ExternalEventSource.polar', '"polymorphic_identity": ExternalEventSource.repalis'),
    
    # Metrics
    ("polar_checkout_created_total", "repalis_checkout_created_total"),
    ("polar_checkout_succeeded_total", "repalis_checkout_succeeded_total"),
    ("polar_http_request_duration_seconds", "repalis_http_request_duration_seconds"),
    ("polar_http_sse_opened_connection_total", "repalis_http_sse_opened_connection_total"),
    ("polar_task_executions_total", "repalis_task_executions_total"),
    ("polar_task_duration_seconds", "repalis_task_duration_seconds"),
    ("polar_task_retries_total", "repalis_task_retries_total"),
    ("polar_task_debounced_total", "repalis_task_debounced_total"),
    ("polar_task_debounce_delay_seconds", "repalis_task_debounce_delay_seconds"),
    ("polar_staged_events_backlog", "repalis_staged_events_backlog"),
    ("polar_staged_events_oldest_age_seconds", "repalis_staged_events_oldest_age_seconds"),
    ("polar_operational_error_total", "repalis_operational_error_total"),
    ("polar_slo_p99_target_seconds", "repalis_slo_p99_target_seconds"),
    ("polar_slo_availability_target", "repalis_slo_availability_target"),
    ("polar_tax_calculation_total", "repalis_tax_calculation_total"),
    ("polar_queue_size", "repalis_queue_size"),
    ("polar_queue_oldest_message_age_seconds", "repalis_queue_oldest_message_age_seconds"),
    
    # TokenType Enum
    ('client_secret = "polar_client_secret"', 'client_secret = "repalis_client_secret"'),
    ('client_registration_token = "polar_client_registration_token"', 'client_registration_token = "repalis_client_registration_token"'),
    ('authorization_code = "polar_authorization_code"', 'authorization_code = "repalis_authorization_code"'),
    ('access_token = "polar_access_token"', 'access_token = "repalis_access_token"'),
    ('refresh_token = "polar_refresh_token"', 'refresh_token = "repalis_refresh_token"'),
    ('personal_access_token = "polar_personal_access_token"', 'personal_access_token = "repalis_personal_access_token"'),
    ('organization_access_token = "polar_organization_access_token"', 'organization_access_token = "repalis_organization_access_token"'),
    ('user_session_token = "polar_user_session_token"', 'user_session_token = "repalis_user_session_token"'),
    
    # Token Prefixes
    ('CLAIM_TOKEN_PREFIX = "polar_act_"', 'CLAIM_TOKEN_PREFIX = "repalis_act_"'),
    ('CLAIM_LINK_TOKEN_PREFIX = "polar_acl_"', 'CLAIM_LINK_TOKEN_PREFIX = "repalis_acl_"'),
    ('CHECKOUT_CLIENT_SECRET_PREFIX = "polar_c_"', 'CHECKOUT_CLIENT_SECRET_PREFIX = "repalis_c_"'),
    ('CHECKOUT_LINK_CLIENT_SECRET_PREFIX = "polar_cl_"', 'CHECKOUT_LINK_CLIENT_SECRET_PREFIX = "repalis_cl_"'),
    ('CUSTOMER_SESSION_TOKEN_PREFIX = "polar_cst_"', 'CUSTOMER_SESSION_TOKEN_PREFIX = "repalis_cst_"'),
    ('MEMBER_SESSION_TOKEN_PREFIX = "polar_mst_"', 'MEMBER_SESSION_TOKEN_PREFIX = "repalis_mst_"'),
    ('USER_SESSION_TOKEN_PREFIX = "polar_us_"', 'USER_SESSION_TOKEN_PREFIX = "repalis_us_"'),
    ('TOKEN_PREFIX = "polar_auth_session_"', 'TOKEN_PREFIX = "repalis_auth_session_"'),
    ('TOKEN_PREFIX = "polar_oauth2_"', 'TOKEN_PREFIX = "repalis_oauth2_"'),
    ('TOKEN_PREFIX = "polar_cev_"', 'TOKEN_PREFIX = "repalis_cev_"'),
    ('TOKEN_PREFIX = "polar_ev_"', 'TOKEN_PREFIX = "repalis_ev_"'),
    ('TOKEN_PREFIX = "polar_oat_"', 'TOKEN_PREFIX = "repalis_oat_"'),
    ('TOKEN_PREFIX = "polar_pat_"', 'TOKEN_PREFIX = "repalis_pat_"'),
    ('CLIENT_SECRET_PREFIX = "polar_cs_"', 'CLIENT_SECRET_PREFIX = "repalis_cs_"'),
    ('AUTHORIZATION_CODE_PREFIX = "polar_ac_"', 'AUTHORIZATION_CODE_PREFIX = "repalis_ac_"'),
    ('SubType.organization: "polar_at_o_"', 'SubType.organization: "repalis_at_o_"'),
    ('SubType.organization: "polar_rt_o_"', 'SubType.organization: "repalis_rt_o_"'),
    ('token_prefix = "polar_backoffice_oauth2_"', 'token_prefix = "repalis_backoffice_oauth2_"'),
    ('AUTHENTICATION_TOKEN_PREFIX = "polar_backoffice_auth_"', 'AUTHENTICATION_TOKEN_PREFIX = "repalis_backoffice_auth_"'),
    ('USER_SESSION_TOKEN_PREFIX = "polar_backoffice_session_"', 'USER_SESSION_TOKEN_PREFIX = "repalis_backoffice_session_"'),
    
    # Cookie Keys & JWK in config
    ('"kid": "polar_dev"', '"kid": "repalis_dev"'),
    ('LOCAL_JWK_KID: str = "polar_dev"', 'LOCAL_JWK_KID: str = "repalis_dev"'),
    ('BACKOFFICE_AUTHENTICATION_SESSION_COOKIE_KEY: str = "polar_backoffice_auth_session"', 'BACKOFFICE_AUTHENTICATION_SESSION_COOKIE_KEY: str = "repalis_backoffice_auth_session"'),
    ('BACKOFFICE_USER_SESSION_COOKIE_KEY: str = "polar_backoffice_session"', 'BACKOFFICE_USER_SESSION_COOKIE_KEY: str = "repalis_backoffice_session"'),
    ('AUTHENTICATION_SESSION_COOKIE_KEY: str = "polar_auth_session"', 'AUTHENTICATION_SESSION_COOKIE_KEY: str = "repalis_auth_session"'),
    ('OAUTH2_SESSION_STATE_COOKIE_KEY: str = "polar_oauth2_state"', 'OAUTH2_SESSION_STATE_COOKIE_KEY: str = "repalis_oauth2_state"'),
    ('USER_SESSION_COOKIE_KEY: str = "polar_session"', 'USER_SESSION_COOKIE_KEY: str = "repalis_session"'),
    ('IMPERSONATION_COOKIE_KEY: str = "polar_original_session"', 'IMPERSONATION_COOKIE_KEY: str = "repalis_original_session"'),
    ('IMPERSONATION_INDICATOR_COOKIE_KEY: str = "polar_is_impersonating"', 'IMPERSONATION_INDICATOR_COOKIE_KEY: str = "repalis_is_impersonating"'),
    ('"polar_last_login_method"', '"repalis_last_login_method"'),
    
    # S3 Assets & Logos
    ("polar-public-assets.s3.us-east-2.amazonaws.com", "repalis-public-assets.s3.us-east-2.amazonaws.com"),
    ("polar-logo-2026-black-badge.png", "repalis-logo-2026-black-badge.png"),
    ('alt="Polar Logo"', 'alt="Repalis Logo"'),
    
    # App & Functions
    ("def polar_frontend_matcher", "def repalis_frontend_matcher"),
    ("polar_frontend_config", "repalis_frontend_config"),
    ("polar_redirection_exception_handler", "repalis_redirection_exception_handler"),
    ("polar_organization_id", "repalis_organization_id"),
    ("polar_site_url", "repalis_site_url"),
    ("is_polar_bot", "is_repalis_bot"),
    ("polar_failed_sync_payment", "repalis_failed_sync_payment"),
    ("polar_setup_intent", "repalis_setup_intent"),
    ("sub_polar_scope_probe", "sub_repalis_scope_probe"),
    
    # Merchant migration identifiers
    ("product_exists_in_polar", "product_exists_in_repalis"),
    ("_CUSTOMER_SUBSCRIBED_ON_POLAR_REASON", "_CUSTOMER_SUBSCRIBED_ON_REPALIS_REASON"),
    ("polar_amounts", "repalis_amounts"),
    ("polar_orders", "repalis_orders"),
    
    # Seeds
    ("POLAR_SELF_BENEFITS", "REPALIS_SELF_BENEFITS"),
    ("POLAR_SELF_PRODUCTS", "REPALIS_SELF_PRODUCTS"),
    ("POLAR_SELF_EXTERNAL_BENEFITS", "REPALIS_SELF_EXTERNAL_BENEFITS"),
    ("POLAR_SELF_MONTHLY_PRODUCTS", "REPALIS_SELF_MONTHLY_PRODUCTS"),
    ("_seed_polar_self_billing_catalog", "_seed_repalis_self_billing_catalog"),
    ("polar_seed_simple_complement:", "repalis_seed_simple_complement:"),
    ("seed_polar_for_polar", "seed_repalis_for_repalis"),
    ("Polar-for-Polar", "Repalis-for-Repalis"),
    
    # Email schema names
    ("schemas['PolarSelf", "schemas['RepalisSelf"),
    ("PolarSelfStartupProgramWelcome", "RepalisSelfStartupProgramWelcome"),
    ("PolarSelfSubscriptionCancellation", "RepalisSelfSubscriptionCancellation"),
    ("PolarSelfSubscriptionConfirmation", "RepalisSelfSubscriptionConfirmation"),
    ("PolarSelfSubscriptionCycled", "RepalisSelfSubscriptionCycled"),
    ("PolarSelfSubscriptionPastDue", "RepalisSelfSubscriptionPastDue"),
    ("PolarSelfSubscriptionRevoked", "RepalisSelfSubscriptionRevoked"),
    
    # Risk signal
    ("OrganizationRiskSignal.Source.POLAR", "OrganizationRiskSignal.Source.REPALIS"),
    ('POLAR = "polar"', 'REPALIS = "repalis"'),
    ('POLAR = "POLAR"', 'REPALIS = "REPALIS"'),
]

modified = 0
for root, _, files in os.walk('server'):
    for f in files:
        if f.endswith(('.py', '.tsx', '.ts', '.json', '.md', '.mdx', '.html', '.sh', '.yml', '.yaml')):
            p = os.path.join(root, f)
            if replace_in_file(p, core_replacements):
                modified += 1

print(f"Modified {modified} files in server/")
