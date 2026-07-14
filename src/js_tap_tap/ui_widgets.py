# ui_widgets.py — JS Tap-Tap (Chip-X)
# Responsibility: Reusable Pygame GUI primitives (TextInput, Button).
# These classes are UI-only — no game logic, no auth, no data persistence.
# They depend on Pygame being initialised and on the shared clock/font
# objects provided by main.py at module load time.

import pygame


class TextInput:
    """A single-line text input box rendered in Pygame.

    Supports placeholder text, password masking, cursor blink,
    Tab focus-switching, and Enter submission signal.

    Attributes:
        rect (pygame.Rect): Bounding box for hit-testing and drawing.
        text (str):         Current input content (not masked).
        placeholder (str):  Hint shown when the box is empty and unfocused.
        password (bool):    When True, renders content as asterisks.
        active (bool):      True when this box has keyboard focus.
        maxlen (int):       Maximum number of characters allowed.
    """

    def __init__(
        self,
        rect: tuple,
        placeholder: str = "",
        password: bool = False,
        maxlen: int = 32,
        font: pygame.font.Font = None,
        clock: pygame.time.Clock = None,
    ):
        self.rect = pygame.Rect(rect)
        self.text = ""
        self.placeholder = placeholder
        self.password = password
        self.active = False
        self.maxlen = maxlen
        self._font = font
        self._clock = clock
        self.cursor_visible = True
        self.cursor_timer = 0.0

    def handle_event(self, e: pygame.event.Event) -> str | None:
        """Process a single Pygame event.

        Returns:
            "enter" when Enter is pressed while focused.
            "tab"   when Tab is pressed while focused.
            None    for all other events.
        """
        if e.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(e.pos)
        if e.type == pygame.KEYDOWN and self.active:
            if e.key == pygame.K_RETURN:
                return "enter"
            elif e.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif e.key == pygame.K_TAB:
                return "tab"
            else:
                if len(self.text) < self.maxlen and e.unicode.isprintable():
                    self.text += e.unicode
        return None

    def draw(self, surf: pygame.Surface) -> None:
        """Draw the input box onto *surf*."""
        border_color = (255, 255, 255) if self.active else (180, 180, 180)
        pygame.draw.rect(surf, border_color, self.rect, 2, border_radius=6)

        if self.text == "" and not self.active:
            display = self.placeholder
            color = (180, 180, 180)
        else:
            display = ("*" * len(self.text)) if self.password else self.text
            color = (240, 240, 240)

        # Cursor blink
        if self._clock is not None:
            self.cursor_timer += self._clock.get_time() / 1000.0
        if self.cursor_timer > 0.5:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0.0

        cursor_suffix = "|" if self.active and self.cursor_visible else ""
        txt_surf = self._font.render(display + cursor_suffix, True, color)
        surf.blit(
            txt_surf,
            (self.rect.x + 8, self.rect.y + (self.rect.h - txt_surf.get_height()) / 2),
        )

    def get_value(self) -> str:
        """Return the stripped text value."""
        return self.text.strip()


class Button:
    """A simple clickable rectangular button rendered in Pygame.

    Attributes:
        rect (pygame.Rect): Bounding box for hit-testing and drawing.
        text (str):         Label displayed on the button.
    """

    def __init__(
        self,
        rect: tuple,
        text: str,
        font: pygame.font.Font = None,
        color: tuple = (70, 130, 180),
        text_color: tuple = (255, 255, 255),
    ):
        self.rect = pygame.Rect(rect)
        self.text = text
        self._font = font
        self._color = color
        self._text_color = text_color

    def draw(self, surf: pygame.Surface) -> None:
        """Draw the button onto *surf*."""
        pygame.draw.rect(surf, self._color, self.rect, border_radius=8)
        txt = self._font.render(self.text, True, self._text_color)
        surf.blit(
            txt,
            (
                self.rect.centerx - txt.get_width() / 2,
                self.rect.centery - txt.get_height() / 2,
            ),
        )

    def clicked(self, pos: tuple) -> bool:
        """Return True if *pos* is inside the button's bounding box."""
        return self.rect.collidepoint(pos)
