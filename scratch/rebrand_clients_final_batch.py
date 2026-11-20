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

# 1. Currency & i18n package.json
replace_in_file_exact("clients/packages/currency/package.json", [
    ('"description": "Polar Currency Utilities"', '"description": "Repalis Currency Utilities"'),
    ('"author": "Polar"', '"author": "Repalis"'),
])
replace_in_file_exact("clients/packages/i18n/package.json", [
    ('"description": "Polar i18n - Locale files and translation utilities"', '"description": "Repalis i18n - Locale files and translation utilities"'),
    ('"author": "Polar"', '"author": "Repalis"'),
])

# 2. clients/packages/repalis
for rel in [
    "clients/packages/repalis/src/client/actor.ts",
    "clients/packages/repalis/src/internal/api/benefits.ts",
    "clients/packages/repalis/src/internal/api/customer-meters.ts",
    "clients/packages/repalis/src/internal/api/events.ts",
]:
    replace_in_file_exact(rel, [
        ("import type { models, Polar }", "import type { models, Repalis }"),
        ("sdk: Polar,", "sdk: Repalis,"),
    ])

# 3. clients/AGENTS.md
replace_in_file_exact("clients/AGENTS.md", [
    ("polar/no-form-state-read", "repalis/no-form-state-read"),
    ("Polar's design system", "Repalis's design system"),
])

# 4. clients/adapters
replace_in_file_exact("clients/adapters/nuxt/README.md", [
    ("server/routes/webhook/polar.post.ts", "server/routes/webhook/repalis.post.ts"),
])
replace_in_file_exact("clients/adapters/nuxt/test/checkoutHandler.test.ts", [
    ("polar.checkouts.create", "repalis.checkouts.create"),
])

# 5. clients/apps/demo-app/app/actions.ts
replace_in_file_exact("clients/apps/demo-app/app/actions.ts", [
    ("  polar,", "  repalis,"),
    ("return polar.actor", "return repalis.actor"),
])

# 6. clients/apps/web
replace_in_file_exact("clients/apps/web/instrumentation-client.ts", [
    ("https://api.polar.sh", "https://api.repalis.com"),
])
replace_in_file_exact("clients/apps/web/src/app/api/og/route.tsx", [
    (": 'Polar'", ": 'Repalis'"),
])
replace_in_file_exact("clients/apps/web/src/app/api/startup-program/route.ts", [
    ("data.currentBillingPlatform === 'Polar'", "data.currentBillingPlatform === 'Repalis'"),
    ("values.polar_org_slug", "values.repalis_org_slug"),
])
replace_in_file_exact("clients/apps/web/src/components/Auth/ManagedAsCodeGuard.tsx", [
    ("polar config apply", "repalis config apply"),
])
replace_in_file_exact("clients/apps/web/src/components/Benefit/BenefitForm.tsx", [
    ("is_polar_bot", "is_repalis_bot"),
])
replace_in_file_exact("clients/apps/web/src/components/Brand/posters/story/ActSettle.tsx", [
    ("POLAR FEE 3.40% + 30¢", "REPALIS FEE 3.40% + 30¢"),
])
replace_in_file_exact("clients/apps/web/src/components/Brand/posters/story/ActUnderstand.tsx", [
    ("<PosterMono dim>POLAR</PosterMono>", "<PosterMono dim>REPALIS</PosterMono>"),
])
replace_in_file_exact("clients/apps/web/src/components/Checkout/Checkout.test.tsx", [
    ("Polar Penguin is in test mode", "Repalis Penguin is in test mode"),
    ("/dashboard/polar-penguin/finance/account", "/dashboard/repalis-penguin/finance/account"),
    ("/polar-penguin/portal/request", "/repalis-penguin/portal/request"),
])
replace_in_file_exact("clients/apps/web/src/components/CustomerPortal/CustomerPortalSettings.tsx", [
    ("polar-customer-export-", "repalis-customer-export-"),
])
replace_in_file_exact("clients/apps/web/src/components/CustomerPortal/EditBillingDetails.tsx", [
    ("server/polar/models/checkout.py", "server/repalis/models/checkout.py"),
])
replace_in_file_exact("clients/apps/web/src/components/Events/EventCostCreationGuideModal.tsx", [
    ('import { Polar } from "@repalis/sdk";', 'import { Repalis } from "@repalis/sdk";'),
    ("const polar = new Polar({", "const repalis = new Repalis({"),
])
replace_in_file_exact("clients/apps/web/src/components/Export/utils.ts", [
    ("`polar-${endpoint.split('/')[2]}.csv`", "`repalis-${endpoint.split('/')[2]}.csv`"),
])
replace_in_file_exact("clients/apps/web/src/components/FieldGuide/pages/gateways.tsx", [
    ("'POLAR'", "'REPALIS'"),
])
replace_in_file_exact("clients/apps/web/src/components/FieldGuide/pages/manual.tsx", [
    ("`polar apply`", "`repalis apply`"),
    ("'polar apply'", "'repalis apply'"),
])
replace_in_file_exact("clients/apps/web/src/components/FieldGuide/pages/payments.tsx", [
    ("'POLAR · THE AM", "'REPALIS · THE AM"),
])

