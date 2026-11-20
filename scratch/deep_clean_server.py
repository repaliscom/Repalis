import os
import re

targets = ['server/repalis', 'server/tests', 'server/benchmarks', 'server/scripts']

replacements = [
    # SDK imports in server
    ('PolarNetworkError', 'RepalisNetworkError'),
    ('PolarServerError', 'RepalisServerError'),
    ('PolarClientError', 'RepalisClientError'),
    ('PolarAsync', 'RepalisAsync'),
    ('from repalis.v2026_10 import Polar', 'from repalis.v2026_10 import Repalis'),
    ('from repalis.v2027_01 import Polar', 'from repalis.v2027_01 import Repalis'),
    ('from repalis.v2026_04 import Polar', 'from repalis.v2026_04 import Repalis'),
    ('import Polar', 'import Repalis'),

    # VAT and Seller helpers
    ('get_polar_vat_label', 'get_repalis_vat_label'),
    ('get_polar_vat_number', 'get_repalis_vat_number'),
    ('polar_http_request_total', 'repalis_http_request_total'),
    ('reverse_balance_polar', 'reverse_balance_repalis'),
    ('polar_ops', 'repalis_ops'),
    ('polar_download_url', 'repalis_download_url'),
    ('_CARDS_ALREADY_ON_POLAR', '_CARDS_ALREADY_ON_REPALIS'),

    # Email and User strings
    ('on Polar', 'on Repalis'),
    ('from Polar', 'from Repalis'),
    ('to Polar', 'to Repalis'),
    ('by Polar', 'by Repalis'),
    ('with Polar', 'with Repalis'),
    ('into Polar', 'into Repalis'),
    ('onto Polar', 'onto Repalis'),
    ('Polar API', 'Repalis API'),
    ('Polar platform', 'Repalis platform'),
    ('Polar organization', 'Repalis organization'),
    ('Polar Organization', 'Repalis Organization'),
    ('Polar customer', 'Repalis customer'),
    ('Polar Customer', 'Repalis Customer'),
    ('Polar event', 'Repalis event'),
    ('Polar Event', 'Repalis Event'),
    ('Polar product', 'Repalis product'),
    ('Polar Product', 'Repalis Product'),
    ('Polar subscription', 'Repalis subscription'),
    ('Polar Subscription', 'Repalis Subscription'),
    ('from_name="Polar"', 'from_name="Repalis"'),
    ('from_name = "Polar"', 'from_name = "Repalis"'),
    ('for Polar, a Merchant of Record', 'for Repalis, a Merchant of Record'),
    ('Polar self-billing', 'Repalis self-billing'),
    ('Polar\'s Stripe account', 'Repalis\'s Stripe account'),
    ('Polar’s Stripe account', 'Repalis’s Stripe account'),
    ('Polar received a payment', 'Repalis received a payment'),
    ('Polar creates subscriptions', 'Repalis creates subscriptions'),
    ('Polar holding it up', 'Repalis holding it up'),

    # Fixtures & Tokens
    ('polar_at_u_', 'repalis_at_u_'),
    ('polar_crt_', 'repalis_crt_'),
    ('polar_ci_', 'repalis_ci_'),
    ('polar_at_a_', 'repalis_at_a_'),
    ('polar_rt_u_', 'repalis_rt_u_'),
    ('polar_at_xxx', 'repalis_at_xxx'),
    ('polar_customer', 'repalis_customer'),
    ('polar_product', 'repalis_product'),
]

def clean_file(p):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    orig = content

    for t, r in replacements:
        content = content.replace(t, r)

    if orig != content:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

updated = 0
for target in targets:
    if os.path.isfile(target):
        if clean_file(target):
            updated += 1
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            if any(x in root for x in ['__pycache__']):
                continue
            for f in files:
                if f.endswith(('.py', '.md')):
                    if clean_file(os.path.join(root, f)):
                        updated += 1

print(f"Deep cleaned {updated} files across server.")
