# Badges (`badges`)

Provenance: `official-md3` (design semantics) + `platform-adaptation` (implementation).

## Purpose

Communicate a count or status near an icon or navigation destination.

## Variants

- `small`
- `large`

## States

- `default`

## Token groups

`color`, `typography`, `shape`, `state`

## Interaction

Keep visual state, input behavior, and semantic state synchronized. When a target platform has no direct component equivalent, compose platform primitives while preserving the component purpose and interaction semantics.

## Accessibility

Expose the badge count or status to assistive technology.

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

- https://m3.material.io/components/badges/overview
