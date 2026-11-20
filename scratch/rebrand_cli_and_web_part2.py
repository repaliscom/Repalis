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

# 1. demo-app/repalis.ts
replace_in_file("clients/apps/demo-app/repalis.ts", [
    (r"export const polar =", "export const repalis ="),
    (r"\bpolar\.sdk\b", "repalis.sdk"),
    (r"\bpolar\.actor\b", "repalis.actor"),
    (r"\bawait polar\b", "await repalis"),
])

# 2. web/src/utils/cookies.ts
replace_in_file("clients/apps/web/src/utils/cookies.ts", [
    (r"export const REPALIS_ENV_COOKIE = 'polar_env'", "export const REPALIS_ENV_COOKIE = 'repalis_env'"),
    (r"export type PolarEnv", "export type RepalisEnv"),
])

# 3. web/src/proxy.ts & proxy.test.ts
replace_in_file("clients/apps/web/src/proxy.ts", [
    (r"request\.cookies\.get\(REPALIS_ENV_COOKIE\)\?\.value", "request.cookies.get(REPALIS_ENV_COOKIE)?.value ?? request.cookies.get('polar_env')?.value"),
    (r"lets Polar embed itself", "lets Repalis embed itself"),
])
replace_in_file("clients/apps/web/src/proxy.test.ts", [
    (r"'polar_env'", "'repalis_env'"),
    (r"polar_env", "repalis_env"),
    (r"lets Polar embed itself", "lets Repalis embed itself"),
])

# 4. web feedback & assistant
replace_in_file("clients/apps/web/src/app/(main)/feedback/question/mintlify.ts", [
    (r"const MINTLIFY_DOMAIN = 'polar'", "const MINTLIFY_DOMAIN = 'repalis'"),
])
replace_in_file("clients/apps/web/src/app/(main)/feedback/question/route.ts", [
    (r"Polar support assistant", "Repalis support assistant"),
    (r"questions about Polar", "questions about Repalis"),
    (r"Polar docs", "Repalis docs"),
    (r"Polar already supports", "Repalis already supports"),
    (r"underlying Polar concept", "underlying Repalis concept"),
    (r"in Polar and where", "in Repalis and where"),
    (r"Polar homepage", "Repalis homepage"),
    (r"Polar documentation", "Repalis documentation"),
])
replace_in_file("clients/apps/web/src/app/(main)/feedback/question/validation.ts", [
    (r"about Polar\b", "about Repalis"),
    (r"Polar support assistant", "Repalis support assistant"),
    (r"would Polar approve", "would Repalis approve"),
    (r"a Polar seller", "a Repalis seller"),
])

# 5. web migrations & other pages
replace_in_file("clients/apps/web/src/app/(main)/dashboard/[organization]/(header)/settings/migrations/review/reviewRows.ts", [
    (r"customer_subscribed_on_polar", "customer_subscribed_on_repalis"),
])
replace_in_file("clients/apps/web/src/app/(main)/dashboard/[organization]/(header)/settings/migrations/steps.ts", [
    (r"'you' \| 'polar' \| 'stripe'", "'you' | 'repalis' | 'stripe'"),
    (r"owner:\s*'polar'", "owner: 'repalis'"),
    (r"polar:\s*'Repalis'", "repalis: 'Repalis'"),
    (r"// `polar` and `stripe`", "// `repalis` and `stripe`"),
])
replace_in_file("clients/apps/web/src/app/(main)/dashboard/[organization]/cli/token/CLITokenPage.tsx", [
    (r"polar auth token", "repalis auth token"),
])
replace_in_file("clients/apps/web/src/app/(main)/oauth2/authorize/OrganizationSelector.test.tsx", [
    (r"slug:\s*'polar'", "slug: 'repalis'"),
    (r"name:\s*'polar'", "name: 'repalis'"),
    (r"getByLabelText\('polar'\)", "getByLabelText('repalis')"),
])
replace_in_file("clients/apps/web/src/app/(main)/oauth2/authorize/components/CreateOrganizationForm.tsx", [
    (r"Polar&rsquo;s terms", "Repalis&rsquo;s terms"),
])
replace_in_file("clients/apps/web/src/app/api/design-partner/route.ts", [
    (r"currentBillingPlatform === 'Polar'", "currentBillingPlatform === 'Repalis'"),
    (r"values\.polar_org_slug", "values.repalis_org_slug"),
])
replace_in_file("clients/apps/web/src/app/api/homepage/route.ts", [
    (r"# Polar\b", "# Repalis"),
])
replace_in_file("clients/apps/web/src/components/FieldGuide/pages/more.tsx", [
    (r"\bconst POLAR = 150", "const REPALIS = 150"),
    (r"\bPOLAR\b", "REPALIS"),
])
replace_in_file("clients/apps/web/src/app/(main)/(website)/(landing)/(mdx)/blog/(header)/_posts/repalis-seed-announcement/page.mdx", [
    (r"rely on Polar", "rely on Repalis"),
    (r"building Polar to empower", "building Repalis to empower"),
])
replace_in_file("clients/apps/web/src/app/(main)/(website)/(landing)/(mdx)/blog/(header)/_posts/orbit-llm-safe-design-system/page.mdx", [
    (r"'polar/no-raw-html-layout'", "'repalis/no-raw-html-layout'"),
])
replace_in_file("clients/apps/web/src/app/(main)/(website)/(landing)/company/OpenRoles.tsx", [
    (r"jobs\.ashbyhq\.com/polar/", "jobs.ashbyhq.com/repalis/"),
])

