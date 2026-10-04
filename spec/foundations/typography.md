# Typography

Provenance: `official-md3` + `repo-convention`.

Use semantic M3 type roles rather than page-local font sizes. The canonical scale is stored in `tokens/source/typography.tokens.json` and mapped to platform units by the token generator.

## Role families

- Display — large expressive page or content titles.
- Headline — high-level section headings.
- Title — component and subsection headings.
- Body — primary reading text.
- Label — controls, navigation, and compact supporting text.

Text scaling and platform accessibility settings take precedence over fixed pixel matching. Do not clip labels or body text to preserve a nominal component height.
