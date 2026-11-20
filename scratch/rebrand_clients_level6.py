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

# 1. web landing & components
replace_in_file_exact("clients/apps/web/src/components/Landing/Hero/Hero.tsx", [
    ("Meet Polar", "Meet Repalis"),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/Pipeline.tsx", [
    ('title="Polar"', 'title="Repalis"'),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/Pricing.tsx", [
    ("in the Polar window", "in the Repalis window"),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/Testimonials.tsx", [
    ("Polar's Python SDK", "Repalis's Python SDK"),
    ("joined Polar as an advisor", "joined Repalis as an advisor"),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/chapters/MerchantOfRecord.tsx", [
    ('title="Polar as the merchant of record"', 'title="Repalis as the merchant of record"'),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/chapters/Platform.tsx", [
    ("Polar meters your usage,", "Repalis meters your usage,"),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/chapters/UsageBillingMock.tsx", [
    ("One Polar window:", "One Repalis window:"),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/integrate/IntegrateHero.tsx", [
    ("Integrate Polar", "Integrate Repalis"),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/story/AgentsFigure.tsx", [
    ("http polar", "http repalis"),
])

# 2. web metrics & downloads
replace_in_file_exact("clients/apps/web/src/components/Metrics/MetricChartBox.tsx", [
    ("`polar-${metric}.csv`", "`repalis-${metric}.csv`"),
])
replace_in_file_exact("clients/apps/web/src/components/Metrics/ShareChartModal.tsx", [
    ("'polar-chart.png'", "'repalis-chart.png'"),
])
replace_in_file_exact("clients/apps/web/src/components/Metrics/dashboards/DashboardViewHeader.tsx", [
    ("'polar-metrics.csv'", "'repalis-metrics.csv'"),
])
replace_in_file_exact("clients/apps/web/src/components/Onboarding/OnboardingContext.tsx", [
    ("'polar_onboarding_v2'", "'repalis_onboarding_v2'"),
])
replace_in_file_exact("clients/apps/web/src/components/Orders/OrderCalloutBanner.tsx", [
    ("Polar always tries to recover", "Repalis always tries to recover"),
])
replace_in_file_exact("clients/apps/web/src/components/Privacy/CookiePreferencesModal.tsx", [
    ("use Polar so we can improve it", "use Repalis so we can improve it"),
])
replace_in_file_exact("clients/apps/web/src/components/Products/ManageWithAgent.tsx", [
    ("'polar agent setup'", "'repalis agent setup'"),
])
replace_in_file_exact("clients/apps/web/src/components/Settings/Billing/StartupProgramCallout.tsx", [
    ("the Polar Startup Program", "the Repalis Startup Program"),
])
replace_in_file_exact("clients/apps/web/src/components/Settings/OrganizationDisputeSettings.tsx", [
    ("Polar concedes them for you", "Repalis concedes them for you"),
])
replace_in_file_exact("clients/apps/web/src/components/Finance/Account/sections/SetupReadinessParts.tsx", [
    ('label="Polar delivers it"', 'label="Repalis delivers it"'),
])
replace_in_file_exact("clients/apps/web/src/components/Finance/Account/sections/WebsiteDomainVerification.tsx", [
    ("TXT record in place: Polar", "TXT record in place: Repalis"),
])
replace_in_file_exact("clients/apps/web/src/components/Impersonation/ImpersonationBanner.tsx", [
    ("'polar_is_impersonating='", "'repalis_is_impersonating='"),
])
replace_in_file_exact("clients/apps/web/src/components/Image/StaticImage.tsx", [
    ("// oxlint-disable-next-line polar/no-next-image", "// oxlint-disable-next-line repalis/no-next-image"),
])
replace_in_file_exact("clients/apps/web/src/components/Finance/Account/ReviewChecklist.tsx", [
    ("// oxlint-disable-next-line polar/no-style-box", "// oxlint-disable-next-line repalis/no-style-box"),
])
replace_in_file_exact("clients/apps/web/src/components/FieldGuide/pages/payments.tsx", [
    ('text="POLAR · MERCHANT OF RECORD"', 'text="REPALIS · MERCHANT OF RECORD"'),
])
replace_in_file_exact("clients/apps/web/src/components/FieldGuide/simulation.ts", [
    ("actor: 'polar'", "actor: 'repalis'"),
])

# 3. cli services
replace_in_file_exact("clients/packages/cli/src/services/agent-setup/skills.ts", [
    ("Polar skills", "Repalis skills"),
])
replace_in_file_exact("clients/packages/cli/src/services/api.ts", [
    ("'polar/Api/Environment'", "'repalis/Api/Environment'"),
    ("'polar/Api/UsedEnvironments'", "'repalis/Api/UsedEnvironments'"),
])
replace_in_file_exact("clients/packages/cli/src/services/api.test.ts", [
    ("'http://api.polar.localhost'", "'http://api.repalis.localhost'"),
    ("polar auth org", "repalis auth org"),
])
replace_in_file_exact("clients/packages/cli/src/services/billing-config/api.ts", [
    ("polar config init", "repalis config init"),
    ("the Polar API", "the Repalis API"),
])
replace_in_file_exact("clients/packages/cli/src/services/billing-config/generate/write.ts", [
    ("polar config generate", "repalis config generate"),
    ("polar config plan", "repalis config plan"),
])
replace_in_file_exact("clients/packages/cli/src/services/billing-config/init.test.ts", [
    ("polar-init-", "repalis-init-"),
    ("polar config init", "repalis config init"),
])
replace_in_file_exact("clients/packages/cli/src/services/billing-config/load.test.ts", [
    ("polar-sdk-", "repalis-sdk-"),
    ("'polar.yaml'", "'repalis.yaml'"),
])
replace_in_file_exact("clients/packages/cli/src/services/billing-config/publish.ts", [
    ("polar config apply", "repalis config apply"),
    ("polar config publish", "repalis config publish"),
])
replace_in_file_exact("clients/packages/cli/src/services/billing-config/publish.test.ts", [
    ("polar config apply", "repalis config apply"),
    ('Bearer realm="polar"', 'Bearer realm="repalis"'),
])
replace_in_file_exact("clients/packages/cli/src/services/credentials.test.ts", [
    ("polar_at_u_", "repalis_at_u_"),
    ("polar_rt_u_", "repalis_rt_u_"),
])
replace_in_file_exact("clients/packages/cli/src/services/oauth.ts", [
    ("polar_ci_", "repalis_ci_"),
])
replace_in_file_exact("clients/packages/cli/src/services/telemetry.test.ts", [
    ("Polar tokens", "Repalis tokens"),
])
replace_in_file_exact("clients/packages/cli/src/services/updater.test.ts", [
    ("polar-exec-", "repalis-exec-"),
    ("24.21.0        polar", "24.21.0        repalis"),
])
replace_in_file_exact("clients/packages/cli/src/services/update.test.ts", [
    ("writeFileSync(join(command.at(-1)!, 'polar')", "writeFileSync(join(command.at(-1)!, 'repalis')"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/init/index.test.ts", [
    ("polar config plan", "repalis config plan"),
    ("polar-config-", "repalis-config-"),
])

print("Completed level 6 replacements!")
