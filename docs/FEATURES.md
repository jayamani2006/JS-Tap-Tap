# Features — JS Tap-Tap

A complete list of features in the current release (v1.0.0).

---

## Gameplay

- **30-second timed rounds** — each round is exactly 30 seconds, creating urgency.
- **Randomised target spawning** — circles appear at random positions every 0.6 seconds.
- **Target expiry** — each target disappears after 1 second if not clicked, rewarding quick reactions.
- **Variable target sizes** — circles range from 20 to 40 pixel radius, making some harder to hit than others.
- **Vivid colour variety** — each target has a randomly generated bright colour with a white inner circle for visual clarity.
- **Real-time HUD** — score counter, countdown timer, and personal highscore visible throughout gameplay.

---

## Authentication

- **Local user registration** — create an account with a username and password; stored entirely on the local machine.
- **Password masking** — password field renders as `*****` during input.
- **Secure-ish hashing** — passwords stored as SHA-256 with a per-user 16-byte random salt (see [SECURITY.md](../SECURITY.md) and [DISCLAIMER.md](../DISCLAIMER.md) for scope).
- **Multi-user support** — multiple user accounts on the same machine, each with independent highscores.
- **Tab to switch fields** — keyboard-friendly login form navigation.
- **Enter to submit** — submit login without using the mouse.

---

## Highscore Persistence

- **Per-user highscore** — each account's best score is saved automatically at the end of every round.
- **Automatic update** — highscore is updated only when the new score surpasses the previous record.
- **Visible on login screen** — your current highscore is shown while typing your username.
- **Visible during gameplay** — highscore displayed in the HUD as a live reference.
- **Visible on results screen** — final score compared to personal highscore after each round.

---

## Results Screen

- **End-of-round summary** — shows current score and all-time highscore.
- **Three post-round options:**
  - **Restart (R)** — play another round instantly with the same account.
  - **Logout (L)** — return to the login screen to switch users.
  - **Quit (Q)** — exit the application.
- **Keyboard shortcuts** — R, L, Q work alongside button clicks.

---

## Windows Installer

- **One-click installation** — `Install.bat` requires no user input beyond running it.
- **Desktop shortcut** — EXE is copied to the Desktop automatically.
- **Start Menu integration** — a shortcut is created so the game is searchable from Windows.
- **Post-install welcome popup** — a Tkinter window with quick-start instructions opens after installation.

---

## Standalone Executable

- **No Python required for end users** — the EXE is fully self-contained, bundled by PyInstaller.
- **No installation required for portable mode** — the EXE can run from any folder.
- **Embedded icon** — custom Chip-X icon embedded in the EXE and visible in File Explorer / taskbar.

---

## Developer / Build Features

- **Modular source layout** — `src/js_tap_tap/` package with `auth.py`, `ui_widgets.py`, `entities.py`, `screens.py`, `main.py` — each with a single clear responsibility.
- **Reproducible builds** — `packaging/game.spec` and `requirements.txt` with pinned versions.
- **Unit tests** — `tests/test_auth.py` covers authentication logic without requiring a display.
- **CI/CD** — GitHub Actions workflows for lint (flake8) and auto-build on tagged release.
- **`.gitignore`** — prevents build artefacts, binaries, `users.json`, and `.venv` from being committed.
