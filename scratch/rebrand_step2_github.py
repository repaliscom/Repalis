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

# 1. Scripts
for root, _, files in os.walk('.github/scripts'):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('polar-merge-bot', 'repalis-merge-bot'),
            ('https://logfire-us.pydantic.dev/polar/polar/', 'https://logfire-us.pydantic.dev/repalis/repalis/'),
            ('https://polar-sh.sentry.io/issues/', 'https://repalis.sentry.io/issues/'),
            ('https://polar-sh.sentry.io', 'https://repalis.sentry.io'),
            ('polar_deployment_reply', 'repalis_deployment_reply'),
        ])

# 2. Workflows
for root, _, files in os.walk('.github/workflows'):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('server/polar/', 'server/repalis/'),
            ('server/polar/**', 'server/repalis/**'),
            ('polar-merge-bot', 'repalis-merge-bot'),
            ('polar-cli', 'repalis-cli'),
            ('polar-darwin-', 'repalis-darwin-'),
            ('polar-linux-', 'repalis-linux-'),
            ('polar-windows-', 'repalis-windows-'),
            ('--outfile polar', '--outfile repalis'),
            ('./polar --version', './repalis --version'),
            ('./polar.exe --version', './repalis.exe --version'),
            ('codesign --verify --strict --verbose=2 ./polar', 'codesign --verify --strict --verbose=2 ./repalis'),
            ('Compress-Archive -Path polar.exe', 'Compress-Archive -Path repalis.exe'),
            ('ditto -c -k polar', 'ditto -c -k repalis'),
            ('tar -czf "${{ matrix.archive }}" polar', 'tar -czf "${{ matrix.archive }}" repalis'),
            ('pattern: polar-*', 'pattern: repalis-*'),
            ('release-assets/polar-$target', 'release-assets/repalis-$target'),
            ('binary=polar.exe', 'binary=repalis.exe'),
            ('binary=polar', 'binary=repalis'),
            ('POLAR_CLI_BUILD', 'REPALIS_CLI_BUILD'),
            ('POLAR_CLI_TELEMETRY_OPTOUT', 'REPALIS_CLI_TELEMETRY_OPTOUT'),
            ('cache-key: polar/', 'cache-key: repalis/'),
            ('polar-sandbox-lambda-worker', 'repalis-sandbox-lambda-worker'),
            ('polar-production-lambda-worker', 'repalis-production-lambda-worker'),
            ('polar-test-lambda-worker', 'repalis-test-lambda-worker'),
            ('polar-sandbox-worker-', 'repalis-sandbox-worker-'),
            ('polar-production-worker-', 'repalis-production-worker-'),
            ('polar-test-worker-', 'repalis-test-worker-'),
            ('CLUSTER: polar-test', 'CLUSTER: repalis-test'),
            ('SERVICE: polar-test-api-events-test', 'SERVICE: repalis-test-api-events-test'),
            ('polar-sandbox-image-resizer', 'repalis-sandbox-image-resizer'),
            ('polar-image-resizer', 'repalis-image-resizer'),
            ('POSTGRES_USER=polar', 'POSTGRES_USER=repalis'),
            ('POSTGRES_PASSWORD=polar', 'POSTGRES_PASSWORD=repalis'),
            ('POSTGRES_DB=polar_test', 'POSTGRES_DB=repalis_test'),
            ('POSTGRES_USER: polar', 'POSTGRES_USER: repalis'),
            ('POSTGRES_PASSWORD: polar', 'POSTGRES_PASSWORD: repalis'),
            ('POSTGRES_DB: polar_development', 'POSTGRES_DB: repalis_development'),
            ('pg_isready -U polar', 'pg_isready -U repalis'),
            ('the wait for Polar', 'the wait for Repalis'),
            ('polar_cst_', 'repalis_cst_'),
        ])

print("Step 2 script execution complete.")
