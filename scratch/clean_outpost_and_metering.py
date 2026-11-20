import os
import re

targets = [
    'sdk/python/repalis',
    'sdk/python/tests',
    'sdk/typescript/src',
    'sdk/generator',
    'sdk/cli-commands',
    'sdk/e2e',
]

def clean_file(p):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    orig = content

    # 1. Variables and methods
    content = content.replace('as polar:', 'as repalis:')
    content = content.replace('as polar,', 'as repalis,')
    content = content.replace('client=polar.', 'client=repalis.')
    content = content.replace('polar._client', 'repalis._client')
    content = content.replace('polar.metering', 'repalis.metering')
    content = content.replace('polar.events', 'repalis.events')
    content = content.replace('polar.customers', 'repalis.customers')
    content = content.replace('polar.checkouts', 'repalis.checkouts')
    content = content.replace('polar.subscriptions', 'repalis.subscriptions')
    content = content.replace('polar.products', 'repalis.products')
    content = content.replace('polar.orders', 'repalis.orders')
    content = content.replace('polar.benefits', 'repalis.benefits')
    content = content.replace('polar.meters', 'repalis.meters')
    content = content.replace('polar.webhooks', 'repalis.webhooks')
    content = content.replace('polar.files', 'repalis.files')
    content = content.replace('polar.discounts', 'repalis.discounts')
    content = content.replace('polar.disputes', 'repalis.disputes')
    content = content.replace('polar.refunds', 'repalis.refunds')
    content = content.replace('polar.oauth2', 'repalis.oauth2')
    content = content.replace('polar.metrics', 'repalis.metrics')
    content = content.replace('polar.outpost', 'repalis.outpost')
    content = content.replace('"polar.outpost"', '"repalis.outpost"')
    content = content.replace("'polar.outpost'", "'repalis.outpost'")

    # Outpost sources
    content = content.replace('Literal["redis", "polar", "either"]', 'Literal["redis", "repalis", "either"]')
    content = content.replace('Literal["redis", "polar"]', 'Literal["redis", "repalis"]')
    content = content.replace('"redis" | "polar"', '"redis" | "repalis"')
    content = content.replace('"redis" | "polar" | "either"', '"redis" | "repalis" | "either"')
    content = content.replace('source == "polar"', 'source == "repalis"')
    content = content.replace('source === "polar"', 'source === "repalis"')
    content = content.replace('source = "polar"', 'source = "repalis"')
    content = content.replace('source: "polar"', 'source: "repalis"')
    content = content.replace('_configure("polar")', '_configure("repalis")')
    content = content.replace("_configure('polar')", "_configure('repalis')")

    # Error strings
    content = content.replace("Polar refused Outpost", "Repalis refused Outpost")
    content = content.replace("Polar rejected the pull", "Repalis rejected the pull")

    # In comments:
    content = content.replace("Polar's", "Repalis's")
    content = content.replace("Polar’s", "Repalis’s")
    content = content.replace("Polar", "Repalis")
    content = re.sub(r'\bpolar\b', 'repalis', content)

    if orig != content:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

updated = 0
for target in targets:
    for root, dirs, files in os.walk(target):
        if any(x in root for x in ['node_modules', 'dist', '__pycache__']):
            continue
        for f in files:
            if f.endswith(('.py', '.ts', '.jinja', '.md', '.json')):
                if clean_file(os.path.join(root, f)):
                    updated += 1

print(f"Cleaned {updated} files across SDK targets.")
