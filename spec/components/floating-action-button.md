# Floating action button (`floating-action-button`)

Provenance: `official-md3` (design semantics) + `platform-adaptation` (implementation).

## Purpose

Emphasize a high-priority action for the current screen.

## Variants

- `small`
- `regular`
- `large`
- `extended`

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

Icon-only FABs require an accessible name.

## Adaptive behavior

Use a FAB only for a high-priority action. Reposition it when wider layouts change the information architecture.

## Platform implementation

Check `platforms/<platform>/components.md` and `metadata/support-matrix.yaml`. A same-named native control still requires review of M3 visual roles, states, and semantics.

## Common issues

- Use semantic color roles rather than arbitrary local colors.
- Cover applicable focus, disabled, selected, and error states.
- Review platform-default styling before calling an implementation M3-aligned.
- Keep Expressive-only variants outside this baseline.

## Official source

- https://m3.material.io/components/floating-action-button/overview
