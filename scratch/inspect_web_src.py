import subprocess

proc = subprocess.run(["git", "grep", "-i", "-n", "polar", "clients/apps/web/src"], capture_output=True, text=True, encoding="utf-8")
lines = proc.stdout.splitlines()
print(f"Total web src matches: {len(lines)}")
for l in lines[:40]:
    print(l)
