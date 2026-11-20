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

# 1. packages/cli
cli_dir = 'clients/packages/cli'
replace_in_file(os.path.join(cli_dir, 'scripts/npm-manifest.ts'), [
    ("export const COMMAND = 'polar'", "export const COMMAND = 'repalis'"),
    ("Polar CLI", "Repalis CLI"),
    ("polar auth login", "repalis auth login"),
    ("polar webhook listen", "repalis webhook listen"),
    ("polar --version", "repalis --version"),
    ("`polar`", "`repalis`"),
    ("polar products list", "repalis products list"),
    ("polar customers delete", "repalis customers delete"),
    ("Polar MCP server", "Repalis MCP server"),
    ("polar auth org", "repalis auth org"),
    ("polar webhook trigger", "repalis webhook trigger"),
    ("polar customers get", "repalis customers get"),
    ("polar orders list", "repalis orders list"),
    ("polar subscriptions revoke", "repalis subscriptions revoke"),
    ("polar auth token", "repalis auth token"),
    ("polar update", "repalis update"),
    ("polar auth logout", "repalis auth logout"),
    ("rm /usr/local/bin/polar", "rm /usr/local/bin/repalis"),
    (".polar\\bin", ".repalis\\bin"),
])

replace_in_file(os.path.join(cli_dir, 'install.ps1'), [
    ('@polar-sh/cli@', '@repalis/cli@'),
    ('$BinaryName = "polar.exe"', '$BinaryName = "repalis.exe"'),
    ('$Archive = "polar-windows-x64.zip"', '$Archive = "repalis-windows-x64.zip"'),
    ('polar-install-', 'repalis-install-'),
    ('polar is running', 'repalis is running'),
    ("'polar --help'", "'repalis --help'"),
])

replace_in_file(os.path.join(cli_dir, 'install.sh'), [
    ('TAG_PREFIX="@polar-sh/cli@"', 'TAG_PREFIX="@repalis/cli@"'),
    ('BINARY_NAME="polar"', 'BINARY_NAME="repalis"'),
    ('No Polar CLI release', 'No Repalis CLI release'),
    ('${HOME}/.polar/tokens.json', '${HOME}/.config/repalis-cli/config.json'),
    ('Polar CLI ${version}', 'Repalis CLI ${version}'),
    ("'polar --help'", "'repalis --help'"),
])

replace_in_file(os.path.join(cli_dir, 'src/services/repalis.ts'), [
    ("class Polar extends Context.Service<Polar, PolarImpl>()('Polar')", "class Repalis extends Context.Service<Repalis, RepalisImpl>()('Repalis')"),
    ("PolarImpl", "RepalisImpl"),
    ("PolarState", "RepalisState"),
])

for root, _, files in os.walk(cli_dir):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('import { Polar }', 'import { Repalis }'),
            ('Polar.layer', 'Repalis.layer'),
            ('Polar.of', 'Repalis.of'),
            ('Polar.pipe', 'Repalis.pipe'),
            ('yield* Polar', 'yield* Repalis'),
            ('fakePolar', 'fakeRepalis'),
            ('polar.zip', 'repalis.zip'),
            ('polar.tar.gz', 'repalis.tar.gz'),
            ('polar-update-', 'repalis-update-'),
            ('.polar-update-', '.repalis-update-'),
            ('polar-cursor-', 'repalis-cursor-'),
            ('polar-skills-', 'repalis-skills-'),
            ('.polar/', '.repalis/'),
            ('/.polar', '/.repalis'),
            ('"${HOME}/.polar', '"${HOME}/.repalis'),
            ('polar-sh', 'repalis'),
        ])

# 2. apps/web
web_dir = 'clients/apps/web'
replace_in_file(os.path.join(web_dir, '.oxlintrc.json'), [
    ('"polar/', '"repalis/'),
])
replace_in_file(os.path.join(web_dir, 'oxlint-plugins/index.mjs'), [
    ("name: 'polar'", "name: 'repalis'"),
    ('polarPlugin', 'repalisPlugin'),
])
replace_in_file(os.path.join(web_dir, 'instrumentation-client.ts'), [
    ('api.polar.sh', 'api.repalis.com'),
])

