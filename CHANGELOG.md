# Changelog

All notable changes to JS Tap-Tap are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2026-07-14

### Added
- Core Pygame target-clicking game: 30-second timed rounds, coloured circles.
- Local login and registration system with per-user SHA-256 + salt password hashing.
- Persistent highscore system stored in `users.json` (local file).
- Windows installer (`installer/Install.bat`): copies EXE to Desktop, creates Start Menu shortcut.
- Post-install welcome popup (`installer/welcome.py`) with quick-start guide.
- PyInstaller spec (`packaging/game.spec`) for standalone EXE build.
- Full documentation set: USER_GUIDE, BUILD, PROJECT_ARCHITECTURE, FEATURES, KNOWN_ISSUES, FAQ.
- Community files: LICENSE (MIT), CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, DISCLAIMER.
- GitHub Actions CI: lint workflow (flake8) and build-release workflow (Windows PyInstaller).
- GitHub issue and PR templates.

### Changed
- Source reorganised from single `game.py` into `src/js_tap_tap/` package with modules:
  `auth.py`, `ui_widgets.py`, `entities.py`, `screens.py`, `main.py`.
- Window caption corrected from `"Tap The Targets"` to `"JS Tap-Tap"` for brand consistency.
- `welcome.py` hardcoded absolute path (`E:\Chip-X\...`) replaced with relative path resolution.
- `Install.bat` updated for `installer/` subfolder location.

### Fixed
- `welcome.py` crash on any machine other than original developer's PC (hardcoded path bug).
- `logout` action now correctly returns to login screen instead of restarting the game.

### Removed
- `build/` PyInstaller cache folder (was 21MB of build artefacts, zero source value).
- Duplicate compiled EXEs from repo root and `dist/` (now distributed via GitHub Releases only).
- `xref-game.html`, `*.toc`, `*.pyz`, `warn-game.txt` PyInstaller intermediates.

---

*Unreleased changes will appear above this line as they are merged.*
