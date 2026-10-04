from pathlib import Path
import re, yaml
root=Path.cwd()

def write_md(rel, body, skill=False):
    p=root/rel
    p.parent.mkdir(parents=True,exist_ok=True)
    body=body.strip()+"\n"
    p.write_text(body if skill else '\ufeff'+body,encoding='utf-8',newline='\n')

write_md('README.md', r'''
# Material Design 3 Cross-Platform

Classic Material Design 3 specs, tokens, platform mappings, component catalogs, reference apps, and an AI Skill.

Version: `0.2.0`  
Baseline: `classic-md3-2024-en`  
Compatibility data checked: `2026-10-03`

## Scope

Core scope is Classic Material Design 3. Material Design 1, Material Design 2, and Material 3 Expressive-only rules are excluded.

Native platform behavior stays native: safe areas, back gestures, text input, window management, accessibility APIs, system navigation, and lifecycle behavior.

## Layout

- `metadata/` — sources, baseline, components, platforms, compatibility, support status.
- `spec/` — foundations, components, adaptive behavior, accessibility.
- `tokens/` — token sources, schemas, generated platform output.
- `skill/` — distributable AI Skill.
- `platforms/` — Web, Android, HarmonyOS, iOS, Windows, GTK, Qt guidance.
- `examples/reference-app/` — seven-platform reference app.
- `examples/component-catalog/` — 31-component catalog for seven platforms.
- `tools/` — generators and validators.
- `tests/` — repository and Skill tests.
- `.github/workflows/` — CI.

## Source of truth

Canonical data lives in `metadata/`, `tokens/source/`, and `spec/`. Generators produce platform tokens, component pages, and support matrices.

```bash
make check
```

## Platforms

| Platform | Stack | M3 layer |
|---|---|---|
| Web | HTML / CSS / JavaScript | Semantic HTML, CSS, tokens, custom components |
| Android | Kotlin / Jetpack Compose | Compose Material 3 filtered to the Classic baseline |
| HarmonyOS | ArkTS / ArkUI | ArkUI primitives + M3 tokens/components |
| iOS | Swift / SwiftUI | SwiftUI primitives + M3 tokens/components |
| Windows | C# / WinUI 3 | ResourceDictionary, styles, control templates |
| Linux GTK | GTK 4 | GTK widgets + CSS/tokens |
| Linux Qt | Qt 6 / QML | Qt Quick Controls + M3 tokens/components |

Verification status: `PROJECT_STATUS.md`, `metadata/support-matrix.yaml`.

## CI

- `validate.yml` — schema, tokens, generated files, Skill, docs, unit tests.
- `web.yml` — Playwright, axe, visual regression.
- `android.yml` — assemble, lint, tests.
- `ios.yml` — Xcode build, tests, accessibility audit.
- `windows.yml` — restore, build.
- `linux-ui.yml` — GTK/Qt build, smoke tests, screenshots.
- `harmonyos.yml` — project structure, ArkTS static checks.
- `source-freshness.yml` — scheduled source checks.

## Editions

English and Chinese editions share component IDs, token semantics, schema keys, platform IDs, and source IDs. See `docs/translation-sync.md`.

## Encoding

Paths are ASCII. Markdown uses UTF-8 with BOM. `SKILL.md` uses UTF-8 without BOM so YAML frontmatter starts at byte zero.

## Attribution

Community project. No affiliation with Google, Huawei, Apple, Microsoft, GNOME, Qt, or W3C. See `metadata/sources.yaml`, `NOTICE.md`, and `docs/guides/licensing.md`.
''')

write_md('CODE_OF_CONDUCT.md', r'''
# Code of Conduct

Be professional. Keep technical discussions evidence-based and reproducible. No harassment or personal attacks.

Report conduct issues privately to the repository owner.
''')

write_md('NOTICE.md', r'''
# Notice

Material Design and Material Symbols are Google projects and trademarks. This community project has no Google endorsement or certification.

Platform names and frameworks belong to their owners. Upstream documentation is linked and paraphrased.

Source and license notes: `metadata/sources.yaml`, `docs/guides/licensing.md`.
''')

