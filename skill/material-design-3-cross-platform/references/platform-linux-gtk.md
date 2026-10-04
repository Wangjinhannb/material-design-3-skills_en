# Linux — GTK 4

GTK and libadwaita provide Linux/GNOME platform behavior. Adwaita styling is separate from Material 3, so the repository applies its own Classic M3 visual layer.

## Implementation

Use GTK widgets for semantics and accessibility, then apply M3 CSS, sizing, state, and component structure. Avoid unnecessary custom drawing.

## Theme and tokens

Map semantic M3 roles into GTK CSS and application resources. Avoid inheriting Adwaita visuals where they conflict with the M3 component specification. Consume generated GTK token outputs or CSS variables/constants derived from them. Keep role names traceable to canonical token IDs.

## Input and accessibility

Support keyboard, mouse, touch where available, focus, selection, and drag behavior through GTK event/controller APIs. Use GtkAccessible roles, states, properties, and relationships. Verify with Orca and keyboard traversal when a runtime environment is available.

## Verification

CI builds GTK targets, runs headless smoke checks, and may collect screenshot artifacts. Manual Orca and desktop-theme checks remain separate.
