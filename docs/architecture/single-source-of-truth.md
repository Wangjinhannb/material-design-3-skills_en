# Single Source of Truth

Canonical data lives in:

- `metadata/` for source, component, platform, support, and compatibility facts;
- `tokens/source/` for design values;
- `spec/` for normative and explanatory design guidance.

Regenerate generated files after source changes. Platform examples consume generated tokens. AI references stay shorter than the canonical docs.

CI runs determinism checks to catch drift between canonical files and generated outputs.
