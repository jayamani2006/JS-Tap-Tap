# Known Issues — JS Tap-Tap v1.0.0

This document lists current limitations, intentional design choices that may
look like bugs, and out-of-scope items. Being transparent about these is
intentional — a well-documented limitation is better than a hidden surprise.

---

## 1. Silent Exception Handling (Intentional)

**Description:** When the packaged EXE encounters an unhandled exception,
it exits silently. No crash log, no error message, no traceback is shown to the user.

**Root cause (by design):** `main.py` wraps `main()` in a bare `try/except Exception`
and both `sys.stdout` and `sys.stderr` are redirected to a null writer at startup.

**Why this is intentional:**
- The game is distributed to non-technical users who would be confused or alarmed
  by a Python traceback in a popup window.
- This is a standard pattern for `--noconsole` PyInstaller EXEs.

**Impact:**
- Crashes during gameplay produce no visible feedback to the user.
- During development, the try/except makes debugging harder.

**Workaround for developers:**
Comment out the try/except in `main.py` and the `sys.stdout`/`sys.stderr`
redirects during development. Re-enable them before building the release EXE.

**Status:** Intentional design tradeoff. Will remain as-is for the EXE.
Future consideration: write a crash log to `%APPDATA%\JS Tap-Tap\crash.log`
before exiting, so technical users can diagnose issues.

---

## 2. Local-Only Authentication (By Design)

**Description:** The login system stores credentials in a local `users.json` file.
It is not networked, not synced, and not suitable for multi-user or server-side use.

**Why this is intentional:** JS Tap-Tap is a local single-player game.
A networked auth system would require a backend, TLS, session tokens, and account
management infrastructure that is entirely out of scope for this project.

**Impact:**
- Highscores and accounts are machine-specific — no cross-device sync.
- Anyone with local filesystem access to the machine can inspect `users.json`.
- SHA-256 is used (not bcrypt/Argon2) — acceptable for a local toy game, not for production.

**Status:** Documented in [SECURITY.md](../SECURITY.md) and [DISCLAIMER.md](../DISCLAIMER.md).
Will not be "fixed" — it is correct for the intended scope.

---

## 3. Windows Only

**Description:** JS Tap-Tap is currently Windows 10/11 only.

**Root causes:**
- `Install.bat` and the Start Menu shortcut use Windows-specific paths and PowerShell.
- The EXE is built with PyInstaller on Windows for Windows.

**Impact:** Linux and macOS users cannot run the installed version.
The Pygame source code itself is cross-platform and would run on other OSes
with Python + Pygame installed.

**Status:** Out of scope for v1.0.0. Linux/macOS support is on the [Roadmap](../ROADMAP.md).

---

## 4. Welcome Popup Requires Python + Pillow

**Description:** `installer/welcome.py` is a Tkinter script that requires a
system Python installation and the Pillow library. The game EXE itself does NOT
require Python — only this post-install popup does.

**Impact:** On machines without Python + Pillow, the welcome popup will either
fail silently or not display the logo image. The game still runs fine.

**Workaround:** Skip the welcome popup — run `JS Tap-Tap.exe` directly from the Desktop.

**Status:** Documented in [INSTALL.md](../INSTALL.md). A future version may rewrite
the welcome popup as a secondary Pygame window bundled into the EXE, eliminating
the Python dependency.

---

## 5. No Password Reset

**Description:** There is no in-app password reset mechanism.

**Impact:** If a user forgets their password, they must manually delete their entry
from `users.json` using a text editor, then re-register.

**Status:** Known limitation. Password reset is planned for v1.1 (see [ROADMAP.md](../ROADMAP.md)).

---

## 6. users.json Location Depends on Working Directory

**Description:** `users.json` is written to the **current working directory**
when the game runs, not a fixed data folder like `%APPDATA%`.

**Impact:** If the EXE is launched from different folders (e.g. Desktop vs Downloads),
each location will have its own `users.json` with separate accounts.

**Workaround:** Always launch from the Desktop shortcut (which sets the working
directory correctly) or ensure the portable EXE is always in the same folder.

**Status:** Low-priority. Future fix: resolve to `%APPDATA%\JS Tap-Tap\users.json`
for a consistent, user-specific data location.
