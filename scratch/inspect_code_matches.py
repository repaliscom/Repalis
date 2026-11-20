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

files_and_lines = defaultdict(list)
for line in lines:
    parts = line.split(":", 2)
    if len(parts) < 3:
        continue
    path, lineno, content = parts[0], parts[1], parts[2]
    if path.startswith("scratch/"):
        continue
    files_and_lines[path].append((lineno, content.strip()))

# Print all non-test, non-terraform, non-env files
print("=== NON-TERRAFORM, NON-ENV, NON-DOCKER FILES WITH POLAR ===")
count = 0
for path in sorted(files_and_lines.keys()):
    if any(k in path for k in ["terraform", ".env", "docker", "scratch"]):
        continue
    print(f"\n--- {path} ({len(files_and_lines[path])} matches) ---")
    for l, c in files_and_lines[path][:10]:
        print(f"  L{l}: {c}")
    if len(files_and_lines[path]) > 10:
        print(f"  ... and {len(files_and_lines[path]) - 10} more")
    count += 1

print(f"\nTotal such files: {count}")
