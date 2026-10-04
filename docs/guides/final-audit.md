# Final Audit

Run this checklist before a release or major baseline update.

## Baseline

- No Material 1, Material 2, or Expressive-only rule entered the Classic M3 baseline.
- Normative claims have an appropriate source or documented repository rationale.
- Platform adaptations are not labeled as official Material guidance.

## Data and generation

- Component IDs, token IDs, and platform IDs are stable.
- Generated outputs match canonical sources.
- No platform implementation bypasses the shared token layer without a documented reason.

## Components

- All 31 registered components appear in the catalog for each target platform.
- Applicable states, variants, accessibility behavior, and adaptive behavior are documented.

## Verification

- Repository validation passes.
- Platform builds that can run in CI pass.
- Runtime-only checks are marked with their actual verification status.
- Visual baselines are current and reviewed.

## Documentation

- English-facing files contain no Chinese UI or documentation text.
- Documentation uses direct product/engineering language.
- Compatibility dates and known limitations are current.
