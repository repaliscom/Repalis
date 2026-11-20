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

# 1. demo app
replace_in_file_exact("clients/apps/demo-app/app/steps.ts", [
    ("export const polar =", "export const repalis ="),
    ("const customer = polar.actor", "const customer = repalis.actor"),
])
replace_in_file_exact("clients/apps/demo-app/.github/workflows/repalis.yml", [
    ("POLAR_PREVIEW: '1'", "REPALIS_PREVIEW: '1'"),
    ("polar config plan", "repalis config plan"),
    ("polar config apply", "repalis config apply"),
    ("secrets.POLAR_READ_TOKEN", "secrets.REPALIS_READ_TOKEN"),
    ("secrets.POLAR_WRITE_TOKEN", "secrets.REPALIS_WRITE_TOKEN"),
])

# 2. web homepage & telemetry
replace_in_file_exact("clients/apps/web/src/app/api/homepage/route.ts", [
    ("## What Polar does", "## What Repalis does"),
    ("Polar draws the credits", "Repalis draws the credits"),
    ("Merchant of Record**: Polar resells", "Merchant of Record**: Repalis resells"),
    ("## When to use Polar", "## When to use Repalis"),
    ("Use Polar when", "Use Repalis when"),
])
replace_in_file_exact("clients/apps/web/src/utils/aiTelemetry.ts", [
    ("polarAISpanProcessor", "repalisAISpanProcessor"),
    ("polar-ai", "repalis-ai"),
])

# 3. web components
replace_in_file_exact("clients/apps/web/src/components/Brand/posters/story/ActInvoice.tsx", [
    ("'POLAR'", "'REPALIS'"),
])
replace_in_file_exact("clients/apps/web/src/components/FieldGuide/pages/principles.tsx", [
    ("['POLAR',", "['REPALIS',"),
    ("polar = BOXES", "repalis = BOXES"),
    ("(outpostEnd + polar)", "(outpostEnd + repalis)"),
    ("x2={polar}", "x2={repalis}"),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/integrate/ConnectPanel.tsx", [
    ("http polar", "http repalis"),
    ('"polar": {', '"repalis": {'),
    ("add polar --url", "add repalis --url"),
    ("--skill polar-integration", "--skill repalis-integration"),
])
replace_in_file_exact("clients/apps/web/src/components/Landing/story/chapters.tsx", [
    ("followed through Polar.", "followed through Repalis."),
    ("Polar draws credits down first,", "Repalis draws credits down first,"),
    ("Polar collects the revenue,", "Repalis collects the revenue,"),
    ("Polar in Claude, Cursor and ChatGPT", "Repalis in Claude, Cursor and ChatGPT"),
])
replace_in_file_exact("clients/apps/web/src/components/Onboarding/IntegrateStep.tsx", [
    ('import { polar, checkout', 'import { repalis, checkout'),
    ('polar({', 'repalis({'),
    ('const polar = new Repalis', 'const repalis = new Repalis'),
    (') as polar:', ') as repalis:'),
])

# 4. cli services and utils
replace_in_file_exact("clients/packages/cli/src/services/organizations.ts", [
    ("const polar = yield* Repalis", "const repalis = yield* Repalis"),
    ("polar.use", "repalis.use"),
    ("polar auth login", "repalis auth login"),
    ("polar auth list", "repalis auth list"),
])
replace_in_file_exact("clients/packages/cli/src/services/telemetry.ts", [
    ("polar/Telemetry/Environment", "repalis/Telemetry/Environment"),
    ("polar/Telemetry/Build", "repalis/Telemetry/Build"),
    ("polar/Telemetry/Sender", "repalis/Telemetry/Sender"),
    ("polar/Telemetry", "repalis/Telemetry"),
    ("join(homedir(), '.polar', 'telemetry.json')", "join(homedir(), '.repalis', 'telemetry.json')"),
    ("polar_", "repalis_"),
])
replace_in_file_exact("clients/packages/cli/src/utils/agent-setup.ts", [
    ("polar agent setup", "repalis agent setup"),
    ("Polar MCP server", "Repalis MCP server"),
    ("sign in to polar or repalis-sandbox", "sign in to repalis or repalis-sandbox"),
    ("codex mcp login polar", "codex mcp login repalis"),
    ("connect polar or repalis-sandbox", "connect repalis or repalis-sandbox"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/generate.ts", [
    ("polar config generate", "repalis config generate"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/plan.ts", [
    ("polar config plan", "repalis config plan"),
])
replace_in_file_exact("clients/packages/cli/src/utils/callback-page.ts", [
    ("polar auth login", "repalis auth login"),
    ("polar auth token", "repalis auth token"),
    ("<title>Polar CLI</title>", "<title>Repalis CLI</title>"),
])

# 5. cli services update.test.ts
replace_in_file_exact("clients/packages/cli/src/services/update.test.ts", [
    ("expect(binaryNameFor('darwin')).toBe('polar')", "expect(binaryNameFor('darwin')).toBe('repalis')"),
    ("expect(binaryNameFor('linux')).toBe('polar')", "expect(binaryNameFor('linux')).toBe('repalis')"),
    ("polar-new", "repalis-new"),
    ("binaryPath = join(dir, 'polar')", "binaryPath = join(dir, 'repalis')"),
])

# 6. cli organizations.test.ts
replace_in_file_exact("clients/packages/cli/src/services/organizations.test.ts", [
    ("const environmentOf = () => polar.state.requests.at(-1)!.environment", "const environmentOf = () => repalis.state.requests.at(-1)!.environment"),
    ("const polar = fakeRepalis", "const repalis = fakeRepalis"),
    ("Layer.succeed(Polar,", "Layer.succeed(Repalis,"),
])

print("Completed cleanup batch clients!")
