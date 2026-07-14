# installer/welcome.py — JS Tap-Tap (Chip-X)
# Post-installation welcome popup shown by Install.bat after copying
# the EXE to the Desktop and creating the Start Menu shortcut.
#
# Requirements: Python 3.x + Pillow (pip install pillow)
# Note: This is the only component that requires a Python install on the
# end-user's machine. See docs/KNOWN_ISSUES.md for discussion.
#
# Bug fixed: removed hardcoded absolute path "E:\Chip-X\..." that was
# present in the original welcome.py. Logo is now resolved relative
# to this script's own location, targeting assets/branding/logo.png.

import tkinter as tk
from pathlib import Path

# Attempt to import Pillow — fail gracefully if unavailable
try:
    from PIL import Image, ImageTk
    _PILLOW_AVAILABLE = True
except ImportError:
    _PILLOW_AVAILABLE = False

import subprocess
import os

# ─── Guide content ────────────────────────────────────────────────────────────
guide_text = """
🎯 JS Tap-Tap — Chip-X

Welcome to JS Tap-Tap, a fast-paced target clicking
game by Jayasubramani!

Quick Start:
  1. Double-click JS Tap-Tap.exe on your Desktop.
  2. Register or Login.
  3. Click targets fast! Game lasts 30 seconds.
  4. After each round: Restart, Logout, or Quit.

Highscore:
  • Your best score is saved per user.
  • Scores persist between sessions.

Tips:
  • Quick clicks = higher score!
  • Challenge friends and beat your highscore.
  • Press R to restart, L to logout, Q to quit.

Enjoy your game! ❤️
"""

# ─── Resolve logo path relative to this script ────────────────────────────────
# This script lives at:  <repo_root>/installer/welcome.py
# Logo lives at:         <repo_root>/assets/branding/logo.png
_SCRIPT_DIR = Path(__file__).resolve().parent
_LOGO_PATH = _SCRIPT_DIR.parent / "assets" / "branding" / "logo.png"

# ─── Build UI ─────────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Welcome to JS Tap-Tap")
root.geometry("450x520")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Logo (optional — fails gracefully if Pillow unavailable or file missing)
if _PILLOW_AVAILABLE and _LOGO_PATH.exists():
    try:
        img = Image.open(_LOGO_PATH)
        img = img.resize((80, 80), Image.Resampling.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        logo_lbl = tk.Label(root, image=logo, bg="#1e1e2f")
        logo_lbl.pack(pady=10, side=tk.TOP)
    except Exception:
        pass  # Logo loading is non-critical; silently skip

# Title
title_lbl = tk.Label(
    root,
    text="🎯 JS Tap-Tap",
    font=("Arial", 24, "bold"),
    fg="#f5c518",
    bg="#1e1e2f",
)
title_lbl.pack(pady=5, side=tk.TOP)


def launch_game():
    """Launch the game EXE from the Desktop and close this popup."""
    exe_path = Path(os.path.expanduser("~")) / "Desktop" / "JS Tap-Tap.exe"
    if exe_path.exists():
        subprocess.Popen(str(exe_path))
    root.destroy()


# "Let's Play!" button at the bottom
close_btn = tk.Button(
    root,
    text="Let's Play!",
    command=launch_game,
    font=("Arial", 16, "bold"),
    bg="#f5c518",
    fg="#1e1e2f",
    relief=tk.FLAT,
    padx=10,
    pady=5,
    cursor="hand2",
)
close_btn.pack(pady=15, side=tk.BOTTOM)

# Scrollable text body
frame = tk.Frame(root, bg="#2b2b3c")
frame.pack(expand=True, fill="both", padx=15, pady=10)

text_widget = tk.Text(
    frame,
    wrap="word",
    font=("Arial", 13),
    bg="#2b2b3c",
    fg="white",
    bd=0,
    highlightthickness=0,
)
text_widget.insert("1.0", guide_text)
text_widget.config(state="disabled")
text_widget.pack(expand=True, fill="both", padx=5, pady=5)

root.mainloop()
