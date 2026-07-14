# Installation Guide

This guide covers how to install **JS Tap-Tap** on Windows using the
one-click installer. For building from source, see [docs/BUILD.md](docs/BUILD.md).

---

## Prerequisites

| Requirement | Version | End user needs this? |
|-------------|---------|----------------------|
| Windows | 10 or 11 (64-bit) | ✅ Yes |
| Python | 3.11+ | ⚠️ Only for the welcome popup |
| Pillow | 11.x | ⚠️ Only for the welcome popup |
| Pygame | — | ❌ No (bundled in EXE) |

> **Note:** The game EXE itself is fully standalone — no Python required to play.
> Python + Pillow are only needed if you want the post-install welcome popup
> (`installer/welcome.py`) to display the logo image.
> The popup will still open and function without them; only the logo image is skipped.

---

## Method 1 — One-Click Installer (Recommended)

1. **Download** the latest `JS-Tap-Tap-Setup-vX.Y.Z.zip` from the
   [Releases page](../../releases/latest).

2. **Extract** the ZIP to any folder (e.g. your Desktop or Downloads).

3. **Right-click `Install.bat`** and select **"Run as Administrator"**
   (required to create the Start Menu shortcut).

4. The installer will:
   - Copy `JS Tap-Tap.exe` to your Desktop.
   - Create a **Start Menu** shortcut (search "JS Tap-Tap" in Windows).
   - Open a **welcome guide** popup (requires Python + Pillow — optional).

5. **Double-click** `JS Tap-Tap.exe` on your Desktop to launch the game.

---

## Method 2 — Portable (No Installation)

1. **Download** `JS-Tap-Tap-Portable-vX.Y.Z.exe` from the
   [Releases page](../../releases/latest).

2. **Double-click** the EXE to run the game directly — no installation needed.

3. A `users.json` file will be created in the same folder where the EXE is
   located. This file stores highscores and password hashes. **Keep it safe.**

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Windows protected your PC" SmartScreen warning | Click **More info → Run anyway**. The EXE is unsigned (no code signing certificate) but safe. |
| Welcome popup does not open | Python + Pillow not installed. The game itself still works fine — this is cosmetic only. |
| EXE does not appear on Desktop | Ensure you ran `Install.bat` from the extracted folder (not from inside the ZIP). |
| Game window appears but freezes | Try right-clicking the EXE → Properties → Compatibility → "Run as administrator". |
| "users.json not found" error | This file is created automatically on first run. If it's missing, the game will recreate it. |
| I forgot my password | Currently no password reset — delete your entry from `users.json` and re-register. |

---

## Uninstalling

1. Delete `JS Tap-Tap.exe` from your Desktop.
2. Delete the Start Menu shortcut from
   `%APPDATA%\Microsoft\Windows\Start Menu\Programs\`.
3. Optionally delete `users.json` (removes all accounts and highscores).

---

*For full gameplay instructions, see [docs/USER_GUIDE.md](docs/USER_GUIDE.md).*
