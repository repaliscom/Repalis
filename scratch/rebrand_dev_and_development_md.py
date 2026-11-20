import os
import re

def replace_in_file(path, replacements):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    orig = c
    for t, r in replacements:
        c = c.replace(t, r)
    if orig != c:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {path}")

# 1. DEVELOPMENT.md
replace_in_file('DEVELOPMENT.md', [
    ('~/.config/polar/secrets.env', '~/.config/repalis/secrets.env'),
    ('~/.config/polar/docker-instances.json', '~/.config/repalis/docker-instances.json'),
    ('~/.config/polar', '~/.config/repalis'),
    ('polar-sandbox', 'repalis-sandbox'),
    ('polar_dev_<N>', 'repalis_dev_<N>'),
    ('polar_dev_0', 'repalis_dev_0'),
    ('polar_dev_1', 'repalis_dev_1'),
    ('polar-s3-<N>', 'repalis-s3-<N>'),
    ('polar-s3-0', 'repalis-s3-0'),
    ('polar-s3-1', 'repalis-s3-1'),
    ('polar_test_<worker_id>', 'repalis_test_<worker_id>'),
    ('POLAR_TEST_DATABASE_TEMPLATE=polar_test', 'POLAR_TEST_DATABASE_TEMPLATE=repalis_test'),
    ('polar_test', 'repalis_test'),
    ('POLAR_SECRETS_FILE', 'REPALIS_SECRETS_FILE'),
    ('client_id=polar, client_secret=polar-secret', 'client_id=repalis, client_secret=repalis-secret'),
    ('https://linear.app/polarsh/', 'https://linear.app/repalis/'),
    ('polar/integrations/stripe', 'repalis/integrations/stripe'),
])

# 2. dev/cli/
replace_in_file('dev/cli/up_steps/12_build_backoffice.py', [
    ('SERVER_DIR / "polar" / "backoffice"', 'SERVER_DIR / "repalis" / "backoffice"'),
])

replace_in_file('dev/cli/commands/worker.py', [
    ('"--watch", "polar"', '"--watch", "repalis"'),
])

replace_in_file('dev/cli/commands/docker.py', [
    ('SHARED_PROJECT_NAME = "polar-shared"', 'SHARED_PROJECT_NAME = "repalis-shared"'),
    ('SHARED_NETWORK_NAME = "polar-shared"', 'SHARED_NETWORK_NAME = "repalis-shared"'),
    ('/ ".config" / "polar" / "docker-instances.json"', '/ ".config" / "repalis" / "docker-instances.json"'),
    ('return f"polar-app-{instance}"', 'return f"repalis-app-{instance}"'),
    ('return f"polar_dev_{instance}"', 'return f"repalis_dev_{instance}"'),
    ('return f"polar-s3-{instance}"', 'return f"repalis-s3-{instance}"'),
    ('return f"polar-s3-public-{instance}"', 'return f"repalis-s3-public-{instance}"'),
    ('~/.config/polar/secrets.env', '~/.config/repalis/secrets.env'),
    ('"polar-shared"', '"repalis-shared"'),
    ('polar-shared', 'repalis-shared'),
    ('"polar"', '"repalis"'),
    ('-U polar', '-U repalis'),
    ('"name": "polar-app"', '"name": "repalis-app"'),
    ('"name": "polar-api"', '"name": "repalis-api"'),
])

replace_in_file('dev/cli/commands/start.py', [
    ('SESSION = "polar"', 'SESSION = "repalis"'),
    ('@polar_role', '@repalis_role'),
])

replace_in_file('dev/cli/commands/stop.py', [
    ('SESSION = "polar"', 'SESSION = "repalis"'),
])

replace_in_file('dev/cli/commands/switch.py', [
    ('@polar_role', '@repalis_role'),
])

replace_in_file('dev/cli/commands/repalis.py', [
    ('name="polar"', 'name="repalis"'),
])

replace_in_file('dev/cli/commands/seed.py', [
    ('_configure_polar_self_integration', '_configure_repalis_self_integration'),
    ('"polar-self-env"', '"repalis-self-env"'),
])

replace_in_file('dev/cli/commands/snap.py', [
    ('@polar-sh/', '@repalis/'),
])

replace_in_file('dev/cli/secrets_io.py', [
    ('POLAR_SECRETS_FILE', 'REPALIS_SECRETS_FILE'),
    ('/ ".config" / "polar" / "secrets.env"', '/ ".config" / "repalis" / "secrets.env"'),
])

replace_in_file('dev/cli/stripe_config.py', [
    ('STRIPE_CLI_PROFILE = "polar-sandbox"', 'STRIPE_CLI_PROFILE = "repalis-sandbox"'),
])

replace_in_file('dev/cli/up_steps/05_wait_for_services.py', [
    ('["docker", "compose", "exec", "-T", "db", "pg_isready", "-U", "polar"]', '["docker", "compose", "exec", "-T", "db", "pg_isready", "-U", "repalis"]'),
])

