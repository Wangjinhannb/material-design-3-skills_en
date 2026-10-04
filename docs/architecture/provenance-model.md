# Provenance Model

Every design rule belongs to one provenance class.

## `official-md3`

Rules directly supported by official Material Design 3 guidance. Use this class for design semantics, component purpose, and Material-specific behavior.

## `platform-adaptation`

Rules required to implement Classic M3 on a target platform. Examples include SwiftUI focus behavior, WinUI resource mapping, and GTK keyboard handling.

## `repo-convention`

Repository-owned engineering choices such as schema shape, generated-file layout, validation rules, naming, and test IDs.

Platform adaptations and repository conventions must not be presented as Google requirements. Source-sensitive claims include a source ID or rationale.