write_md('SUPPORT.md', r'''
# Support

Use GitHub Issues for reproducible defects, documentation errors, token-generation problems, and platform build failures.

Include platform, toolchain version, affected path, expected behavior, actual behavior, and a minimal reproduction.

For upstream Material or platform APIs, link first-party documentation.
''')

write_md('SECURITY.md', r'''
# Security Policy

Do not post credentials, tokens, private repository URLs, or user data in public issues.

For dependency or workflow vulnerabilities, include the affected file, version, impact, and a minimal reproduction. Remove active secrets and third-party exploit data.

No runtime user data is intentionally collected.
''')

write_md('GOVERNANCE.md', r'''
# Governance

The repository owner maintains the baseline and release branches.

An ADR is required for baseline scope, token schema, source-of-truth rules, or platform-support policy changes. Normative changes also require source review and a baseline-impact note.
''')

write_md('VERSIONING.md', r'''
# Versioning

Repository-owned interfaces and generated artifacts use semantic versioning.

Each release records:

- Classic M3 baseline ID;
- compatibility check date;
- token schema version;
- platform/toolchain versions;
- Skill package status;
- breaking changes and deprecations.

Upstream documentation changes do not alter the baseline until reviewed and released.
''')

write_md('docs/writing-style.md', r'''
# Writing Style

Use product-documentation prose.

- Put the rule, command, or status first.
- Keep one subject per paragraph.
- Use concrete nouns and testable states.
- Delete setup phrases, sales language, rhetorical contrasts, and self-commentary.
- Keep explanations only when they change implementation or verification.
- Use `implemented`, `build-verified`, `runtime-verified`, and similar status labels precisely.
- Keep generated pages shorter than their canonical metadata and sources.

The style validator rejects recurring filler and long prose paragraphs.
''')

write_md('examples/README.md', r'''
# Examples

`reference-app/` contains the shared app structure for seven platforms.

`component-catalog/` contains the 31 Classic M3 component IDs used by build, accessibility, and visual checks.
''')

write_md('reports/final-audit.md', r'''
# Final Audit

## Repository

- Classic M3 baseline separated from Expressive-only scope.
- Provenance classes: `official-md3`, `platform-adaptation`, `repo-convention`.
- Tokens generated from canonical source files.
- 31 component IDs present in metadata, specs, and seven platform catalogs.
- Seven Reference App and Component Catalog projects present.
- Skill routes by task and platform.
- CI covers repository validation and hosted-runner platform builds.
- Markdown encoding, ASCII paths, and Skill frontmatter validated.

## Platform limits

HarmonyOS runtime checks require DevEco Studio/HarmonyOS SDK. Windows GUI visual and accessibility checks require an interactive Windows runner. Automated accessibility checks do not replace assistive-technology testing.
''')

write_md('reports/test-report.md', r'''
# Test Report

Repository checks cover metadata/schema, component IDs, Classic/Expressive scope, tokens, generators, support matrix, Skill eval cases, catalog coverage, documentation style, and generated-file determinism.

Platform results are recorded by GitHub Actions.
''')

write_md('reports/validation-report.md', r'''
# Validation Report

Run:

```bash
make check
```

Platform builds run in GitHub Actions. HarmonyOS runtime checks require DevEco Studio or a runner with the HarmonyOS SDK.
''')

gen=root/'tools/component_generator/generate_component_docs.py'
gen.write_text(r'''#!/usr/bin/env python3
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
''',encoding='utf-8',newline='\n')

write_md('spec/components/README.md', r'''
# Components

Canonical component data: `metadata/components.yaml`.

Generated pages in this directory contain purpose, variants, states, tokens, accessibility, adaptive rules, and the official source link.

Regenerate after metadata changes:

```bash
python tools/component_generator/generate_component_docs.py
```
''')

