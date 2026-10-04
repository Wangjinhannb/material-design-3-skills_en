# Architecture Overview

The repository is split into five layers:

1. **Evidence** — `metadata/sources.yaml` and compatibility records.
2. **Canonical design data** — `metadata/`, `tokens/source/`, and `spec/`.
3. **Generated outputs** — platform token files, component pages, and support-matrix documentation.
4. **Implementations** — platform guidance and runnable examples.
5. **AI interface** — `skill/`, with a compact `SKILL.md` and platform-specific references.

Generated files never define new design rules. Changes start in canonical data and flow outward through generators and tests.
