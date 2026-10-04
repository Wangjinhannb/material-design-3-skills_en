# Contributing

Contributions should preserve the Classic M3 baseline, source provenance, generated-file discipline, and platform verification status.

## Before editing

1. Identify whether the change belongs to `official-md3`, `platform-adaptation`, or `repo-convention`.
2. Add or update a first-party/standards source when a normative rule changes.
3. Edit canonical metadata, token source, or specification files before generated files.
4. Keep paths and code identifiers ASCII.

## Components

A component change normally updates:

- `metadata/components.yaml`;
- `spec/components/` through the component generator;
- `metadata/support-matrix.yaml` when support changes;
- affected platform guidance or examples;
- tests and catalog coverage when behavior changes.

## Tokens

Edit files under `tokens/source/` and regenerate platform outputs. Do not hand-edit generated token files.

## Platform implementations

Record the target OS/framework version, implementation status, and actual verification level. Do not mark an implementation runtime-verified without a successful runtime check.

## Skill

Keep `SKILL.md` compact and route detailed rules through `skill/references/`. Run the Skill validator and package the complete Skill as `skill.zip`.

## Checks

```bash
make check
```

Platform-specific builds are defined under `.github/workflows/`.
