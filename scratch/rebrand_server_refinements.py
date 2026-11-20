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

# 1. config.py
replace_in_file("server/repalis/config.py", [
    (r'env = Environment\(os\.getenv\("POLAR_ENV", Environment\.development\)\)',
     'env = Environment(os.getenv("REPALIS_ENV") or os.getenv("POLAR_ENV") or Environment.development)'),
    (r'POLAR_USER_AGENT: str = "Repalis/1\.0 \(\+https://repalis\.com\)"',
     'REPALIS_USER_AGENT: str = "Repalis/1.0 (+https://repalis.com)"\n    POLAR_USER_AGENT: str = "Repalis/1.0 (+https://repalis.com)"'),
    (r'    # Repalis\'s usage of Repalis\n    POLAR_ACCESS_TOKEN: str = ""\n    POLAR_WEBHOOK_SECRET: str = ""\n    POLAR_ORGANIZATION_ID: str = ""\n    # Scale plan product, used by the Startup Program to grant a 100% discount\n    REPALIS_SCALE_PRODUCT_ID: str = ""\n    POLAR_API_URL: str = "https://api\.repalis\.com"',
     '''    # Repalis's usage of Repalis
    REPALIS_ACCESS_TOKEN: str = ""
    REPALIS_WEBHOOK_SECRET: str = ""
    REPALIS_ORGANIZATION_ID: str = ""
    POLAR_ACCESS_TOKEN: str = ""
    POLAR_WEBHOOK_SECRET: str = ""
    POLAR_ORGANIZATION_ID: str = ""
    # Scale plan product, used by the Startup Program to grant a 100% discount
    REPALIS_SCALE_PRODUCT_ID: str = ""
    REPALIS_API_URL: str = "https://api.repalis.com"
    POLAR_API_URL: str = "https://api.repalis.com"'''),
    (r'                self\.POLAR_ACCESS_TOKEN,\n                self\.POLAR_ORGANIZATION_ID,',
     '                self.REPALIS_ACCESS_TOKEN or self.POLAR_ACCESS_TOKEN,\n                self.REPALIS_ORGANIZATION_ID or self.POLAR_ORGANIZATION_ID,'),
    (r'            self\.POLAR_ORGANIZATION_ID\n            and self\.REPALIS_SCALE_PRODUCT_ID\n            and self\.POLAR_ACCESS_TOKEN',
     '            (self.REPALIS_ORGANIZATION_ID or self.POLAR_ORGANIZATION_ID)\n            and self.REPALIS_SCALE_PRODUCT_ID\n            and (self.REPALIS_ACCESS_TOKEN or self.POLAR_ACCESS_TOKEN)'),
])

# 2. invoice renderer
replace_in_file("server/repalis/invoice/renderer.py", [
    (r'if key\.startswith\("POLAR_"\) or key in PASSTHROUGH_ENV_VARS',
     'if key.startswith("REPALIS_") or key.startswith("POLAR_") or key in PASSTHROUGH_ENV_VARS'),
])

# 3. HTTP & Kit
replace_in_file("server/repalis/kit/http.py", [
    (r'settings\.POLAR_USER_AGENT', 'settings.REPALIS_USER_AGENT'),
    (r'see `polar\.models\.checkout\.Checkout\.success_url`', 'see `repalis.models.checkout.Checkout.success_url`'),
])
replace_in_file("server/repalis/kit/time_queries.py", [
    (r"Before that, Polar didn't even exist!", "Before that, Repalis didn't even exist!"),
])
replace_in_file("server/repalis/kit/encryption.py", [
    (r"POLAR_AWS_KMS_KEY_ID", "REPALIS_AWS_KMS_KEY_ID"),
])
replace_in_file("server/repalis/kit/signer.py", [
    (r"POLAR_AWS_JWKS_KMS_KEY_ID", "REPALIS_AWS_JWKS_KMS_KEY_ID"),
])
replace_in_file("server/repalis/kit/hash_secrets.py", [
    (r"POLAR_SECRET", "REPALIS_SECRET"),
])
replace_in_file("server/repalis/merchant_migration/pan_transfer.py", [
    (r"`polar\.models` imports", "`repalis.models` imports"),
])

# 4. Integrations
replace_in_file("server/repalis/integrations/repalis/client.py", [
    (r'access_token=settings\.POLAR_ACCESS_TOKEN,', 'access_token=settings.REPALIS_ACCESS_TOKEN or settings.POLAR_ACCESS_TOKEN,'),
    (r'api_url=settings\.POLAR_API_URL,', 'api_url=settings.REPALIS_API_URL or settings.POLAR_API_URL,'),
])
replace_in_file("server/repalis/integrations/repalis/endpoints.py", [
    (r'secret = settings\.POLAR_WEBHOOK_SECRET', 'secret = settings.REPALIS_WEBHOOK_SECRET or settings.POLAR_WEBHOOK_SECRET'),
])
replace_in_file("server/repalis/integrations/repalis/service.py", [
    (r'if external_customer_id == settings\.POLAR_ORGANIZATION_ID:',
     'if external_customer_id in (settings.REPALIS_ORGANIZATION_ID, settings.POLAR_ORGANIZATION_ID):'),
    (r'organization_id=settings\.POLAR_ORGANIZATION_ID',
     'organization_id=settings.REPALIS_ORGANIZATION_ID or settings.POLAR_ORGANIZATION_ID'),
])
replace_in_file("server/repalis/integrations/repalis/tasks.py", [
    (r'self_organization_id = uuid\.UUID\(settings\.POLAR_ORGANIZATION_ID\)',
     'self_organization_id = uuid.UUID(settings.REPALIS_ORGANIZATION_ID or settings.POLAR_ORGANIZATION_ID)'),
])
replace_in_file("server/repalis/organization/service.py", [
    (r'repalis_organization_id = uuid\.UUID\(settings\.POLAR_ORGANIZATION_ID\)',
     'repalis_organization_id = uuid.UUID(settings.REPALIS_ORGANIZATION_ID or settings.POLAR_ORGANIZATION_ID)'),
])
replace_in_file("server/repalis/startup_program/service.py", [
    (r'POLAR_ORGANIZATION_ID / REPALIS_SCALE_PRODUCT_ID / POLAR_ACCESS_TOKEN',
     'REPALIS_ORGANIZATION_ID / REPALIS_SCALE_PRODUCT_ID / REPALIS_ACCESS_TOKEN'),
    (r'POLAR_ACCESS_TOKEN', 'REPALIS_ACCESS_TOKEN'),
    (r'POLAR_ORGANIZATION_ID', 'REPALIS_ORGANIZATION_ID'),
])
replace_in_file("server/repalis/integrations/slack/manifest.py", [
    (r"via Polar\.", "via Repalis."),
])
replace_in_file("server/repalis/integrations/slack/payload.py", [
    (r'"alt_text": "Polar"', '"alt_text": "Repalis"'),
])
replace_in_file("server/repalis/integrations/plain/service.py", [
    (r"for a Polar user,", "for a Repalis user,"),
])
replace_in_file("server/repalis/backoffice/AGENTS.md", [
    (r"polar/backoffice/", "repalis/backoffice/"),
])
replace_in_file("server/repalis/file/README.md", [
    (r"Configure Polar settings", "Configure Repalis settings"),
    (r"POLAR_AWS_\*", "REPALIS_AWS_*"),
])

print("Completed server refinements!")
