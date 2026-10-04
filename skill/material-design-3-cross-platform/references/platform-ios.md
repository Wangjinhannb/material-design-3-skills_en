# iOS / iPadOS — Swift / SwiftUI

SwiftUI supplies Apple platform behavior and accessibility primitives. The repository applies Classic M3 tokens, component styling, and state behavior.

## Implementation

Build M3 components from SwiftUI primitives while preserving native gestures, safe areas, text input, VoiceOver, and system sheet/navigation behavior.

## Theme and tokens

Expose semantic M3 colors, type roles, shapes, and elevation through Swift values/environment or repository theme objects. Respect system appearance and Dynamic Type. Consume generated Swift token values. Keep semantic roles separate from asset/color literals used by platform integration code.

## Input and accessibility

Support touch, hardware keyboard, pointer, focus, and platform gestures. Preserve native dismissal and back/navigation expectations. Use SwiftUI accessibility modifiers, VoiceOver labels/values/traits, Dynamic Type, Reduce Motion, and sufficient target sizes.

## Verification

Run Xcode build/test and UI accessibility audits on macOS. Record simulator/device and Xcode versions for runtime claims.
