import os
import re

def replace_in_file(path, replacements):
    if not os.path.exists(path):
        return 0
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    orig = content
    for pattern, repl in replacements:
        if isinstance(pattern, str):
            content = content.replace(pattern, repl)
        else:
            content = pattern.sub(repl, content)
    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return 1
    return 0

# 1. Root files
replace_in_file('AGENTS.md', [
    (re.compile(r'\bPolarError\b'), 'RepalisError'),
    (re.compile(r'\bPolar(?!\w)'), 'Repalis'),
    ('linear.app/polar', 'linear.app/repalis'),
    ('linear.app/polarsh', 'linear.app/repalis'),
])

replace_in_file('DEVELOPMENT.md', [
    ('client_id=polar, `client_secret=polar`', 'client_id=repalis, `client_secret=repalis`'),
    ('client_id=polar', 'client_id=repalis'),
    ('client_secret=polar', 'client_secret=repalis'),
])

# 2. ADR files
for adr_file in os.listdir('adr'):
    if adr_file.endswith('.md'):
        p = os.path.join('adr', adr_file)
        replace_in_file(p, [
            ('@polar-sh/orbit', '@repalis/orbit'),
            ('PolarError', 'RepalisError'),
            (re.compile(r'\bPolar(?!\w)'), 'Repalis'),
            (re.compile(r'\bpolar(?!\w)'), 'repalis'),
        ])

# 3. .claude/
for root, _, files in os.walk('.claude'):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('server/polar/', 'server/repalis/'),
            ('polar-dev-', 'repalis-dev-'),
            ('polar-session-start.log', 'repalis-session-start.log'),
            ('polar-dockerd.log', 'repalis-dockerd.log'),
            ('polar-compose-pull.log', 'repalis-compose-pull.log'),
            ('Polar pattern enforcement', 'Repalis pattern enforcement'),
            ('Polar local development', 'Repalis local development'),
            (re.compile(r'\bPolar\b'), 'Repalis'),
        ])

# 4. docs/
replace_in_file('docs/docs.json', [
    ('/documentation/welcome-to-polar', '/documentation/welcome-to-repalis'),
    ('/documentation/tools/polar-migrate', '/documentation/tools/repalis-migrate'),
    ('/documentation/tools/polar-init', '/documentation/tools/repalis-init'),
    ('/documentation/integrations/polar-for-raycast', '/documentation/integrations/repalis-for-raycast'),
    ('/documentation/integrations/polar-for-framer', '/documentation/integrations/repalis-for-framer'),
    ('/documentation/integrations/polar-for-zapier', '/documentation/integrations/repalis-for-zapier'),
    ('/documentation/integration-guides/authenticating-with-polar', '/documentation/integration-guides/authenticating-with-repalis'),
    ('/documentation/adapters/polar-shnextjs', '/documentation/adapters/repalis-nextjs'),
    ('/documentation/adapters/polar-shastro', '/documentation/adapters/repalis-astro'),
    ('/documentation/adapters/polar-shremix', '/documentation/adapters/repalis-remix'),
    ('/documentation/adapters/polar-shsveltekit', '/documentation/adapters/repalis-sveltekit'),
    ('/documentation/adapters/polar-shdeno', '/documentation/adapters/repalis-deno'),
    ('/documentation/adapters/polar-shelysia', '/documentation/adapters/repalis-elysia'),
    ('/documentation/adapters/polar-shexpress', '/documentation/adapters/repalis-express'),
    ('/documentation/adapters/polar-shfastify', '/documentation/adapters/repalis-fastify'),
    ('/documentation/adapters/polar-shhono', '/documentation/adapters/repalis-hono'),
    ('/documentation/polar-as-merchant-of-record/', '/documentation/repalis-as-merchant-of-record/'),
])

for openapi in ['docs/openapi/2026-04.openapi.json', 'docs/openapi/2026-10.openapi.json', 'docs/openapi/2027-01.openapi.json']:
    replace_in_file(openapi, [
        ('and use Polar.', 'and use Repalis.'),
        ('their Polar\\npurchases library', 'their Repalis\\npurchases library'),
        ('Polar IDs', 'Repalis IDs'),
        ('Polar purchases library', 'Repalis purchases library'),
    ])

# 5. sdk/
replace_in_file('sdk/CHANGELOG.md', [(re.compile(r'\bPolar\b'), 'Repalis')])
replace_in_file('sdk/generator/python/template/LICENSE', [('Polar Software, Inc.', 'Repalis Software, Inc.'), ('Polar', 'Repalis')])
replace_in_file('sdk/generator/typescript/template/LICENSE', [('Polar Software, Inc.', 'Repalis Software, Inc.'), ('Polar', 'Repalis')])
replace_in_file('sdk/python/LICENSE', [('Polar Software, Inc.', 'Repalis Software, Inc.'), ('Polar', 'Repalis')])
replace_in_file('sdk/typescript/LICENSE', [('Polar Software, Inc.', 'Repalis Software, Inc.'), ('Polar', 'Repalis')])

for pyproject in ['sdk/python/pyproject.toml', 'sdk/generator/python/template/pyproject.toml']:
    replace_in_file(pyproject, [
        ('path = "polar/__init__.py"', 'path = "repalis/__init__.py"'),
        ('packages = ["polar"]', 'packages = ["repalis"]'),
        ('artifacts = ["/polar/.agents/**"]', 'artifacts = ["/repalis/.agents/**"]'),
        ('polar-sdk', 'repalis-sdk'),
    ])

for outpost_f in ['sdk/generator/outpost/apply_snapshot.lua', 'sdk/generator/outpost/confirm.lua',
                  'sdk/generator/outpost/constants.toml', 'sdk/generator/outpost/write_bucket.lua']:
    replace_in_file(outpost_f, [
        (re.compile(r'\bPolar\b'), 'Repalis'),
        (re.compile(r"\bPolar's\b"), "Repalis's"),
    ])

# 6. .agents/
for root, _, files in os.walk('.agents'):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('author: polar', 'author: repalis'),
            ('polar-shared', 'repalis-shared'),
            ('polar-app', 'repalis-app'),
            ('logfire_polar', 'logfire_repalis'),
            ('sentry_polar', 'sentry_repalis'),
            ('polar-${CANDIDATE}', 'repalis-${CANDIDATE}'),
            ('polar-source', 'repalis-source'),
            ('polar_deployment', 'repalis_deployment'),
            ('server/polar/', 'server/repalis/'),
            ('polar/openapi.py', 'repalis/openapi.py'),
            ('PolarError', 'RepalisError'),
            ('PolarRequestValidationError', 'RepalisRequestValidationError'),
            ('@polar-sh/orbit', '@repalis/orbit'),
            ('linear.app/polarsh', 'linear.app/repalis'),
            ('linear.app/polar', 'linear.app/repalis'),
            ('polar-sh.sentry.io', 'repalis.sentry.io'),
            (re.compile(r'\bPolar(?!\w)'), 'Repalis'),
            (re.compile(r'\bpolar(?!\w)'), 'repalis'),
        ])

print("Step 1 script execution complete.")
