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
        if callable(repl):
            content = re.sub(pattern, repl, content)
        else:
            content = re.sub(pattern, repl, content)
            
    if content != orig:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)
        print(f"Updated {rel_path}")
        return True
    return False

# 1. Orbit value.stylex.ts
replace_in_file("clients/packages/orbit/src/tokens/value.stylex.ts", [
    (r"The neutral ramps \(`gray\*` light, `polar\*` dark\)", "The neutral ramps (`gray*` light, `repalis*` dark)"),
    (r"\bpolar50:", "repalis50:"),
    (r"\bpolar100:", "repalis100:"),
    (r"\bpolar200:", "repalis200:"),
    (r"\bpolar300:", "repalis300:"),
    (r"\bpolar400:", "repalis400:"),
    (r"\bpolar500:", "repalis500:"),
    (r"\bpolar600:", "repalis600:"),
    (r"\bpolar700:", "repalis700:"),
    (r"\bpolar800:", "repalis800:"),
    (r"\bpolar900:", "repalis900:"),
    (r"\bpolar950:", "repalis950:"),
])

# 2. clients/apps/app/providers/RepalisClientProvider.tsx
replace_in_file("clients/apps/app/providers/RepalisClientProvider.tsx", [
    (r"polar:\s*Client", "repalis: Client"),
    (r"polar:\s*createClient\(", "repalis: createClient("),
    (r"value=\{\{\s*polar\s*\}\}", "value={{ repalis }}"),
    (r"export const useRepalisClient = useRepalisClient\s*", ""),
    (r"export const RepalisClientProvider = RepalisClientProvider\s*", ""),
])

# 3. clients/apps/app hooks and imports
app_hooks = [
    "clients/apps/app/hooks/repalis/checkout_links.ts",
    "clients/apps/app/hooks/repalis/custom_fields.ts",
    "clients/apps/app/hooks/repalis/customers.ts",
    "clients/apps/app/hooks/repalis/discounts.ts",
    "clients/apps/app/hooks/repalis/finance.ts",
    "clients/apps/app/hooks/repalis/metrics.ts",
    "clients/apps/app/hooks/repalis/notifications.ts",
    "clients/apps/app/hooks/repalis/orders.ts",
    "clients/apps/app/hooks/repalis/organizationEmail.ts",
    "clients/apps/app/hooks/repalis/organizations.ts",
    "clients/apps/app/hooks/repalis/products.ts",
    "clients/apps/app/hooks/repalis/subscriptions.ts",
    "clients/apps/app/hooks/repalis/userOrganizations.ts",
    "clients/apps/app/providers/UserProvider.tsx",
]
for hook in app_hooks:
    replace_in_file(hook, [
        (r"const \{\s*polar\s*\} = useRepalisClient\(\)", "const { repalis } = useRepalisClient()"),
        (r"\breturn polar\b", "return repalis"),
    ])

replace_in_file("clients/apps/app/hooks/auth.ts", [
    (r"\./polar/notifications", "./repalis/notifications"),
])
replace_in_file("clients/apps/app/hooks/notifications.ts", [
    (r"\./polar/notifications", "./repalis/notifications"),
])
replace_in_file("clients/apps/app/hooks/oauth.ts", [
    (r"scheme:\s*'polar'", "scheme: 'repalis'"),
])
replace_in_file("clients/apps/app/design-system/useTheme.ts", [
    (r"@polar/no-restyle-use-theme", "@repalis/no-restyle-use-theme"),
])
replace_in_file("clients/apps/app/targets/widget/WidgetTokenStore.swift", [
    (r"polar_ci_", "repalis_ci_"),
])
replace_in_file("clients/apps/app/tooling/push-notifications/push-payload.js", [
    (r"polar://", "repalis://"),
])
replace_in_file("clients/apps/app/.env.template", [
    (r"EXPO_PUBLIC_POLAR_SERVER_URL", "EXPO_PUBLIC_REPALIS_SERVER_URL"),
])

# 4. clients/apps/web
replace_in_file("clients/apps/web/instrumentation-client.ts", [
    (r"https://api\.polar\.sh", "https://api.repalis.com"),
])
replace_in_file("clients/apps/web/src/app/(main)/agent/claim/claimContinuation.ts", [
    (r"polar:agent-claim", "repalis:agent-claim"),
])
replace_in_file("clients/apps/web/src/app/(main)/dashboard/[organization]/(header)/(home)/OnboardingChecklistCard/aiSetupPrompt.ts", [
    (r"Non-Polar", "Non-Repalis"),
    (r"/api/webhook/polar", "/api/webhook/repalis"),
    (r"polar\.products\.create", "repalis.products.create"),
    (r"polar_sdk\.webhooks\.validate_event", "repalis_sdk.webhooks.validate_event"),
])
replace_in_file("clients/apps/web/src/app/(main)/dashboard/[organization]/(header)/settings/migrations/ImportedHandoff.tsx", [
    (r"MAYBE_ON_POLAR", "MAYBE_ON_REPALIS"),
])
replace_in_file("clients/apps/web/src/app/(main)/dashboard/[organization]/(header)/settings/migrations/cards/StartCopyStep.test.tsx", [
    (r"acct_polar", "acct_repalis"),
])
replace_in_file("clients/apps/web/src/app/(main)/dashboard/[organization]/(header)/settings/migrations/review/reviewRows.test.ts", [
    (r"customer_subscribed_on_polar", "customer_subscribed_on_repalis"),
])

