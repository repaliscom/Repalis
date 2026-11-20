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

# Server tests
replace_in_file("server/tests/organization/test_endpoints.py", [
    (r"https://x\.com/polar\b", "https://x.com/repalis"),
])
replace_in_file("server/tests/backoffice/impersonation/test_endpoints.py", [
    (r'"backoffice\.polar\.test"', '"backoffice.repalis.test"'),
])
replace_in_file("server/tests/backoffice/test_versioned_static.py", [
    (r'parents\[2\] / "polar" / "backoffice"', 'parents[2] / "repalis" / "backoffice"'),
])
replace_in_file("server/tests/customer_email_update/test_service.py", [
    (r"polar_cev_bogustoken", "repalis_cev_bogustoken"),
])
replace_in_file("server/tests/customer_portal/endpoints/test_customer.py", [
    (r"polar_cev_bogus", "repalis_cev_bogus"),
])
replace_in_file("server/tests/fixtures/random_objects.py", [
    (r'rstr\("POLAR-"\)', 'rstr("REPALIS-")'),
])
replace_in_file("server/tests/license_key/test_schemas.py", [
    (r'prefix="POLAR"', 'prefix="REPALIS"'),
    (r'== "POLAR"', '== "REPALIS"'),
])
replace_in_file("server/tests/merchant_migration/test_endpoints.py", [
    (r'"acct_polar"', '"acct_repalis"'),
])
replace_in_file("server/tests/merchant_migration/test_service.py", [
    (r'"acct_polar"', '"acct_repalis"'),
])
replace_in_file("server/tests/oauth2/grants/test_claim.py", [
    (r'"polar_act_claim"', '"repalis_act_claim"'),
])
replace_in_file("server/tests/oauth2/service/test_oauth2_token.py", [
    (r'"polar_rt_o_123"', '"repalis_rt_o_123"'),
])
replace_in_file("server/tests/observability/observability/test_log_correlation_middleware.py", [
    (r'b"x-polar-client-runtime"', 'b"x-repalis-client-runtime"'),
    (r'b"x-polar-client-update"', 'b"x-repalis-client-update"'),
])
replace_in_file("server/tests/observability/observability/test_posthog_client_context.py", [
    (r'b"x-polar-client-runtime"', 'b"x-repalis-client-runtime"'),
    (r'b"x-polar-client-update"', 'b"x-repalis-client-update"'),
])
replace_in_file("server/tests/payout/test_service.py", [
    (r'"POLAR-12345"', '"REPALIS-12345"'),
])
replace_in_file("server/tests/subscription/test_endpoints.py", [
    (r'polar-subscriptions', 'repalis-subscriptions'),
])
replace_in_file("server/tests/test_config.py", [
    (r'username="polar"', 'username="repalis"'),
    (r'database="polar"', 'database="repalis"'),
    (r'postgresql\+asyncpg://polar:s3cret@primary\.example\.com:6432/polar', 'postgresql+asyncpg://repalis:s3cret@primary.example.com:6432/repalis'),
    (r'database_key\] == "polar"', 'database_key] == "repalis"'),
])
replace_in_file("server/tests/test_rate_limit.py", [
    (r"polar_acl_link", "repalis_acl_link"),
])
replace_in_file("server/tests/integrations/github/service/test_secret_scanning.py", [
    (r'"polar_personal_access_token"', '"repalis_personal_access_token"'),
    (r'"polar_client_secret"', '"repalis_client_secret"'),
    (r'"POLAR_PERSONAL_ACCESS_TOKEN"', '"REPALIS_PERSONAL_ACCESS_TOKEN"'),
])
replace_in_file("server/tests/backoffice/merchant_migrations/test_service.py", [
    (r'"polar:fx:usd:v1:eur"', '"repalis:fx:usd:v1:eur"'),
])
replace_in_file("server/tests/organization_domain/test_endpoints.py", [
    (r"_polar-challenge\.", "_repalis-challenge."),
])
replace_in_file("server/tests/organization_domain/test_service.py", [
    (r"_polar-challenge\.", "_repalis-challenge."),
])
replace_in_file("server/tests/e2e/infra/task_drain.py", [
    (r"polar_root", "repalis_root"),
])
replace_in_file("server/tests/test_openapi.py", [
    (r"polar/openapi\.py", "repalis/openapi.py"),
])

print("Completed server tests script!")
