# -*- mode: python ; coding: utf-8 -*-
# packaging/game.spec — JS Tap-Tap (Chip-X)
#
# PyInstaller spec file updated for the new src/ layout.
# Build command (run from repo root):
#
#   pyinstaller packaging/game.spec
#
# Output EXE will be at dist/JS Tap-Tap.exe
# See docs/BUILD.md for full build instructions.

from pathlib import Path

# Repo root is one level above this spec file
REPO_ROOT = Path(SPECPATH).parent  # noqa: F821 — SPECPATH is injected by PyInstaller

a = Analysis(
    [str(REPO_ROOT / "src" / "js_tap_tap" / "main.py")],
    pathex=[str(REPO_ROOT / "src")],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)  # noqa: F821

exe = EXE(  # noqa: F821
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    exclude_binaries=False,
    name="JS Tap-Tap",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(REPO_ROOT / "assets" / "branding" / "icon.ico"),
    onefile=True,
)
