# Color

Provenance: `official-md3` + `repo-convention`.

## Rules

- Use semantic color roles.
- Use paired `on-*` roles for foreground content.
- Use surface-container roles for surface hierarchy.
- Pair error colors with text or another non-color cue.
- Review light and dark schemes separately.

## Role groups

Primary, Secondary, Tertiary, Error, Background/Surface, Outline, Inverse, Fixed, and Surface Container roles are defined in `tokens/source/color-*.tokens.json`.

The bundled purple scheme is test/reference data.

## Dynamic color

Dynamic color MAY be used with a deterministic fallback and intact semantic roles.
