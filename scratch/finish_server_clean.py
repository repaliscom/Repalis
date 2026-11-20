import os
import re

def clean_file(p):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    orig = content

    # Migrations header
    content = content.replace('# Polar Custom Imports', '# Repalis Custom Imports')

    # Config realm
    content = content.replace('WWW_AUTHENTICATE_REALM: str = "polar"', 'WWW_AUTHENTICATE_REALM: str = "repalis"')

    # S3 schemas
    content = content.replace('"polar-id":', '"repalis-id":')

    # Worker test queues
    content = content.replace('polar-sandbox-tasks', 'repalis-sandbox-tasks')
    content = content.replace('polar-test-tasks', 'repalis-test-tasks')

    # SDK test fixture
    content = content.replace('async def polar(app: FastAPI)', 'async def repalis_sdk(app: FastAPI)')
    content = content.replace('async def test_openapi(polar: RepalisAsync)', 'async def test_openapi(repalis_sdk: RepalisAsync)')
    content = content.replace('async def test_webhooks(polar: RepalisAsync)', 'async def test_webhooks(repalis_sdk: RepalisAsync)')
    content = content.replace('await polar.', 'await repalis_sdk.')

    # Load tests
    content = content.replace('Polar API', 'Repalis API')
    content = content.replace('Polar payment infrastructure', 'Repalis payment infrastructure')

    # Analyzer
    content = content.replace("SELL ON POLAR", "SELL ON REPALIS")
    content = content.replace("Polar's acceptable use policy", "Repalis's acceptable use policy")
    content = content.replace("Polar’s acceptable use policy", "Repalis’s acceptable use policy")

    # Generic Polar mentions in docstrings/comments/descriptions
    content = content.replace("Polar creates", "Repalis creates")
    content = content.replace("Polar won't", "Repalis won't")
    content = content.replace("Polar can't", "Repalis can't")
    content = content.replace("Polar will", "Repalis will")
    content = content.replace("Polar sells", "Repalis sells")
    content = content.replace("Polar refunded", "Repalis refunded")
    content = content.replace("Polar received", "Repalis received")
    content = content.replace("Polar checkout session", "Repalis checkout session")
    content = content.replace("This Polar environment", "This Repalis environment")
    content = content.replace("into Polar", "into Repalis")
    content = content.replace("onto Polar", "onto Repalis")
    content = content.replace("on Polar", "on Repalis")
    content = content.replace("from Polar", "from Repalis")
    content = content.replace("to Polar", "to Repalis")
    content = content.replace("with Polar", "with Repalis")
    content = content.replace("by Polar", "by Repalis")
    content = content.replace("via the Polar SDK", "via the Repalis SDK")
    content = content.replace("Polar SDK", "Repalis SDK")

    if orig != content:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

updated = 0
for root, dirs, files in os.walk('server'):
    if any(x in root for x in ['__pycache__']):
        continue
    for f in files:
        if f.endswith('.py'):
            if clean_file(os.path.join(root, f)):
                updated += 1

print(f"Cleaned {updated} files in server/.")
