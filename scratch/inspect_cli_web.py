import subprocess

def search_dir(d):
    proc = subprocess.run(["git", "grep", "-i", "-n", "polar", d], capture_output=True, text=True, encoding="utf-8", errors="replace")
    return [l for l in proc.stdout.splitlines() if not l.startswith("scratch/")]

print("=== CLI MATCHES ===")
cli_matches = search_dir("clients/packages/cli")
print(f"Total: {len(cli_matches)}")
for l in cli_matches[:25]:
    print(l)

print("\n=== WEB MATCHES ===")
web_matches = search_dir("clients/apps/web")
print(f"Total: {len(web_matches)}")
for l in web_matches[:25]:
    print(l)

print("\n=== MCP MATCHES ===")
mcp_matches = search_dir("clients/apps/mcp")
print(f"Total: {len(mcp_matches)}")
for l in mcp_matches[:15]:
    print(l)
