import subprocess
from collections import defaultdict

proc = subprocess.run(["git", "grep", "-i", "-n", "polar", "server"], capture_output=True, text=True, encoding="utf-8", errors="replace")
lines = proc.stdout.splitlines()
print(f"Total server matches: {len(lines)}")

files = defaultdict(list)
for l in lines:
    parts = l.split(":", 2)
    if len(parts) >= 3:
        files[parts[0]].append((parts[1], parts[2]))

print(f"Total server files with matches: {len(files)}")
print("\nTop 25 files in server:")
for f, items in sorted(files.items(), key=lambda x: -len(x[1]))[:25]:
    print(f"  {f:50}: {len(items)}")
