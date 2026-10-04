# Search (`search`)

Provenance: `official-md3` (design semantics) + `platform-adaptation` (implementation).

## Purpose

Start a search, accept input, and present results.

## Variants

- `bar`
- `view`

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

The input requires an accessible name. Announce meaningful result updates when appropriate.

## Adaptive behavior

Adapt to the current window and input method while preserving readability and operability.

## Platform implementation

Check `platforms/<platform>/components.md` and `metadata/support-matrix.yaml`. A same-named native control still requires review of M3 visual roles, states, and semantics.

## Common issues

- Use semantic color roles rather than arbitrary local colors.
- Cover applicable focus, disabled, selected, and error states.
- Review platform-default styling before calling an implementation M3-aligned.
- Keep Expressive-only variants outside this baseline.

## Official source

- https://m3.material.io/components/search/overview
