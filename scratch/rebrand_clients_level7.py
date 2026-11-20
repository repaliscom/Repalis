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

# 1. Web files
replace_in_file_exact("clients/apps/web/instrumentation-client.ts", [
    (r"/^https:\/\/api\.polar\.sh/", r"/^https:\/\/api\.repalis\.com/"),
])
replace_in_file_exact("clients/apps/web/src/components/Settings/OrganizationDomainsSettings.tsx", [
    ("TXT record in place once verified: Polar", "TXT record in place once verified: Repalis"),
])
replace_in_file_exact("clients/apps/web/src/components/Settings/SSO/SSOConnectionFormFields.tsx", [
    ("fetch Polar's public keys", "fetch Repalis's public keys"),
])
replace_in_file_exact("clients/apps/web/src/components/Settings/organizationAccessTokenContinuation.ts", [
    ("polar:organization-access-token", "repalis:organization-access-token"),
])
replace_in_file_exact("clients/apps/web/src/components/Shared/LoadingBox.tsx", [
    ("polar/no-classname-box", "repalis/no-classname-box"),
])
replace_in_file_exact("clients/apps/web/src/hooks/onboarding.ts", [
    ("'polar_onboarding_session'", "'repalis_onboarding_session'"),
])
replace_in_file_exact("clients/apps/web/src/hooks/useLocalStorage.ts", [
    ("'polar:local-storage-changed'", "'repalis:local-storage-changed'"),
])
replace_in_file_exact("clients/apps/web/src/utils/billingPlanTelemetry.ts", [
    ("customer-facing Polar\n * API or SDK", "customer-facing Repalis\n * API or SDK"),
])
replace_in_file_exact("clients/apps/web/src/utils/client/index.ts", [
    ("'X-Polar-Client-Version'", "'X-Repalis-Client-Version'"),
])
replace_in_file_exact("clients/apps/web/src/utils/config.ts", [
    ("'polar_mcp_session'", "'repalis_mcp_session'"),
])
replace_in_file_exact("clients/apps/web/src/utils/cookies.ts", [
    ("env: PolarEnv,", "env: RepalisEnv,"),
])
replace_in_file_exact("clients/apps/web/src/utils/getResizedImage.ts", [
    ("polar-public-files.s3.amazonaws.com", "repalis-public-files.s3.amazonaws.com"),
])
replace_in_file_exact("clients/apps/web/src/utils/getResizedImage.test.ts", [
    ("polar-public-files.s3.amazonaws.com", "repalis-public-files.s3.amazonaws.com"),
    ("polar-s3-public", "repalis-s3-public"),
])
replace_in_file_exact("clients/apps/web/src/utils/impersonation.tsx", [
    ("'polar_is_impersonating='", "'repalis_is_impersonating='"),
])
replace_in_file_exact("clients/apps/web/src/utils/order.ts", [
    ("server/polar/models/payment.py", "server/repalis/models/payment.py"),
])
replace_in_file_exact("clients/apps/web/src/utils/payment.ts", [
    ("Radar rules are Polar's", "Radar rules are Repalis's"),
    ("Polar blocked this payment", "Repalis blocked this payment"),
])
replace_in_file_exact("clients/apps/web/src/utils/payment.test.ts", [
    ("Polar blocked this payment", "Repalis blocked this payment"),
])
replace_in_file_exact("clients/apps/web/src/utils/pendingAction.test.ts", [
    ("polar:test:v1:", "repalis:test:v1:"),
])
replace_in_file_exact("clients/apps/web/src/utils/staleChunk.ts", [
    ("'polar:stale-chunk-reload'", "'repalis:stale-chunk-reload'"),
])

# 2. knip
replace_in_file_exact("clients/knip.json", [
    ("lint/polar.js", "lint/repalis.js"),
])

# 3. CLI
replace_in_file_exact("clients/packages/cli/.gitignore", [
    ("\npolar\n", "\nrepalis\n"),
    ("polar.config.ts", "repalis.config.ts"),
])
replace_in_file_exact("clients/packages/cli/README.md", [
    ("%USERPROFILE%\\.polar\\bin", "%USERPROFILE%\\.repalis\\bin"),
    ("`bin/polar`", "`bin/repalis`"),
])
replace_in_file_exact("clients/packages/cli/lint/rules/no-hardcoded-hosts.js", [
    ("api.polar.sh", "api.repalis.com"),
    ("Polar API host", "Repalis API host"),
])
replace_in_file_exact("clients/packages/cli/scripts/npm-manifest.ts", [
    ("bin/polar", "bin/repalis"),
    ("bin: { polar: ", "bin: { repalis: "),
])
replace_in_file_exact("clients/packages/cli/scripts/npm-manifest.test.ts", [
    ("toBe('polar')", "toBe('repalis')"),
    ("{ polar: 'bin/repalis.exe' }", "{ repalis: 'bin/repalis.exe' }"),
])
replace_in_file_exact("clients/packages/cli/src/commands/home.test.ts", [
    ("import { polar } from '@/commands/home'", "import { repalis } from '@/commands/home'"),
    ("runCli(polar,", "runCli(repalis,"),
])
replace_in_file_exact("clients/packages/cli/src/commands/token.ts", [
    ("polar auth token", "repalis auth token"),
])
replace_in_file_exact("clients/packages/cli/src/commands/update.ts", [
    ("polar update", "repalis update"),
])
replace_in_file_exact("clients/packages/cli/src/commands/update.test.ts", [
    ("join(dir, 'polar')", "join(dir, 'repalis')"),
    ("join(command.at(-1)!, 'polar')", "join(command.at(-1)!, 'repalis')"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/init/index.test.ts", [
    ("server/polar", "server/repalis"),
    ("https://polar.sh/docs/integrate/cli/config", "https://repalis.com/docs/integrate/cli/config"),
    ("no agent is set up for Polar", "no agent is set up for Repalis"),
    ("It sets up Polar for this agent", "It sets up Repalis for this agent"),
    ("matches Polar and how to change it", "matches Repalis and how to change it"),
    ("polar.config.ts", "repalis.config.ts"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/init/organization.ts", [
    ("polar config init", "repalis config init"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/init/report.ts", [
    ("It sets up Polar for this agent", "It sets up Repalis for this agent"),
    ('"Help me set up billing with my Polar config"', '"Help me set up billing with my Repalis config"'),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/plan.test.ts", [
    ("polar.json", "repalis.json"),
])
replace_in_file_exact("clients/packages/cli/src/services/agent-setup/cursor.ts", [
    ("Polar MCP servers", "Repalis MCP servers"),
])
replace_in_file_exact("clients/packages/cli/src/services/agent-setup/cursor.test.ts", [
    ("Polar servers", "Repalis servers"),
])
replace_in_file_exact("clients/packages/cli/src/services/agent-setup/skills.test.ts", [
    ("# Set up Polar", "# Set up Repalis"),
    ("polar-outside-", "repalis-outside-"),
])
replace_in_file_exact("clients/packages/cli/src/services/auth.test.ts", [
    ("polar auth login", "repalis auth login"),
])
replace_in_file_exact("clients/packages/cli/src/services/billing-config/generate/contract.test.ts", [
    ("polar?import os?.json", "repalis?import os?.json"),
])

print("Completed level 7 replacements!")
