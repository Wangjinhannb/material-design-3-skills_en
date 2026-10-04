# Linux Qt Component Catalog

Configure and build with Qt 6 and the required Qt Quick modules installed.

CI performs a build, headless smoke check, and screenshot artifact where supported.

The implementation uses the same token semantics and stable test IDs as the other platform examples.

GitHub Actions installs the Qt Quick runtime modules required by the Material-style QML controls before running the headless smoke test.