#!/usr/bin/env python3
from pathlib import Path
import argparse, urllib.request, yaml
ROOT=Path(__file__).resolve().parents[2]
items=yaml.safe_load((ROOT/"metadata/sources.yaml").read_text(encoding="utf-8"))["sources"]
parser=argparse.ArgumentParser(); parser.add_argument("--network", action="store_true"); args=parser.parse_args()
required={"id","title","organization","url","retrieved_at","category","status","normative_or_informative","license_or_usage_notes","notes"}
errors=[]
ids=set()
for s in items:
    miss=required-set(s)
    if miss: errors.append(f'{s.get("id","?")}: missing {sorted(miss)}')
    if s.get("id") in ids: errors.append(f'duplicate source id: {s.get("id")}')
    ids.add(s.get("id"))
    if args.network:
        try:
            req=urllib.request.Request(s["url"],method="HEAD",headers={"User-Agent":"md3-source-checker/0.1"})
            with urllib.request.urlopen(req,timeout=15) as r:
                if r.status>=400: errors.append(f'{s["id"]}: HTTP {r.status}')
        except Exception as e: errors.append(f'{s["id"]}: network check failed: {e}')
if errors:
    print("\n".join(errors)); raise SystemExit(1)
print(f"Validated {len(items)} source records" + (" with network checks" if args.network else ""))
