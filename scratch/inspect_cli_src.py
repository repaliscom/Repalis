import subprocess

proc = subprocess.run(["git", "grep", "-i", "-n", "polar", "clients/packages/cli/src"], capture_output=True, text=True, encoding="utf-8", errors="replace")
lines = proc.stdout.splitlines()
print(f"Total src matches in cli: {len(lines)}")
for l in lines[:30]:
    print(l)
