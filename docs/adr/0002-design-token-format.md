# ADR 0002: Design Token Format

## Decision

Color tokens use the stable DTCG 2025.10 core structure where practical. Other token categories use the repository-owned `repo-md3-token-v1` schema until equivalent support is adopted.

## Consequences

- Canonical values live under `tokens/source/`.
- Platform token files are generated.
- Repository-specific tokens are labeled as repository conventions rather than official Material tokens.
