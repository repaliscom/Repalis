import os

REPO_DIR = r"d:\Repalis"

def replace_in_file_exact(rel_path, replacements):
    path = os.path.join(REPO_DIR, rel_path.replace("/", os.sep))
    if not os.path.exists(path):
        print(f"Warning: file {rel_path} does not exist")
        return False
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {rel_path}: {e}")
        return False
        
    orig = content
    for target, repl in replacements:
        content = content.replace(target, repl)
            
    if content != orig:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)
        print(f"Updated {rel_path}")
        return True
    return False

# 1. CLI files exact replacements
cli_files = [
    "clients/packages/cli/src/commands/config/init/index.test.ts",
    "clients/packages/cli/src/commands/config/init/report.ts",
    "clients/packages/cli/src/commands/config/plan.test.ts",
    "clients/packages/cli/src/commands/config/publish.ts",
    "clients/packages/cli/src/commands/config/publish.test.ts",
    "clients/packages/cli/src/commands/config/prune.ts",
    "clients/packages/cli/src/commands/config/prune.test.ts",
    "clients/packages/cli/src/commands/config/apply.test.ts",
    "clients/packages/cli/src/commands/webhook/trigger.test.ts",
    "clients/packages/cli/src/commands/webhook/listen.ts",
    "clients/packages/cli/src/services/agent-setup/plugins.test.ts",
    "clients/packages/cli/src/services/agent-setup/cursor.ts",
    "clients/packages/cli/src/services/agent-setup/cursor.test.ts",
    "clients/packages/cli/src/services/billing-config/apply.test.ts",
    "clients/packages/cli/src/services/billing-config/generate/contract.ts",
    "clients/packages/cli/src/services/billing-config/prune.test.ts",
    "clients/packages/cli/src/services/billing-config/prune.ts",
    "clients/packages/cli/src/services/credentials.ts",
    "clients/packages/cli/src/services/deliveries.test.ts",
    "clients/packages/cli/src/services/deliveries.ts",
    "clients/packages/cli/src/services/listen.test.ts",
    "clients/packages/cli/src/services/listen.ts",
    "clients/packages/cli/src/services/repalis.ts",
    "clients/packages/cli/src/services/trigger.test.ts",
    "clients/packages/cli/src/services/trigger.ts",
    "clients/packages/cli/src/services/update.test.ts",
    "clients/packages/cli/src/services/updater.test.ts",
    "clients/packages/cli/src/services/update-check.ts",
    "clients/packages/cli/src/utils/billing-config/markdown.test.ts",
    "clients/packages/cli/src/utils/billing-config/markdown.ts",
    "clients/packages/cli/src/utils/billing-config/problems.test.ts",
    "clients/packages/cli/src/utils/billing-config/problems.ts",
    "clients/packages/cli/src/utils/callback-page.test.ts",
    "clients/packages/cli/src/utils/flags.ts",
    "clients/packages/cli/src/utils/json.ts",
    "clients/packages/cli/src/utils/url.test.ts",
    "clients/packages/cli/scripts/docs.ts",
]

replacements = [
    ("polar-init-cmd-", "repalis-init-cmd-"),
    ("polar-prune-", "repalis-prune-"),
    ("polar-deliveries-", "repalis-deliveries-"),
    ("polar.config.ts", "repalis.config.ts"),
    ("polar.config.js", "repalis.config.js"),
    ("polar.config.", "repalis.config."),
    ("polar.json", "repalis.json"),
    ("polar config", "repalis config"),
    ("polar agent setup", "repalis agent setup"),
    ("polar webhook", "repalis webhook"),
    ("polar events", "repalis events"),
    ("polar auth", "repalis auth"),
    ("polar update", "repalis update"),
    (".polar/", ".repalis/"),
    (".polar\\", ".repalis\\"),
    ("join(homedir(), '.polar'", "join(homedir(), '.repalis'"),
    ("join(home, '.polar'", "join(home, '.repalis'"),
    ("Polar API", "Repalis API"),
    ("Polar billing plan", "Repalis billing plan"),
    ("Polar skills", "Repalis skills"),
    ("Polar plugin", "Repalis plugin"),
    ("Polar stack", "Repalis stack"),
    ("Polar config", "Repalis config"),
    ("polar/Json/Environment", "repalis/Json/Environment"),
    ("bin/polar", "bin/repalis"),
    ("'bin', 'polar'", "'bin', 'repalis'"),
    ("source=polar", "source=repalis"),
    ("const polar =", "const repalis ="),
    ("polar.name", "repalis.name"),
    ("polar.subcommands", "repalis.subcommands"),
    ("runWith(polar,", "runWith(repalis,"),
    ("Layer.effect(Polar,", "Layer.effect(Repalis,"),
    ("@repalis/polar installed", "@repalis/repalis installed"),
    ("polar:", "repalis:"),
]

