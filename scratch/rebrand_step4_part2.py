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

# 1. merchant_migration/
mm_dir = 'server/repalis/merchant_migration'
for f in os.listdir(mm_dir):
    p = os.path.join(mm_dir, f)
    if os.path.isfile(p):
        replace_in_file(p, [
            ('Polar support', 'Repalis support'),
            ('in Polar', 'in Repalis'),
            ('on Polar', 'on Repalis'),
            ('to Polar', 'to Repalis'),
            ('from Polar', 'from Repalis'),
            ('Polar calculated', 'Repalis calculated'),
            ('Polar calculates', 'Repalis calculates'),
            ('Polar would', 'Repalis would'),
            ('Polar keeps', 'Repalis keeps'),
            ('Polar imports', 'Repalis imports'),
            ('Polar takes', 'Repalis takes'),
            ('Polar doesn\'t', 'Repalis doesn\'t'),
            ('Polar bills', 'Repalis bills'),
            ('Polar taxes', 'Repalis taxes'),
            ('Polar supports', 'Repalis supports'),
            ('Polar puts', 'Repalis puts'),
            ('polar_product', 'repalis_product'),
            ('polar_customer', 'repalis_customer'),
            ('polar_subscription', 'repalis_subscription'),
            ('polar_amounts', 'repalis_amounts'),
            ('polar_orders', 'repalis_orders'),
            ('polar.subscribed', 'repalis.subscribed'),
            ('polar.stripe_customer_id', 'repalis.stripe_customer_id'),
            ('polar.id', 'repalis.id'),
            ('polar: CustomerStripeIdentity', 'repalis: CustomerStripeIdentity'),
            ('polar is not None', 'repalis is not None'),
            ('product_exists_in_polar', 'product_exists_in_repalis'),
            ('CUSTOMER_SUBSCRIBED_ON_POLAR', 'CUSTOMER_SUBSCRIBED_ON_REPALIS'),
            (re.compile(r'\bPolar\b'), 'Repalis'),
        ])

# 2. organization endpoints & schemas
replace_in_file('server/repalis/organization/endpoints.py', [
    ('Polar orders', 'Repalis orders'),
    ('Polar invoices', 'Repalis invoices'),
    ('Polar billing', 'Repalis billing'),
    ('Polar order', 'Repalis order'),
    (re.compile(r'\bPolar\b'), 'Repalis'),
])
replace_in_file('server/repalis/organization/schemas.py', [
    (re.compile(r'\bPolar\b'), 'Repalis'),
])

# 3. docs & guides
replace_in_file('server/repalis/agent/auth.md', [
    (re.compile(r'\bPolar\b'), 'Repalis'),
    ("Polar's", "Repalis's"),
    ('polar_act_', 'repalis_act_'),
])
replace_in_file('server/repalis/backoffice/DEVELOPMENT_GUIDE.md', [
    (re.compile(r'\bPolar\b'), 'Repalis'),
    ('polar/backoffice/', 'repalis/backoffice/'),
])
replace_in_file('server/repalis/backoffice/merchant_migrations/status.py', [
    (re.compile(r'\bPolar\b'), 'Repalis'),
])

# 4. repalis integration client & service
replace_in_file('server/repalis/integrations/repalis/client.py', [
    ('PolarRateLimitError', 'RepalisRateLimitError'),
    ('as PolarSDK', 'as RepalisSDK'),
    ('PolarSDK', 'RepalisSDK'),
    ('Polar billing', 'Repalis billing'),
    (re.compile(r'\bPolar\b'), 'Repalis'),
])
replace_in_file('server/repalis/integrations/repalis/service.py', [
    ('Polar checkout', 'Repalis checkout'),
    ('Polar billing', 'Repalis billing'),
    ('polar-self', 'repalis-self'),
    ('"Polar"', '"Repalis"'),
    (re.compile(r'\bPolar\b'), 'Repalis'),
])

# 5. organization review
replace_in_file('server/repalis/organization_review/acceptable-use-policy.fallback.mdx', [
    ('Polar Acceptable Use Policy', 'Repalis Acceptable Use Policy'),
    ('Polar Software, Inc.', 'Repalis Software, Inc.'),
    ('“Polar”', '“Repalis”'),
    ('Polar IP', 'Repalis IP'),
    (re.compile(r'\bPolar\b'), 'Repalis'),
])
replace_in_file('server/repalis/organization_review/analyzer.py', [
    (re.compile(r'\bPolar\b'), 'Repalis'),
])

