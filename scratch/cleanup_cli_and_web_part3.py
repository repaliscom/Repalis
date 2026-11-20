import os
import re

REPO_DIR = r"d:\Repalis"

def replace_in_file(rel_path, replacements):
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
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)
            
    if content != orig:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)
        print(f"Updated {rel_path}")
        return True
    return False

# 1. Logfire URLs and Linear URLs in server
replace_in_file("server/repalis/backoffice/external_events/endpoints.py", [
    (r"logfire-us\.pydantic\.dev/polar/polar", "logfire-us.pydantic.dev/repalis/repalis"),
])
replace_in_file("server/repalis/backoffice/organizations_v2/views/detail_view.py", [
    (r"logfire-us\.pydantic\.dev/polar/polar", "logfire-us.pydantic.dev/repalis/repalis"),
])
replace_in_file("server/repalis/kit/encryption.py", [
    (r"linear\.app/polarsh", "linear.app/repalis"),
])
replace_in_file("server/repalis/kit/hash_secrets.py", [
    (r"linear\.app/polarsh", "linear.app/repalis"),
])

# 2. CLI commands, tests, services
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

for f in cli_files:
    replace_in_file(f, [
        (r"polar-init-cmd-", "repalis-init-cmd-"),
        (r"polar-prune-", "repalis-prune-"),
        (r"polar-deliveries-", "repalis-deliveries-"),
        (r"polar\.config\.", "repalis.config."),
        (r"polar\.json\b", "repalis.json"),
        (r"\bpolar config\b", "repalis config"),
        (r"\bpolar agent setup\b", "repalis agent setup"),
        (r"\bpolar webhook\b", "repalis webhook"),
        (r"\bpolar events\b", "repalis events"),
        (r"\bpolar auth\b", "repalis auth"),
        (r"\bpolar update\b", "repalis update"),
        (r"\.polar/", ".repalis/"),
        (r"\.polar\\", ".repalis\\"),
        (r"join\(homedir\(\), '\.polar'", "join(homedir(), '.repalis'"),
        (r"join\(home, '\.polar'", "join(home, '.repalis'"),
        (r"Polar API", "Repalis API"),
        (r"Polar billing plan", "Repalis billing plan"),
        (r"Polar skills", "Repalis skills"),
        (r"Polar plugin", "Repalis plugin"),
        (r"Polar stack", "Repalis stack"),
        (r"Polar config", "Repalis config"),
        (r"polar/Json/Environment", "repalis/Json/Environment"),
        (r"bin/polar\b", "bin/repalis"),
        (r"'bin', 'polar'", "'bin', 'repalis'"),
        (r"source=polar", "source=repalis"),
        (r"const polar =", "const repalis ="),
        (r"\bpolar\.name\b", "repalis.name"),
        (r"\bpolar\.subcommands\b", "repalis.subcommands"),
        (r"runWith\(polar,", "runWith(repalis,"),
        (r"Layer\.effect\(Polar,", "Layer.effect(Repalis,"),
    ])

# 3. igloo.tsx
replace_in_file("clients/apps/web/src/components/FieldGuide/pages/igloo.tsx", [
    (r"const polar = \{", "const repalis = {"),
    (r"\bpolar\.x\b", "repalis.x"),
    (r"\bpolar\.w\b", "repalis.w"),
    (r"\.\.\.polar\}", "...repalis}"),
    (r'name="POLAR"', 'name="REPALIS"'),
])

# 4. update-sdk-dependencies
replace_in_file("clients/scripts/update-sdk-dependencies.mjs", [
    (r"packageJson\.name !== 'polar-cli'", "packageJson.name !== '@repalis/cli'"),
])

# 5. i18n
replace_in_file("clients/packages/i18n/scripts/translate.ts", [
    (r"'Polar i18n'", "'Repalis i18n'"),
])
replace_in_file("clients/packages/i18n/scripts/validate.ts", [
    (r"'Polar i18n Validation'", "'Repalis i18n Validation'"),
])

print("Completed cli and web cleanup!")
