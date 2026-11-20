import os
import re

clients_dirs = ['clients', '.github', 'terraform']

# Exact string replacements
exact_replacements = [
    # Package scopes
    ('@polar-sh/adapter-utils', '@repalis/adapter-utils'),
    ('@polar-sh/app', '@repalis/app'),
    ('@polar-sh/better-auth', '@repalis/better-auth'),
    ('@polar-sh/box-codemod', '@repalis/box-codemod'),
    ('@polar-sh/checkout', '@repalis/checkout'),
    ('@polar-sh/cli-commands', '@repalis/cli-commands'),
    ('@polar-sh/cli', '@repalis/cli'),
    ('@polar-sh/client', '@repalis/client'),
    ('@polar-sh/currency', '@repalis/currency'),
    ('@polar-sh/i18n', '@repalis/i18n'),
    ('@polar-sh/nextjs', '@repalis/nextjs'),
    ('@polar-sh/nuxt', '@repalis/nuxt'),
    ('@polar-sh/orbit', '@repalis/orbit'),
    ('@polar-sh/oxlint-config', '@repalis/oxlint-config'),
    ('@polar-sh/sdk', '@repalis/sdk'),
    ('@polar-sh/tanstack-start', '@repalis/tanstack-start'),
    ('@polar-sh/typescript-config', '@repalis/typescript-config'),
    ('@polar-sh/ui', '@repalis/ui'),
    ('"name": "polar"', '"name": "repalis"'),
    ('polar-nuxt-playground', 'repalis-nuxt-playground'),

    # CSS color tokens
    ('--color-polar-50:', '--color-repalis-50:'),
    ('--color-polar-100:', '--color-repalis-100:'),
    ('--color-polar-200:', '--color-repalis-200:'),
    ('--color-polar-300:', '--color-repalis-300:'),
    ('--color-polar-400:', '--color-repalis-400:'),
    ('--color-polar-500:', '--color-repalis-500:'),
    ('--color-polar-600:', '--color-repalis-600:'),
    ('--color-polar-700:', '--color-repalis-700:'),
    ('--color-polar-800:', '--color-repalis-800:'),
    ('--color-polar-900:', '--color-repalis-900:'),
    ('--color-polar-950:', '--color-repalis-950:'),
    ('var(--color-polar-', 'var(--color-repalis-'),

    ('-polar-50', '-repalis-50'),
    ('-polar-100', '-repalis-100'),
    ('-polar-200', '-repalis-200'),
    ('-polar-300', '-repalis-300'),
    ('-polar-400', '-repalis-400'),
    ('-polar-500', '-repalis-500'),
    ('-polar-600', '-repalis-600'),
    ('-polar-700', '-repalis-700'),
    ('-polar-800', '-repalis-800'),
    ('-polar-900', '-repalis-900'),
    ('-polar-950', '-repalis-950'),

    # Spinner and scroll
    ('polar-loader-spinner', 'repalis-loader-spinner'),
    ('polar-no-scroll', 'repalis-no-scroll'),

    # Components and hooks
    ('usePolarClient', 'useRepalisClient'),
    ('PolarEmbedCheckout', 'RepalisEmbedCheckout'),
    ('PolarEmbedPaymentMethod', 'RepalisEmbedPaymentMethod'),
    ('createMockPolarClient', 'createMockRepalisClient'),
    ('createTestPolarOptions', 'createTestRepalisOptions'),
    ('MockPolarClient', 'MockRepalisClient'),
    ('mapBetterAuthRoleToPolarRole', 'mapBetterAuthRoleToRepalisRole'),
    ('polarClient', 'repalisClient'),
    ('createPolarCore', 'createRepalisCore'),
    ('createPolar', 'createRepalis'),
    ('PolarCore', 'RepalisCore'),
    ('PolarOptions', 'RepalisOptions'),
    ('PolarEnvironment', 'RepalisEnvironment'),
    ('polar-client', 'repalis-client'),

    # Enums & Constants
    ('POLAR_CHECKOUT', 'REPALIS_CHECKOUT'),
    ('POLAR_PAYMENT_METHOD', 'REPALIS_PAYMENT_METHOD'),
    ('polar-mcp', 'repalis-mcp'),
    ('POLAR_ACCESS_TOKEN', 'REPALIS_ACCESS_TOKEN'),
    ('POLAR_WEBHOOK_SECRET', 'REPALIS_WEBHOOK_SECRET'),
    ('POLAR_ORGANIZATION_ID', 'REPALIS_ORGANIZATION_ID'),
    ('POLAR_API_URL', 'REPALIS_API_URL'),
    ('POLAR_USER_HEADER', 'REPALIS_USER_HEADER'),
    ('POLAR_AUTH_COOKIE_KEY', 'REPALIS_AUTH_COOKIE_KEY'),
    ('POLAR_AUTH_MCP_COOKIE_KEY', 'REPALIS_AUTH_MCP_COOKIE_KEY'),
    ('POLAR_EMBED_ORIGIN_HEADER', 'REPALIS_EMBED_ORIGIN_HEADER'),
    ('POLAR_ENV_COOKIE', 'REPALIS_ENV_COOKIE'),
    ('POLAR_DESCRIPTION', 'REPALIS_DESCRIPTION'),
    ('POLAR_SETUP', 'REPALIS_SETUP'),
    ('POLAR_SERVER', 'REPALIS_SERVER'),
    ('POLAR_TOKEN', 'REPALIS_TOKEN'),
    ('POLAR_SUCCESS_URL', 'REPALIS_SUCCESS_URL'),
    ('NEXT_PUBLIC_POLAR_', 'NEXT_PUBLIC_REPALIS_'),
    ("'polar_session'", "'repalis_session'"),
    ('"polar_session"', '"repalis_session"'),
    ('polar_session', 'repalis_session'),
    ('polar_cl_', 'repalis_cl_'),

    # Sentry & Assets
    ("org: 'polar-sh'", "org: 'repalis'"),
    ('org: "polar-sh"', 'org: "repalis"'),
    ('polar-public-assets', 'repalis-public-assets'),
    ('form-action \'self\' ${process.env.NEXT_PUBLIC_API_URL} polar:;', 'form-action \'self\' ${process.env.NEXT_PUBLIC_API_URL} repalis:;'),
    ('http://api.polar.test', 'http://api.repalis.test'),
    ('Polar Software', 'Repalis Software'),
]

def clean_file(p):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    orig = content
    for t, r in exact_replacements:
        content = content.replace(t, r)
    if orig != content:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

updated = 0
for target in clients_dirs:
    for root, dirs, files in os.walk(target):
        if any(x in root for x in ['node_modules', '.next', '.turbo', 'dist', '__pycache__']):
            continue
        for f in files:
            if f.endswith(('.ts', '.tsx', '.mjs', '.js', '.json', '.css', '.md', '.yml', '.yaml', '.tf')):
                if clean_file(os.path.join(root, f)):
                    updated += 1

print(f"Updated {updated} files across clients, github, and terraform.")
