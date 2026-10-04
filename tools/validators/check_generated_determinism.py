#!/usr/bin/env python3
from pathlib import Path
import hashlib, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
paths=[ROOT/'tokens/generated', ROOT/'spec/components', ROOT/'docs/support-matrix.md']
def hashes():
    out={}
    for x in paths:
        files=[x] if x.is_file() else sorted(p for p in x.rglob('*') if p.is_file())
        for p in files: out[str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
    return out
before=hashes()
for script in ['tools/token_generator/generate.py','tools/component_generator/generate_component_docs.py','tools/support_matrix/generate.py']:
    subprocess.run([sys.executable,str(ROOT/script)],check=True)
after=hashes()
if before!=after:
    keys=sorted(set(before)|set(after))
    for k in keys:
        if before.get(k)!=after.get(k): print('non-deterministic generated output:',k)
    raise SystemExit(1)
print('Generated outputs are deterministic')
