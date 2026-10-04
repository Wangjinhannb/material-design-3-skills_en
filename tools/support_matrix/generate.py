#!/usr/bin/env python3
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[2]
components=yaml.safe_load((ROOT/"metadata/components.yaml").read_text(encoding="utf-8"))["components"]
plats=yaml.safe_load((ROOT/"metadata/platforms.yaml").read_text(encoding="utf-8"))["platforms"]
matrix=yaml.safe_load((ROOT/"metadata/support-matrix.yaml").read_text(encoding="utf-8"))["components"]
header="| Component | "+" | ".join(p["id"] for p in plats)+" |\n|---|"+"|".join(["---"]*len(plats))+"|\n"
rows=[]
for c in components:
    cells=[]
    for p in plats:
        v=matrix[c["id"]][p["id"]]
        cells.append(f"{v['framework_relation']} / {v['repo_status']}")
    rows.append("| `"+c["id"]+"` | "+" | ".join(cells)+" |")
text="# Support Matrix\n\nGenerated from metadata. Cell format: `framework_relation / repo_status`.\n\n"+header+"\n".join(rows)+"\n"
(ROOT/"docs/support-matrix.md").write_text("\ufeff"+text,encoding="utf-8")
print("Generated support matrix")
