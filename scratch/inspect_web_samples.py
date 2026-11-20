import subprocess

def inspect(files):
    for f in files:
        proc = subprocess.run(["git", "grep", "-i", "-n", "polar", f], capture_output=True, text=True, encoding="utf-8")
        print(f"\n--- {f} ---")
        for l in proc.stdout.splitlines():
            print(l)

inspect([
    "clients/apps/demo-app/repalis.ts",
    "clients/apps/web/src/proxy.test.ts",
    "clients/apps/web/src/app/(main)/feedback/question/route.ts",
    "clients/apps/web/src/components/FieldGuide/pages/more.tsx",
])