for root, _, files in os.walk(web_dir):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('https://x.com/polar', 'https://x.com/repalis'),
            ('https://x.com/polar_sh', 'https://x.com/repalis'),
            ('x.com/polar_sh', 'x.com/repalis'),
            ('x.com/polar', 'x.com/repalis'),
            ('@polar_sh', '@repalis'),
            ('The Polar team', 'The Repalis team'),
            ('Polar team', 'Repalis team'),
            ('Polar Plans', 'Repalis Plans'),
            ('Polar Plan', 'Repalis Plan'),
            ('Polar API', 'Repalis API'),
            ('Polar SDK', 'Repalis SDK'),
            ('Polar dashboard', 'Repalis dashboard'),
            ('Polar organization', 'Repalis organization'),
            ('Polar Organization', 'Repalis Organization'),
            ('Polar account', 'Repalis account'),
            ('Polar Account', 'Repalis Account'),
            ('Polar checkout', 'Repalis checkout'),
            ('Polar Checkout', 'Repalis Checkout'),
            ('Polar customer', 'Repalis customer'),
            ('Polar Customer', 'Repalis Customer'),
            ('Polar subscription', 'Repalis subscription'),
            ('Polar Subscription', 'Repalis Subscription'),
            ('Polar product', 'Repalis product'),
            ('Polar Product', 'Repalis Product'),
            ('Polar benefit', 'Repalis benefit'),
            ('Polar Benefit', 'Repalis Benefit'),
            ('Polar webhook', 'Repalis webhook'),
            ('Polar Webhook', 'Repalis Webhook'),
            ('Polar orders', 'Repalis orders'),
            ('Polar Orders', 'Repalis Orders'),
            ('Polar order', 'Repalis order'),
            ('Polar Order', 'Repalis Order'),
            ('Polar invoice', 'Repalis invoice'),
            ('Polar Invoice', 'Repalis Invoice'),
            ('Polar receipt', 'Repalis receipt'),
            ('Polar Receipt', 'Repalis Receipt'),
            ('Polar fee', 'Repalis fee'),
            ('Polar Fee', 'Repalis Fee'),
            ('Polar logo', 'Repalis logo'),
            ('Polar Logo', 'Repalis Logo'),
            ('Polar CLI', 'Repalis CLI'),
            ('Polar MCP', 'Repalis MCP'),
            ('The next evolution of Polar', 'The next evolution of Repalis'),
            ('Introducing Polar', 'Introducing Repalis'),
            ('Welcome to Polar', 'Welcome to Repalis'),
            ('Why Polar', 'Why Repalis'),
            ('About Polar', 'About Repalis'),
            ('Polar is', 'Repalis is'),
            ('Polar was', 'Repalis was'),
            ('Polar has', 'Repalis has'),
            ('Polar allows', 'Repalis allows'),
            ('Polar lets', 'Repalis lets'),
            ('Polar provides', 'Repalis provides'),
            ('Polar handles', 'Repalis handles'),
            ('Polar supports', 'Repalis supports'),
            ('polar.events.ingest', 'repalis.events.ingest'),
            ('polar.checkouts.create', 'repalis.checkouts.create'),
            ('polar.customerSessions.create', 'repalis.customerSessions.create'),
            ('polar.subscriptions.list', 'repalis.subscriptions.list'),
            ('polar.products.list', 'repalis.products.list'),
            ('polar.customers.get', 'repalis.customers.get'),
            ('polar.orders.list', 'repalis.orders.list'),
            ('polar.oauth2.', 'repalis.oauth2.'),
            ('polar_setup_intent', 'repalis_setup_intent'),
            ('polar_distinct_id', 'repalis_distinct_id'),
            ('polar_last_login_method', 'repalis_last_login_method'),
            ('polarBotRolePosition', 'repalisBotRolePosition'),
            ('polarBilling', 'repalisBilling'),
            ('polar-sh', 'repalis'),
            ('polar.sh', 'repalis.com'),
        ])

