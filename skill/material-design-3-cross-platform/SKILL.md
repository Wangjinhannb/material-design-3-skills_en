---
name: material-design-3-cross-platform
description: Build, audit, refactor, or explain Classic Material Design 3 interfaces for Web, Android, HarmonyOS, iOS, Windows, Linux GTK, and Linux Qt. Use for M3 UI work, Material You interfaces, cross-platform tokens/components, adaptive layout, state coverage, accessibility review, or migration from an existing UI. Keep Classic M3 separate from Material 3 Expressive, route to the target platform reference, and verify version-sensitive APIs against current first-party documentation.
---

# Material Design 3 Cross-Platform

## Baseline

- Use the project Classic M3 baseline.
- Exclude Material Design 1, Material Design 2, and Expressive-only rules unless scope changes explicitly.
- Do not label SwiftUI, ArkUI, WinUI, GTK/libadwaita, or Qt defaults as official M3 implementations.
- Do not invent APIs, versions, components, or execution results.
- Read `references/source-policy.md` for normative or version-sensitive work.

## Modes

- **Build** — create an interface or component.
- **Audit** — inspect an existing interface or project.
- **Refactor** — move an existing UI to Classic M3 without changing product behavior.
- **Explain** — explain a rule, component, token, or platform mapping.

## Platform reference

- Web → `references/platform-web.md`
- Android / Compose → `references/platform-android.md`
- HarmonyOS / ArkUI → `references/platform-harmonyos.md`
- iOS / SwiftUI → `references/platform-ios.md`
- Windows / WinUI 3 → `references/platform-windows.md`
- Linux / GTK → `references/platform-linux-gtk.md`
- Linux / Qt / QML → `references/platform-linux-qt.md`

Infer the platform from project files. Ask only if the choice changes the implementation and cannot be inferred.

## Core references

For Build, Audit, and Refactor, load:

- `references/core.md`
- `references/components.md`
- `references/accessibility.md`
- the target-platform reference

Load only when relevant:

- color → `references/color.md`
- type/shape → `references/typography-shape.md`
- motion/states → `references/motion-states.md`
- adaptive layout → `references/adaptive.md`
- audit/refactor → `references/audit.md`

## Build

1. Identify screen purpose, platform, window range, and input methods.
2. Select components and bind semantic color, type, shape, elevation, motion, and state tokens.
3. Implement applicable hover, focus, pressed, selected, disabled, error, loading, and dragged states.
4. Handle window changes, keyboard, screen reader, text scaling, reduced motion, high contrast, and RTL as required.
5. Keep system behavior native to the target platform.
6. Run the audit checklist before delivery.

## Audit

Check baseline scope, color roles, typography, shape, elevation, component variants, interaction states, adaptive layout, accessibility, platform behavior, API validity, hard-coded values, deprecated APIs, and unsupported conformance claims.

Report each finding with location, rule class, problem, impact, fix, and severity.

## Refactor

Preserve business logic and information architecture. Establish the token/theme layer first, then replace component styling and state behavior.

## Explain

Separate official M3 guidance, platform adaptation, repository convention, and unverified behavior.

## Verification

Claim build, runtime, accessibility, or visual verification only when that check ran. Use target-platform code conventions and avoid presenting approximations as exact official values.

With project filesystem access:

```bash
python scripts/static_audit.py <project-path>
```

The script covers a limited set of static risks; use the full audit for design review.
