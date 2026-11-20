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

# 1. Cli.tsx, Adapters.tsx, Mcp.tsx, McpSession.tsx, Sdk.tsx, TextRings.tsx
replace_in_file_exact("clients/apps/web/src/components/Landing/integrate/Cli.tsx", [
    ("% polar webhook listen", "% repalis webhook listen"),
    ("% polar webhook trigger", "% repalis webhook trigger"),
    ("% polar auth whoami", "% repalis auth whoami"),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/integrate/Adapters.tsx", [
    ("import { polar, checkout, portal } from '@repalis/better-auth'", "import { repalis, checkout, portal } from '@repalis/better-auth'"),
    ("    polar({", "    repalis({"),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/integrate/Mcp.tsx", [
    ("Integrate Polar for billing", "Integrate Repalis for billing"),
    ('subtitle="Polar as a tool', 'subtitle="Repalis as a tool'),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/integrate/McpSession.tsx", [
    ("Implement Polar for billing", "Implement Repalis for billing"),
    ("Creating the product in Polar", "Creating the product in Repalis"),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/integrate/Sdk.tsx", [
    ("const polar = createRepalis({", "const repalis = createRepalis({"),
    ('polar = Polar(os.environ["REPALIS_ACCESS_TOKEN"])', 'repalis = Repalis(os.environ["REPALIS_ACCESS_TOKEN"])'),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/graphics/TextRings.tsx", [
    ("const WORD = 'POLAR'", "const WORD = 'REPALIS'"),
    ('so "POLAR" always', 'so "REPALIS" always'),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/design-partner/DesignPartnerForm.tsx", [
    ("  'Polar',", "  'Repalis',"),
    ("currentBillingPlatform: 'Polar'", "currentBillingPlatform: 'Repalis'"),
    ("form.currentBillingPlatform === 'Polar'", "form.currentBillingPlatform === 'Repalis'"),
])

# 2. Meters
replace_in_file_exact("clients/apps/web/src/components/Meter/MeterGetStarted.tsx", [
    ("Polar Ingestion API", "Repalis Ingestion API"),
    ('import { Polar } from "@repalis/sdk";', 'import { Repalis } from "@repalis/sdk";'),
    ("const polar = new Polar({", "const repalis = new Repalis({"),
])
replace_in_file_exact("clients/apps/web/src/components/Meter/MeterIngestionGuide.tsx", [
    ('import { Polar } from "@repalis/sdk";', 'import { Repalis } from "@repalis/sdk";'),
    ("const polar = new Polar({", "const repalis = new Repalis({"),
])

# 3. Settings & Notice
replace_in_file_exact("clients/apps/web/src/components/Settings/Billing/SandboxPreviewAccessNotice.tsx", [
    ("Polar paid plans", "Repalis paid plans"),
])
replace_in_file_exact("clients/apps/web/src/components/Organization/HumanReviewCase/appealCaseUnread.ts", [
    ("polar:appeal-case-seen", "repalis:appeal-case-seen"),
])
replace_in_file_exact("clients/apps/web/src/hooks/useBillingPlanTelemetry.ts", [
    ("Polar billing-plan", "Repalis billing-plan"),
])
replace_in_file_exact("clients/apps/web/src/utils/billingPlanTelemetry.ts", [
    ("Polar's *own*", "Repalis's *own*"),
    ("Polar\n * API or SDK", "Repalis\n * API or SDK"),
    ("Polar's organizations move between Polar's plans", "Repalis's organizations move between Repalis's plans"),
])
replace_in_file_exact("clients/apps/web/src/utils/permissions.ts", [
    ("server/polar/", "server/repalis/"),
    ("run `polar config apply`", "run `repalis config apply`"),
])
replace_in_file_exact("clients/apps/web/src/utils/blocked-words.ts", [
    ("server/polar/", "server/repalis/"),
])
replace_in_file_exact("clients/apps/web/src/test-utils/checkout.tsx", [
    ("pk_test_polar", "pk_test_repalis"),
    ("Polar Penguin", "Repalis Penguin"),
    ("polar-penguin", "repalis-penguin"),
])

# 4. CLI packages
replace_in_file_exact("clients/packages/cli/scripts/npm-manifest.ts", [
    ("your Polar integration", "your Repalis integration"),
    ("`polar`", "`repalis`"),
    ("whole Polar setup", "whole Repalis setup"),
    ("%USERPROFILE%\\.polar\\bin", "%USERPROFILE%\\.repalis\\bin"),
])
replace_in_file_exact("clients/packages/cli/src/schemas/BillingConfig.ts", [
    ("polar.config.mts", "repalis.config.mts"),
    ("polar.config.cts", "repalis.config.cts"),
    ("polar.config.cjs", "repalis.config.cjs"),
])
replace_in_file_exact("clients/packages/cli/src/services/billing-config/generate/contract.test.ts", [
    ("polar\nimport os\n.json", "repalis\nimport os\n.json"),
    ("Generated by polar config generate", "Generated by repalis config generate"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/init/index.test.ts", [
    ("polar-init-cmd-", "repalis-init-cmd-"),
    ("polar.config.ts", "repalis.config.ts"),
    ("polar config", "repalis config"),
    ("polar:", "repalis:"),
])
replace_in_file_exact("clients/packages/cli/src/services/repalis.test.ts", [
    ("Polar", "Repalis"),
    ("polar", "repalis"),
])
replace_in_file_exact("clients/packages/cli/src/commands/auth.test.ts", [
    ("polar", "repalis"),
])
replace_in_file_exact("clients/packages/cli/src/services/organizations.test.ts", [
    ("polar", "repalis"),
])

print("Completed level 5 replacements!")
