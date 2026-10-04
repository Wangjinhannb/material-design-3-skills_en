# Single Source of Truth

Canonical data lives in:

- `metadata/` for source, component, platform, support, and compatibility facts;
- `tokens/source/` for design values;
- `spec/` for normative and explanatory design guidance.

Generated files are replaced by generators rather than edited independently. Platform examples consume generated tokens where practical. AI references summarize canonical rules and stay intentionally smaller than the human documentation.

CI runs determinism checks to catch drift between canonical files and generated outputs.
