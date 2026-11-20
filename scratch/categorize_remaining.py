import subprocess
from collections import defaultdict

proc = subprocess.run(
    ["git", "grep", "-i", "-n", "polar"],
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace"
)

lines = proc.stdout.splitlines()

categories = defaultdict(list)

for line in lines:
    parts = line.split(":", 2)
    if len(parts) < 3:
        continue
    path, lineno, content = parts[0], parts[1], parts[2]
    if path.startswith("scratch/"):
        continue
    
    # Check categorization
    content_lower = content.lower()
    
    if "polars" in content_lower and not "polarsource" in content_lower:
        # Check if it's the polars python/rust library
        categories["polars_lib"].append((path, lineno, content))
    elif "polar_" in content_lower or "polar-" in content_lower:
        if "env" in path or "docker" in path or "terraform" in path or "config" in path:
            categories["env_vars_and_infra"].append((path, lineno, content))
        else:
            categories["prefixed_identifiers"].append((path, lineno, content))
    elif "polarnight" in content_lower or "polarblue" in content_lower or "polar," in content_lower:
        categories["orbit_or_theme"].append((path, lineno, content))
    elif "test" in path:
        categories["tests_and_mocks"].append((path, lineno, content))
    elif path.endswith(".md") or path.endswith(".txt") or "docs" in path:
        categories["docs_and_markdown"].append((path, lineno, content))
    else:
        categories["other_code"].append((path, lineno, content))

print("Breakdown of 1911 matches:")
for cat, items in categories.items():
    print(f"  {cat:25}: {len(items)}")

print("\n--- SAMPLE FROM other_code (first 30) ---")
for p, l, c in categories["other_code"][:30]:
    print(f"{p}:{l} -> {c.strip()}")
