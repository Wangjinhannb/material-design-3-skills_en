# Known Limitations

1. Standard GitHub-hosted runners do not provide DevEco Studio or the HarmonyOS SDK. HarmonyOS receives project-structure and ArkTS static checks; runtime verification requires DevEco Studio or a configured self-hosted runner.
2. Windows hosted runners can restore and build WinUI projects, but GUI screenshot, Narrator, and High Contrast automation require an interactive runner.
3. Automated accessibility checks do not replace screen-reader, keyboard, touch, switch-control, or user testing.
4. DTCG 2025.10 structure is used for color tokens. Other token categories currently use the repository-owned `repo-md3-token-v1` schema.
5. Pixel-identical rendering across platforms is not a project goal. Semantic roles, component behavior, accessibility, and visual hierarchy are the comparison targets.
