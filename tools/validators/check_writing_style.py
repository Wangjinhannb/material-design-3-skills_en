#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[2]
PATTERNS={
    "contrast-formula": re.compile(r"\bnot\s+.{0,55}\bbut\b", re.I),
    "filler": re.compile(r"\b(simply put|in essence|needless to say|it is worth noting|it should be noted|obviously|basically|essentially|ultimately|in other words|for clarity|at the end of the day|keep in mind|remember that|note that)\b", re.I),
    "marketing": re.compile(r"\b(game[- ]changing|revolutionary|seamless experience|ultimate solution|next[- ]level|supercharge|best[- ]in[- ]class|enterprise[- ]grade)\b", re.I),
    "meta-prose": re.compile(r"\b(the purpose of this (document|section|file)|this document is intended to|this section is intended to)\b", re.I),
}
EXCLUDE={ROOT/"docs/writing-style.md"}
issues=[]
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or p in EXCLUDE:
        continue
    text=p.read_text(encoding="utf-8-sig")
    for name,rx in PATTERNS.items():
        for m in rx.finditer(text):
            issues.append((p.relative_to(ROOT).as_posix(),text.count("\n",0,m.start())+1,name,m.group(0)))
if issues:
    for path,line,name,value in issues:
        print(f"{path}:{line}: {name}: {value}")
    sys.exit(1)
print("Writing style check passed")
