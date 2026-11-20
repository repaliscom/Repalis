import os
import re

server_dirs = ['server/repalis', 'server/tests', 'server/benchmarks', 'server/AGENTS.md']

# Explicit replacements
replacements = [
    # Core exception classes
    ('PolarRequestValidationError', 'RepalisRequestValidationError'),
    ('PolarAuthRedirectionError', 'RepalisAuthRedirectionError'),
    ('PolarRedirectionError', 'RepalisRedirectionError'),
    ('PolarTaskError', 'RepalisTaskError'),
    ('PolarAuthError', 'RepalisAuthError'),
    ('PolarError', 'RepalisError'),

    # Handlers
    ('backoffice_polar_exception_handler', 'backoffice_repalis_exception_handler'),
    ('polar_exception_handler', 'repalis_exception_handler'),

    # Math and invoice
    ('polar_round', 'repalis_round'),
    ('get_polar_additional_info', 'get_repalis_additional_info'),

    # Repalis self integration
    ('PolarSelfService', 'RepalisSelfService'),
    ('PolarSelfClient', 'RepalisSelfClient'),
    ('PolarSelfClientError', 'RepalisSelfClientError'),
    ('PolarSelfClientOperationalError', 'RepalisSelfClientOperationalError'),
    ('PolarSelfClientValidationError', 'RepalisSelfClientValidationError'),
    ('PolarSelfNotConfigured', 'RepalisSelfNotConfigured'),
    ('PolarSelfInvoiceNotReady', 'RepalisSelfInvoiceNotReady'),
    ('PolarSelfWebhookError', 'RepalisSelfWebhookError'),
    ('PolarSelfNotApproved', 'RepalisSelfNotApproved'),
    ('PolarSelfOrderNotFound', 'RepalisSelfOrderNotFound'),
    ('PolarSelfCustomerNotFound', 'RepalisSelfCustomerNotFound'),
    ('PolarSelfPlanNotFound', 'RepalisSelfPlanNotFound'),
    ('PolarSelfPaidSubscriptionAlreadyExists', 'RepalisSelfPaidSubscriptionAlreadyExists'),
    ('PolarSelfNoActiveSubscription', 'RepalisSelfNoActiveSubscription'),
    ('PolarSelfBenefitGrantNotFound', 'RepalisSelfBenefitGrantNotFound'),
    ('PolarSelfPaymentMethodNotFound', 'RepalisSelfPaymentMethodNotFound'),
    ('PolarSelfPaymentMethodInUse', 'RepalisSelfPaymentMethodInUse'),
    ('PolarSelfOrderNotEligible', 'RepalisSelfOrderNotEligible'),
    ('PolarSelfEvent', 'RepalisSelfEvent'),
    ('PolarSelfSubscriptionConfirmationEmail', 'RepalisSelfSubscriptionConfirmationEmail'),
    ('PolarSelfSubscriptionConfirmationProps', 'RepalisSelfSubscriptionConfirmationProps'),
    ('PolarSelfSubscriptionCycledEmail', 'RepalisSelfSubscriptionCycledEmail'),
    ('PolarSelfSubscriptionCycledProps', 'RepalisSelfSubscriptionCycledProps'),
    ('PolarSelfSubscriptionCancellationEmail', 'RepalisSelfSubscriptionCancellationEmail'),
    ('PolarSelfSubscriptionCancellationProps', 'RepalisSelfSubscriptionCancellationProps'),
    ('PolarSelfSubscriptionRevokedEmail', 'RepalisSelfSubscriptionRevokedEmail'),
    ('PolarSelfSubscriptionRevokedProps', 'RepalisSelfSubscriptionRevokedProps'),
    ('PolarSelfSubscriptionPastDueEmail', 'RepalisSelfSubscriptionPastDueEmail'),
    ('PolarSelfSubscriptionPastDueProps', 'RepalisSelfSubscriptionPastDueProps'),
    ('PolarSelfStartupProgramWelcomeEmail', 'RepalisSelfStartupProgramWelcomeEmail'),
    ('PolarSelfStartupProgramWelcomeProps', 'RepalisSelfStartupProgramWelcomeProps'),

    ('polar_self_service', 'repalis_self_service'),
    ('polar_self', 'repalis_self'),
    ('POLAR_SELF_ENABLED', 'REPALIS_SELF_ENABLED'),
    ('POLAR_SCALE_PRODUCT_ID', 'REPALIS_SCALE_PRODUCT_ID'),

    # Migration
    ('polar_discount_code', 'repalis_discount_code'),
    ('polar_discount_amounts', 'repalis_discount_amounts'),
    ('polar_discount', 'repalis_discount'),
    ('on_polar', 'on_repalis'),
    ('share_on_polar', 'share_on_repalis'),
    ('"On Polar"', '"On Repalis"'),
    ("'On Polar'", "'On Repalis'"),
    ('"product_name_on_polar"', '"product_name_on_repalis"'),
    ('"customer_subscribed_on_polar"', '"customer_subscribed_on_repalis"'),
    ('_cards_already_on_polar', '_cards_already_on_repalis'),
    ('NON_POLAR_SELLERS', 'NON_REPALIS_SELLERS'),
    ('"non_polar_sellers"', '"non_repalis_sellers"'),

    # Test fixtures & mocks
    ('polar_cs_123', 'repalis_cs_123'),
    ('polar_app', 'repalis_app'),
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
for target in server_dirs:
    if os.path.isfile(target):
        if clean_file(target):
            updated += 1
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            if any(x in root for x in ['__pycache__']):
                continue
            for f in files:
                if f.endswith('.py') or f.endswith('.md'):
                    if clean_file(os.path.join(root, f)):
                        updated += 1

print(f"Updated {updated} files across server.")
