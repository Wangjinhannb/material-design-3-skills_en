#!/usr/bin/env python3
from pathlib import Path
import re, sys
patterns={
    "material2_import": re.compile(r"androidx\.compose\.material\.(?!3)"),
    "hardcoded_hex": re.compile(r"#[0-9a-fA-F]{6,8}"),
    "expressive_term": re.compile(r"Material\s*3\s*Expressive|M3\s*Expressive", re.I),
}
paths=[Path(x) for x in sys.argv[1:]]
if not paths:
    print("usage: static_audit.py <file-or-dir> [...]"); raise SystemExit(2)
findings=[]
for root in paths:
    files=[root] if root.is_file() else [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".kt",".kts",".ets",".swift",".cs",".xaml",".qml",".js",".ts",".css",".html"}]
    for p in files:
        try: text=p.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError: continue
        for name,rx in patterns.items():
            for m in rx.finditer(text):
                findings.append((str(p),name,text.count("\n",0,m.start())+1,m.group(0)))
for f in findings: print(f"{f[0]}:{f[2]}: {f[1]}: {f[3]}")
# Hex values are informational because generated token files legitimately contain them.
blocking=[f for f in findings if f[1] in {"material2_import","expressive_term"}]
raise SystemExit(1 if blocking else 0)
