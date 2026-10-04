# Material Design 3 Cross-Platform

A cross-platform Classic Material Design 3 engineering repository with specifications, design tokens, component guidance, an AI Skill, reference applications, and automated checks.

Current version: `0.2.0`  
Baseline: `classic-md3-2024-en`  
Compatibility data checked: `2026-10-03`

## Scope

This repository targets Classic Material Design 3. Material Design 1, Material Design 2, and Material 3 Expressive-only rules are outside the core baseline.

Native platform behavior remains native: safe areas, back gestures, text input, window management, accessibility APIs, system navigation, and lifecycle behavior.

## Repository layout

- `metadata/` — sources, baseline, components, platforms, compatibility data, and support status.
- `spec/` — Classic M3 foundations, components, adaptive behavior, and accessibility guidance.
- `tokens/` — machine-readable design-token sources, schemas, and generated platform outputs.
- `skill/` — distributable AI Skill for building, auditing, refactoring, and explaining Classic M3 interfaces.
- `platforms/` — implementation guidance for Web, Android, HarmonyOS, iOS, Windows, GTK, and Qt.
- `examples/reference-app/` — the same reference application structure across seven platforms.
- `examples/component-catalog/` — a 31-component catalog across seven platforms.
- `tools/` — token generation, component generation, source checks, repository validation, and Skill packaging.
- `tests/` — metadata, token, Skill, catalog, and generated-output tests.
- `.github/workflows/` — repository validation and platform build workflows.

## Source of truth

`metadata/`, `tokens/source/`, and `spec/` contain canonical project data. Generators produce platform token outputs, component pages, and support matrices. `skill/references/` contains concise AI-facing rules derived from the same baseline.

```bash
python tools/token_generator/generate.py
python tools/component_generator/generate_component_docs.py
python tools/support_matrix/generate.py
python tools/validators/validate_repo.py
python tools/validators/check_writing_style.py
python -m unittest discover -s tests -p 'test_*.py'
```

Or run:

```bash
make check
```

## Platforms

| Platform | Primary stack | M3 implementation |
|---|---|---|
| Web | HTML / CSS / JavaScript | Semantic HTML, CSS, tokens, and custom components |
| Android | Kotlin / Jetpack Compose | Compose Material 3 with Classic-baseline filtering |
| HarmonyOS | ArkTS / ArkUI | ArkUI primitives with an M3 token/component layer |
| iOS | Swift / SwiftUI | SwiftUI primitives with an M3 token/component layer |
| Windows | C# / WinUI 3 | ResourceDictionary, styles, and control templates |
| Linux GTK | GTK 4 | GTK widgets with CSS/token mapping |
| Linux Qt | Qt 6 / QML | Qt Quick Controls with an M3 token/component layer |

See `PROJECT_STATUS.md` and `metadata/support-matrix.yaml` for implementation and verification status.

## Reference app and component catalog

`examples/reference-app/` uses the same information architecture on every platform: overview, list, form, and settings.

`examples/component-catalog/` covers the 31 Classic M3 component IDs registered in `metadata/components.yaml`. Stable `component-<id>` markers are checked automatically.

## CI

- `validate.yml` — schema, tokens, generated output, Skill, documentation style, and unit tests.
- `web.yml` — functional tests, axe accessibility checks, and Playwright visual regression.
- `android.yml` — assemble, lint, and tests.
- `ios.yml` — Xcode build, tests, and accessibility audit.
- `windows.yml` — Windows App SDK restore and build.
- `linux-ui.yml` — GTK and Qt build, headless smoke tests, and screenshot artifacts.
- `harmonyos.yml` — HarmonyOS project structure and ArkTS static validation.
- `source-freshness.yml` — scheduled source-link checks.

## English and Chinese editions

The English and Chinese repositories share the same machine-readable component IDs, token semantics, schema keys, platform IDs, and source IDs. Human-facing documentation is localized independently.

See `docs/translation-sync.md`.

## Encoding and paths

All file names, directory names, and ZIP entries use ASCII. Markdown files use UTF-8 with BOM, except `SKILL.md`, which uses UTF-8 without BOM so YAML frontmatter starts at byte zero.

## Attribution

This is a community project and is not affiliated with Google, Huawei, Apple, Microsoft, GNOME, Qt, or W3C. Source and license notes are listed in `metadata/sources.yaml`, `NOTICE.md`, and `docs/guides/licensing.md`.
