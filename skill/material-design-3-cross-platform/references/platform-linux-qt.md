# Linux — Qt 6 / QML

Qt Material Style is a useful reference but is not treated as complete current Classic M3 conformance. The repository applies its own token and component review.

## Implementation

Use Qt Quick Controls when semantics and behavior fit, then style or compose them to meet the repository M3 specification.

## Theme and tokens

Expose M3 semantic roles through a QML singleton/theme object and bind controls to those values. Keep application palettes separate from component semantics. Consume generated QML/theme values. Preserve stable token IDs so visual changes remain traceable to canonical sources.

## Input and accessibility

Support keyboard, mouse, touch, focus, hover, selection, and wheel behavior expected from Qt desktop applications. Expose accessible names, roles, values, states, and focus order through Qt accessibility APIs and test with available Linux assistive technology.

## Verification

CI builds Qt targets, runs headless smoke checks, and may collect screenshot artifacts. Accessibility and platform-theme behavior need runtime review.
