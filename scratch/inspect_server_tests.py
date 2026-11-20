import subprocess
from collections import defaultdict

proc = subprocess.run(["git", "grep", "-i", "-n", "polar", "server/tests"], capture_output=True, text=True, encoding="utf-8", errors="replace")
lines = proc.stdout.splitlines()
print(f"Total test matches in server: {len(lines)}")

files = defaultdict(list)
for l in lines:
    parts = l.split(":", 2)
    if len(parts) >= 3:
        files[parts[0]].append((parts[1], parts[2].strip()))

for f, items in sorted(files.items()):
    print(f"\n{f} ({len(items)} matches):")
    for lineno, content in items[:5]:
        print(f"  L{lineno}: {content}")
    if len(items) > 5:
        print(f"  ... and {len(items)-5} more")
