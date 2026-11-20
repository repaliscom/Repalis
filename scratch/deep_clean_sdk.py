import os
import re

def clean_file(p):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    orig = content

    # 1. Phrases and comments
    content = content.replace("Polar organization", "Repalis organization")
    content = content.replace("Polar Organization", "Repalis Organization")
    content = content.replace("Polar customer", "Repalis customer")
    content = content.replace("Polar Customer", "Repalis Customer")
    content = content.replace("Polar event", "Repalis event")
    content = content.replace("Polar Event", "Repalis Event")
    content = content.replace("Polar checkout", "Repalis checkout")
    content = content.replace("Polar Checkout", "Repalis Checkout")
    content = content.replace("Polar subscription", "Repalis subscription")
    content = content.replace("Polar Subscription", "Repalis Subscription")
    content = content.replace("Polar order", "Repalis order")
    content = content.replace("Polar Order", "Repalis Order")
    content = content.replace("Polar product", "Repalis product")
    content = content.replace("Polar Product", "Repalis Product")
    content = content.replace("Polar discount", "Repalis discount")
    content = content.replace("Polar Discount", "Repalis Discount")
    content = content.replace("Polar benefit", "Repalis benefit")
    content = content.replace("Polar Benefit", "Repalis Benefit")
    content = content.replace("Polar meter", "Repalis meter")
    content = content.replace("Polar Meter", "Repalis Meter")
    content = content.replace("Polar account", "Repalis account")
    content = content.replace("Polar Account", "Repalis Account")
    content = content.replace("Polar user", "Repalis user")
    content = content.replace("Polar User", "Repalis User")
    content = content.replace("Polar dashboard", "Repalis dashboard")
    content = content.replace("Polar Dashboard", "Repalis Dashboard")
    content = content.replace("Polar purchases library", "Repalis purchases library")
    content = content.replace("Polar Slack integration", "Repalis Slack integration")
    content = content.replace("Polar iframe", "Repalis iframe")

    # 2. Sentences with Polar
    content = content.replace("What Polar has not sent", "What Repalis has not sent")
    content = content.replace("what Polar has not confirmed", "what Repalis has not confirmed")
    content = content.replace("when Polar drops the connection", "when Repalis drops the connection")
    content = content.replace("Polar is unreachable", "Repalis is unreachable")
    content = content.replace("Polar's configuration", "Repalis's configuration")
    content = content.replace("Polar ingested", "Repalis ingested")
    content = content.replace("Polar stored", "Repalis stored")
    content = content.replace("fake Polar", "fake Repalis")
    content = content.replace('step.client == "polar"', 'step.client == "repalis"')
    content = content.replace('step.client not in ("polar", "redis")', 'step.client not in ("repalis", "redis")')
    content = content.replace('client: typing.ClassVar[typing.Literal["polar"]] = "polar"', 'client: typing.ClassVar[typing.Literal["repalis"]] = "repalis"')
    content = content.replace('Literal["polar"]', 'Literal["repalis"]')
    content = content.replace('[*client_names, "polar", "redis"]', '[*client_names, "repalis", "redis"]')
    content = content.replace('"Polar" + "".join', '"Repalis" + "".join')
    content = content.replace("sdk_namespace }}.Polar", "sdk_namespace }}.Repalis")
    content = content.replace('polar-organization', 'repalis-organization')

    # Readmes
    content = content.replace("# Polar TypeScript SDK", "# Repalis TypeScript SDK")
    content = content.replace("# Polar Python SDK", "# Repalis Python SDK")
    content = content.replace("npm install @polar-sh/sdk", "npm install @repalis/sdk")
    content = content.replace("pnpm add @polar-sh/sdk", "pnpm add @repalis/sdk")
    content = content.replace("pip install polar-sdk", "pip install repalis-sdk")
    content = content.replace("uv add polar-sdk", "uv add repalis-sdk")

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

print(f"Deep cleaned {updated} files in sdk/.")
