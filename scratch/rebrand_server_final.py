import os
import re

REPO_DIR = r"d:\Repalis"

def replace_in_file(rel_path, replacements):
    path = os.path.join(REPO_DIR, rel_path.replace("/", os.sep))
    if not os.path.exists(path):
        print(f"Warning: file {rel_path} does not exist")
        return False
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {rel_path}: {e}")
        return False
        
    orig = content
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)
            
    if content != orig:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)
        print(f"Updated {rel_path}")
        return True
    return False

# 1. Backoffice logo and strings
replace_in_file("server/repalis/backoffice/ascii_logo.py", [
    (r"POLAR_ASCII_LOGO", "REPALIS_ASCII_LOGO"),
])
# Add backwards compatibility alias at end of ascii_logo.py
with open(os.path.join(REPO_DIR, "server", "repalis", "backoffice", "ascii_logo.py"), "a", encoding="utf-8") as f:
    f.write("\nPOLAR_ASCII_LOGO = REPALIS_ASCII_LOGO\n")

replace_in_file("server/repalis/backoffice/__init__.py", [
    (r"POLAR_ASCII_LOGO", "REPALIS_ASCII_LOGO"),
])
replace_in_file("server/repalis/backoffice/components/_layout.py", [
    (r'"Polar Backoffice"', '"Repalis Backoffice"'),
])
replace_in_file("server/repalis/backoffice/layout.py", [
    (r"Polar logo in sidebar", "Repalis logo in sidebar"),
])
replace_in_file("server/repalis/backoffice/merchant_migrations/service.py", [
    (r'"polar:fx:usd:v1"', '"repalis:fx:usd:v1"'),
])
replace_in_file("server/repalis/backoffice/orders/endpoints.py", [
    (r"Only Polar support can undo", "Only Repalis support can undo"),
])
replace_in_file("server/repalis/backoffice/organizations_v2/endpoints.py", [
    (r"Resolves the Polar-for-Repalis", "Resolves the Repalis-for-Repalis"),
    (r"in Polar's org", "in Repalis's org"),
])
replace_in_file("server/repalis/backoffice/organizations_v2/forms.py", [
    (r"integrate and use Polar", "integrate and use Repalis"),
])
replace_in_file("server/repalis/backoffice/organizations_v2/views/sections/risk_signals.py", [
    (r"Polar checks", "Repalis checks"),
])

# 2. Domain verification
replace_in_file("server/repalis/models/organization_domain.py", [
    (r'return f"_polar-challenge\.\{self\.domain\}"', 'return f"_repalis-challenge.{self.domain}"'),
])
replace_in_file("server/repalis/organization_domain/service.py", [
    (r'records = await _lookup_txt\(organization_domain\.verification_record_name\)',
     'records = await _lookup_txt(organization_domain.verification_record_name)\n        if organization_domain.verification_record_value not in records:\n            records.update(await _lookup_txt(f"_polar-challenge.{organization_domain.domain}"))'),
])
replace_in_file("server/repalis/organization_domain/schemas.py", [
    (r"When Polar verified the domain", "When Repalis verified the domain"),
])

# 3. CSV / Export Filenames and Cache Keys
replace_in_file("server/repalis/customer/endpoints.py", [
    (r'"polar-customers\.csv"', '"repalis-customers.csv"'),
])
replace_in_file("server/repalis/customer/service.py", [
    (r'"polar:customer_state:v8:', '"repalis:customer_state:v8:'),
])
replace_in_file("server/repalis/customer_portal/endpoints/customer.py", [
    (r'filename = f"polar-customer-export-', 'filename = f"repalis-customer-export-'),
])
replace_in_file("server/repalis/metrics/endpoints.py", [
    (r'"polar-metrics\.csv"', '"repalis-metrics.csv"'),
])
replace_in_file("server/repalis/order/export.py", [
    (r'filename = "polar-orders"', 'filename = "repalis-orders"'),
])
replace_in_file("server/repalis/payout/endpoints.py", [
    (r'"polar-payout-', '"repalis-payout-'),
])
replace_in_file("server/repalis/subscription/export.py", [
    (r'filename = "polar-subscriptions"', 'filename = "repalis-subscriptions"'),
])
replace_in_file("server/repalis/transaction/export.py", [
    (r'filename = "polar-income"', 'filename = "repalis-income"'),
])
replace_in_file("server/repalis/worker/_sqs.py", [
    (r'return f"polar-retry-', 'return f"repalis-retry-'),
])

# 4. Notifications & Client Names
replace_in_file("server/repalis/notifications/tasks/push.py", [
    (r'title="Polar"', 'title="Repalis"'),
])
replace_in_file("server/repalis/oauth2/mcp_client.py", [
    (r'"client_name": "Polar MCP Client"', '"client_name": "Repalis MCP Client"'),
])
replace_in_file("server/repalis/oauth2/metadata.py", [
    (r'resource_name="Polar"', 'resource_name="Repalis"'),
])
replace_in_file("server/repalis/oauth2/service/oauth2_token.py", [
    (r"Your Polar Access Token has been leaked", "Your Repalis Access Token has been leaked"),
])
replace_in_file("server/repalis/personal_access_token/service.py", [
    (r"Your Polar Personal Access Token has been leaked", "Your Repalis Personal Access Token has been leaked"),
])