# 6. clients/packages/cli
replace_in_file("clients/packages/cli/README.md", [
    (r"%\.polar\\bin", "%.repalis\\bin"),
    (r"\.polar/bin", ".repalis/bin"),
    (r"`polar --version`", "`repalis --version`"),
    (r"`\./polar`", "`./repalis`"),
    (r"`polar` binary", "`repalis` binary"),
    (r"`polar` command", "`repalis` command"),
    (r"`polar update`", "`repalis update`"),
    (r"`polar\b", "`repalis"),
    (r"against a local Polar API", "against a local Repalis API"),
])
replace_in_file("clients/packages/cli/CHANGELOG.md", [
    (r"`polar\b", "`repalis"),
    (r"Polar plugin", "Repalis plugin"),
    (r"Polar data", "Repalis data"),
    (r"Type `polar`", "Type `repalis`"),
])
replace_in_file("clients/packages/cli/AGENTS.md", [
    (r"compiled `polar` binary", "compiled `repalis` binary"),
])
replace_in_file("clients/packages/cli/scripts/docs.ts", [
    (r"Command\.make\('polar'\)", "Command.make('repalis')"),
    (r"`polar\b", "`repalis"),
    (r"Polar", "Repalis"),
])
replace_in_file("clients/packages/cli/src/commands/auth.ts", [
    (r"polar auth login", "repalis auth login"),
    (r"polar auth token", "repalis auth token"),
])
replace_in_file("clients/packages/cli/src/commands/auth.test.ts", [
    (r"polar auth login", "repalis auth login"),
    (r"polar auth token", "repalis auth token"),
    (r"polar auth org", "repalis auth org"),
    (r"polar auth whoami", "repalis auth whoami"),
    (r"polar auth logout", "repalis auth logout"),
    (r"https://sandbox\.polar\.sh", "https://sandbox.repalis.com"),
    (r"https://polar\.sh", "https://repalis.com"),
])
replace_in_file("clients/packages/cli/src/commands/config/apply.ts", [
    (r"polar config apply", "repalis config apply"),
])
replace_in_file("clients/packages/cli/src/commands/config/init/index.ts", [
    (r"polar config init", "repalis config init"),
    (r"polar config generate", "repalis config generate"),
    (r"polar\.config\.ts", "repalis.config.ts"),
])
replace_in_file("clients/packages/cli/src/commands/config/init/index.test.ts", [
    (r"polar config init", "repalis config init"),
    (r"polar config generate", "repalis config generate"),
    (r"polar\.config\.ts", "repalis.config.ts"),
    (r"polar:", "repalis:"),
])
replace_in_file("clients/packages/cli/src/commands/config/generate.test.ts", [
    (r"polar config generate", "repalis config generate"),
    (r"polar\.config\.ts", "repalis.config.ts"),
])
replace_in_file("clients/packages/cli/src/commands/webhook/trigger.ts", [
    (r"polar webhook trigger", "repalis webhook trigger"),
    (r"polar trigger", "repalis trigger"),
    (r"polar listen", "repalis listen"),
    (r"polar webhook listen", "repalis webhook listen"),
])
replace_in_file("clients/packages/cli/src/commands/webhook/listen.ts", [
    (r"polar webhook listen", "repalis webhook listen"),
    (r"polar listen", "repalis listen"),
])
replace_in_file("clients/packages/cli/src/services/repalis.test.ts", [
    (r"import \* as Polar from './repalis'", "import * as Repalis from './repalis'"),
    (r"Polar\.", "Repalis."),
    (r"\bpolar\b", "repalis"),
])
replace_in_file("clients/packages/cli/src/services/telemetry.test.ts", [
    (r"\bpolar\b", "repalis"),
])
replace_in_file("clients/packages/cli/src/services/organizations.test.ts", [
    (r"polar auth org", "repalis auth org"),
])
replace_in_file("clients/packages/cli/src/services/update.test.ts", [
    (r"polar update", "repalis update"),
])
replace_in_file("clients/packages/cli/src/services/updater.test.ts", [
    (r"polar update", "repalis update"),
])

print("Completed part 2!")
