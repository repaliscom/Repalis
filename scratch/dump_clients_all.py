import subprocess

proc = subprocess.run(['git', 'grep', '-i', '-n', 'polar', 'clients/'], capture_output=True, text=True, encoding='utf-8')
lines = proc.stdout.splitlines()

for l in lines:
    print(l)
