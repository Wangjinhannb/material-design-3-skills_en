# Architecture

GTK 4 with CSS/resource mapping; libadwaita may be used selectively for platform capabilities.

GTK and libadwaita provide Linux/GNOME platform behavior. Adwaita styling is separate from Material 3, so the repository applies its own Classic M3 visual layer.

Platform code consumes generated tokens or an equivalent shared theme entry point. Business logic stays outside the visual mapping layer.
