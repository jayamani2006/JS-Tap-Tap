# screens.py — JS Tap-Tap (Chip-X)
# Responsibility: All three game screens (login, game, results).
# Each screen function runs its own event loop and returns a value
# that drives the state machine in main.py.
#
# State machine:
#   login_screen()  → returns username (str) on successful login/register
#   game_screen()   → returns score (int) when the 30-second round ends
#   results_screen()→ returns "restart" | "logout" to continue the main loop

import sys
import time
import random

import pygame

from .auth import (
    verify_user,
    create_user,
    get_highscore,
    update_highscore,
)
from .entities import Target
from .ui_widgets import TextInput, Button


# ─── Screen: Login / Register ────────────────────────────────────────────────

def login_screen(
    screen: pygame.Surface,
    clock: pygame.time.Clock,
    fonts: dict,
    config: dict,
) -> str:
    """Display the login / register screen and block until a user logs in.

    Args:
        screen:  The main Pygame display surface.
        clock:   The shared Pygame clock (used for delta-time and cursor blink).
        fonts:   Dict with keys "small", "medium", "large" → pygame.font.Font.
        config:  Game constants dict (SCREEN_W, SCREEN_H, BG_COLOR, FPS).

    Returns:
        The authenticated username string.
    """
    W, H = config["SCREEN_W"], config["SCREEN_H"]
    FPS = config["FPS"]
    BG = config["BG_COLOR"]
    font_sm = fonts["small"]
    font_lg = fonts["large"]

    username_input = TextInput(
        (W // 2 - 160, 160, 320, 40),
        placeholder="Username",
        font=font_sm,
        clock=clock,
    )
    password_input = TextInput(
        (W // 2 - 160, 220, 320, 40),
        placeholder="Password",
        password=True,
        font=font_sm,
        clock=clock,
    )
    login_btn = Button((W // 2 - 160, 280, 150, 44), "Login", font=font_sm)
    reg_btn = Button((W // 2 + 10, 280, 150, 44), "Register", font=font_sm)

    info_msg = ""
    msg_timer = 0.0
    active_box_index = 0  # 0 = username, 1 = password

    while True:
        dt = clock.tick(FPS) / 1000.0

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            res = username_input.handle_event(e)
            res2 = password_input.handle_event(e)

            # Tab cycles focus between the two input boxes
            if res == "tab" or res2 == "tab":
                active_box_index = (active_box_index + 1) % 2
                username_input.active = active_box_index == 0
                password_input.active = active_box_index == 1

            if e.type == pygame.MOUSEBUTTONDOWN:
                u = username_input.get_value()
                p = password_input.get_value()
                if login_btn.clicked(e.pos):
                    if not u or not p:
                        info_msg = "Enter username and password."
                        msg_timer = 2.0
                    else:
                        ok, msg = verify_user(u, p)
                        info_msg = msg
                        msg_timer = 2.0
                        if ok:
                            return u
                if reg_btn.clicked(e.pos):
                    if not u or not p:
                        info_msg = "Enter username and password to register."
                        msg_timer = 2.0
                    else:
                        ok, msg = create_user(u, p)
                        info_msg = msg
                        msg_timer = 2.0

            # Enter key submits login
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                u = username_input.get_value()
                p = password_input.get_value()
                if u and p:
                    ok, msg = verify_user(u, p)
                    info_msg = msg
                    msg_timer = 2.0
                    if ok:
                        return u

        # ── Draw ──────────────────────────────────────────────────────────────
        screen.fill(BG)

        title = font_lg.render("JS Tap-Tap", True, (220, 220, 220))
        screen.blit(title, (W // 2 - title.get_width() // 2, 40))

        sub = font_sm.render(
            "Login or Register (local, secure-ish hashing)", True, (180, 180, 180)
        )
        screen.blit(sub, (W // 2 - sub.get_width() // 2, 110))

        username_input.draw(screen)
        password_input.draw(screen)
        login_btn.draw(screen)
        reg_btn.draw(screen)

        if info_msg:
            msg_surf = font_sm.render(info_msg, True, (255, 215, 0))
            screen.blit(msg_surf, (W // 2 - msg_surf.get_width() // 2, 350))
            msg_timer -= dt
            if msg_timer <= 0:
                info_msg = ""

        uval = username_input.get_value()
        if uval:
            hs = get_highscore(uval)
            hs_surf = font_sm.render(f"Saved highscore: {hs}", True, (160, 160, 160))
            screen.blit(hs_surf, (W // 2 - hs_surf.get_width() // 2, 390))

        hint = font_sm.render(
            "Password is masked. Register creates account.", True, (120, 120, 120)
        )
        screen.blit(hint, (W // 2 - hint.get_width() // 2, H - 40))

        pygame.display.flip()


# ─── Screen: Gameplay ─────────────────────────────────────────────────────────

def game_screen(
    username: str,
    screen: pygame.Surface,
    clock: pygame.time.Clock,
    fonts: dict,
    config: dict,
) -> int:
    """Run the 30-second tap-the-targets gameplay loop.

    Args:
        username:  The logged-in player's username (for HUD display).
        screen:    The main Pygame display surface.
        clock:     The shared Pygame clock.
        fonts:     Dict with keys "small", "medium", "large".
        config:    Game constants dict.

    Returns:
        The final integer score when time runs out.
    """
    W, H = config["SCREEN_W"], config["SCREEN_H"]
    FPS = config["FPS"]
    BG = config["BG_COLOR"]
    GAME_DURATION = config["GAME_DURATION"]
    TARGET_LIFETIME = config["TARGET_LIFETIME"]
    SPAWN_INTERVAL = config["SPAWN_INTERVAL"]
    TARGET_MIN_R = config["TARGET_MIN_RADIUS"]
    TARGET_MAX_R = config["TARGET_MAX_RADIUS"]
    font_sm = fonts["small"]
    font_md = fonts["medium"]

    score = 0
    start_time = time.time()
    last_spawn = 0.0
    targets: list[Target] = []

    while True:
        dt = clock.tick(FPS) / 1000.0  # noqa: F841  (kept for consistency)
        now = time.time()
        elapsed = now - start_time
        time_left = max(0.0, GAME_DURATION - elapsed)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(targets) - 1, -1, -1):
                    if targets[i].alive and targets[i].hit_test(e.pos):
                        score += 1
                        del targets[i]
                        break  # one click = one target

        # Spawn a new target at fixed intervals
        if now - last_spawn >= SPAWN_INTERVAL:
            last_spawn = now
            r = random.randint(TARGET_MIN_R, TARGET_MAX_R)
            margin = r + 8
            x = random.randint(margin, W - margin)
            y = random.randint(120 + margin, H - margin)
            targets.append(Target((x, y), r, now))

        # Expire old targets
        for i in range(len(targets) - 1, -1, -1):
            if now - targets[i].spawn > TARGET_LIFETIME:
                del targets[i]

        # ── Draw ──────────────────────────────────────────────────────────────
        screen.fill(BG)

        player_surf = font_md.render(f"Player: {username}", True, (230, 230, 230))
        screen.blit(player_surf, (20, 10))

        score_surf = font_sm.render(f"Score: {score}", True, (230, 230, 230))
        screen.blit(score_surf, (20, 60))

        time_surf = font_sm.render(f"Time left: {time_left:.1f}s", True, (230, 230, 230))
        screen.blit(time_surf, (W - 190, 10))

        hs = get_highscore(username)
        hs_surf = font_sm.render(f"Highscore: {hs}", True, (200, 200, 200))
        screen.blit(hs_surf, (W - 190, 40))

        instr = font_sm.render(
            "Click the circles before they vanish. Fast taps win!", True, (160, 160, 160)
        )
        screen.blit(instr, (W // 2 - instr.get_width() // 2, 60))

        for t in targets:
            t.draw(screen)

        pygame.display.flip()

        if time_left <= 0.0:
            update_highscore(username, score)
            return score


# ─── Screen: Results ──────────────────────────────────────────────────────────

def results_screen(
    username: str,
    score: int,
    screen: pygame.Surface,
    clock: pygame.time.Clock,
    fonts: dict,
    config: dict,
) -> str:
    """Display the end-of-round results screen.

    Args:
        username:  Logged-in player's username.
        score:     The score achieved in the just-completed round.
        screen:    The main Pygame display surface.
        clock:     The shared Pygame clock.
        fonts:     Dict with keys "small", "medium", "large".
        config:    Game constants dict.

    Returns:
        "restart" to play again (same user).
        "logout"  to return to the login screen.
    """
    W, H = config["SCREEN_W"], config["SCREEN_H"]
    FPS = config["FPS"]
    BG = config["BG_COLOR"]
    font_sm = fonts["small"]
    font_md = fonts["medium"]
    font_lg = fonts["large"]

    hs = get_highscore(username)

    restart_btn = Button((W // 2 - 160, H - 140, 140, 40), "Restart (R)", font=font_sm)
    logout_btn = Button((W // 2 + 20, H - 140, 140, 40), "Logout (L)", font=font_sm)
    quit_btn = Button((W // 2 - 70, H - 80, 140, 40), "Quit (Q)", font=font_sm)

    while True:
        clock.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    return "restart"
                if e.key == pygame.K_l:
                    return "logout"
                if e.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                if restart_btn.clicked(e.pos):
                    return "restart"
                if logout_btn.clicked(e.pos):
                    return "logout"
                if quit_btn.clicked(e.pos):
                    pygame.quit()
                    sys.exit()

        # ── Draw ──────────────────────────────────────────────────────────────
        screen.fill(BG)

        title = font_lg.render("Time's Up!", True, (250, 250, 250))
        screen.blit(title, (W // 2 - title.get_width() // 2, 40))

        score_t = font_md.render(f"Your Score: {score}", True, (230, 230, 230))
        screen.blit(score_t, (W // 2 - score_t.get_width() // 2, 140))

        hs_t = font_sm.render(f"Your Highscore: {hs}", True, (200, 200, 200))
        screen.blit(hs_t, (W // 2 - hs_t.get_width() // 2, 200))

        restart_btn.draw(screen)
        logout_btn.draw(screen)
        quit_btn.draw(screen)

        hint = font_sm.render(
            "Click Restart or press R to play again.", True, (160, 160, 160)
        )
        screen.blit(hint, (W // 2 - hint.get_width() // 2, H - 180))

        pygame.display.flip()
