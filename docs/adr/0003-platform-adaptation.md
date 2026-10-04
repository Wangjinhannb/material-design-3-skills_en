# ADR 0003: Platform Adaptation

## Decision

Use native platform primitives for system behavior and accessibility while applying Classic M3 semantic tokens, component anatomy, state behavior, and visual hierarchy through a repository-owned design-system layer when no official M3 implementation exists.

## Consequences

- Android Compose Material 3 is the primary official implementation reference.
- SwiftUI, ArkUI, WinUI, GTK/libadwaita, and Qt defaults are not labeled as official Material 3.
- Platform-native navigation, windowing, text input, safe areas, and accessibility behavior remain intact.