replace_in_file('dev/cli/_analytics_send.py', [
    ('/ ".config" / "polar"', '/ ".config" / "repalis"'),
])

# 3. dev/ scripts
replace_in_file('dev/create-test-db', [
    ('user="polar"', 'user="repalis"'),
    ('password="polar"', 'password="repalis"'),
    ('test_database="polar_test"', 'test_database="repalis_test"'),
])

replace_in_file('dev/create-worktree', [
    ('db_name="polar_dev_$name"', 'db_name="repalis_dev_$name"'),
    ('user="polar"', 'user="repalis"'),
    ('password="polar"', 'password="repalis"'),
])

replace_in_file('dev/secrets.env.template', [
    ('~/.config/polar/secrets.env', '~/.config/repalis/secrets.env'),
])

# 4. dev/docker/
replace_in_file('dev/docker/scripts/startup.sh', [
    ('options = {\'kid\': \'polar_dev\', \'use\': \'sig\'}', 'options = {\'kid\': \'repalis_dev\', \'use\': \'sig\'}'),
    ('READ_USER="${POLAR_POSTGRES_READ_USER:-polar_read}"', 'READ_USER="${POLAR_POSTGRES_READ_USER:-repalis_read}"'),
    ('--reload-dir polar', '--reload-dir repalis'),
    ('--watch polar', '--watch repalis'),
])

replace_in_file('dev/docker/scripts/startup-web.sh', [
    ('@polar-sh/client', '@repalis/client'),
    ('@polar-sh/ui', '@repalis/ui'),
    ('@polar-sh/orbit', '@repalis/orbit'),
    ('@polar-sh/checkout', '@repalis/checkout'),
])

replace_in_file('dev/docker/docker-compose.shared.yml', [
    ('polar-shared', 'repalis-shared'),
    ('POSTGRES_USER: polar', 'POSTGRES_USER: repalis'),
    ('POSTGRES_PASSWORD: polar', 'POSTGRES_PASSWORD: repalis'),
    ('POSTGRES_DB: polar', 'POSTGRES_DB: repalis'),
    ('POLAR_READ_USER: polar_read', 'POLAR_READ_USER: repalis_read'),
    ('POLAR_READ_PASSWORD: polar', 'POLAR_READ_PASSWORD: repalis'),
    ('"pg_isready", "-q", "-d", "polar", "-U", "polar"', '"pg_isready", "-q", "-d", "repalis", "-U", "repalis"'),
    ('MINIO_ROOT_USER: polar-development', 'MINIO_ROOT_USER: repalis-development'),
    ('MINIO_ROOT_PASSWORD: polar123456789', 'MINIO_ROOT_PASSWORD: repalis123456789'),
    ('BUCKET_NAME: polar-s3', 'BUCKET_NAME: repalis-s3'),
    ('PUBLIC_BUCKET_NAME: polar-s3-public', 'PUBLIC_BUCKET_NAME: repalis-s3-public'),
    ('ACCESS_KEY: polar-development', 'ACCESS_KEY: repalis-development'),
    ('SECRET_ACCESS_KEY: polar123456789', 'SECRET_ACCESS_KEY: repalis123456789'),
    ('GF_SECURITY_ADMIN_USER=polar', 'GF_SECURITY_ADMIN_USER=repalis'),
    ('GF_SECURITY_ADMIN_PASSWORD=polar', 'GF_SECURITY_ADMIN_PASSWORD=repalis'),
])

replace_in_file('dev/docker/docker-compose.dev.yml', [
    ('polar-shared', 'repalis-shared'),
    ('polar-app-', 'repalis-app-'),
    ('polar-s3-', 'repalis-s3-'),
    ('polar-s3-public-', 'repalis-s3-public-'),
    ('polar_dev_', 'repalis_dev_'),
    ('polar-development', 'repalis-development'),
    ('polar123456789', 'repalis123456789'),
    ('polar_read', 'repalis_read'),
])

replace_in_file('dev/CLOUD_AGENTS.md', [
    ('polar-session-start.log', 'repalis-session-start.log'),
    ('polar-dockerd.log', 'repalis-dockerd.log'),
    ('polar-pnpm', 'repalis-pnpm'),
    ('tmux session `polar`', 'tmux session `repalis`'),
    ('session `polar`', 'session `repalis`'),
    ('-s polar', '-s repalis'),
    ('`polar` tmux pane', '`repalis` tmux pane'),
    ('`polar` tmux session', '`repalis` tmux session'),
    ('`polar_test_<worker_id>`', '`repalis_test_<worker_id>`'),
    ('`polar_test_master`', '`repalis_test_master`'),
    ('`polar_test`', '`repalis_test`'),
    ('`polar/config.py`', '`repalis/config.py`'),
])

print("dev/ and DEVELOPMENT.md updated.")
