# auth.py — JS Tap-Tap (Chip-X)
# Responsibility: All user authentication and persistence logic.
# No Pygame or UI imports — this module is pure Python and fully testable in isolation.
#
# Security note (see SECURITY.md and DISCLAIMER.md for full context):
#   Credentials are stored as SHA-256(salt + password) in a local JSON file (users.json).
#   This is intentionally designed for local single-player use ONLY.
#   It is NOT suitable for networked or multi-user production environments.

import os
import json
import hashlib

USER_DB = "users.json"


def load_users() -> dict:
    """Load the user database from disk. Returns an empty dict if the file
    does not exist or is corrupted. Creates the file if missing."""
    if not os.path.exists(USER_DB):
        with open(USER_DB, "w") as f:
            json.dump({}, f)
    with open(USER_DB, "r") as f:
        try:
            return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return {}


def save_users(d: dict) -> None:
    """Write the user database dict back to disk (pretty-printed JSON)."""
    with open(USER_DB, "w") as f:
        json.dump(d, f, indent=2)


def hash_password(password: str, salt_hex: str) -> str:
    """Return SHA-256(salt_bytes + password_bytes) as a hex string.

    Args:
        password:  The plaintext password entered by the user.
        salt_hex:  A per-user random salt encoded as a lowercase hex string.

    Returns:
        The hex digest of the salted hash.
    """
    h = hashlib.sha256()
    h.update(bytes.fromhex(salt_hex))
    h.update(password.encode("utf-8"))
    return h.hexdigest()


def create_user(username: str, password: str) -> tuple[bool, str]:
    """Register a new user account.

    Args:
        username:  Desired username (must be unique).
        password:  Plaintext password to hash and store.

    Returns:
        (True, "Registered.") on success.
        (False, reason_string) if username already exists.
    """
    users = load_users()
    if username in users:
        return False, "Username already exists."
    salt = os.urandom(16).hex()
    users[username] = {
        "salt": salt,
        "hash": hash_password(password, salt),
        "highscore": 0,
    }
    save_users(users)
    return True, "Registered."


def verify_user(username: str, password: str) -> tuple[bool, str]:
    """Verify login credentials against the stored hash.

    Args:
        username:  The username to look up.
        password:  The plaintext password to verify.

    Returns:
        (True, "Login successful.") on match.
        (False, reason_string) if not found or password incorrect.
    """
    users = load_users()
    if username not in users:
        return False, "Account not found."
    u = users[username]
    if hash_password(password, u["salt"]) == u["hash"]:
        return True, "Login successful."
    return False, "Incorrect password."


def update_highscore(username: str, score: int) -> None:
    """Persist a new highscore for *username* if *score* beats the current record.

    Args:
        username:  The logged-in player's username.
        score:     The score achieved in the just-finished round.
    """
    users = load_users()
    if username in users:
        if score > users[username].get("highscore", 0):
            users[username]["highscore"] = score
            save_users(users)


def get_highscore(username: str) -> int:
    """Return the stored highscore for *username*, or 0 if not found.

    Args:
        username:  The player's username.

    Returns:
        Integer highscore value.
    """
    users = load_users()
    return users.get(username, {}).get("highscore", 0)