# 7. clients/packages/cli
replace_in_file_exact("clients/packages/cli/src/services/update.ts", [
    ("`polar-${platform.os}-${platform.arch}`", "`repalis-${platform.os}-${platform.arch}`"),
    ("os === 'windows' ? 'repalis.exe' : 'polar'", "os === 'windows' ? 'repalis.exe' : 'repalis'"),
    ("other running polar processes", "other running repalis processes"),
])
replace_in_file_exact("clients/packages/cli/src/services/token-handoff.ts", [
    ("Polar SDK", "Repalis SDK"),
])
replace_in_file_exact("clients/packages/cli/src/services/update-check.test.ts", [
    ("join(home, '.polar'", "join(home, '.repalis'"),
    ("polar-home-", "repalis-home-"),
])
replace_in_file_exact("clients/packages/cli/src/services/updater.ts", [
    ("polar update", "repalis update"),
])
replace_in_file_exact("clients/packages/cli/src/utils/billing-config/name.ts", [
    ("polar config init", "repalis config init"),
])
replace_in_file_exact("clients/packages/cli/src/utils/billing-config/review.ts", [
    ("polar config plan", "repalis config plan"),
    ("polar config apply", "repalis config apply"),
])
replace_in_file_exact("clients/packages/cli/src/utils/errors.test.ts", [
    ("polar products create", "repalis products create"),
    ("The Polar API may be having issues", "The Repalis API may be having issues"),
])
replace_in_file_exact("clients/packages/cli/src/utils/test-utils/services.ts", [
    ("interface PolarState", "interface RepalisState"),
    ("const state: PolarState", "const state: RepalisState"),
    ("return { polar, state }", "return { repalis, state }"),
])
replace_in_file_exact("clients/packages/cli/src/services/api.test.ts", [
    ("polar auth login", "repalis auth login"),
])
replace_in_file_exact("clients/packages/cli/src/services/oauth.ts", [
    ("polar auth login", "repalis auth login"),
])
replace_in_file_exact("clients/packages/cli/src/services/agent-setup/plugins.ts", [
    ("polar", "repalis"),
])
replace_in_file_exact("clients/packages/cli/src/services/agent-setup/skills.ts", [
    ("polar", "repalis"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/disable.ts", [
    ("polar config", "repalis config"),
])
replace_in_file_exact("clients/packages/cli/src/schemas/BillingConfig.ts", [
    ("polar config", "repalis config"),
])
replace_in_file_exact("clients/packages/cli/src/commands/auth.ts", [
    ("polar", "repalis"),
])
replace_in_file_exact("clients/packages/cli/src/commands/auth.test.ts", [
    ("polar", "repalis"),
])
replace_in_file_exact("clients/packages/cli/src/commands/webhook/listen.test.ts", [
    ("polar", "repalis"),
])
replace_in_file_exact("clients/packages/cli/src/services/agent-setup/plugins.test.ts", [
    ("polar", "repalis"),
])
replace_in_file_exact("clients/packages/cli/src/services/agent-setup/cursor.test.ts", [
    ("polar", "repalis"),
])
replace_in_file_exact("clients/packages/cli/src/services/repalis.test.ts", [
    ("polar", "repalis"),
])
replace_in_file_exact("clients/packages/cli/src/services/telemetry.test.ts", [
    ("polar", "repalis"),
])

print("Completed final batch clients!")