platform_edits={
'android/layout.md':'Use WindowSizeClass/adaptive APIs and window insets. Recompose for large screens and foldables; do not scale phone layouts.',
'android/navigation.md':'Choose navigation from destination hierarchy and available window space. Use baseline-compatible Material3 navigation components.',
'harmonyos/navigation.md':'Choose navigation from destination hierarchy and available window space. Keep ArkUI system navigation behavior.',
'ios/layout.md':'Use size classes, layout containers, safe areas, and Dynamic Type. Reflow iPad and resizable-window layouts.',
'ios/navigation.md':'Use `NavigationStack` and native navigation behavior. Map visible structure to M3 bar, rail, or drawer patterns where needed.',
'linux-gtk/navigation.md':'Choose navigation from destination hierarchy and available window space. Keep GTK keyboard and focus behavior.',
'linux-qt/navigation.md':'Choose navigation from destination hierarchy and available window space. Keep Qt keyboard and focus behavior.',
'web/navigation.md':'Choose navigation from destination hierarchy and available viewport space. Preserve browser history, keyboard navigation, and landmarks.',
'web/tokens.md':'Consume `tokens/generated/web/` through CSS custom properties. Application styles reference semantic roles, not raw palette values.',
'windows/layout.md':'Use responsive XAML layout, effective-pixel/DPI scaling, and resize events. Reflow content as the window changes.',
'windows/navigation.md':'Choose navigation from destination hierarchy and available window space. Preserve WinUI keyboard and focus behavior.',
'windows/theming.md':'Define semantic M3 theme resources with XAML resources and styles. Respect system High Contrast overrides.',
}
for rel,body in platform_edits.items():
    write_md('platforms/'+rel, '# '+rel.split('/')[-1].replace('.md','').replace('-',' ').title()+"\n\n"+body)

for platform in ['android','harmonyos','ios','windows','linux-gtk','linux-qt','web']:
    for name in ['accessibility.md','compatibility.md','components.md','interaction.md','testing.md','tokens.md','theming.md']:
        p=root/'platforms'/platform/name
        if not p.exists(): continue
        txt=p.read_text(encoding='utf-8-sig')
        blocks=txt.strip().split('\n\n')
        keep=blocks[:2]
        if name=='testing.md' and len(blocks)>2 and platform in {'harmonyos','windows'}:
            keep=blocks[:3]
        p.write_text('\ufeff'+'\n\n'.join(keep).strip()+'\n',encoding='utf-8',newline='\n')

for platform in ['android','harmonyos','ios','windows','linux-gtk','linux-qt','web']:
    p=root/'platforms'/platform/'architecture.md'
    txt=p.read_text(encoding='utf-8-sig')
    blocks=txt.strip().split('\n\n')
    p.write_text('\ufeff'+'\n\n'.join(blocks[:3]).strip()+'\n',encoding='utf-8',newline='\n')

for platform in ['android','harmonyos','ios','windows','linux-gtk','linux-qt','web']:
    p=root/'platforms'/platform/'README.md'
    txt=p.read_text(encoding='utf-8-sig')
    blocks=txt.strip().split('\n\n')
    if len(blocks)>=3:
        blocks[2]='Status: `metadata/platforms.yaml`, `PROJECT_STATUS.md`.'
    p.write_text('\ufeff'+'\n\n'.join(blocks[:3]).strip()+'\n',encoding='utf-8',newline='\n')

for p in list((root/'examples/reference-app').rglob('README.md'))+list((root/'examples/component-catalog').rglob('README.md')):
    txt=p.read_text(encoding='utf-8-sig')
    txt=txt.replace('\n\nThe implementation uses the same token semantics and stable test IDs as the other platform examples.','')
    p.write_text('\ufeff'+txt.lstrip('\ufeff').strip()+'\n',encoding='utf-8',newline='\n')

