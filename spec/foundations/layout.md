# Layout

Provenance: `official-md3` + `platform-adaptation`.

Layout responds to available window size, text scale, system insets, input method, and content requirements.

- Use compact, medium, and expanded semantics where they are useful; map them to platform window APIs rather than device marketing names.
- Reflow desktop content when a window resizes instead of scaling a fixed mobile canvas.
- Preserve safe areas and system gesture regions.
- Keep reading order and keyboard order consistent with the visual layout.
- Allow CJK, RTL, long translations, and text scaling to expand content without hidden controls.
