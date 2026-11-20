import os
import re

def replace_in_file(path, replacements):
    if not os.path.exists(path):
        return 0
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, PermissionError):
        return 0
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

client_replacements = [
    # 1. Config and file names
    ('polar.config.ts', 'repalis.config.ts'),
    ('polar.config.json', 'repalis.config.json'),
    ('polar.config.mjs', 'repalis.config.mjs'),
    ('polar.config.js', 'repalis.config.js'),
    ('polar.json', 'repalis.json'),
    ('polar.exe', 'repalis.exe'),
    ('polar.ts', 'repalis.ts'),
    ('polar-config', 'repalis-config'),
    
    # 2. Env vars
    ('POLAR_PREVIEW', 'REPALIS_PREVIEW'),
    ('POLAR_DASHBOARD_URL', 'REPALIS_DASHBOARD_URL'),
    ('POLAR_ENVIRONMENT', 'REPALIS_ENVIRONMENT'),
    ('POLAR_CLI_TELEMETRY_OPTOUT', 'REPALIS_CLI_TELEMETRY_OPTOUT'),
    ('POLAR_CLI_BUILD', 'REPALIS_CLI_BUILD'),
    ('POLAR_CLI_POSTHOG_KEY', 'REPALIS_CLI_POSTHOG_KEY'),
    ('POLAR_CLI_TELEMETRY_URL', 'REPALIS_CLI_TELEMETRY_URL'),
    ('POLAR_CLI_TELEMETRY_FORCE', 'REPALIS_CLI_TELEMETRY_FORCE'),
    ('POLAR_SKIP_DTS', 'REPALIS_SKIP_DTS'),
    ('POLAR_LOCAL_API_URL', 'REPALIS_LOCAL_API_URL'),
    ('EXPO_PUBLIC_POLAR_SERVER_URL', 'EXPO_PUBLIC_REPALIS_SERVER_URL'),
    ('POLAR_READ_TOKEN', 'REPALIS_READ_TOKEN'),
    ('POLAR_WRITE_TOKEN', 'REPALIS_WRITE_TOKEN'),
    
    # 3. HTTP Headers & Embed attributes
    ('x-polar-triggered', 'x-repalis-triggered'),
    ('x-polar-embed-origin', 'x-repalis-embed-origin'),
    ('x-polar-distinct-id', 'x-repalis-distinct-id'),
    ('REPALIS_EMBED_ORIGIN_HEADER = \'x-polar-embed-origin\'', 'REPALIS_EMBED_ORIGIN_HEADER = \'x-repalis-embed-origin\''),
    ('DISTINCT_ID_HEADER = \'x-polar-distinct-id\'', 'DISTINCT_ID_HEADER = \'x-repalis-distinct-id\''),
    ('polar-embed-layout', 'repalis-embed-layout'),
    ('data-polar-embed-theme', 'data-repalis-embed-theme'),
    ('polar-embed-content', 'repalis-embed-content'),
    
    # 4. Stripe and Checkout helpers
    ('loadPolarStripe', 'loadRepalisStripe'),
    ('PolarHog', 'RepalisHog'),
    ('window.Polar', 'window.Repalis'),
    ('PolarWindow', 'RepalisWindow'),
    ('polarBilling', 'repalisBilling'),
    ('polarBotRolePosition', 'repalisBotRolePosition'),
    ('polar_last_login_method', 'repalis_last_login_method'),
    ('polar_distinct_id', 'repalis_distinct_id'),
    ('polar_setup_intent', 'repalis_setup_intent'),
    
    # 5. Token prefixes & test tokens
    ('polar_oat_secret', 'repalis_oat_secret'),
    ('polar_oat_test', 'repalis_oat_test'),
    ('polar_oat_', 'repalis_oat_'),
    ('polar_pat_', 'repalis_pat_'),
    ('polar_cst_', 'repalis_cst_'),
    ('polar_mst_', 'repalis_mst_'),
    ('polar_acl_', 'repalis_acl_'),
    ('polar_act_', 'repalis_act_'),
    ('polar_c_123', 'repalis_c_123'),
    ('polar_c_test', 'repalis_c_test'),
    ('polar_c_', 'repalis_c_'),
    ('polar_st_', 'repalis_st_'),
    
    # 6. Better-auth adapter
    ('PolarNonOwnerMemberRole', 'RepalisNonOwnerMemberRole'),
    ('polarOwner', 'repalisOwner'),
    ('PolarOrganizationCustomerTypeError', 'RepalisOrganizationCustomerTypeError'),
    ('PolarEndpoints', 'RepalisEndpoints'),
    ('PolarOrganizationTeamCustomerNotFoundError', 'RepalisOrganizationTeamCustomerNotFoundError'),
    ('PolarOrganizationMemberRoleMappingError', 'RepalisOrganizationMemberRoleMappingError'),
    ('polarSDK', 'repalisSDK'),
    ('polarWebhooks', 'repalisWebhooks'),
    ('PolarPlugin', 'RepalisPlugin'),
    ('PolarClientMocks', 'RepalisClientMocks'),
    ('PolarOrganizationMemberRoleInput', 'RepalisOrganizationMemberRoleInput'),
    ('PolarOrganizationCustomerData', 'RepalisOrganizationCustomerData'),
    ('PolarOrganizationCustomer', 'RepalisOrganizationCustomer'),
    ('polarCallOrder', 'repalisCallOrder'),
    ('polar-organization', 'repalis-organization'),
    ('polar-member-', 'repalis-member-'),
    
    # 7. Nuxt, Nextjs & Tanstack adapters
    ('polarServer', 'repalisServer'),
    ('polarCheckoutSuccessUrl', 'repalisCheckoutSuccessUrl'),
    ('polarWebhookSecret', 'repalisWebhookSecret'),
    ('polarWith', 'repalisWith'),
    ('polarLayer', 'repalisLayer'),
    
    # 8. MCP & Client
    ('api.polar.test', 'api.repalis.test'),
    ('mcp.polar.test', 'mcp.repalis.test'),
    ('polarApiClient', 'repalisApiClient'),
    ('PolarApiOutbound', 'RepalisApiOutbound'),
    ('polar-local', 'repalis-local'),
    ('PolarAuthError', 'RepalisAuthError'),
    ('PolarSelfPaidSubscriptionAlreadyExists', 'RepalisSelfPaidSubscriptionAlreadyExists'),
    ('PolarSelfPaymentMethodInUse', 'RepalisSelfPaymentMethodInUse'),
    ('PolarNotification', 'RepalisNotification'),
    ('PolarOrganizationProvider', 'RepalisOrganizationProvider'),
    ('PolarConfig', 'RepalisConfig'),
    ('PolarSDK', 'RepalisSDK'),
    
    # 9. Orbit tokens & pages
    ('palette.polar800', 'palette.repalis800'),
    ('palette.polar950', 'palette.repalis950'),
    ('palette.polar900', 'palette.repalis900'),
    ('palette.polar400', 'palette.repalis400'),
    ('palette.polar', 'palette.repalis'),
    ('WhyPolarPage', 'WhyRepalisPage'),
    ('PolarLogotype', 'RepalisLogotype'),
    ('PolarLemonSqueezyPage', 'RepalisLemonSqueezyPage'),
    ('PolarPaddlePage', 'RepalisPaddlePage'),
    
    # 10. URLs and releases
    ('polar-darwin-', 'repalis-darwin-'),
    ('polar-linux-', 'repalis-linux-'),
    ('polar-windows-', 'repalis-windows-'),
    ('polar-sandbox', 'repalis-sandbox'),
    ('polar-test', 'repalis-test'),
]

modified = 0
for root, _, files in os.walk('clients'):
    for f in files:
        if f.endswith(('.ts', '.tsx', '.js', '.jsx', '.json', '.md', '.mdx', '.css', '.mjs', '.mts')):
            p = os.path.join(root, f)
            if replace_in_file(p, client_replacements):
                modified += 1

print(f"Modified {modified} files in clients/")
