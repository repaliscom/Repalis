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

# 1. pnpm-lock.yaml
replace_in_file_exact("clients/pnpm-lock.yaml", [
    ("link:../../packages/polar", "link:../../packages/repalis"),
    ("link:../polar", "link:../repalis"),
    ("packages/polar:", "packages/repalis:"),
])

# 2. changelogs
replace_in_file_exact("clients/adapters/nextjs/CHANGELOG.md", [
    ("@polar-sh/adapter-core", "@repalis/adapter-core"),
])
replace_in_file_exact("clients/adapters/nuxt/CHANGELOG.md", [
    ("@polar-sh/adapter-core", "@repalis/adapter-core"),
])

# 3. app google-services.json
replace_in_file_exact("clients/apps/app/google-services.json", [
    ('"project_id": "polar-770de"', '"project_id": "repalis-770de"'),
    ('"storage_bucket": "polar-770de.firebasestorage.app"', '"storage_bucket": "repalis-770de.firebasestorage.app"'),
])

# 4. web downloads
replace_in_file_exact("clients/apps/web/src/app/(main)/(website)/(landing)/downloads/page.tsx", [
    ("https://apps.apple.com/se/app/polar-monetize-your-software/id6746640471", "https://apps.apple.com/se/app/repalis-monetize-your-software/id6746640471"),
    ("https://www.raycast.com/emilwidlund/polar", "https://www.raycast.com/repalis/repalis"),
    ("https://www.framer.com/marketplace/plugins/polar", "https://www.framer.com/marketplace/plugins/repalis"),
])

# 5. cli
replace_in_file_exact("clients/packages/cli/lint/rules/no-hardcoded-hosts.js", [
    ("api.polar.sh", "api.repalis.com"),
])
replace_in_file_exact("clients/packages/cli/scripts/npm-manifest.ts", [
    ("agent at `polar` and", "agent at `repalis` and"),
    (r"%USERPROFILE%\.polar\bin", r"%USERPROFILE%\.repalis\bin"),
])
replace_in_file_exact("clients/packages/cli/src/commands/config/init/index.test.ts", [
    ("@repalis/polar installed", "@repalis/repalis installed"),
])

print("Completed final strip in clients!")
