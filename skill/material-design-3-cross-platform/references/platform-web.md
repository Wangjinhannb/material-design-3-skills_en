# Web — HTML / CSS / JavaScript

Use semantic HTML, generated CSS tokens, and custom M3 styling. `@material/web` is optional.

## Implementation

Start with native HTML semantics. Add ARIA only for custom patterns. Preserve keyboard behavior, focus visibility, form semantics, and disabled/error states.

## Theme

Bind generated CSS custom properties to semantic M3 roles. Support system theme plus an explicit app override.

## Accessibility

Support keyboard, pointer, touch, and screen readers. Use `:focus-visible`, WCAG 2.2 checks, ARIA APG for custom patterns, and axe regression tests.

## Verification

Run syntax checks, Playwright flows, axe, and screenshot regression.
