---
name: material-design-3-cross-platform
description: Build, audit, refactor, or explain strict Classic Material Design 3 interfaces for Web, Android, HarmonyOS, iOS, Windows, Linux GTK, and Linux Qt. Use when the user requests Material Design 3, M3, Material You UI, cross-platform M3 tokens/components, or an audit of an existing interface for M3, adaptive layout, state coverage, and accessibility. Distinguish Classic M3 from Material 3 Expressive, identify the target platform/framework, load only the relevant references, and never label a platform-default visual system as official Material 3.
---

# Material Design 3 Cross-Platform

## Baseline

1. Apply the repository Classic Material Design 3 baseline.
2. Keep Material Design 1, Material Design 2, and Expressive-only rules out unless the user explicitly changes scope.
3. Current SDKs may contain Expressive APIs. Use only capabilities confirmed to fit the Classic baseline.
4. Do not describe SwiftUI, ArkUI, WinUI, GTK/libadwaita, or Qt defaults as official M3 implementations.
5. Do not invent APIs, versions, components, or execution results. Check current first-party documentation for version-sensitive APIs.

Read `references/source-policy.md` before version-sensitive or normative work.

## Modes

Classify the task as one of:

- **Build** — create a new interface or component.
- **Audit** — inspect an existing interface or project.
- **Refactor** — convert existing UI to Classic M3 while preserving product behavior.
- **Explain** — explain a rule, component, token, or platform mapping.

## Platform routing

- Web / HTML / CSS / JavaScript → `references/platform-web.md`
- Android / Kotlin / Compose → `references/platform-android.md`
- HarmonyOS / ArkTS / ArkUI → `references/platform-harmonyos.md`
- iOS / iPadOS / SwiftUI → `references/platform-ios.md`
- Windows / WinUI 3 / XAML → `references/platform-windows.md`
- Linux / GTK → `references/platform-linux-gtk.md`
- Linux / Qt / QML → `references/platform-linux-qt.md`

Infer the platform from project files when possible. Ask only when platform choice materially changes the implementation and cannot be inferred.

## Core references

For Build, Audit, and Refactor, load:

- `references/core.md`
- `references/components.md`
- `references/accessibility.md`
- the target-platform reference

Load as needed:

- theme/color → `references/color.md`
- type/shape → `references/typography-shape.md`
- interaction/motion → `references/motion-states.md`
- large screens/window changes → `references/adaptive.md`
- Audit/Refactor → `references/audit.md`

## Build

1. Identify the screen purpose, platform, window range, and input methods.
2. Select M3 components before defining container structure.
3. Bind semantic color, type, shape, elevation, motion, and state tokens.
4. Implement applicable hover, focus, pressed, selected, disabled, error, loading, and dragged states.
5. Handle compact/medium/expanded or the platform-equivalent window changes.
6. Handle keyboard, screen reader, text scaling, reduced motion, high contrast, and RTL where applicable.
7. Use native platform APIs for system behavior. Mark repository-owned M3 implementations as adaptations.
8. Run the audit checklist before delivery.

## Audit

Check:

1. Classic baseline and Expressive contamination;
2. semantic color roles and paired foreground roles;
3. typography roles;
4. shape roles;
5. elevation and tonal hierarchy;
6. component choice and variants;
7. interaction-state coverage;
8. navigation and adaptive layout;
9. accessibility and input methods;
10. platform behavior and API validity;
11. hard-coded design values, deprecated APIs, invented APIs, and unsupported conformance claims.

For each finding, include location, rule class, problem, impact, recommended fix, and severity/requirement level.

## Refactor

Preserve business logic and information architecture first. Establish a shared token/theme layer, then replace component styling and state behavior. Avoid blanket corner-radius, color-swap, or shadow-only conversions.

## Explain

Separate:

- confirmed official M3 guidance;
- platform adaptation;
- repository convention;
- unverified/currently ambiguous behavior.

## Output quality

- Follow target-platform code conventions.
- Prefer minimal-intrusion changes in existing projects.
- Claim build/runtime verification only when the check actually ran.
- Do not present approximations as official exact values.
- Load only references relevant to the current platform/task.

## Optional static audit

When the project filesystem is available:

```bash
python scripts/static_audit.py <project-path>
```

The script catches a small set of high-value static risks and does not replace a full M3 audit.
