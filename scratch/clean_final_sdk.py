import os
import re

p1 = 'sdk/typescript/package.json'
with open(p1, 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('"polar"', '"repalis"')
with open(p1, 'w', encoding='utf-8') as f:
    f.write(c)

p2 = 'sdk/cli-commands/README.md'
with open(p2, 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('POLAR_ENVIRONMENT', 'REPALIS_ENVIRONMENT')
with open(p2, 'w', encoding='utf-8') as f:
    f.write(c)

for root, _, files in os.walk('sdk/typescript/.agents/skills/repalis-typescript-sdk'):
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fl:
                c = fl.read()
            orig = c
            c = c.replace('polar.customers', 'repalis.customers')
            c = c.replace('polar.checkouts', 'repalis.checkouts')
            c = c.replace('polar.customerSessions', 'repalis.customerSessions')
            c = c.replace('polar.organizations', 'repalis.organizations')
            c = c.replace('polar.events', 'repalis.events')
            c = c.replace('import { Polar } from', 'import { Repalis } from')
            c = c.replace('new Polar', 'new Repalis')
            c = c.replace('Polar', 'Repalis')
            if orig != c:
                with open(path, 'w', encoding='utf-8') as fl:
                    fl.write(c)
                print(f"Cleaned {path}")

print("Cleaned final SDK references.")
