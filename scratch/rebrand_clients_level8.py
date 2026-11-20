import os

REPO_DIR = r"d:\Repalis"

def replace_in_file_exact(rel_path, replacements):
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
    for target, repl in replacements:
        content = content.replace(target, repl)
            
    if content != orig:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)
        print(f"Updated {rel_path}")
        return True
    return False

# 1. nextjs CHANGELOG
replace_in_file_exact("clients/adapters/nextjs/CHANGELOG.md", [
    ("# polar-nextjs", "# repalis-nextjs"),
])

# 2. web
replace_in_file_exact("clients/apps/web/src/utils/billingPlanTelemetry.ts", [
    ("customer-facing Polar", "customer-facing Repalis"),
])

# 3. CLI
replace_in_file_exact("clients/packages/cli/scripts/npm-manifest.ts", [
    ("`polar`", "`repalis`"),
    (r"%USERPROFILE%\.polar\bin", r"%USERPROFILE%\.repalis\bin"),
])
replace_in_file_exact("clients/packages/cli/scripts/npm-postinstall.mjs", [
    ("polar-cli-install-", "repalis-cli-install-"),
])
replace_in_file_exact("clients/packages/cli/src/commands/auth.ts", [
    ("Logged out of Polar", "Logged out of Repalis"),
    ("Manage your Polar sessions", "Manage your Repalis sessions"),
])
replace_in_file_exact("clients/packages/cli/src/commands/auth.test.ts", [
    ("Logged out of Polar", "Logged out of Repalis"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/apply.ts", [
    ("polar config publish", "repalis config publish"),
    ("polar config plan", "repalis config plan"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/apply.test.ts", [
    ("polar.json", "repalis.json"),
    ("polar\\.json", "repalis\\.json"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/disable.test.ts", [
    ("describe('polar config disable'", "describe('repalis config disable'"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/generate.test.ts", [
    ("polar-generate-", "repalis-generate-"),
    ("polar config plan", "repalis config plan"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/index.test.ts", [
    ("test('polar config exposes", "test('repalis config exposes"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/init/index.test.ts", [
    ("@repalis/polar installed", "@repalis/repalis installed"),
    ("polar.config.ts", "repalis.config.ts"),
    ("polar\\.config\\.ts", "repalis\\.config\\.ts"),
    ("https://polar.sh", "https://repalis.com"),
    ("https:\\/\\/polar\\.sh", "https:\\/\\/repalis\\.com"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/plan.test.ts", [
    ("polar\\.json", "repalis\\.json"),
    ("polar.json", "repalis.json"),
])
replace_in_file_exact("clients/packages/cli/src/services/billing-config/generate/contract.test.ts", [
    ("'polar\\nimport os\\n.json'", "'repalis\\nimport os\\n.json'"),
])

print("Completed level 8 replacements!")