# 5. Docstrings, comments and helpers
replace_in_file("server/repalis/credit_note/generator.py", [
    (r'self\.set_creator\("Polar"\)', 'self.set_creator("Repalis")'),
])
replace_in_file("server/repalis/benefit/grant/endpoints.py", [
    (r"Polar IDs", "Repalis IDs"),
])
replace_in_file("server/repalis/benefit/grant/schemas.py", [
    (r"Polar IDs", "Repalis IDs"),
])
replace_in_file("server/repalis/benefit/strategies/discord/service.py", [
    (r"Polar bot", "Repalis bot"),
])
replace_in_file("server/repalis/checkout/ip_geolocation.py", [
    (r"python -m polar\.checkout", "python -m repalis.checkout"),
])
replace_in_file("server/repalis/checkout/schemas.py", [
    (r"Polar iframe", "Repalis iframe"),
])
replace_in_file("server/repalis/checkout/service.py", [
    (r"default Polar", "default Repalis"),
])
replace_in_file("server/repalis/cli/schemas.py", [
    (r"when Polar sends this event", "when Repalis sends this event"),
])
replace_in_file("server/repalis/cli/service.py", [
    (r"polar webhook listen", "repalis webhook listen"),
])
replace_in_file("server/repalis/customer_meter/schemas.py", [
    (r"Polar IDs", "Repalis IDs"),
])
replace_in_file("server/repalis/declarative_config/guard.py", [
    (r"polar config apply", "repalis config apply"),
])
replace_in_file("server/repalis/discount/repository.py", [
    (r"polar\.kit\.email", "repalis.kit.email"),
])
replace_in_file("server/repalis/event/mover.py", [
    (r"python -m polar\.event\.mover", "python -m repalis.event.mover"),
])
replace_in_file("server/repalis/models/discord_guild_connection.py", [
    (r"The Polar bot", "The Repalis bot"),
])
replace_in_file("server/repalis/models/payout.py", [
    (r"server/polar/models/payout_attempt\.py", "server/repalis/models/payout_attempt.py"),
])
replace_in_file("server/repalis/models/product.py", [
    (r"polar\.product", "repalis.product"),
])
replace_in_file("server/repalis/models/file.py", [
    (r"# Flag for Polar to disable", "# Flag for Repalis to disable"),
])
replace_in_file("server/repalis/models/organization_risk_signal.py", [
    (r"\(Polar\)\.", "(Repalis)."),
])
replace_in_file("server/repalis/models/support_case.py", [
    (r"# Polar conceding a dispute", "# Repalis conceding a dispute"),
])
replace_in_file("server/repalis/order/service.py", [
    (r"Contact Polar support", "Contact Repalis support"),
])
replace_in_file("server/repalis/organization_review/analyzer.py", [
    (r"'polar' signals come from our own", "'repalis' signals come from our own"),
])
replace_in_file("server/repalis/organization_review/collectors/setup.py", [
    (r"PolarReviewBot/1\.0", "RepalisReviewBot/1.0"),
])
replace_in_file("server/repalis/outpost/endpoints.py", [
    (r"Polar counts", "Repalis counts"),
])
replace_in_file("server/repalis/outpost/schemas.py", [
    (r"is Polar's", "is Repalis's"),
])
replace_in_file("server/repalis/outpost/service.py", [
    (r"all in Polar:", "all in Repalis:"),
])
replace_in_file("server/repalis/payment/repository.py", [
    (r"polar\.models\.payment", "repalis.models.payment"),
])
replace_in_file("server/repalis/product/name_check.py", [
    (r"Polar's Acceptable Use Policy", "Repalis's Acceptable Use Policy"),
])
replace_in_file("server/repalis/support_case/tasks.py", [
    (r"Polar staff", "Repalis staff"),
])
replace_in_file("server/repalis/transaction/service/payment.py", [
    (r"Polar Custom Checkout", "Repalis Custom Checkout"),
])
replace_in_file("server/repalis/transaction/service/transaction.py", [
    (r"Main Polar currency", "Main Repalis currency"),
])
replace_in_file("server/repalis/user/endpoints.py", [
    (r"Polar account\.", "Repalis account."),
])
replace_in_file("server/repalis/webhook/constants.py", [
    (r"Polar's original HMAC", "Repalis's original HMAC"),
])
replace_in_file("server/repalis/webhook/eventstream.py", [
    (r"polar webhook trigger", "repalis webhook trigger"),
])
replace_in_file("server/repalis/webhook/service.py", [
    (r"the Polar webhook", "the Repalis webhook"),
])
replace_in_file("server/repalis/webhook/webhooks.py", [
    (r"Sent when Polar takes over", "Sent when Repalis takes over"),
])
replace_in_file("server/repalis/worker/_runner.py", [
    (r"polar/worker", "repalis/worker"),
])
replace_in_file("server/repalis/meter/service.py", [
    (r"the Polar meter ID", "the Repalis meter ID"),
])

# 6. server/scripts
replace_in_file("server/scripts/check_env_vars.py", [
    (r'CONFIG = REPO / "server" / "polar" / "config\.py"', 'CONFIG = REPO / "server" / "repalis" / "config.py"'),
])
replace_in_file("server/scripts/shell.py", [
    (r"Welcome to the Polar shell!", "Welcome to the Repalis shell!"),
])
replace_in_file("server/scripts/linters/hash_secret.py", [
    (r"polar\.kit\.hash_secrets", "repalis.kit.hash_secrets"),
    (r"polar\.kit\.crypto", "repalis.kit.crypto"),
])
replace_in_file("server/scripts/backfill_customer_first_user_event_at.py", [
    (r"Polar id,", "Repalis id,"),
])
replace_in_file("server/scripts/backfill_generated_sepa.py", [
    (r"Polar-billed", "Repalis-billed"),
])
replace_in_file("server/scripts/backfill_trial_redemption_customer_email.py", [
    (r"polar\.kit\.email", "repalis.kit.email"),
])
replace_in_file("server/scripts/loadtest_setup.py", [
    (r"polar_pat_", "repalis_pat_"),
    (r"polar_oat_", "repalis_oat_"),
])

print("Completed server final script!")
