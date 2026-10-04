# HarmonyOS — ArkTS / ArkUI

ArkUI supplies platform primitives and system behavior. The repository supplies the Classic M3 visual, token, and component mapping layer.

## Implementation

Compose ArkUI controls into M3 component anatomy and states. Verify APIs against the target DevEco Studio/HarmonyOS SDK before relying on version-sensitive behavior.

## Theme and tokens

Expose M3 semantic roles through ArkTS theme/resource constants and map them to ArkUI properties. Keep resource lookup centralized. Consume generated HarmonyOS token outputs or equivalent resource mappings. Keep code identifiers aligned with repository token IDs.

## Input and accessibility

Support touch, keyboard, mouse, and accessibility interaction on devices that expose them. Keep focus state visible on desktop-style form factors. Expose labels, roles, values, state, focus order, text scaling, and screen-reader semantics through current ArkUI accessibility APIs.

## Verification

The repository performs project-structure and ArkTS static checks on hosted CI. Runtime verification requires DevEco Studio/HarmonyOS SDK or a self-hosted runner.