# 6. models
replace_in_file('server/repalis/models/pledge.py', [
    (re.compile(r'\bPolar\b'), 'Repalis'),
    (re.compile(r'\bpolar\b'), 'repalis'),
])
replace_in_file('server/repalis/models/transaction.py', [
    (re.compile(r'\bPolar\b'), 'Repalis'),
    ("Polar's", "Repalis's"),
])

# 7. scripts
for s in ['server/scripts/seeds_load.py', 'server/scripts/seed_repalis_for_repalis.py', 'server/scripts/assign_organization_owner.py']:
    replace_in_file(s, [
        ('POLAR_SELF', 'REPALIS_SELF'),
        ('polar_self', 'repalis_self'),
        ('polar_seed', 'repalis_seed'),
        ('seed_polar_for_polar', 'seed_repalis_for_repalis'),
        ('polar: RepalisAsync', 'repalis: RepalisAsync'),
        ('polar.', 'repalis.'),
        (re.compile(r'\bPolar\b'), 'Repalis'),
    ])

# 8. emails
for root, _, files in os.walk('server/emails'):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('PolarSelf', 'RepalisSelf'),
            ('Polar Logo', 'Repalis Logo'),
            ('Polar Software Inc', 'Repalis Software Inc'),
            ('Polar Software, Inc.', 'Repalis Software, Inc.'),
            ('Polar', 'Repalis'),
            ('polar-logo', 'repalis-logo'),
            ('polar-public-assets', 'repalis-public-assets'),
        ])

# 9. monitoring grafana dashboards
for root, _, files in os.walk('server/monitoring/grafana/dashboards'):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('polar_http_', 'repalis_http_'),
            ('polar_checkout_', 'repalis_checkout_'),
            ('polar_task_', 'repalis_task_'),
            ('polar_slo_', 'repalis_slo_'),
            ('polar_queue_', 'repalis_queue_'),
            ('polar_tax_', 'repalis_tax_'),
            ('polar_staged_', 'repalis_staged_'),
            ('Polar', 'Repalis'),
        ])

# 10. tests
for root, _, files in os.walk('server/tests'):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('x-polar-allowed-subjects', 'x-repalis-allowed-subjects'),
            ('x-polar-pagination', 'x-repalis-pagination'),
            ('x-polar-environment', 'x-repalis-environment'),
            ('x-polar-client-version', 'x-repalis-client-version'),
            ('Polar-Version', 'Repalis-Version'),
            ('Polar-Organization', 'Repalis-Organization'),
            ('polar_pat_', 'repalis_pat_'),
            ('polar_oat_', 'repalis_oat_'),
            ('polar_cst_', 'repalis_cst_'),
            ('polar_mst_', 'repalis_mst_'),
            ('polar_cs_', 'repalis_cs_'),
            ('polar_cl_', 'repalis_cl_'),
            ('polar_c_', 'repalis_c_'),
            ('polar_us_', 'repalis_us_'),
            ('polar_at_o_', 'repalis_at_o_'),
            ('polar_ac_', 'repalis_ac_'),
            ('polar_secret', 'repalis_secret'),
            ('polar_wh_secret_', 'repalis_wh_secret_'),
            ('polar-retry-', 'repalis-retry-'),
            ('POLAR-0001', 'REPALIS-0001'),
            ('product_exists_in_polar', 'product_exists_in_repalis'),
            ('CUSTOMER_SUBSCRIBED_ON_POLAR', 'CUSTOMER_SUBSCRIBED_ON_REPALIS'),
            ('PolarSelf', 'RepalisSelf'),
            ('Polar Software Inc', 'Repalis Software Inc'),
            ('Polar Software, Inc.', 'Repalis Software, Inc.'),
            ('polar-public-assets', 'repalis-public-assets'),
            ('polar-logo-2026-black-badge.png', 'repalis-logo-2026-black-badge.png'),
            ('alt="Polar Logo"', 'alt="Repalis Logo"'),
            ('"title": "Polar API"', '"title": "Repalis API"'),
            ('"summary": "Polar HTTP and Webhooks API"', '"summary": "Repalis HTTP and Webhooks API"'),
            ('Polar API documentation', 'Repalis API documentation'),
            ("Polar's MCP server", "Repalis's MCP server"),
            ("Polar's CLI", "Repalis's CLI"),
            ('Polar purchases library', 'Repalis purchases library'),
            ('Polar', 'Repalis'),
        ])

print("Server Part 2 completed cleanly.")
