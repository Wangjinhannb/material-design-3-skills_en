# Architecture

Semantic HTML, CSS custom properties, and JavaScript. Framework adapters may reuse the same token and component layer.

The repository uses a custom Classic M3 layer. `@material/web` is optional and is not treated as a complete current-M3 dependency because the upstream project is in maintenance mode.

Platform code consumes generated tokens or an equivalent shared theme entry point. Business logic stays outside the visual mapping layer.