repls={
'Report conduct problems privately through the repository owner rather than escalating them in public threads.':'Report conduct problems privately to the repository owner.',
'Platform names and frameworks belong to their respective owners. Upstream documentation is linked and paraphrased rather than reproduced wholesale.':'Platform names and frameworks belong to their owners. Upstream documentation is linked and paraphrased.',
'- Repository-specific tokens are labeled as repository conventions rather than official Material tokens.':'- Repository-specific tokens are labeled `repo-convention`.',
'Generated files are replaced by generators rather than edited independently. Platform examples consume generated tokens where practical. AI references summarize canonical rules and stay intentionally smaller than the human documentation.':'Regenerate generated files after source changes. Platform examples consume generated tokens. AI references stay shorter than the canonical docs.',
'Window-state changes trigger layout recomputation rather than proportional canvas scaling.':'Window-state changes trigger layout recomputation. Fixed-canvas scaling is unsupported.',
'Material Symbols are the preferred Material icon reference. Icon meaning, accessible name, optical size, fill, weight, and grade are chosen intentionally rather than treated as decorative font settings.':'Material Symbols are the preferred icon reference. Set meaning, accessible name, optical size, fill, weight, and grade explicitly.',
'- Use compact, medium, and expanded semantics where they are useful; map them to platform window APIs rather than device marketing names.':'- Map compact, medium, and expanded semantics to platform window APIs.',
'- Reflow desktop content when a window resizes instead of scaling a fixed mobile canvas.':'- Reflow desktop content when the window resizes.',
'Classic M3 uses a discrete shape scale. Components consume semantic shape roles rather than arbitrary local corner radii.':'Classic M3 uses a discrete shape scale. Components consume semantic shape roles.',
'Use semantic M3 type roles rather than page-local font sizes. The canonical scale is stored in `tokens/source/typography.tokens.json` and mapped to platform units by the token generator.':'Use semantic M3 type roles. Canonical values live in `tokens/source/typography.tokens.json`.',
'The validator checks structure and required expectations. Model-level prompt evaluation should compare semantic properties rather than exact prose.':'The validator checks structure and required expectations. Model evals compare semantic properties.',
'Generated output is checked for determinism. Edit token source files rather than generated platform files.':'Generated output is deterministic. Edit `tokens/source/`, then regenerate.',
}
for p in root.rglob('*.md'):
    skill=p.name=='SKILL.md'
    txt=p.read_text(encoding='utf-8-sig')
    body=txt.lstrip('\ufeff')
    for a,b in repls.items(): body=body.replace(a,b)
    p.write_text(body if skill else '\ufeff'+body,encoding='utf-8',newline='\n')

