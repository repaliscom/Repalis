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

replace_in_file('server/repalis/locker.py', [
    ('polarlock:', 'repalislock:'),
])

replace_in_file('server/repalis/operational_errors.py', [
    ('polar.worker', 'repalis.worker'),
])

replace_in_file('server/repalis/transaction/service/balance.py', [
    ('Polar currency', 'Repalis currency'),
    ('Polar account', 'Repalis account'),
])

replace_in_file('server/repalis/models/merchant_migration_record.py', [
    ('Polar bills', 'Repalis bills'),
    ('Polar counterpart', 'Repalis counterpart'),
    ('Polar object', 'Repalis object'),
])

replace_in_file('server/load_tests/README.md', [
    ("Polar's payment infrastructure", "Repalis's payment infrastructure"),
    ('Polar API server', 'Repalis API server'),
    ('polar_oat_', 'repalis_oat_'),
    ('polar_pat_', 'repalis_pat_'),
])

replace_in_file('server/scripts/seeds_load.py', [
    ('POLAR_ORG_SLUG = "polar"', 'REPALIS_ORG_SLUG = "repalis"'),
    ('POLAR_ORG_SLUG', 'REPALIS_ORG_SLUG'),
    ('"client_id": "polar"', '"client_id": "repalis"'),
    ('"client_secret": "polar-secret"', '"client_secret": "repalis-secret"'),
    ('"slug": "polar"', '"slug": "repalis"'),
    ('org_data["slug"] == "polar"', 'org_data["slug"] == "repalis"'),
    ('name="polar-self-env"', 'name="repalis-self-env"'),
    ('prefix="polar_cl_"', 'prefix="repalis_cl_"'),
    ('prefix="polar_c_"', 'prefix="repalis_c_"'),
    ('prefix="polar_oat_"', 'prefix="repalis_oat_"'),
    ('client_secret="polar_cl_e2e_seed_trial_subscription"', 'client_secret="repalis_cl_e2e_seed_trial_subscription"'),
    ('`polar auth login`', '`repalis auth login`'),
    ('WEBHOOK_SECRET_ENV_KEY = "POLAR_POLAR_WEBHOOK_SECRET"', 'WEBHOOK_SECRET_ENV_KEY = "REPALIS_WEBHOOK_SECRET"'),
    ('POLAR_POLAR_ORGANIZATION_ID', 'REPALIS_ORGANIZATION_ID'),
    ('POLAR_POLAR_SCALE_PRODUCT_ID', 'REPALIS_SCALE_PRODUCT_ID'),
    ('POLAR_POLAR_ACCESS_TOKEN', 'REPALIS_ACCESS_TOKEN'),
    ('POLAR_POLAR_API_URL', 'REPALIS_API_URL'),
])

replace_in_file('server/scripts/seed_repalis_for_repalis.py', [
    ('POLAR_ACCESS_TOKEN', 'REPALIS_ACCESS_TOKEN'),
    ('as polar:', 'as repalis:'),
    ('(polar,', '(repalis,'),
    ('polar,', 'repalis,'),
])

replace_in_file('server/scripts/assign_organization_owner.py', [
    ('--sync-polar-for-polar', '--sync-repalis-for-repalis'),
    ('sync_polar_for_polar', 'sync_repalis_for_repalis'),
])

print("Server Part 4 execution complete.")
