#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[2]
rx=re.compile(r'[\u3400-\u9fff]')
allowed={ROOT/'docs/translation-sync.md'}
issues=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.parts or p in allowed: continue
    try: text=p.read_text(encoding='utf-8-sig')
    except (UnicodeDecodeError,OSError): continue
    if rx.search(text):
        for i,line in enumerate(text.splitlines(),1):
            if rx.search(line): issues.append((p.relative_to(ROOT).as_posix(),i,line.strip()[:160]))
if issues:
    for path,line,value in issues[:200]: print(f'{path}:{line}: CJK text: {value}')
    if len(issues)>200: print(f'... and {len(issues)-200} more')
    sys.exit(1)
print('English-only check passed')
