#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, re, sys, yaml, subprocess
ROOT=Path(__file__).resolve().parents[2]
errors=[]

# ASCII paths
for p in ROOT.rglob("*"):
    rel=str(p.relative_to(ROOT))
    try: rel.encode("ascii")
    except UnicodeEncodeError: errors.append(f"non-ASCII path: {rel}")

# Markdown encoding policy
for p in ROOT.rglob("*.md"):
    data=p.read_bytes()
    if p.name=="SKILL.md":
        if data.startswith(b"\xef\xbb\xbf"): errors.append(f"SKILL.md must not have BOM: {p.relative_to(ROOT)}")
        if not data.startswith(b"---\n"): errors.append(f"SKILL.md frontmatter must start at byte 0: {p.relative_to(ROOT)}")
    else:
        if not data.startswith(b"\xef\xbb\xbf"): errors.append(f"markdown missing UTF-8 BOM: {p.relative_to(ROOT)}")
    text=data.decode("utf-8-sig")
    if r"\(" in text or r"\[" in text: errors.append(f"forbidden markdown math delimiter in {p.relative_to(ROOT)}")

# YAML/JSON parse
for p in ROOT.rglob("*.yaml"):
    try: yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception as e: errors.append(f"yaml parse failed {p.relative_to(ROOT)}: {e}")
for p in ROOT.rglob("*.json"):
    try: json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: errors.append(f"json parse failed {p.relative_to(ROOT)}: {e}")

required=[
"README.md","metadata/sources.yaml","metadata/md3-baseline.yaml","metadata/components.yaml","metadata/platforms.yaml","metadata/support-matrix.yaml",
"tokens/source/color-light.tokens.json","tokens/source/color-dark.tokens.json",
"skill/material-design-3-cross-platform/SKILL.md","skill/material-design-3-cross-platform/agents/openai.yaml"
]
for x in required:
    if not (ROOT/x).exists(): errors.append(f"missing required file: {x}")

# Metadata integrity
try:
    src=yaml.safe_load((ROOT/"metadata/sources.yaml").read_text(encoding="utf-8"))["sources"]
    source_ids={x["id"] for x in src}
    comps=yaml.safe_load((ROOT/"metadata/components.yaml").read_text(encoding="utf-8"))["components"]
    if len(comps)<31: errors.append(f"component catalog too small: {len(comps)}")
    ids=[x["id"] for x in comps]
    if len(ids)!=len(set(ids)): errors.append("duplicate component id")
    for c in comps:
        if not c["official_url"].startswith("https://m3.material.io/components/"): errors.append(f"unexpected component source: {c['id']}")
    plats=yaml.safe_load((ROOT/"metadata/platforms.yaml").read_text(encoding="utf-8"))["platforms"]
    for p in plats:
        for sid in p["official_sources"]:
            if sid not in source_ids: errors.append(f"unknown source id {sid} in platform {p['id']}")
    matrix=yaml.safe_load((ROOT/"metadata/support-matrix.yaml").read_text(encoding="utf-8"))["components"]
    if set(matrix)!=set(ids): errors.append("support matrix component ids differ from component catalog")
except Exception as e: errors.append(f"metadata integrity check failed: {e}")

# DTCG color subset
for fn in ["color-light.tokens.json","color-dark.tokens.json"]:
    try:
        data=json.loads((ROOT/"tokens/source"/fn).read_text(encoding="utf-8"))
        if data["color"].get("$type")!="color": errors.append(f"{fn}: color group type missing")
        for k,v in data["color"].items():
            if k.startswith("$"): continue
            value=v.get("$value",{})
            if value.get("colorSpace")!="srgb" or len(value.get("components",[]))!=3: errors.append(f"{fn}:{k}: invalid DTCG color subset")
    except Exception as e: errors.append(f"color token validation failed {fn}: {e}")

# No M2 Compose import in source examples
for p in list((ROOT/"examples").rglob("*.kt"))+list((ROOT/"platforms").rglob("*.kt")):
    txt=p.read_text(encoding="utf-8-sig")
    if re.search(r"import\s+androidx\.compose\.material\.(?!3)",txt): errors.append(f"Material 2 import: {p.relative_to(ROOT)}")

# Generated content existence
for x in ["tokens/generated/web/tokens.css","tokens/generated/android/MaterialTokens.kt","tokens/generated/harmonyos/MaterialTokens.ets","tokens/generated/ios/MaterialTokens.swift","tokens/generated/windows/MaterialTokens.xaml","tokens/generated/linux-gtk/md3-tokens.css","tokens/generated/linux-qt/MaterialTokens.qml","docs/support-matrix.md"]:
    if not (ROOT/x).exists(): errors.append(f"generated file missing: {x}")

if errors:
    print("Repository validation failed:")
    for e in errors: print(" -",e)
    raise SystemExit(1)
print("Repository validation passed")
