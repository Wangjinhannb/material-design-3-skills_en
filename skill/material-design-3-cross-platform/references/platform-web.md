# Web — HTML / CSS / JavaScript

The repository uses a custom Classic M3 layer. `@material/web` is optional and is not treated as a complete current-M3 dependency because the upstream project is in maintenance mode.

## Implementation

Prefer semantic HTML elements first, then add the minimum ARIA required by the component pattern. Custom components preserve keyboard behavior, focus visibility, form semantics, and disabled/error states.

## Theme and tokens

Map generated CSS custom properties to semantic M3 color, type, shape, state, elevation, and motion roles. Use `prefers-color-scheme` for system theme integration and keep an explicit application override when required. Consume `tokens/generated/web/` outputs through CSS custom properties. Application CSS should reference semantic roles instead of raw palette values.

## Input and accessibility

Support mouse, trackpad, keyboard, touch, and screen-reader interaction. Use `:focus-visible`; do not remove focus outlines without a visible replacement. Use native semantics where possible, ARIA Authoring Practices for custom patterns, WCAG 2.2 checks, keyboard tests, and axe for automated regression coverage.

## Verification

Run syntax checks, unit/interaction tests, Playwright flows, axe accessibility checks, and screenshot regression in the Web workflow.