# 3. adapters/better-auth
ba_dir = 'clients/adapters/better-auth'
for root, _, files in os.walk(ba_dir):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('getCurrentPolarOwner', 'getCurrentRepalisOwner'),
            ('polarSuccessor', 'repalisSuccessor'),
            ('polarRole', 'repalisRole'),
            ('polarOwner', 'repalisOwner'),
            ('polarMember', 'repalisMember'),
            ('polarClient', 'repalisClient'),
            ('polarUser', 'repalisUser'),
            ('polarOrg', 'repalisOrg'),
            ('polarCallOrder', 'repalisCallOrder'),
            ('polar-organization', 'repalis-organization'),
            ('polar-member-', 'repalis-member-'),
            ('PolarOrganization', 'RepalisOrganization'),
            ('PolarEndpoints', 'RepalisEndpoints'),
            ('PolarPlugin', 'RepalisPlugin'),
            ('PolarClientMocks', 'RepalisClientMocks'),
            ('polarSDK', 'repalisSDK'),
            ('polarWebhooks', 'repalisWebhooks'),
            ('Polar', 'Repalis'),
            ('polar', 'repalis'),
        ])

# 4. apps/app
app_dir = 'clients/apps/app'
replace_in_file(os.path.join(app_dir, '.oxlintrc.json'), [
    ('@polar/', '@repalis/'),
    ('"@polar"', '"@repalis"'),
])
replace_in_file(os.path.join(app_dir, 'app.config.js'), [
    ("project: 'polar-app'", "project: 'repalis-app'"),
    ("organization: 'polar-sh'", "organization: 'repalis'"),
    ("owner: 'polar-sh'", "owner: 'repalis'"),
    ("scheme: 'polar'", "scheme: 'repalis'"),
    ('polar.godetour.link', 'repalis.godetour.link'),
    ('@polar/', '@repalis/'),
])
replace_in_file(os.path.join(app_dir, 'auth/oauthConfig.ts'), [
    ('polar://oauth/callback', 'repalis://oauth/callback'),
    ('polar_ci_', 'repalis_ci_'),
])
replace_in_file(os.path.join(app_dir, 'app/(authenticated)/settings/index.tsx'), [
    ('Polar (${APP_VERSION})', 'Repalis (${APP_VERSION})'),
])
for root, _, files in os.walk(app_dir):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('polar.GET', 'repalis.GET'),
            ('polar.POST', 'repalis.POST'),
            ('polar.PATCH', 'repalis.PATCH'),
            ('polar.DELETE', 'repalis.DELETE'),
            ('const polar =', 'const repalis ='),
            ('PolarNotification', 'RepalisNotification'),
            ('PolarOrganizationProvider', 'RepalisOrganizationProvider'),
            ('Polar', 'Repalis'),
        ])

# 5. apps/mcp
mcp_dir = 'clients/apps/mcp'
for root, _, files in os.walk(mcp_dir):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ("resource_name: 'Polar'", "resource_name: 'Repalis'"),
            ('api.polar.test', 'api.repalis.test'),
            ('mcp.polar.test', 'mcp.repalis.test'),
            ('polarApiClient', 'repalisApiClient'),
            ('PolarApiOutbound', 'RepalisApiOutbound'),
            ('polar.request', 'repalis.request'),
            ('polar-local', 'repalis-local'),
            ('polar_oat_', 'repalis_oat_'),
            ('Polar', 'Repalis'),
            ('polar', 'repalis'),
        ])

