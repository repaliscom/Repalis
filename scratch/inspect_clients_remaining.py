import subprocess
from collections import defaultdict

proc = subprocess.run(["git", "grep", "-i", "-n", "polar", "clients/"], capture_output=True, text=True, encoding="utf-8", errors="replace")
lines = proc.stdout.splitlines()

by_pkg = defaultdict(int)
by_file = defaultdict(int)

for l in lines:
    parts = l.split(":", 2)
    if len(parts) >= 2:
        f = parts[0]
        pkg = "/".join(f.split("/")[:3])
        by_pkg[pkg] += 1
        by_file[f] += 1

print("Matches by clients package:")
for p, c in sorted(by_pkg.items(), key=lambda x: -x[1]):
    print(f"  {p:40}: {c}")

print("\nTop 20 files in clients:")
for f, c in sorted(by_file.items(), key=lambda x: -x[1])[:20]:
    print(f"  {f:60}: {c}")
