# Color

Provenance: `official-md3` + `repo-convention`.

## Rules

- UI uses semantic color roles. Brand values stay in the theme/token layer.
- Foreground content uses the paired `on-*` role for its container.
- Surface hierarchy uses surface-container roles and tonal hierarchy; shadow is added only where the component/elevation model calls for it.
- Error roles communicate error semantics, with text or another non-color cue when the state matters.
- Light and dark schemes are reviewed independently for readability and state visibility.

## Role groups

Primary, Secondary, Tertiary, Error, Background/Surface, Outline, Inverse, Fixed, and Surface Container roles are registered in `tokens/source/color-*.tokens.json`.

The repository ships a purple reference scheme for examples and generator tests. Product themes may use another seed or brand palette while preserving role semantics.

## Dynamic color

Dynamic color MAY be used on platforms that support it when role semantics, light/dark readability, brand requirements, state meaning, and deterministic fallback remain intact.
