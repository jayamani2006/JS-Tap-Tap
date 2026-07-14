# Release Notes — JS Tap-Tap

---

## v1.0.0 — 2026-07-14

**First public release of JS Tap-Tap.**

### Download

| Asset | Description |
|-------|-------------|
| `JS-Tap-Tap-Setup-v1.0.0.zip` | Full installer bundle (EXE + Install.bat + welcome.py + icon) |
| `JS-Tap-Tap-Portable-v1.0.0.exe` | Portable standalone EXE — no installer needed |
| `checksums-v1.0.0.txt` | SHA-256 checksums for both assets |

### What's New

**Core Game**
- 30-second timed target-clicking rounds with randomised coloured circles.
- Targets expire after 1 second if not clicked — fast reactions required.
- Score counter and countdown HUD visible during gameplay.

**Authentication**
- Local user registration with per-user random-salt SHA-256 password hashing.
- Persistent highscore saved per user in `users.json`.
- Login / Register on the same screen; Tab to switch fields, Enter to submit.

**Windows Installer**
- `Install.bat` copies EXE to Desktop and creates a Start Menu shortcut.
- Post-install welcome popup with quick-start instructions.

**Source & Build**
- Source reorganised into a clean `src/js_tap_tap/` Python package.
- `packaging/game.spec` for reproducible PyInstaller builds.
- CI: `lint.yml` (flake8 on every PR) + `build-release.yml` (auto-build EXE on tagged release).

### Known Issues at Release

- **Windows only.** No Linux or macOS support (Pygame works cross-platform, but `Install.bat` is Windows-specific).
- **Silent crashes.** The packaged EXE suppresses all exception output. Crashes are silent with no log file. See [docs/KNOWN_ISSUES.md](docs/KNOWN_ISSUES.md).
- **Welcome popup requires Python + Pillow.** The game itself does not — only the post-install popup script.
- **No password reset.** Forgotten passwords require manual deletion of the entry from `users.json`.

### Checksums

> Generate and paste SHA-256 checksums here before publishing the release.

```
# Run in PowerShell:
Get-FileHash JS-Tap-Tap-Setup-v1.0.0.zip   -Algorithm SHA256
Get-FileHash JS-Tap-Tap-Portable-v1.0.0.exe -Algorithm SHA256
```

---

*For a terse version history, see [CHANGELOG.md](CHANGELOG.md).*
