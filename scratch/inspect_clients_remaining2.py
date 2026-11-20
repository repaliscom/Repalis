import subprocess
from collections import defaultdict

proc = subprocess.run(["git", "grep", "-i", "-n", "polar", "clients/"], capture_output=True, text=True, encoding="utf-8")
lines = proc.stdout.splitlines()

by_file = defaultdict(list)
for l in lines:
    parts = l.split(":", 2)
    if len(parts) >= 3:
        by_file[parts[0]].append((parts[1], parts[2].strip()))

print(f"Total remaining files in clients: {len(by_file)}")
for f, items in sorted(by_file.items(), key=lambda x: -len(x[1])):
    print(f"\n{f} ({len(items)}):")
    for lineno, content in items[:5]:
        print(f"  L{lineno}: {content}")
    if len(items) > 5:
        print(f"  ... and {len(items)-5} more")
