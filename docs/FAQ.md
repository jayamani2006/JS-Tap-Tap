# FAQ — JS Tap-Tap

Frequently asked questions. If yours isn't here, open a
[GitHub Issue](../../issues/new/choose).

---

## Gameplay Questions

### Q: I clicked a target but didn't get a point — why?

**A:** Targets expire after exactly **1 second**. If your click arrives
a few milliseconds after the target has already been removed from the screen,
the hit is not registered. This is intentional — fast reactions are the
core challenge. Keep practicing!

---

### Q: Can I change the game duration or target speed?

**A:** Not in v1.0.0 — the game is fixed at 30 seconds with current spawn
and lifetime settings. Configurable difficulty modes are planned for v1.1.
See the [Roadmap](../ROADMAP.md).

---

### Q: Can I play on Mac or Linux?

**A:** The compiled EXE is Windows-only. However, the Python source code uses
Pygame, which runs on Linux and macOS. If you have Python 3.11+ and Pygame
installed, you can run the game from source:

```bash
python -m src.js_tap_tap.main
```

Full macOS/Linux support (including installers) is on the [Roadmap](../ROADMAP.md).

---

## Account & Password Questions

### Q: I forgot my password — what do I do?

**A:** There is currently no in-app password reset. To recover:

1. Open `users.json` in a text editor (it's in the same folder as the EXE).
2. Find and delete your username's entry.
3. Save the file.
4. Re-register with the same username (your highscore will be reset to 0).

A proper password reset feature is planned for v1.1.

---

### Q: Will my highscore be erased if I reinstall?

**A:** Highscores are stored in `users.json` in the same folder as the EXE.
If you keep that file when reinstalling, your scores are preserved.
If you delete the EXE and `users.json` together, the scores are lost.
To back up your scores, copy `users.json` somewhere safe before reinstalling.

---

### Q: Is my password safe?

**A:** Within the scope of a local single-player game — yes, reasonably.
Passwords are stored as a salted SHA-256 hash (not plaintext). However, this
is **not** a production-grade security system — see [SECURITY.md](../SECURITY.md)
and [DISCLAIMER.md](../DISCLAIMER.md) for the full picture.

---

## Installation Questions

### Q: Windows says "Windows protected your PC" when I run the EXE — is it safe?

**A:** Yes. This SmartScreen warning appears because the EXE is not signed with
a code-signing certificate (which costs money and is not practical for a hobby
project). Click **"More info" → "Run anyway"** to proceed. The source code is
publicly available in this repository for review.

---

### Q: The game window won't close when I click X.

**A:** Click the X or press **Q** on the results screen / login screen.
During gameplay, closing the window via X should work — if it freezes, press
`Alt+F4` to force-close. This is a known edge case in some Pygame + PyInstaller
configurations.

---

### Q: The welcome popup opened but no logo image appeared.

**A:** The logo in the welcome popup requires Python and the Pillow library.
If they're not installed, the popup still opens and works — only the image
is skipped. The game itself is unaffected. See [INSTALL.md](../INSTALL.md).
