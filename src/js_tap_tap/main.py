# main.py — JS Tap-Tap (Chip-X)
# Responsibility: Application entry point.
#   - Silence pygame/stdout noise before any imports
#   - Initialise Pygame, create window, fonts, clock
#   - Run the login → game → results state machine loop
#   - Handle top-level silent exception mode (intentional for end-user EXE)
#
# See docs/PROJECT_ARCHITECTURE.md for the full state machine diagram.
# See docs/KNOWN_ISSUES.md for documented rationale on silent exception handling.

import os
import sys
import warnings

# ─── Silence everything before importing pygame ──────────────────────────────
warnings.filterwarnings("ignore")
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"


class _NullWriter:
    """Discards all writes — used to suppress stdout/stderr in the packaged EXE."""
    def write(self, _):
        pass

    def flush(self):
        pass


# Redirect standard streams (intentional for packaged EXE — see KNOWN_ISSUES.md)
sys.stdout = _NullWriter()
sys.stderr = _NullWriter()

# ─── Now safe to import pygame and local modules ──────────────────────────────
import pygame  # noqa: E402

from .screens import login_screen, game_screen, results_screen  # noqa: E402

# ─── Game Configuration ───────────────────────────────────────────────────────
CONFIG = {
    "SCREEN_W": 800,
    "SCREEN_H": 600,
    "BG_COLOR": (30, 30, 40),
    "FPS": 60,
    "GAME_DURATION": 30.0,       # seconds per round
    "TARGET_LIFETIME": 1.0,      # seconds a target stays on screen
    "SPAWN_INTERVAL": 0.6,       # seconds between new target spawns
    "TARGET_MIN_RADIUS": 20,
    "TARGET_MAX_RADIUS": 40,
}


def _init_pygame() -> tuple:
    """Initialise Pygame and return (screen, clock, fonts).

    Returns:
        screen (pygame.Surface): The 800×600 display surface.
        clock  (pygame.time.Clock): Shared frame-rate clock.
        fonts  (dict): "small", "medium", "large" font objects.
    """
    pygame.init()
    pygame.display.set_caption("JS Tap-Tap")
    screen = pygame.display.set_mode((CONFIG["SCREEN_W"], CONFIG["SCREEN_H"]))
    clock = pygame.time.Clock()
    fonts = {
        "small":  pygame.font.SysFont("arial", 20),
        "medium": pygame.font.SysFont("arial", 36),
        "large":  pygame.font.SysFont("arial", 54),
    }
    return screen, clock, fonts


def main() -> None:
    """Run the full application: login → game → results, looping until quit.

    State machine:
        login_screen()  → username
        game_screen()   → score
        results_screen()→ "restart" | "logout"
            restart → back to game_screen (same user)
            logout  → back to login_screen
    """
    screen, clock, fonts = _init_pygame()

    while True:
        # ── Login / Register ─────────────────────────────────────────────────
        user = login_screen(screen, clock, fonts, CONFIG)

        # ── Game loop ────────────────────────────────────────────────────────
        while True:
            score = game_screen(user, screen, clock, fonts, CONFIG)
            action = results_screen(user, score, screen, clock, fonts, CONFIG)
            if action == "restart":
                continue   # same user, play again
            else:          # "logout"
                break      # go back to login


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Fully silent crash mode — intentional for end-user EXE distribution.
        # During development, comment out this try/except to see full tracebacks.
        # See docs/KNOWN_ISSUES.md for the documented rationale.
        pygame.quit()
        sys.exit()
