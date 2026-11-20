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

more_replacements = [
    # Global & Organizations
    ('workspace  = "polar"', 'workspace  = "repalis"'),
    ('workspace = "polar"', 'workspace = "repalis"'),
    ('name = "polar"', 'name = "repalis"'),
    ('team = "polar-sh"', 'team = "repalis"'),
    ('polar = [', 'repalis = ['),
    ('organization      = "polar-sh"', 'organization      = "repalis"'),
    ('key             = "polar_access_token"', 'key             = "repalis_access_token"'),
    ('key             = "polar_webhook_secret"', 'key             = "repalis_webhook_secret"'),
    ('key             = "polar_organization_id"', 'key             = "repalis_organization_id"'),
    ('key             = "polar_scale_product_id"', 'key             = "repalis_scale_product_id"'),
    ('polar_domain_verification', 'repalis_domain_verification'),
    ('DenyAssumingOrPassingNonPolarRoles', 'DenyAssumingOrPassingNonRepalisRoles'),
    ('role/polar-*', 'role/repalis-*'),
    ('polar-retry-*', 'repalis-retry-*'),
    ('polar-${var.environment}', 'repalis-${var.environment}'),
    ('polar-production-', 'repalis-production-'),
    ('polar-sandbox-', 'repalis-sandbox-'),
    ('polar-test-', 'repalis-test-'),
    ('"polar-production"', '"repalis-production"'),
    ('"polar-sandbox"', '"repalis-sandbox"'),
    ('"polar-test"', '"repalis-test"'),
    ('polar_production', 'repalis_production'),
    ('polar_sandbox', 'repalis_sandbox'),
    ('polar_test', 'repalis_test'),
    ('The project ID for the Polar Render project', 'The project ID for the Repalis Render project'),
    ('within the Polar project', 'within the Repalis project'),
    ('# Polar\nvariable', '# Repalis\nvariable'),
    ('# Polar Vercel project setup', '# Repalis Vercel project setup'),
    ('# Polar Render service setup', '# Repalis Render service setup'),
    ('polar-test-services', 'repalis-test-services'),
    ('polar-production-worker-', 'repalis-production-worker-'),
    ('polar-sandbox-worker-', 'repalis-sandbox-worker-'),
    ('polar-test-worker-', 'repalis-test-worker-'),
    ('polar-production-tasks-', 'repalis-production-tasks-'),
    ('polar-sandbox-tasks-', 'repalis-sandbox-tasks-'),
    ('polar-test-tasks-', 'repalis-test-tasks-'),
    ('polar-production-s3-', 'repalis-production-s3-'),
    ('polar-sandbox-s3-', 'repalis-sandbox-s3-'),
    ('polar-test-s3-', 'repalis-test-s3-'),
    ('polar-production-grafana-', 'repalis-production-grafana-'),
    ('polar-sandbox-grafana-', 'repalis-sandbox-grafana-'),
    ('polar-test-grafana-', 'repalis-test-grafana-'),
    ('polar-production-lambda', 'repalis-production-lambda'),
    ('polar-sandbox-lambda', 'repalis-sandbox-lambda'),
    ('polar-test-lambda', 'repalis-test-lambda'),
    ('polar-production-egress', 'repalis-production-egress'),
    ('polar-sandbox-egress', 'repalis-sandbox-egress'),
    ('polar-test-egress', 'repalis-test-egress'),
    ('polar-production-ec2-tailscale', 'repalis-production-ec2-tailscale'),
    ('polar-sandbox-ec2-tailscale', 'repalis-sandbox-ec2-tailscale'),
    ('polar-test-ec2-tailscale', 'repalis-test-ec2-tailscale'),
    ('polar-production-aws-router', 'repalis-production-aws-router'),
    ('polar-sandbox-aws-router', 'repalis-sandbox-aws-router'),
    ('polar-test-aws-router', 'repalis-test-aws-router'),
    ('polar-production-planetscale', 'repalis-production-planetscale'),
    ('polar-sandbox-planetscale', 'repalis-sandbox-planetscale'),
    ('polar-test-planetscale', 'repalis-test-planetscale'),
    ('polar-production-worker', 'repalis-production-worker'),
    ('polar-sandbox-worker', 'repalis-sandbox-worker'),
    ('polar-test-worker', 'repalis-test-worker'),
    ('polar-production-worker-redis', 'repalis-production-worker-redis'),
    ('polar-sandbox-worker-redis', 'repalis-sandbox-worker-redis'),
    ('polar-test-worker-redis', 'repalis-test-worker-redis'),
    ('polar-sandbox-worker-redis-b', 'repalis-sandbox-worker-redis-b'),
    ('polar-test-worker-redis-b', 'repalis-test-worker-redis-b'),
    ('polar-production', 'repalis-production'),
    ('polar-sandbox', 'repalis-sandbox'),
    ('polar-test', 'repalis-test'),
    ('polar workspace', 'repalis workspace'),
    ('Polar<Tier><Account>', 'Repalis<Tier><Account>'),
    ('Must start with polar-', 'Must start with repalis-'),
    ('^polar-[a-z0-9-]+$', '^repalis-[a-z0-9-]+$'),
    ('must start with polar-', 'must start with repalis-'),
    ('ENV_PREFIX_RE = re.compile(r"\\bpolar-(?:production|sandbox|test)-")', 'ENV_PREFIX_RE = re.compile(r"\\brepalis-(?:production|sandbox|test)-")'),
    ('ENV_PREFIX_RE.sub("polar-", value)', 'ENV_PREFIX_RE.sub("repalis-", value)'),
    ('name_prefix         = (var.environment == "production" ? "polar" : "polar-${var.environment}")', 'name_prefix         = (var.environment == "production" ? "repalis" : "repalis-${var.environment}")'),
    ('value     = "[TEST] Polar"', 'value     = "[TEST] Repalis"'),
    ('polar_cpit', 'repalis_cpit'),
]

modified_count = 0
for root, _, files in os.walk('terraform'):
    for f in files:
        p = os.path.join(root, f)
        if replace_in_file(p, more_replacements):
            modified_count += 1

print(f"Modified {modified_count} additional files in terraform/")
