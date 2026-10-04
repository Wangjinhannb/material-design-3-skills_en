# Component Catalog

The catalog covers all 31 components registered in `metadata/components.yaml`.

Platforms:

- `web/`
- `android/`
- `harmonyos/`
- `ios/`
- `windows/`
- `linux-gtk/`
- `linux-qt/`

Every platform source contains stable `component-<id>` markers. `tests/test_catalog_coverage.py` verifies that all 31 IDs are present on all seven platforms.

Visual and interaction behavior follows `spec/components/`, generated tokens, and the relevant platform guide.
