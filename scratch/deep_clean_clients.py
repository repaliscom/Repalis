import os
import re

clients_dirs = ['clients', '.github']

replacements = [
    # Better Auth adapter
    ('export { polar } from', 'export { repalis } from'),
    ('PolarBetterAuthPlugin', 'RepalisBetterAuthPlugin'),
    ('PolarOrganizationCustomerCreateParams', 'RepalisOrganizationCustomerCreateParams'),
    ('PolarOrganizationOptions', 'RepalisOrganizationOptions'),
    ('PolarOrganizationOwnerInvariantError', 'RepalisOrganizationOwnerInvariantError'),
    ('PolarOrganizationRoleSyncOptions', 'RepalisOrganizationRoleSyncOptions'),
    ('mapBetterAuthRoleToPolar', 'mapBetterAuthRoleToRepalis'),
    ('polarMember', 'repalisMember'),
    ('PolarMember', 'RepalisMember'),
    ('polarOrgSlug', 'repalisOrgSlug'),
    ('polarAccessToken', 'repalisAccessToken'),

    # Checkout & payment embed
    ('data-polar-checkout', 'data-repalis-checkout'),
    ('data-polar-payment-method', 'data-repalis-payment-method'),
    ('PolarPaymentMethod', 'RepalisPaymentMethod'),
    ('PolarApiOutboundProps', 'RepalisApiOutboundProps'),

    # Headers & attributes
    ('Polar-Organization', 'Repalis-Organization'),
    ('Polar-Version', 'Repalis-Version'),
    ('x-polar-user', 'x-repalis-user'),
    ('polar_types', 'repalis_types'),
    ('setup-polar', 'setup-repalis'),
    ('POLAR_SKIP_DTS', 'REPALIS_SKIP_DTS'),

    # Webhooks
    ('PolarWebhookError', 'RepalisWebhookError'),
    ('PolarWebhookVerificationError', 'RepalisWebhookVerificationError'),
    ('PolarWebhookUnknownTypeError', 'RepalisWebhookUnknownTypeError'),
    ('PolarRequestValidationError', 'RepalisRequestValidationError'),

    # Phrases
    ('Polar account', 'Repalis account'),
    ('Polar Account', 'Repalis Account'),
    ('Polar organization', 'Repalis organization'),
    ('Polar Organization', 'Repalis Organization'),
    ('Polar customer', 'Repalis customer'),
    ('Polar Customer', 'Repalis Customer'),
    ('Polar checkout', 'Repalis checkout'),
    ('Polar Checkout', 'Repalis Checkout'),
    ('Polar subscription', 'Repalis subscription'),
    ('Polar Subscription', 'Repalis Subscription'),
    ('Polar product', 'Repalis product'),
    ('Polar Product', 'Repalis Product'),
    ('Polar dashboard', 'Repalis dashboard'),
    ('Polar Dashboard', 'Repalis Dashboard'),
    ('on Polar', 'on Repalis'),
    ('from Polar', 'from Repalis'),
    ('to Polar', 'to Repalis'),
    ('with Polar', 'with Repalis'),
    ('by Polar', 'by Repalis'),
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
for target in clients_dirs:
    for root, dirs, files in os.walk(target):
        if any(x in root for x in ['node_modules', '.next', '.turbo', 'dist', '__pycache__']):
            continue
        for f in files:
            if f.endswith(('.ts', '.tsx', '.mjs', '.js', '.json', '.css', '.md')):
                if clean_file(os.path.join(root, f)):
                    updated += 1

print(f"Deep cleaned {updated} files in clients and github.")
