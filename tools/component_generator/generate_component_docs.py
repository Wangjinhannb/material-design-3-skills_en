#!/usr/bin/env python3
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[2]
data=yaml.safe_load((ROOT/"metadata/components.yaml").read_text(encoding="utf-8"))
OUT=ROOT/"spec/components"
OUT.mkdir(parents=True,exist_ok=True)
def write_md(p,s): p.write_text("\ufeff"+s.rstrip()+"\n",encoding="utf-8")
for c in data["components"]:
    variants="\n".join(f"- `{x}`" for x in c["variants"])
    states="\n".join(f"- `{x}`" for x in c["states"])
    groups=", ".join(f"`{x}`" for x in c["required_token_groups"])
    adaptive=(f"\n## Adaptive\n\n{c['adaptive']}\n" if c.get('adaptive') else '')
    text=f"""# {c['name']} (`{c['id']}`)

Provenance: `official-md3` + `platform-adaptation`.

## Purpose

{c['purpose']}

## Variants

{variants}

## States

{states}

## Tokens

{groups}

## Accessibility

{c['accessibility']}
{adaptive}
## Source

- {c['official_url']}
"""
    write_md(OUT/f"{c['id']}.md",text)
print(f"Generated {len(data['components'])} component documents")
