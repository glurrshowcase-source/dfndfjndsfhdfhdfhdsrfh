#!/usr/bin/env python3
"""Rebrand GxLx internals without changing third-party licensing or dependency IDs."""
import json
import shutil
import sys
from pathlib import Path

root = Path(sys.argv[1])
assert (root / "mod.json").exists(), "Mod source folder not found"

files = (
    list((root / "src").rglob("*"))
    + list((root / "include").rglob("*"))
    + list((root / "cmake").rglob("*.cmake"))
    + [root / "CMakeLists.txt"]
)
changed = 0
for f in files:
    if not f.is_file() or f.suffix not in (".cpp", ".hpp", ".h", ".cmake", ".txt"):
        continue
    old = f.read_text(encoding="utf-8-sig")
    new = old
    for a, b in (
        ("namespace eclipse", "namespace gxlx"),
        ("eclipse::", "gxlx::"),
        ("ECLIPSE_", "GXLX_"),
        ("EclipseButtonMLHook", "GxLxButtonMLHook"),
        ("getEclipseUILayer", "getGxLxUILayer"),
        ("Eclipse Recorder Thread", "GxLx Recorder Thread"),
        ("Safe Mode (Eclipse)", "Safe Mode (GxLx)"),
        ("Eclipse Label (*.ecl)", "GxLx Label (*.ecl)"),
        ("EclipseBot", "GxLxBot"),
        ('"eclipse-ui"_spr', '"gxlx-ui"_spr'),
        ('"ECLIPSE-android.png"_spr', '"GXLX-android.png"_spr'),
        ("#include <eclipse.hpp>", "#include <gxlx.hpp>"),
        ("Accessing the Eclipse config file", "Accessing the GxLx config file"),
        ("Add custom modules to Eclipse", "Add custom modules to GxLx"),
        ("variables provided by Eclipse", "variables provided by GxLx"),
    ):
        new = new.replace(a, b)
    if old != new:
        f.write_text(new, encoding="utf-8")
        changed += 1

old_header = root / "include/eclipse.hpp"
if old_header.exists():
    old_header.rename(root / "include/gxlx.hpp")

old_sprite = root / "resources/ECLIPSE-android.png"
if old_sprite.exists():
    shutil.copy2(root / "resources/GxLx/gxlx-logo.png", root / "resources/GXLX-android.png")
    old_sprite.unlink()

meta_path = root / "mod.json"
meta = json.loads(meta_path.read_text(encoding="utf-8-sig"))
meta["version"] = "v1.1.4"
meta["name"] = "GxLx"
meta["developers"] = ["GxLx"]
meta["links"] = {"homepage": "https://www.youtube.com/@DJakDoki"}
meta["description"] = "GxLx — a red-and-black ImGui mod menu for Geometry Dash."
meta["resources"]["sprites"] = [
    name.replace("ECLIPSE-android.png", "GXLX-android.png")
    for name in meta["resources"]["sprites"]
]
for legal_file in ("LICENSE-GXLX-ORIGINAL.md", "README-UPSTREAM.md"):
    if legal_file not in meta["resources"]["files"]:
        meta["resources"]["files"].append(legal_file)
meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

cmake_path = root / "CMakeLists.txt"
cmake = cmake_path.read_text(encoding="utf-8")
cmake = cmake.replace("project(GxLx VERSION 1.1.3 LANGUAGES CXX)",
                      "project(GxLx VERSION 1.1.4 LANGUAGES CXX)")
cmake = cmake.replace("project(GxLx VERSION 1.1.2 LANGUAGES CXX)",
                      "project(GxLx VERSION 1.1.4 LANGUAGES CXX)")
cmake_path.write_text(cmake, encoding="utf-8")

(root / "about.md").write_text("""# GxLx 1.1.4

**GxLx** is a custom, red-and-black mod menu for Geometry Dash on Windows.

## Features

- ImGui interface, animated menu and custom GxLx logo
- Hotkey, visual effects and gameplay utilities
- StartPos Switcher, replay and recording tools where supported

## Developer

**GxLx**

## Channel

[YouTube — @DJakDoki](https://www.youtube.com/@DJakDoki)

## License

Modified upstream source remains available under the **Eclipse Public License 2.0**. Separate, independently authored GxLx material is subject to the **GxLx Original Works License 1.0** where applicable. See bundled legal files and original author notices.
""", encoding="utf-8")
(root / "support.md").write_text("# GxLx Support\n\nDeveloper: GxLx\n\nChannel: https://www.youtube.com/@DJakDoki\n", encoding="utf-8")
(root / "changelog.md").write_text("""# GxLx 1.1.4

- Rebranded internal source-code namespaces and build macros.
- Updated user-facing labels, button logo and Geode metadata.
- Added a separate GxLx original works license.
- Preserved original EPL source licensing, attribution and upstream dependencies.

# GxLx 1.1.3

- Updated description, developer and channel.
""", encoding="utf-8")

license_source = Path(sys.argv[2])
shutil.copy2(license_source, root / "LICENSE-GXLX-ORIGINAL.md")
notice = root / "NOTICE-GXLX.md"
notice.write_text(notice.read_text(encoding="utf-8") +
    "\nGxLx 1.1.4 renames technical namespaces and visible UI branding. "
    "This does not change original authorship, EPL-2.0 coverage or third-party licenses.\n",
    encoding="utf-8")
assert meta["developers"] == ["GxLx"]
assert (root / "include/gxlx.hpp").exists()
assert (root / "resources/GXLX-android.png").exists()
assert "eclipse.ffmpeg-api" in json.dumps(meta)  # keep third-party identity
print("GxLx 1.1.4 rebrand applied:", changed, "implementation files")
