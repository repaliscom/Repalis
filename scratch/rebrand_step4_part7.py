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

replace_in_file('server/repalis/invoice/generator.py', [
    ('statement_descriptor=f"POLAR*', 'statement_descriptor=f"REPALIS*'),
    ('self.set_creator("Polar")', 'self.set_creator("Repalis")'),
])

replace_in_file('server/repalis/receipt/generator.py', [
    ('statement_descriptor=f"POLAR*', 'statement_descriptor=f"REPALIS*'),
    ('self.set_creator("Polar")', 'self.set_creator("Repalis")'),
])

replace_in_file('server/repalis/oauth2/service/oauth2_client.py', [
    ('Your Polar OAuth2', 'Your Repalis OAuth2'),
])

replace_in_file('server/repalis/startup_program/service.py', [
    ('Polar-for-Repalis', 'Repalis-for-Repalis'),
    ('Welcome to the Polar Startup Program', 'Welcome to the Repalis Startup Program'),
    ('Polar Startup Program', 'Repalis Startup Program'),
])

replace_in_file('server/repalis/payout/service.py', [
    ('description = "Polar fee"', 'description = "Repalis fee"'),
    ('Main Polar currency', 'Main Repalis currency'),
])

replace_in_file('server/repalis/kit/routing.py', [
    ('polar.openapi', 'repalis.openapi'),
])

replace_in_file('server/repalis/models/merchant_migration_operation.py', [
    ('polar.models', 'repalis.models'),
    ('polar.merchant_migration', 'repalis.merchant_migration'),
])

replace_in_file('server/repalis/worker/run_without_db.py', [
    ('polar.tasks', 'repalis.tasks'),
    ('polar.worker', 'repalis.worker'),
])

replace_in_file('server/scripts/linters/__main__.py', [
    ('over polar/', 'over repalis/'),
    ('parents[2] / "polar"', 'parents[2] / "repalis"'),
])

replace_in_file('server/repalis/backoffice/merchant_migrations/mrr.py', [
    ('imported Polar', 'imported Repalis'),
    ("Matches Polar's", "Matches Repalis's"),
])

replace_in_file('server/repalis/integrations/repalis/schemas.py', [
    ('Polar Startup Program', 'Repalis Startup Program'),
    ('mirrored Polar billing', 'mirrored Repalis billing'),
])

replace_in_file('server/repalis/models/organization.py', [
    ("in Polar's settlement currency", "in Repalis's settlement currency"),
    ('active Polar support grant', 'active Repalis support grant'),
])

replace_in_file('server/repalis/organization/legacy_schemas.py', [
    ('details Polar needs', 'details Repalis needs'),
])

replace_in_file('server/repalis/organization_review/schemas.py', [
    ('using Polar against', 'using Repalis against'),
    ('non-Polar Sellers', 'non-Repalis Sellers'),
])

replace_in_file('server/repalis/subscription/schemas.py', [
    ('exist in Polar', 'exist in Repalis'),
    ('available in their Polar', 'available in their Repalis'),
])

replace_in_file('server/repalis/tax/repository.py', [
    ('tax Polar remitted', 'tax Repalis remitted'),
])

replace_in_file('server/repalis/webhook/schemas.py', [
    ('Whether Polar signs', 'Whether Repalis signs'),
    ("means Polar's original HMAC", "means Repalis's original HMAC"),
])

replace_in_file('server/repalis/merchant_migration/precheck.py', [
    ('polar = existing.get(customer.email.lower())', 'repalis = existing.get(customer.email.lower())'),
    ('plans[customer.source_id] = stripe_id_conflict_reason(polar)', 'plans[customer.source_id] = stripe_id_conflict_reason(repalis)'),
])

print("Server Part 7 execution complete.")
