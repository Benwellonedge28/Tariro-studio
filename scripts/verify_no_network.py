import ast, sys, os
def check_file(path):
    if not path.endswith(('.py', '.tari')):
        return True
    with open(path) as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            if any(n.name in ["socket", "requests", "urllib"] for n in node.names):
                print(f"FAIL: Network import in {path}")
                sys.exit(1)
    return True
for root, _, files in os.walk(sys.argv[1]):
    for f in files:
        check_file(os.path.join(root, f))
print("PASS: No network imports")