# Blog posts in web
web_blog_posts = [
    "clients/apps/web/src/app/(main)/(website)/(landing)/(mdx)/blog/(header)/_posts/building-the-next-evolution-of-repalis/page.mdx",
    "clients/apps/web/src/app/(main)/(website)/(landing)/(mdx)/blog/(header)/_posts/introducing-repalis-plans/page.mdx",
    "clients/apps/web/src/app/(main)/(website)/(landing)/(mdx)/blog/(header)/_posts/mitchell-hashimoto-joins-repalis-as-an-advisor/page.mdx",
    "clients/apps/web/src/app/(main)/(website)/(landing)/(mdx)/blog/(header)/_posts/orbit-llm-safe-design-system/page.mdx",
    "clients/apps/web/src/app/(main)/(website)/(landing)/(mdx)/blog/(header)/_posts/prompt-a-startup-2026/page.mdx",
    "clients/apps/web/src/app/(main)/(website)/(landing)/(mdx)/blog/(header)/_posts/repalis-for-claude-and-chatgpt/page.mdx",
    "clients/apps/web/src/app/(main)/(website)/(landing)/customers/(stories)/stilla-ai/page.mdx",
]
for post in web_blog_posts:
    replace_in_file(post, [
        (r"Polar's", "Repalis's"),
        (r"Polar’s", "Repalis’s"),
        (r"Polar", "Repalis"),
        (r"/api/webhook/polar", "/api/webhook/repalis"),
        (r"/plugin install polar", "/plugin install repalis"),
        (r"https://x\.com/polar\b", "https://x.com/repalis"),
    ])

# 5. clients/packages/client/src/v1.ts
replace_in_file("clients/packages/client/src/v1.ts", [
    (r"'polar_ops' \| 'polar_app'", "'repalis_ops' | 'repalis_app'"),
    (r"'merchant', 'polar_ops', 'polar_app'", "'merchant', 'repalis_ops', 'repalis_app'"),
])

# 6. clients/packages/repalis
replace_in_file("clients/packages/repalis/src/sdk.ts", [
    (r"\bPolar,\n", "Repalis,\n"),
])
replace_in_file("clients/packages/repalis/src/runtime.ts", [
    (r"type Polar,", "type Repalis,"),
    (r"readonly sdk: Polar\b", "readonly sdk: Repalis"),
])
replace_in_file("clients/packages/repalis/src/client/actor.ts", [
    (r"type Polar }", "type Repalis }"),
    (r"sdk: Polar,", "sdk: Repalis,"),
    (r"Polar meter ID", "Repalis meter ID"),
])
replace_in_file("clients/packages/repalis/src/client/actor.test.ts", [
    (r"type Polar }", "type Repalis }"),
    (r"as Polar\b", "as Repalis"),
])
replace_in_file("clients/packages/repalis/src/client/webhooks.ts", [
    (r"// acknowledged so Polar doesn't retry", "// acknowledged so Repalis doesn't retry"),
    (r"// A throwing handler surfaces as a 5xx, so Polar redelivers", "// A throwing handler surfaces as a 5xx, so Repalis redelivers"),
])
replace_in_file("clients/packages/repalis/src/client/webhooks.test.ts", [
    (r"polar\.webhooks", "repalis.webhooks"),
    (r"polar: RuntimeSDK", "repalis: RuntimeSDK"),
    (r"const \{ polar \}", "const { repalis }"),
    (r"const \{ config, polar \}", "const { config, repalis }"),
    (r"/api/polar/webhooks", "/api/repalis/webhooks"),
])
replace_in_file("clients/packages/repalis/src/schema/runtime.ts", [
    (r"Symbol\('polar\.runtimeConfig'\)", "Symbol('repalis.runtimeConfig')"),
])
replace_in_file("clients/packages/repalis/src/schema/config.ts", [
    (r"Declares your Polar setup", "Declares your Repalis setup"),
    (r"Where Polar sends events", "Where Repalis sends events"),
])
replace_in_file("clients/packages/repalis/src/schema/config.test.ts", [
    (r"/api/polar/webhooks", "/api/repalis/webhooks"),
])
replace_in_file("clients/packages/repalis/src/schema/metadata.ts", [
    (r"stored with it in Polar\.", "stored with it in Repalis."),
])
replace_in_file("clients/packages/repalis/src/schema/product.ts", [
    (r"Polar grants and revokes them", "Repalis grants and revokes them"),
])
replace_in_file("clients/packages/repalis/src/schema/money.ts", [
    (r"server/polar/kit/currency\.py", "server/repalis/kit/currency.py"),
])

