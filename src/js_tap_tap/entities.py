# entities.py — JS Tap-Tap (Chip-X)
# Responsibility: Game entity definitions.
# Currently contains only the Target class — the clickable circles
# that appear and disappear during a gameplay round.
# No auth, no UI widget, no screen logic belongs here.

import random
import pygame


class Target:
    """A single clickable target circle in the JS Tap-Tap game.

    Targets are spawned by the game screen at fixed intervals, rendered
    with a random vivid colour, and expire after TARGET_LIFETIME seconds
    unless the player clicks them first.

    Attributes:
        x (float):      Centre X coordinate (pixels).
        y (float):      Centre Y coordinate (pixels).
        r (int):        Radius in pixels (20–40 range, randomly assigned on spawn).
        spawn (float):  The value of time.time() when this target was created.
                        Used to compute expiry without storing a timer state.
        alive (bool):   True until the target is either clicked or expired.
                        (Legacy flag — currently deletion is done externally.)
        color (tuple):  Random RGB colour in a vivid range, fixed at spawn time.
    """

    def __init__(self, pos: tuple, radius: int, spawn_time: float):
        """Create a target at *pos* with given *radius* and *spawn_time*.

        Args:
            pos:        (x, y) pixel coordinates for the circle centre.
            radius:     Circle radius in pixels.
            spawn_time: Output of time.time() at the moment of spawn.
        """
        self.x, self.y = pos
        self.r = radius
        self.spawn = spawn_time
        self.alive = True
        self.color = (
            random.randint(120, 255),
            random.randint(80, 220),
            random.randint(80, 220),
        )

    def draw(self, surf: pygame.Surface) -> None:
        """Draw this target onto *surf*.

        Renders an outer filled circle in the target's colour plus a small
        white inner circle to create a crosshair-style visual cue.
        """
        pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.r)
        pygame.draw.circle(
            surf,
            (255, 255, 255),
            (int(self.x), int(self.y)),
            max(3, int(self.r * 0.25)),
        )

    def hit_test(self, pos: tuple) -> bool:
        """Return True if *pos* falls within this target's circular area.

        Uses squared-distance comparison to avoid a sqrt call.

        Args:
            pos:  (x, y) pixel coordinates of the mouse click.

        Returns:
            True if the click is inside (or on the edge of) the circle.
        """
        dx = pos[0] - self.x
        dy = pos[1] - self.y
        return dx * dx + dy * dy <= self.r * self.r
