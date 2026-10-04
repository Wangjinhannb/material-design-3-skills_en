# Platform Adaptation Policy

Classic M3 supplies design semantics. Target platforms supply system behavior and accessibility primitives.

Use official M3 components where a current, baseline-compatible implementation exists. Otherwise compose native primitives and apply repository tokens, component anatomy, state behavior, motion, and accessibility mappings.

Do not label SwiftUI, ArkUI, WinUI, GTK/libadwaita, or Qt defaults as official Material 3. Preserve native safe areas, navigation gestures, text input, windowing, lifecycle, and accessibility APIs.

Platform deviations are documented as `platform-adaptation` and include a reason when they affect visible behavior.