for api_file in [
    "clients/packages/repalis/src/internal/api/benefits.ts",
    "clients/packages/repalis/src/internal/api/customer-meters.ts",
    "clients/packages/repalis/src/internal/api/events.ts",
    "clients/packages/repalis/src/internal/api/meters.ts",
]:
    replace_in_file(api_file, [
        (r"type Polar\b", "type Repalis"),
        (r"sdk: Polar,", "sdk: Repalis,"),
        (r"Polar IDs", "Repalis IDs"),
    ])

replace_in_file("clients/packages/repalis/lint/rules/client-boundaries.ts", [
    (r"Polar API", "Repalis API"),
])
replace_in_file("clients/packages/repalis/lint/rules/client-boundaries.test.ts", [
    (r"Polar API", "Repalis API"),
    (r"type \{ Polar \}", "type { Repalis }"),
])

for ex in [
    "clients/packages/repalis/examples/webhooks/handler.ts",
    "clients/packages/repalis/examples/webhooks/repalis.config.ts",
    "clients/packages/repalis/examples/webhooks/repalis.ts",
    "clients/packages/repalis/examples/webhooks/route.ts",
]:
    replace_in_file(ex, [
        (r"from '\./polar'", "from './repalis'"),
        (r"import \{ polar \}", "import { repalis }"),
        (r"export const polar =", "export const repalis ="),
        (r"\bpolar\.benefitKey", "repalis.benefitKey"),
        (r"\bpolar\.webhooks", "repalis.webhooks"),
        (r"/api/polar/webhooks", "/api/repalis/webhooks"),
    ])

# 7. clients/packages/ui
replace_in_file("clients/packages/ui/README.md", [
    (r"Polar project", "Repalis project"),
])
replace_in_file("clients/packages/ui/package.json", [
    (r"Polar UI Components", "Repalis UI Components"),
    (r"Polar project", "Repalis project"),
    (r'"author": "Polar"', '"author": "Repalis"'),
])

# 8. clients/adapters
replace_in_file("clients/adapters/nuxt/src/module.ts", [
    (r"configKey:\s*'polar'", "configKey: 'repalis'"),
])
replace_in_file("clients/adapters/nuxt/playground/nuxt.config.ts", [
    (r"\bpolar:\s*\{\}", "repalis: {}"),
])
replace_in_file("clients/adapters/nextjs/src/checkout/checkout_decodeuri_corruption.repro.test.ts", [
    (r"server/polar/kit/http\.py", "server/repalis/kit/http.py"),
    (r"polar\.models\.checkout\.Checkout", "repalis.models.checkout.Checkout"),
])
replace_in_file("clients/adapters/nextjs/.gitignore", [
    (r"\bpolar\.ts\b", "repalis.ts"),
])
replace_in_file("clients/adapters/tanstack-start/.gitignore", [
    (r"\bpolar\.ts\b", "repalis.ts"),
])

# 9. clients/packages/cli
replace_in_file("clients/packages/cli/src/api-runtime.ts", [
    (r"const polar = yield\* Repalis", "const repalis = yield* Repalis"),
    (r"\bpolar\b", "repalis"),
])
replace_in_file("clients/packages/cli/src/api-runtime.test.ts", [
    (r"import \* as Polar from '@/services/repalis'", "import * as Repalis from '@/services/repalis'"),
    (r"Command\.make\('polar'\)", "Command.make('repalis')"),
    (r"\bpolar products create\b", "repalis products create"),
    (r"\bpolar auth org\b", "repalis auth org"),
    (r"const polar = Repalis\.layer", "const repalis = Repalis.layer"),
    (r"Layer\.mergeAll\(polar,", "Layer.mergeAll(repalis,"),
])
replace_in_file("clients/packages/cli/src/cli.ts", [
    (r"import \* as Polar from '@/services/repalis'", "import * as Repalis from '@/services/repalis'"),
    (r"commandPath\(polar,", "commandPath(repalis,"),
])
replace_in_file("clients/packages/cli/src/commands/agent/setup.ts", [
    (r"Polar plugin, MCP server and skills", "Repalis plugin, MCP server and skills"),
    (r"Polar plugin", "Repalis plugin"),
    (r"Polar skills", "Repalis skills"),
    (r"What should be set up for Polar\?", "What should be set up for Repalis?"),
    (r"polar agent setup", "repalis agent setup"),
])
replace_in_file("clients/packages/cli/src/commands/agent/setup.test.ts", [
    (r"codex mcp login polar", "codex mcp login repalis"),
    (r"Polar plugin", "Repalis plugin"),
    (r"Polar skills", "Repalis skills"),
    (r"What should be set up for Polar\?", "What should be set up for Repalis?"),
])
replace_in_file("clients/packages/cli/lint/rules/command-boundaries.js", [
    (r"Polar service", "Repalis service"),
    (r"Organizations, Polar, Trigger", "Organizations, Repalis, Trigger"),
])
replace_in_file("clients/packages/cli/lint/rules/no-hardcoded-hosts.js", [
    (r"api\.polar\.sh", "api.repalis.com"),
])

print("Completed clients rebrand script!")
