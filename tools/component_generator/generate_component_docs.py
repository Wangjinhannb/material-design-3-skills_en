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
    text=f"""# {c['name']} (`{c['id']}`)

Provenance: `official-md3` (design semantics) + `platform-adaptation` (implementation).

## Purpose

{c['purpose']}

## Variants

{variants}

## States

{states}

## Token groups

{groups}

## Interaction

Keep visual state, input behavior, and semantic state synchronized. When a target platform has no direct component equivalent, compose platform primitives while preserving the component purpose and interaction semantics.

## Accessibility

{c['accessibility']}

## Adaptive behavior

{c['adaptive'] or 'Adapt to the current window and input method while preserving readability and operability.'}

## Platform implementation

Check `platforms/<platform>/components.md` and `metadata/support-matrix.yaml`. A same-named native control still requires review of M3 visual roles, states, and semantics.

## Common issues

- Use semantic color roles rather than arbitrary local colors.
- Cover applicable focus, disabled, selected, and error states.
- Review platform-default styling before calling an implementation M3-aligned.
- Keep Expressive-only variants outside this baseline.

## Official source

- {c['official_url']}
"""
    write_md(OUT/f"{c['id']}.md",text)
print(f"Generated {len(data['components'])} component documents")
