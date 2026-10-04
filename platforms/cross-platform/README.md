# Cross-Platform Frameworks

Flutter, React Native, Compose Multiplatform, Electron, Tauri, and .NET MAUI are adapter targets, not canonical design sources for the project.

An adapter reuses the same component IDs and token semantics, documents framework-specific behavior, and reports its own verification level. Cross-platform abstractions must not erase native accessibility, windowing, text input, navigation, or lifecycle requirements.
