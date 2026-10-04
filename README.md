# Material Design 3 Cross-Platform

Classic Material Design 3 references and implementations for Web, Android, HarmonyOS, iOS, Windows, GTK, and Qt.

Version: `0.2.0`  
Baseline: `classic-md3-2024-en`  
Compatibility data checked: `2026-10-03`

## Contents

- `metadata/` — sources, component IDs, platform data, compatibility, and support status.
- `spec/` — foundations, components, adaptive layout, and accessibility.
- `tokens/` — source tokens, schemas, and generated platform outputs.
- `platforms/` — platform-specific implementation notes.
- `examples/reference-app/` — the same reference app on seven platforms.
- `examples/component-catalog/` — 31 Classic M3 components on seven platforms.
- `skill/` — distributable AI Skill.
- `tools/` and `tests/` — generators, validators, and tests.

## Baseline

The core baseline excludes Material Design 1, Material Design 2, and Material 3 Expressive-only rules. Native platform behavior remains native, including navigation, safe areas, text input, window management, lifecycle, and accessibility APIs.

## Source data

Canonical project data lives in `metadata/`, `tokens/source/`, and `spec/`. Generated platform tokens, component pages, and support matrices are checked in CI.

```bash
make check
```

Individual generators and validators are available under `tools/`.

## Platforms

| Platform | Stack | M3 layer |
|---|---|---|
| Web | HTML / CSS / JavaScript | CSS tokens and custom components |
| Android | Kotlin / Jetpack Compose | Compose Material 3 with Classic-baseline filtering |
| HarmonyOS | ArkTS / ArkUI | ArkUI primitives with M3 tokens and components |
| iOS | Swift / SwiftUI | SwiftUI primitives with M3 tokens and components |
| Windows | C# / WinUI 3 | ResourceDictionary, styles, and control templates |
| Linux GTK | GTK 4 | GTK widgets with CSS/token mapping |
| Linux Qt | Qt 6 / QML | Qt Quick Controls with M3 tokens and components |

Implementation and verification status is recorded in `PROJECT_STATUS.md` and `metadata/support-matrix.yaml`.

## CI

- `validate.yml` — repository structure, generated output, Skill, documentation, and unit tests.
- `web.yml` — Playwright and axe.
- `android.yml` — assemble, lint, and tests.
- `ios.yml` — Xcode build, UI tests, and accessibility audit.
- `windows.yml` — restore and build.
- `linux-ui.yml` — GTK/Qt build, smoke tests, and screenshots.
- `harmonyos.yml` — project structure and ArkTS static validation.

## Editions

The English and Chinese editions share machine-readable IDs, token semantics, schema keys, platform IDs, and source IDs. See `docs/translation-sync.md`.

## Encoding

Paths use ASCII. Markdown uses UTF-8 with BOM, except `SKILL.md`, which is UTF-8 without BOM.

## License

See `LICENSE`, `NOTICE.md`, `metadata/sources.yaml`, and `docs/guides/licensing.md`.
