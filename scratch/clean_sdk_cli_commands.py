import os
import re

def clean_file(p):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    orig = content

    # CLI commands types & hints
    content = content.replace("Parameters<Polar[", "Parameters<Repalis[")
    content = content.replace("<Polar[", "<Repalis[")
    content = content.replace("Polar['", "Repalis['")
    content = content.replace('Polar["', 'Repalis["')
    content = re.sub(r'hint:\s*([\'\"])Example:\s*polar\b', r'hint: \1Example: repalis', content)
    content = re.sub(r'\bpolar\s+([a-z_]+)\s+(create|list|update|delete|get)', r'repalis \1 \2', content)

    # OpenAPI x-polar extensions in generator/tests
    content = content.replace("x-polar-cli-preview", "x-repalis-cli-preview")
    content = content.replace("x-polar-environment", "x-repalis-environment")
    content = content.replace("x-polar-pagination", "x-repalis-pagination")
    content = content.replace("x-polar-allowed-subjects", "x-repalis-allowed-subjects")

    # Benchmarks and test names
    content = content.replace("polar-outpost-bench", "repalis-outpost-bench")
    content = content.replace("test_polar_", "test_repalis_")
    content = content.replace("_while_polar_confirms_it", "_while_repalis_confirms_it")
    content = content.replace("_asks_polar_", "_asks_repalis_")
    content = content.replace("_customer_polar_no_longer_knows_", "_customer_repalis_no_longer_knows_")
    content = content.replace("_when_polar_changed_it", "_when_repalis_changed_it")
    content = content.replace("_without_asking_polar", "_without_asking_repalis")
    content = content.replace("_when_polar_fails_the_relay", "_when_repalis_fails_the_relay")
    content = content.replace("_on_polars_receipt", "_on_repalis_receipt")
    content = content.replace("_polar_read_", "_repalis_read_")
    content = content.replace("polar_server", "repalis_server")
    content = content.replace("polar_webhook", "repalis_webhook")
    content = content.replace("polarCore", "repalisCore")
    content = content.replace("polarFetch", "repalisFetch")

    # In READMEs
    content = content.replace("Command.make('polar')", "Command.make('repalis')")
    content = content.replace("`polar auth org`", "`repalis auth org`")
    content = content.replace("`server/polar/openapi.py`", "`server/repalis/openapi.py`")
    content = content.replace("Polar's `2026-10`", "Repalis's `2026-10`")
    content = content.replace("Polar CLI", "Repalis CLI")

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
