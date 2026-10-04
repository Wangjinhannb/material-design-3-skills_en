#!/usr/bin/env python3
from pathlib import Path
import zipfile, re
ROOT=Path(__file__).resolve().parents[2]
SKILL=ROOT/"skill/material-design-3-cross-platform"
OUT=ROOT/"dist/skill.zip"
text=(SKILL/"SKILL.md").read_text(encoding="utf-8")
if not text.startswith("---\n") or "name: material-design-3-cross-platform" not in text:
    raise SystemExit("Invalid SKILL.md frontmatter")
if (SKILL/"SKILL.md").read_bytes().startswith(b"\xef\xbb\xbf"):
    raise SystemExit("SKILL.md must not contain BOM")
OUT.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(OUT,"w",zipfile.ZIP_DEFLATED) as z:
    for p in sorted(SKILL.rglob("*")):
        if p.is_file(): z.write(p,p.relative_to(SKILL.parent))
print(OUT)
