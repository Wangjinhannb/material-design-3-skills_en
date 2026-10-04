# Project Status

Status reflects committed code and configured CI checks.

| Area | Status | Notes |
|---|---|---|
| Baseline / provenance | complete | Source inventory, scope, and version policy are defined |
| Core specification | complete-v0.2 | Color, type, shape, elevation, motion, states, layout, iconography |
| Component specification | complete-v0.2 | 31 Classic M3 components |
| Design tokens | complete-v0.2 | Light/dark color, typography, shape, elevation, state, motion |
| Token generators | complete-v0.2 | Web, Android, HarmonyOS, iOS, Windows, GTK, Qt |
| AI Skill | complete-v0.2 | Build, Audit, Refactor, Explain |
| Reference App | implemented | Seven platform project entries |
| Component Catalog | implemented | Seven platforms expose all 31 component IDs |
| Web verification | automated | Build, accessibility, visual regression |
| Android verification | automated | Assemble, lint, tests |
| iOS verification | automated | Xcode build, tests, accessibility audit |
| Windows verification | automated-build | Restore/build; interactive GUI checks need an interactive runner |
| GTK verification | automated | Build, headless smoke test, screenshot artifact |
| Qt verification | automated | Build, headless smoke test, screenshot artifact |
| HarmonyOS verification | static | Runtime verification requires DevEco Studio/HarmonyOS SDK |

Component-level status is tracked in `metadata/support-matrix.yaml`.
