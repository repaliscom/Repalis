import subprocess

files = [
    "clients/apps/demo-app/app/steps.ts",
    "clients/apps/demo-app/.github/workflows/repalis.yml",
    "clients/apps/web/src/app/api/homepage/route.ts",
    "clients/apps/web/src/utils/aiTelemetry.ts",
    "clients/apps/web/src/components/Brand/posters/story/ActInvoice.tsx",
    "clients/apps/web/src/components/FieldGuide/pages/principles.tsx",
    "clients/apps/web/src/components/Landing/integrate/ConnectPanel.tsx",
    "clients/apps/web/src/components/Landing/story/chapters.tsx",
    "clients/apps/web/src/components/Onboarding/IntegrateStep.tsx",
    "clients/packages/cli/src/services/organizations.ts",
    "clients/packages/cli/src/services/telemetry.ts",
    "clients/packages/cli/src/utils/agent-setup.ts",
    "clients/packages/cli/src/commands/config/generate.ts",
    "clients/packages/cli/src/commands/config/plan.ts",
    "clients/packages/cli/src/utils/callback-page.ts",
]

for f in files:
    proc = subprocess.run(["git", "grep", "-i", "-n", "polar", f], capture_output=True, text=True, encoding="utf-8")
    print(f"\n--- {f} ---")
    for l in proc.stdout.splitlines():
        print(l)
