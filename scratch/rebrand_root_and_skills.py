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

# 1. CONTRIBUTING.md
replace_in_file_exact("CONTRIBUTING.md", [
    ("@polar-sh/orbit", "@repalis/orbit"),
    ("@polar-sh/ui", "@repalis/ui"),
])

# 2. README.md
replace_in_file_exact("README.md", [
    ("https://www.producthunt.com/posts/polar-5", "https://www.producthunt.com/posts/repalis"),
    ("utm_souce=badge-polar&#0045;5", "utm_souce=badge-repalis"),
])

# 3. .agents
replace_in_file_exact(".agents/skills/local-environment/rules/service-architecture.md", [
    ("polar123456789", "repalis123456789"),
])
replace_in_file_exact(".agents/skills/local-environment/rules/troubleshooting.md", [
    ("polar123456789", "repalis123456789"),
])
replace_in_file_exact(".agents/skills/verifier-web/SKILL.md", [
    ("polar_cl_", "repalis_cl_"),
])
replace_in_file_exact(".agents/skills/render-env/SKILL.md", [
    ("polar_organization_id", "repalis_organization_id"),
    ("polar_access_token", "repalis_access_token"),
])

print("Completed root and skill replacements!")
