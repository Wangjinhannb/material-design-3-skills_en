# Research Summary

The baseline and compatibility files use first-party documentation and standards sources recorded in `metadata/sources.yaml`.

Key findings used by the repository:

- Android Compose Material 3 is the strongest official implementation reference for M3 components, but current packages also include Material 3 Expressive APIs.
- `@material/web` remains an M3 implementation reference and is in maintenance mode, so the repository does not require it as the Web foundation.
- HarmonyOS ArkUI, SwiftUI, WinUI 3, GTK/libadwaita, and Qt provide platform UI primitives or styling systems; the repository supplies a separate Classic M3 mapping layer.
- DTCG 2025.10 provides the stable Community Group design-token format used for the repository color-token structure.
- WCAG 2.2 and WAI-ARIA Authoring Practices provide Web accessibility requirements and interaction references.

Source status, retrieval date, and usage notes are kept in machine-readable metadata so a documentation update can be reviewed without silently changing the baseline.
