import subprocess
import json
from collections import defaultdict

# Run git grep -i "polar" to find all remaining occurrences
proc = subprocess.run(
    ["git", "grep", "-i", "-n", "polar"],
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace"
)

lines = proc.stdout.splitlines()
print(f"Total matching lines: {len(lines)}")

by_dir = defaultdict(int)
by_file = defaultdict(int)
patterns = defaultdict(int)

for line in lines:
    parts = line.split(":", 2)
    if len(parts) >= 2:
        path = parts[0]
        # Ignore scratch/
        if path.startswith("scratch/"):
            continue
        top_dir = path.split("/")[0] if "/" in path else "root"
        by_dir[top_dir] += 1
        by_file[path] += 1
        
print("\nMatches by top-level directory:")
for d, count in sorted(by_dir.items(), key=lambda x: -x[1]):
    print(f"  {d:20}: {count}")

print("\nTop 30 files with matches:")
for f, count in sorted(by_file.items(), key=lambda x: -x[1])[:30]:
    print(f"  {f:60}: {count}")
