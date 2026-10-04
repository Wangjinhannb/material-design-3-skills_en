# Layout

Provenance: `official-md3` + `platform-adaptation`.

Layout responds to available window size, text scale, system insets, input method, and content requirements.

- Map compact, medium, and expanded semantics to platform window APIs.
- Reflow desktop content when the window resizes.
- Preserve safe areas and system gesture regions.
- Keep reading order and keyboard order consistent with the visual layout.
- Allow CJK, RTL, long translations, and text scaling to expand content without hidden controls.
