#!/usr/bin/env python3
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[2]
d=yaml.safe_load((ROOT/'tests/skill/eval-cases.yaml').read_text(encoding='utf-8'))
cases=d.get('cases',[]); errors=[]
required={'id','mode','prompt','expected_platform','required_refs','forbidden'}
for c in cases:
    miss=required-set(c)
    if miss: errors.append(f"{c.get('id','?')}: missing {sorted(miss)}")
ids=[c.get('id') for c in cases]
if len(ids)!=len(set(ids)): errors.append('duplicate eval case id')
modes={c.get('mode') for c in cases}
for m in {'Build','Audit','Explain'}:
    if m not in modes: errors.append(f'missing mode coverage: {m}')
plats={c.get('expected_platform') for c in cases}
for p in {'web','android','harmonyos','ios','windows'}:
    if p not in plats: errors.append(f'missing platform eval: {p}')
if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print(f'Validated {len(cases)} skill eval cases')
