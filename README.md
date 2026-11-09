# GxLx 1.1.5 — Windows build

This repository contains a GitHub Actions workflow that builds the **GxLx 1.1.5** Geode mod for Geometry Dash 2.2081 on Windows x64 (Geode 5.11.2).

## Build

1. Upload exactly one file **GxLx-1.1.5-GitHub-Actions.zip** to the repository root via **Add file → Upload files → Commit changes**. Do not unzip it.
2. GitHub Actions automatically builds the mod (workflow **Build GxLx 1.1.5 Windows**).
3. After the build succeeds, open **Actions → latest successful run → Artifacts → GxLx-1.1.5-Windows**.
4. Extract `gxlx.menu.geode` to `Geometry Dash/geode/mods/` while the game is closed.

## What's new

- 10 menu-key presses within 10 seconds play `10clicks.mp4` over the game until the video ends.
- Press the keys **G X L X** in sequence to enter level **151673976** directly (downloads it if needed).
- Neon red loading bar and `sevvend.mp3` music.
- Reduced menu window sizes and searchable GxLx hack/options names.

**Platform limitation:** The video player is based on Windows Media Foundation and has not been runtime-tested in exclusive fullscreen. This package contains a resized 720p version of the supplied video to keep the archive uploadable via GitHub's web UI.

## Licensing

The modified upstream C++ code remains subject to EPL-2.0 and its original notices. The separate GxLx license applies solely to material originally owned by GxLx.
