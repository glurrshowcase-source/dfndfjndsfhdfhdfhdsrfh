# GxLx 1.1.7

Windows x64 Geode mod for Geometry Dash 2.2081 (Geode 5.11.2).

## Build via GitHub Actions

1. Upload the single archive **GxLx-1.1.7-GitHub-Actions.zip** to the root of this repository (**Add file → Upload files → Commit changes**). Do not unpack it.
2. Workflow **Build GxLx 1.1.7 Windows** runs when that ZIP is added.
3. After successful build, open **Actions → run → Artifacts → GxLx-1.1.7-Windows**.
4. Unpack `gxlx.menu.geode` into `Geometry Dash/geode/mods/` with the game closed.

## Custom loading cover

- User-supplied `loading_screen.png` fills the loading scene.
- Bar uses a fiery, animated progress indicator derived from the supplied `loading_bar.png`.
- `loading_sound.mp3` is played during loading and stopped at 100% or on scene exit.
- Actual Geometry Dash loading progress drives the bar, not a timer.

All earlier GxLx menu features remain in the source archive.

## Licensing

Original upstream EPL-2.0 and attribution notices remain applicable. The GxLx original works license applies only to GxLx-owned new material.

Source archive compilation and runtime behavior are not verified until the new workflow completes.
