# Dependency Policy

Keep runtime and development dependencies small and explicit.

- Prefer platform SDKs and standard libraries before adding third-party UI dependencies.
- Pin CI-sensitive tool versions when reproducibility depends on them.
- Keep lockfiles or wrapper versions where the ecosystem supports them.
- Do not add an unmaintained package when a small repository-owned implementation is sufficient.
- Record the purpose and upstream status of dependencies that materially affect M3 behavior.
- Dependabot may update routine dependencies; baseline-sensitive changes still require review.

A dependency update does not change the Classic M3 baseline by itself.
