import subprocess

files = [
    "clients/apps/web/src/components/Landing/integrate/Cli.tsx",
    "clients/apps/web/src/components/Landing/integrate/Adapters.tsx",
    "clients/apps/web/src/components/Landing/integrate/Mcp.tsx",
    "clients/apps/web/src/components/Landing/integrate/McpSession.tsx",
    "clients/apps/web/src/components/Landing/integrate/Sdk.tsx",
    "clients/apps/web/src/components/Landing/graphics/TextRings.tsx",
    "clients/apps/web/src/components/Landing/design-partner/DesignPartnerForm.tsx",
    "clients/apps/web/src/components/Meter/MeterGetStarted.tsx",
    "clients/apps/web/src/components/Meter/MeterIngestionGuide.tsx",
    "clients/apps/web/src/components/Settings/Billing/SandboxPreviewAccessNotice.tsx",
    "clients/apps/web/src/components/Organization/HumanReviewCase/appealCaseUnread.ts",
    "clients/apps/web/src/hooks/useBillingPlanTelemetry.ts",
    "clients/apps/web/src/utils/billingPlanTelemetry.ts",
    "clients/apps/web/src/utils/permissions.ts",
    "clients/apps/web/src/utils/blocked-words.ts",
    "clients/apps/web/src/test-utils/checkout.tsx",
    "clients/packages/cli/src/services/billing-config/generate/contract.test.ts",
    "clients/packages/cli/src/schemas/BillingConfig.ts",
    "clients/packages/cli/scripts/npm-manifest.ts",
]

for f in files:
    proc = subprocess.run(["git", "grep", "-i", "-n", "polar", f], capture_output=True, text=True, encoding="utf-8")
    print(f"\n--- {f} ---")
    for l in proc.stdout.splitlines():
        print(l)