# 6. packages/checkout
checkout_dir = 'clients/packages/checkout'
for root, _, files in os.walk(checkout_dir):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ("REDIRECT_STATUS_PARAM = 'polar_payment_method_status'", "REDIRECT_STATUS_PARAM = 'repalis_payment_method_status'"),
            ('isPolarMessage', 'isRepalisMessage'),
            ('Polar: Partial<RepalisWindow>', 'Repalis: Partial<RepalisWindow>'),
            ('polar-payment-method', 'repalis-payment-method'),
            ('const polar = createRepalis', 'const repalis = createRepalis'),
            ('polar.customerSessions', 'repalis.customerSessions'),
            ('embedding Polar', 'embedding Repalis'),
            ('Polar iframe', 'Repalis iframe'),
            ('Polar', 'Repalis'),
        ])

# 7. adapters/nextjs, nuxt, tanstack-start, demo-app
for ad_dir in ['clients/adapters/nextjs', 'clients/adapters/nuxt', 'clients/adapters/tanstack-start', 'clients/apps/demo-app', 'clients/adapters/adapter-utils']:
    for root, _, files in os.walk(ad_dir):
        for f in files:
            p = os.path.join(root, f)
            replace_in_file(p, [
                ('const polar = createRepalis', 'const repalis = createRepalis'),
                ('(polar)', '(repalis)'),
                ('polarServer', 'repalisServer'),
                ('polarCheckoutSuccessUrl', 'repalisCheckoutSuccessUrl'),
                ('polarWebhookSecret', 'repalisWebhookSecret'),
                ('api/webhook/polar', 'api/webhook/repalis'),
                ('testing Polar', 'testing Repalis'),
                ('Polar', 'Repalis'),
            ])

# 8. packages/orbit & apps/orbit
for ob_dir in ['clients/packages/orbit', 'clients/apps/orbit']:
    for root, _, files in os.walk(ob_dir):
        for f in files:
            p = os.path.join(root, f)
            replace_in_file(p, [
                ('WhyPolarPage', 'WhyRepalisPage'),
                ('PolarLogotype', 'RepalisLogotype'),
                ('PolarLemonSqueezyPage', 'RepalisLemonSqueezyPage'),
                ('PolarPaddlePage', 'RepalisPaddlePage'),
                ('Polar', 'Repalis'),
            ])

# 9. packages/client
replace_in_file('clients/packages/client/package.json', [
    ('"Polar Internal API Client"', '"Repalis Internal API Client"'),
    ('"author": "Polar"', '"author": "Repalis"'),
])
replace_in_file('clients/packages/client/src/v1.ts', [
    ('List Polar orders', 'List Repalis orders'),
    ('pay Polar invoices', 'pay Repalis invoices'),
    ("org's Polar billing", "org's Repalis billing"),
    ('Polar IDs', 'Repalis IDs'),
    ('Polar iframe', 'Repalis iframe'),
    ('is_polar_bot: boolean', 'is_repalis_bot: boolean'),
    ('Polar event ID', 'Repalis event ID'),
    ('Polar orders', 'Repalis orders'),
    ('Polar order', 'Repalis order'),
    ('Polar invoice', 'Repalis invoice'),
    ('Polar payment', 'Repalis payment'),
    ('Polar subscription', 'Repalis subscription'),
    ('Polar product', 'Repalis product'),
    ('Polar benefit', 'Repalis benefit'),
    ('Polar customer', 'Repalis customer'),
    ('Polar organization', 'Repalis organization'),
    ('Polar checkout', 'Repalis checkout'),
    ('Polar', 'Repalis'),
])

# 10. packages/repalis
replace_in_file('clients/packages/repalis/src/index.ts', [
    ('Polar,', 'Repalis,'),
    ('Polar', 'Repalis'),
])
replace_in_file('clients/packages/repalis/src/schema/config.ts', [
    ('polar.webhooks', 'repalis.webhooks'),
    ('PolarConfig', 'RepalisConfig'),
    ('polar.runtimeConfig', 'repalis.runtimeConfig'),
    ('polar.benefitKey', 'repalis.benefitKey'),
])

print("Clients Part 2 execution complete.")
