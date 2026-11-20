import os
import re

def clean_readme(p):
    if not os.path.exists(p):
        return
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c
    c = c.replace('polar = Polar(', 'repalis = Repalis(')
    c = c.replace('with Polar(', 'with Repalis(')
    c = c.replace('as polar:', 'as repalis:')
    c = c.replace('acme = Polar(', 'acme = Repalis(')
    c = c.replace('polar = RepalisAsync(', 'repalis = RepalisAsync(')
    c = c.replace('polar.customers', 'repalis.customers')
    c = c.replace('polar.metering', 'repalis.metering')
    c = c.replace('reaches Polar', 'reaches Repalis')
    c = c.replace('`Polar`', '`Repalis`')
    c = c.replace('Polar', 'Repalis')
    c = re.sub(r'\bpolar\b', 'repalis', c)
    if orig != c:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Cleaned {p}")

clean_readme('sdk/python/README.md')
clean_readme('sdk/typescript/README.md')
clean_readme('sdk/cli-commands/README.md')
clean_readme('sdk/generator/python/template/README.md')
clean_readme('sdk/generator/typescript/template/README.md')

# Clean test function names in test_client.py
for p in ['sdk/generator/python/template/tests/outpost/test_client.py', 'sdk/python/tests/outpost/test_client.py']:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        orig = c
        c = c.replace('ask_polar_for', 'ask_repalis_for')
        c = c.replace('once_polar_confirmed', 'once_repalis_confirmed')
        c = c.replace('snapshot_polar_did_not', 'snapshot_repalis_did_not')
        c = c.replace('when_polar_refuses', 'when_repalis_refuses')
        c = c.replace('when_polar_rejects', 'when_repalis_rejects')
        c = c.replace('when_polar_refuses_outpost', 'when_repalis_refuses_outpost')
        c = c.replace('asked_polar_for', 'asked_repalis_for')
        if orig != c:
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Cleaned {p}")
