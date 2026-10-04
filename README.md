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
