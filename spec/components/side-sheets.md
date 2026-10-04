# Side sheets (`side-sheets`)

Provenance: `official-md3` (design semantics) + `platform-adaptation` (implementation).

## Purpose

Present supporting content from the side of a wider window.

## Variants

- `standard`
- `modal`

## States

- `default`
- `hovered`
- `focused`
- `pressed`
- `disabled`

## Token groups

`color`, `typography`, `shape`, `state`

## Interaction

Keep visual state, input behavior, and semantic state synchronized. When a target platform has no direct component equivalent, compose platform primitives while preserving the component purpose and interaction semantics.

## Accessibility

Modal side sheets require focus containment and a clear close mechanism.

## Adaptive behavior

Use on layouts with enough width. Prefer another layout on compact windows.

## Platform implementation

Check `platforms/<platform>/components.md` and `metadata/support-matrix.yaml`. A same-named native control still requires review of M3 visual roles, states, and semantics.

## Common issues

- Use semantic color roles rather than arbitrary local colors.
- Cover applicable focus, disabled, selected, and error states.
- Review platform-default styling before calling an implementation M3-aligned.
- Keep Expressive-only variants outside this baseline.

## Official source

- https://m3.material.io/components/side-sheets/overview
