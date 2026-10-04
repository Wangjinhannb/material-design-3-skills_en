# Android — Kotlin / Jetpack Compose

Compose Material 3 is the primary official implementation reference. Current packages also expose Expressive APIs, so repository code stays within the Classic baseline.

## Implementation

Prefer baseline-compatible Material3 composables. Add repository-owned wrappers only when the platform API does not express the required Classic behavior or token mapping.

## Theme and tokens

Use `MaterialTheme` with generated or mapped `ColorScheme`, `Typography`, and `Shapes`. Dynamic color may be enabled where supported, with deterministic fallback. Map repository roles to Compose theme objects and dimension constants. Avoid duplicating semantic values in individual composables.

## Input and accessibility

Support touch, keyboard, mouse/trackpad, stylus, and focus on large-screen/desktop-capable devices. Keep ripple/state behavior aligned with component semantics. Use Compose semantics, content descriptions where needed, meaningful traversal order, touch-target sizing, text scaling, and TalkBack verification.

## Verification

Run Gradle assemble, lint, unit/UI tests, accessibility checks, and emulator screenshots when the configured CI environment supports them.
