#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[2]
PATTERNS={
    'contrast': re.compile(r'\bnot\b[^\n.]{0,70}\bbut\b',re.I),
    'padding': re.compile(r'\b(rather than|instead of|in order to|serves as|acts as|keep in mind|make sure to|note that)\b',re.I),
    'filler': re.compile(r'\b(simply put|in essence|needless to say|it is worth noting|it should be noted|obviously|basically|at its core|in other words)\b',re.I),
    'marketing': re.compile(r'\b(comprehensive|robust|seamless|game[- ]changing|revolutionary|ultimate solution|next[- ]level|supercharge|best[- ]in[- ]class)\b',re.I),
    'meta-intro': re.compile(r'^(this repository|this document|this guide|this section)\b',re.I|re.M),
}
EXCLUDE={ROOT/'docs/writing-style.md'}
issues=[]
long_paragraphs=[]
repeated=Counter()
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts or p in EXCLUDE: continue
    text=p.read_text(encoding='utf-8-sig')
    for name,rx in PATTERNS.items():
        for m in rx.finditer(text):
            issues.append((p.relative_to(ROOT).as_posix(),text.count('\n',0,m.start())+1,name,m.group(0)))
    body=text
    if p.name=='SKILL.md' and body.startswith('---'):
        parts=body.split('---',2)
        if len(parts)==3: body=parts[2]
    body=re.sub(r'```.*?```','',body,flags=re.S)
    for para in re.split(r'\n\s*\n',body):
        s=para.strip()
        if not s or s.startswith(('#','|','- ','* ')) or re.match(r'^\d+\.\s',s): continue
        words=len(re.findall(r"\b[\w'-]+\b",s))
        if words>70:
            line=text.find(para)
            long_paragraphs.append((p.relative_to(ROOT).as_posix(),text.count('\n',0,max(line,0))+1,words))
    for line in text.splitlines():
        s=re.sub(r'^[-*]\s+','',line.strip())
        if len(s)>=90 and not s.startswith(('http','`')):
            repeated[s]+=1
for s,n in repeated.items():
    if n>=10: issues.append(('<repository>',0,'boilerplate',f'{n}x {s[:120]}'))
if issues or long_paragraphs:
    for path,line,name,value in issues: print(f'{path}:{line}: {name}: {value}')
    for path,line,words in long_paragraphs: print(f'{path}:{line}: long-paragraph: {words} words')
    sys.exit(1)
print('Writing style check passed')
