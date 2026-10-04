# Accessibility Testing

Use automated checks for regressions that tooling can detect and manual checks for behavior that requires real interaction.

## Automated

- Web: axe plus keyboard/focus smoke tests.
- Platform builds: lint/static accessibility diagnostics where the framework provides them.
- Catalog coverage: verify stable component IDs exist on every target platform.

## Manual / runtime

- Screen reader or accessibility service navigation.
- Keyboard and switch traversal.
- Text scaling and dynamic type.
- Reduced motion and high contrast.
- RTL and long-string layouts.
- Touch/pointer target behavior.

Record the exact environment when a platform is marked runtime-verified.
