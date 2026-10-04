# ADR 0001: Classic Material Design 3 Scope

## Decision

The repository baseline is Classic Material Design 3 with a historical design cutoff of 2024-12-31. Current platform APIs may be used to implement that baseline. Expressive-only design rules do not enter the baseline automatically.

## Consequences

- Current `androidx.compose.material3` APIs require baseline review before use.
- Material 3 Expressive components, motion schemes, or shape systems remain out of scope unless a future baseline explicitly adopts them.
- Ambiguous current documentation is marked unverified.
