# User Guide — JS Tap-Tap

**Version:** 1.0.0 | **Platform:** Windows 10/11

This guide covers everything you need to play JS Tap-Tap — from creating an
account to understanding the scoring system.

---

## Table of Contents

1. [Starting the Game](#1-starting-the-game)
2. [Registration](#2-registration)
3. [Login](#3-login)
4. [Gameplay](#4-gameplay)
5. [Controls](#5-controls)
6. [Scoring](#6-scoring)
7. [Highscore System](#7-highscore-system)
8. [Results Screen](#8-results-screen)
9. [Troubleshooting](#9-troubleshooting)

---

## 1. Starting the Game

- **Installed:** Double-click **JS Tap-Tap** on your Desktop, or search "JS Tap-Tap" in the Windows Start Menu.
- **Portable:** Double-click the downloaded `JS-Tap-Tap-Portable-vX.Y.Z.exe` directly.

The game opens to the **Login / Register screen**.

---

## 2. Registration

If you are a new player:

1. Click the **Username** field and type your desired username.
2. Press **Tab** to move to the **Password** field (or click it directly).
3. Type your password. It will appear as `*****` for privacy.
4. Click **Register**.
5. A yellow message will confirm: *"Registered."*
6. You can now log in with the same credentials.

> **Tip:** Your username must be unique. If the name is taken, you will see *"Username already exists."*

---

## 3. Login

1. Enter your **Username** and **Password**.
2. Click **Login** or press **Enter**.
3. On success, the game starts immediately.
4. Your current highscore is shown on the login screen beneath the input fields.

---

## 4. Gameplay

After logging in, the 30-second round begins automatically.

**What happens:**
- Coloured circles (**targets**) appear randomly on screen.
- Each target disappears after **1 second** if not clicked.
- Click as many targets as possible before the timer runs out.
- The **HUD** (top bar) shows:
  - Your username (top-left)
  - Current score (left)
  - Time remaining (top-right)
  - Your highscore (right)

**Screenshot: Gameplay**

![Gameplay screenshot](../assets/screenshots/gameplay-01.png)

---

## 5. Controls

| Action | Input |
|--------|-------|
| Click a target | Left mouse button |
| Restart (on results screen) | `R` key or click **Restart** button |
| Logout (on results screen) | `L` key or click **Logout** button |
| Quit the game | `Q` key, click **Quit** button, or close the window |
| Switch input field (login screen) | `Tab` key |
| Submit login | `Enter` key |

---

## 6. Scoring

- Each successfully clicked target = **+1 point**.
- Targets that expire without being clicked score nothing.
- There is no penalty for missed clicks (clicking the background does nothing).
- Score resets to 0 at the start of each new round.

---

## 7. Highscore System

- Your **personal highscore** is saved locally after each round.
- The highscore is updated **only if your new score is higher** than the previous best.
- Highscores are stored in `users.json` in the folder where the EXE runs.
- Each registered user has their own independent highscore.

> **Note:** `users.json` contains your highscore and a salted hash of your password.
> It is a local file — never shared over any network. See [SECURITY.md](../SECURITY.md).

---

## 8. Results Screen

When the 30-second timer reaches zero, the **Results Screen** appears showing:

- **Your Score** — points scored in this round.
- **Your Highscore** — your all-time best.

**Options:**

| Button / Key | Action |
|---|---|
| **Restart (R)** | Play another round immediately (same user) |
| **Logout (L)** | Return to the Login / Register screen |
| **Quit (Q)** | Exit the application |

---

## 9. Troubleshooting

| Issue | Solution |
|-------|----------|
| I forgot my password | Delete your entry from `users.json` with a text editor and re-register. |
| Game won't open | Ensure you're on Windows 10/11. Try right-clicking the EXE → "Run as administrator". |
| Window is too small / too large | The game is fixed at 800×600. Adjust your display scaling if needed. |
| Targets are too fast | This is intentional — reaction speed is the challenge! Try Easy mode (coming in v1.1). |

---

*For installation help, see [INSTALL.md](../INSTALL.md).*  
*For build instructions, see [BUILD.md](BUILD.md).*
