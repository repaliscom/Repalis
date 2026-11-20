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

# Dockerfile
replace_in_file('server/Dockerfile', [
    ('org.opencontainers.image.description="Polar"', 'org.opencontainers.image.description="Repalis"'),
    ('/var/runtime/polar-bootstrap', '/var/runtime/repalis-bootstrap'),
])

# Emails
replace_in_file('server/emails/package.json', [
    ('python -m polar.email.schemas', 'python -m repalis.email.schemas'),
])
replace_in_file('server/emails/README.md', [
    ('server/polar/email/schemas.py', 'server/repalis/email/schemas.py'),
    (re.compile(r'\bPolar\b'), 'Repalis'),
])
replace_in_file('server/emails/src/components/OrganizationHeader.tsx', [
    ('polar-public-files.s3.amazonaws.com', 'repalis-public-files.s3.amazonaws.com'),
    ('polar-public-sandbox-files.s3.amazonaws.com', 'repalis-public-sandbox-files.s3.amazonaws.com'),
])
replace_in_file('server/emails/src/preview.ts', [
    ('polar-public-sandbox-files.s3.amazonaws.com', 'repalis-public-sandbox-files.s3.amazonaws.com'),
])
replace_in_file('server/emails/src/emails/index.ts', [
    ('polar_self_', 'repalis_self_'),
])
replace_in_file('server/emails/src/types/openapi.ts', [
    ('polar_self_', 'repalis_self_'),
    ('PolarSelf', 'RepalisSelf'),
])

# Pyproject
replace_in_file('server/pyproject.toml', [
    ('Polar-Version', 'Repalis-Version'),
])

# Invoice & Stripe Services
replace_in_file('server/repalis/invoice/seller.py', [
    ("Polar's", "Repalis's"),
    ('Polar is', 'Repalis is'),
    (re.compile(r'\bPolar\b'), 'Repalis'),
])
replace_in_file('server/repalis/invoice/service.py', [
    ('Polar revenue share', 'Repalis revenue share'),
    ('Polar Software, Inc.', 'Repalis Software, Inc.'),
    (re.compile(r'\bPolar\b'), 'Repalis'),
])
replace_in_file('server/repalis/integrations/stripe/service.py', [
    ('polar.models.', 'repalis.models.'),
    ('polar.order.', 'repalis.order.'),
    ('polar.integrations.', 'repalis.integrations.'),
    ('polar:transfer_reverse:', 'repalis:transfer_reverse:'),
    ('polar:tax_transaction:', 'repalis:tax_transaction:'),
    ('polar:tax_transaction_revert:', 'repalis:tax_transaction_revert:'),
])
replace_in_file('server/repalis/organization/service.py', [
    ('Polar grants', 'Repalis grants'),
    ('Polar requested', 'Repalis requested'),
    ('Polar self', 'Repalis self'),
    ('Polar-fulfilled', 'Repalis-fulfilled'),
    (re.compile(r'\bPolar\b'), 'Repalis'),
])
replace_in_file('server/repalis/config.py', [
    ('polar123456789', 'repalis123456789'),
    ('polarpolar', 'repalisrepalis'),
])

# Tests
replace_in_file('server/tests/test_sdk.py', [
    ('polar: RepalisAsync', 'repalis: RepalisAsync'),
    ('polar.', 'repalis.'),
])
replace_in_file('server/tests/scripts/test_tinybird.py', [
    ('"polar"', '"repalis"'),
    ('expected polar', 'expected repalis'),
    ('workspace polar', 'workspace repalis'),
])
replace_in_file('server/tests/merchant_migration/test_cutover.py', [
    ('test_no_polar_price', 'test_no_repalis_price'),
    ('paused_polar_subscription', 'paused_repalis_subscription'),
    ('pm_card_polar', 'pm_card_repalis'),
    ('already_in_polar', 'already_in_repalis'),
    ('test_polar_subscription', 'test_repalis_subscription'),
])

print("Server Part 3 execution complete.")
