# ADR 0004: Skill as Control Plane

## Decision

`SKILL.md` stays compact and routes work to focused reference files. Human documentation remains under `docs/`, `spec/`, and `platforms/`.

## Consequences

- The Skill loads only the platform and design references needed for the current task.
- Detailed documentation is not duplicated into `SKILL.md`.
- Skill packaging stays below the platform size limit and remains independently testable.
