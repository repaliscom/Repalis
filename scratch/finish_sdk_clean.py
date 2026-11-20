import os
import re

def clean_file(p):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    orig = content

    # 1. Imports and Types
    content = content.replace("import type { Polar } from '@polar-sh/sdk", "import type { Repalis } from '@repalis/sdk")
    content = content.replace("import type { Polar } from '@repalis/sdk", "import type { Repalis } from '@repalis/sdk")
    content = content.replace("client: V2026_10.Polar", "client: V2026_10.Repalis")
    content = content.replace("client: V2027_01.Polar", "client: V2027_01.Repalis")
    content = content.replace("client: V2026_04.Polar", "client: V2026_04.Repalis")
    content = content.replace("export type { Environment, Polar,", "export type { Environment, Repalis,")
    content = content.replace("from repalis.v2026_10.client import Polar,", "from repalis.v2026_10.client import Repalis,")
    content = content.replace("from repalis.v2027_01.client import Polar,", "from repalis.v2027_01.client import Repalis,")
    content = content.replace("from repalis.v2026_04.client import Polar,", "from repalis.v2026_04.client import Repalis,")
    content = content.replace("from repalis.v2026_10.client import Polar\n", "from repalis.v2026_10.client import Repalis\n")
    content = content.replace("from repalis.v2027_01.client import Polar\n", "from repalis.v2027_01.client import Repalis\n")
    content = content.replace("from repalis.v2026_04.client import Polar\n", "from repalis.v2026_04.client import Repalis\n")

    # 2. Package names
    content = content.replace("@polar-sh/sdk", "@repalis/sdk")
    content = content.replace("@polar-sh/cli-commands", "@repalis/cli-commands")
    content = content.replace("@polar-sh/cli", "@repalis/cli")
    content = content.replace('"author": "Polar"', '"author": "Repalis"')

    # 3. Headers
    content = content.replace('"Polar-Organization"', '"Repalis-Organization"')
    content = content.replace("'Polar-Organization'", "'Repalis-Organization'")
    content = content.replace("`Polar-Organization`", "`Repalis-Organization`")
    content = content.replace("Polar-Organization", "Repalis-Organization")
    content = content.replace("Polar-Version", "Repalis-Version")
    content = content.replace("X-Polar-Affinity-Warmup", "X-Repalis-Affinity-Warmup")
    content = content.replace("x-polar-affinity-warmup", "x-repalis-affinity-warmup")
    content = content.replace("X-Polar-Affinity-Next", "X-Repalis-Affinity-Next")
    content = content.replace("x-polar-affinity-next", "x-repalis-affinity-next")

    # 4. Token fixtures & secrets
    content = content.replace("polar_at_u_", "repalis_at_u_")
    content = content.replace("polar_oat_", "repalis_oat_")
    content = content.replace("POLAR_ACCESS_TOKEN", "REPALIS_ACCESS_TOKEN")
    content = content.replace("POLAR_WEBHOOK_SECRET", "REPALIS_WEBHOOK_SECRET")
    content = content.replace("POLAR_ORGANIZATION_ID", "REPALIS_ORGANIZATION_ID")
    content = content.replace("POLAR_PRODUCT_ID", "REPALIS_PRODUCT_ID")
    content = content.replace("POLAR_BENEFIT_ID", "REPALIS_BENEFIT_ID")
    content = content.replace("POLAR_OUTPOST_TELEMETRY", "REPALIS_OUTPOST_TELEMETRY")
    content = content.replace("POLAR_LATENCY_MS", "REPALIS_LATENCY_MS")

    # 5. Variable names in tests
    content = re.sub(r'\bpolar_client\b', 'repalis_client', content)
    content = re.sub(r'\bpolar_requests\b', 'repalis_requests', content)
    content = re.sub(r'\bpolar_sdk\b', 'repalis_sdk', content)
    content = re.sub(r'\bpolar_class\b', 'repalis_class', content)
    content = re.sub(r'\bwebhooks/polar\b', 'webhooks/repalis', content)
    content = re.sub(r'\bpolar-sdk\b', 'repalis-sdk', content)

    # 6. Doc comments & Readmes
    content = content.replace("Polar TypeScript SDK", "Repalis TypeScript SDK")
    content = content.replace("Polar Python SDK", "Repalis Python SDK")
    content = content.replace("Polar CLI", "Repalis CLI")
    content = content.replace("Polar's side of Outpost", "Repalis's side of Outpost")
    content = content.replace("once Polar confirmed", "once Repalis confirmed")
    content = content.replace("request Outpost sent Polar", "request Outpost sent Repalis")
    content = content.replace("organization Polar configures", "organization Repalis configures")
    content = content.replace("each of Polar's", "each of Repalis's")
    content = content.replace("part of each bucket Polar", "part of each bucket Repalis")
    content = content.replace("external_id Polar has not", "external_id Repalis has not")
    content = content.replace("Polar compares strings", "Repalis compares strings")
    content = content.replace("delivery to Polar", "delivery to Repalis")
    content = content.replace("flush that waits on Polar", "flush that waits on Repalis")
    content = content.replace("Polar meter ID", "Repalis meter ID")
    content = content.replace("Polar meter", "Repalis meter")
    content = content.replace("Polar IDs", "Repalis IDs")
    content = content.replace("by Polar", "by Repalis")
    content = content.replace("when Polar takes over", "when Repalis takes over")
    content = content.replace("created by Polar", "created by Repalis")
    content = content.replace("Polar webhook", "Repalis webhook")
    content = content.replace("Polar Webhook", "Repalis Webhook")

    if orig != content:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

updated = 0
for root, dirs, files in os.walk('sdk'):
    if any(x in root for x in ['node_modules', 'dist', '__pycache__']):
        continue
    for f in files:
        if f.endswith(('.py', '.ts', '.jinja', '.md', '.json')):
            if clean_file(os.path.join(root, f)):
                updated += 1

print(f"Cleaned {updated} files in sdk/.")
