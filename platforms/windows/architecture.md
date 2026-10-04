# Architecture

C#, XAML, WinUI 3, and Windows App SDK.

WinUI 3 defaults to Fluent. The repository maps Classic M3 semantics through ResourceDictionary, styles, templates, and control behavior.

Platform code consumes generated tokens or an equivalent shared theme entry point. Business logic stays outside the visual mapping layer.
