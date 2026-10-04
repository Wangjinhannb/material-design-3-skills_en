# Windows — C# / WinUI 3

WinUI 3 defaults to Fluent. The repository maps Classic M3 semantics through ResourceDictionary, styles, templates, and control behavior.

## Implementation

Style or template WinUI controls to match M3 anatomy and states while retaining UI Automation, keyboard, pointer, touch, and pen behavior.

## Theme and tokens

Define semantic M3 theme resources and use XAML resources/styles rather than per-control literal values. Respect system high contrast where the platform overrides custom styling. Generate XAML resources and C# constants where needed. Treat generated resources as the bridge from canonical tokens to controls.

## Input and accessibility

Support keyboard, mouse, touch, pen, focus visuals, accelerator behavior, and desktop selection patterns. Preserve UI Automation properties, Narrator navigation, visible focus, text scaling, and High Contrast behavior.

## Verification

Hosted CI restores and builds the WinUI projects. Interactive screenshot, Narrator, and High Contrast tests require an interactive Windows runner.
