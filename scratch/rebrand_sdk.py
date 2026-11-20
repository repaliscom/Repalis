import os
import re

directories = ['sdk', 'server/repalis/__init__.py', 'clients/packages/cli/src/services/repalis.ts', 'clients/packages/cli/src/utils/test-utils/services.ts']

replacements = [
    # Functions and types
    ('createPolarCore', 'createRepalisCore'),
    ('createPolar', 'createRepalis'),
    ('PolarCore', 'RepalisCore'),
    ('PolarOptions', 'RepalisOptions'),
    ('PolarAsync', 'RepalisAsync'),
    ('PolarClientError', 'RepalisClientError'),
    ('PolarDeserializationError', 'RepalisDeserializationError'),
    ('PolarNetworkError', 'RepalisNetworkError'),
    ('PolarRateLimitError', 'RepalisRateLimitError'),
    ('PolarServerError', 'RepalisServerError'),
    ('PolarWebhookVerificationError', 'RepalisWebhookVerificationError'),
    ('PolarWebhookUnknownTypeError', 'RepalisWebhookUnknownTypeError'),
    ('PolarWebhookError', 'RepalisWebhookError'),
    ('PolarOutpostError', 'RepalisOutpostError'),
    ('PolarServer', 'RepalisServer'),
    ('startPolarServer', 'startRepalisServer'),
    ('PolarError', 'RepalisError'),
    ('PolarClient', 'RepalisClient'),

    # String error messages and user agents
    ('Polar API network error', 'Repalis API network error'),
    ('Polar API returned a server error', 'Repalis API returned a server error'),
    ('Polar API returned an error', 'Repalis API returned an error'),
    ('Polar API', 'Repalis API'),
    ('Polar Webhooks', 'Repalis Webhooks'),
    ('Polar webhooks', 'Repalis webhooks'),
    ('Polar SDK', 'Repalis SDK'),

    # Class definitions
    ('class Polar:', 'class Repalis:'),
    ('class Polar(', 'class Repalis('),
    ('export type Polar =', 'export type Repalis ='),
    ('type PolarSDK =', 'type RepalisSDK ='),
    ('fakePolar', 'fakeRepalis'),
    ('const polar =', 'const repalis ='),
    ('polar: Repalis', 'repalis: Repalis'),
    ('polar: Polar', 'repalis: Repalis'),
    ('client: Polar', 'client: Repalis'),
    ('client: Repalis', 'client: Repalis'),
    ('client: RepalisCore', 'client: RepalisCore'),
    ('client: PolarCore', 'client: RepalisCore'),
]

updated_files = []

def process_file(p):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    orig = content
    for t, r in replacements:
        content = content.replace(t, r)
    
    # Specific regex replacements for python / ts
    # e.g. "from repalis.v2026_10 import Polar" -> "from repalis.v2026_10 import Repalis"
    content = re.sub(r'from (repalis(?:\.v[0-9_]+)?) import ([^,\n]*, )?Polar\b', r'from \1 import \2Repalis', content)
    content = re.sub(r'from (repalis(?:\.v[0-9_]+)?) import Polar\b', r'from \1 import Repalis', content)
    content = re.sub(r'\btype\s+Polar\s+as\s+PolarSDK\b', 'type Repalis as RepalisSDK', content)
    content = re.sub(r'\bPolarSDK\b', 'RepalisSDK', content)

    if orig != content:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_files.append(p)

for target in directories:
    if os.path.isfile(target):
        process_file(target)
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            if any(x in root for x in ['node_modules', 'dist', '__pycache__']):
                continue
            for f in files:
                if f.endswith(('.py', '.ts', '.jinja', '.md', '.json')):
                    process_file(os.path.join(root, f))

print(f"Updated {len(updated_files)} files in SDK and related directories.")