for f in cli_files:
    replace_in_file_exact(f, replacements)

# 2. igloo.tsx
replace_in_file_exact("clients/apps/web/src/components/FieldGuide/pages/igloo.tsx", [
    ("const polar = {", "const repalis = {"),
    ("polar.x", "repalis.x"),
    ("polar.w", "repalis.w"),
    ("...polar}", "...repalis}"),
    ('name="POLAR"', 'name="REPALIS"'),
])

# 3. update-sdk-dependencies
replace_in_file_exact("clients/scripts/update-sdk-dependencies.mjs", [
    ("packageJson.name !== 'polar-cli'", "packageJson.name !== '@repalis/cli'"),
])

# 4. i18n
replace_in_file_exact("clients/packages/i18n/scripts/translate.ts", [
    ("'Polar i18n'", "'Repalis i18n'"),
])
replace_in_file_exact("clients/packages/i18n/scripts/validate.ts", [
    ("'Polar i18n Validation'", "'Repalis i18n Validation'"),
])

# 5. .claude & sdk & docs
replace_in_file_exact(".claude/hooks/session-start.sh", [
    ('export POLAR_TEST_DATABASE_TEMPLATE="polar_test"', 'export POLAR_TEST_DATABASE_TEMPLATE="repalis_test"'),
    ('POLAR_TEST_DATABASE_TEMPLATE=polar_test is set', 'POLAR_TEST_DATABASE_TEMPLATE=repalis_test is set'),
    ('MYPY_LOG="$TMP/polar-mypy-warm.log"', 'MYPY_LOG="$TMP/repalis-mypy-warm.log"'),
])

replace_in_file_exact("sdk/CHANGELOG.md", [
    ("polar.events.ingest()", "repalis.events.ingest()"),
])

replace_in_file_exact("docs/docs.json", [
    ("https://www.evendeals.com/integrations/polar", "https://www.evendeals.com/integrations/repalis"),
    ("https://refgrow.com/polar-affiliate-software", "https://refgrow.com/repalis-affiliate-software"),
])

# 6. dev CLI and docs
replace_in_file_exact("dev/cli/cli.py", [
    ("Polar Development CLI", "Repalis Development CLI"),
    ("Polar dev", "Repalis dev"),
    ("Polar development environment", "Repalis development environment"),
])
replace_in_file_exact("dev/cli/commands/docker.py", [
    ("Polar Docker Development Environment", "Repalis Docker Development Environment"),
    ("Starting Polar shared infra", "Starting Repalis shared infra"),
    ("Starting Polar app stack", "Starting Repalis app stack"),
    ("`polar-app-N` project", "`repalis-app-N` project"),
    ("Polar Docker dev env", "Repalis Docker dev env"),
])
replace_in_file_exact("dev/cli/commands/down.py", [
    ("Stopping Polar development environment", "Stopping Repalis development environment"),
])
replace_in_file_exact("dev/cli/README.md", [
    ("dev docker exec db psql -U polar", "dev docker exec db psql -U repalis"),
])
replace_in_file_exact("dev/CLOUD_AGENTS.md", [
    ("`acme-corp`, `polar`, etc.", "`acme-corp`, `repalis`, etc."),
])

print("Completed exact replacements!")
