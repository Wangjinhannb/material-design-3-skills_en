# English / Chinese Edition Sync

The English and Chinese repositories are separate deployments of the same design system.

## Keep identical

- component IDs;
- token IDs and values;
- schema keys;
- platform IDs;
- support-status enums;
- source IDs and URLs;
- the semantic meaning of the baseline.

## Localize

- README and explanatory documentation;
- Skill instructions;
- component display names;
- validation messages and example UI copy.

## Release flow

1. Compare semantic diffs for machine-readable files.
2. Review localized documentation.
3. Run validators in both repositories.
4. Record the sibling release version in release notes.

Code identifiers, IDs, URLs, and YAML keys stay stable across editions unless the schema itself changes.