refs={
'adaptive.md':'''# Adaptive Layout\n\nUse window size, input method, insets, and content as layout inputs. Reflow fixed layouts. Preserve reading order, focus order, RTL, text expansion, and safe areas.''',
'core.md':'''# Core Rules\n\n- Use the repository Classic M3 baseline.\n- Use semantic tokens.\n- Preserve component purpose, anatomy, state, and accessibility behavior.\n- Preserve platform-native system behavior.\n- Exclude Expressive-only rules unless requested.\n- Label official guidance, platform adaptation, and repository convention separately.''',
'source-policy.md':'''# Source Policy\n\nUse official Material Design, first-party platform docs, W3C/WAI, and DTCG reports for normative or version-sensitive claims. Record unresolved ambiguity. Keep ambiguous current Material guidance outside the Classic baseline.''',
'typography-shape.md':'''# Typography and Shape\n\nUse semantic M3 type and shape roles. Support platform text scaling and prevent clipping. Exclude Expressive-only shape additions.''',
'platform-ios.md':'''# iOS / iPadOS — Swift / SwiftUI\n\nSwiftUI provides platform behavior and accessibility primitives. Apply Classic M3 tokens and component styling on top.\n\n## Implementation\n\nUse SwiftUI primitives. Keep native gestures, safe areas, text input, VoiceOver, sheets, and navigation.\n\n## Theme\n\nMap generated Swift tokens to semantic colors, type, shapes, and elevation. Support system appearance and Dynamic Type.\n\n## Accessibility\n\nSupport touch, keyboard, pointer, focus, VoiceOver, Dynamic Type, Reduce Motion, and minimum target sizes.\n\n## Verification\n\nRun Xcode build/test and UI accessibility audits. Record Xcode and simulator/device versions.''',
'platform-web.md':'''# Web — HTML / CSS / JavaScript\n\nUse semantic HTML, generated CSS tokens, and custom M3 styling. `@material/web` is optional.\n\n## Implementation\n\nStart with native HTML semantics. Add ARIA only for custom patterns. Preserve keyboard behavior, focus visibility, form semantics, and disabled/error states.\n\n## Theme\n\nBind generated CSS custom properties to semantic M3 roles. Support system theme plus an explicit app override.\n\n## Accessibility\n\nSupport keyboard, pointer, touch, and screen readers. Use `:focus-visible`, WCAG 2.2 checks, ARIA APG for custom patterns, and axe regression tests.\n\n## Verification\n\nRun syntax checks, Playwright flows, axe, and screenshot regression.''',
'platform-windows.md':'''# Windows — C# / WinUI 3\n\nWinUI 3 uses Fluent by default. Apply Classic M3 through resources, styles, templates, and control behavior.\n\n## Implementation\n\nKeep UI Automation, keyboard, pointer, touch, and pen behavior while styling M3 anatomy and states.\n\n## Theme\n\nMap generated tokens to XAML resources and C# constants. Respect system High Contrast.\n\n## Accessibility\n\nPreserve Narrator semantics, focus visuals, text scaling, accelerators, and High Contrast behavior.\n\n## Verification\n\nHosted CI restores and builds. GUI screenshots, Narrator, and High Contrast checks need an interactive Windows runner.''',
'platform-android.md':'''# Android — Kotlin / Jetpack Compose\n\nUse Compose Material 3 APIs that fit the Classic baseline. Filter out Expressive-only APIs.\n\n## Theme\n\nMap tokens to `ColorScheme`, `Typography`, `Shapes`, and dimensions. Dynamic color needs a deterministic fallback.\n\n## Accessibility\n\nSupport touch, keyboard, mouse/trackpad, stylus, focus, Compose semantics, text scaling, touch targets, and TalkBack.\n\n## Verification\n\nRun assemble, lint, tests, accessibility checks, and emulator screenshots when configured.''',
'platform-harmonyos.md':'''# HarmonyOS — ArkTS / ArkUI\n\nUse ArkUI for platform behavior and apply Classic M3 through generated tokens and component mappings.\n\n## Implementation\n\nCompose ArkUI controls into M3 anatomy and states. Verify version-sensitive APIs against the target SDK.\n\n## Accessibility\n\nExpose labels, roles, values, state, focus order, text scaling, and screen-reader semantics through current ArkUI APIs.\n\n## Verification\n\nHosted CI checks project structure and ArkTS. Runtime checks require DevEco Studio/HarmonyOS SDK or a self-hosted runner.''',
'platform-linux-gtk.md':'''# Linux — GTK 4\n\nUse GTK widgets for platform semantics and accessibility. Apply M3 CSS, sizing, states, and component structure.\n\n## Theme\n\nMap generated M3 tokens to GTK CSS and app resources.\n\n## Accessibility\n\nSupport keyboard, pointer, touch where available, focus, selection, drag behavior, and GtkAccessible semantics.\n\n## Verification\n\nCI builds, runs headless smoke checks, and captures screenshots. Orca checks remain manual.''',
'platform-linux-qt.md':'''# Linux — Qt 6 / QML\n\nUse Qt Quick Controls for platform behavior and apply the repository M3 token/component layer.\n\n## Theme\n\nExpose generated tokens through a QML theme object. Keep token IDs traceable to canonical sources.\n\n## Accessibility\n\nSupport keyboard, pointer, touch, focus, hover, selection, wheel input, and Qt accessibility semantics.\n\n## Verification\n\nCI builds, runs headless smoke checks, and captures screenshots. Assistive-technology checks remain manual.''',
}
for name,body in refs.items(): write_md('skill/material-design-3-cross-platform/references/'+name,body)

skill=root/'skill/material-design-3-cross-platform/SKILL.md'
s=skill.read_text(encoding='utf-8')
s=s.replace('Classify the task as one of:\n','Use one mode:\n')
s=s.replace('Infer the platform from project files when possible. Ask only when platform choice materially changes the implementation and cannot be inferred.','Infer the platform from project files. Ask only when it cannot be inferred and changes the implementation.')
s=s.replace('Preserve business logic and information architecture first. Establish a shared token/theme layer, then replace component styling and state behavior. Avoid blanket corner-radius, color-swap, or shadow-only conversions.','Preserve business logic and information architecture. Establish the token/theme layer, then replace component styling and state behavior. Reject corner-radius, color-swap, and shadow-only conversions.')
s=s.replace('The script catches a small set of high-value static risks and does not replace a full M3 audit.','The script checks selected static risks. Run the full audit separately.')
skill.write_text(s,encoding='utf-8',newline='\n')

(root/'tools/validators/check_writing_style.py').write_text(r'''#!/usr/bin/env python3
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
''',encoding='utf-8',newline='\n')

print('cleanup complete')
