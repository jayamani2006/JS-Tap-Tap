# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| 1.0.x   | ✅ Yes              |
| < 1.0   | ❌ No               |

---

## Scope of This Project's Security Model

> **Important:** JS Tap-Tap is a **local single-player game** intended for personal and portfolio use.
> Its authentication system is **not designed for networked or multi-user production environments**.

### What the auth system does
- Passwords are stored as **SHA-256(salt + password)** using a per-user random 16-byte salt.
- Credentials are persisted in `users.json`, a local plaintext-adjacent JSON file.
- The salt is randomly generated per user using `os.urandom(16)` — not reused.

### What the auth system does NOT do
- It does not protect against local file system access (anyone with OS access to the machine can read `users.json`).
- It does not use a key-derivation function (KDF) like bcrypt, scrypt, or Argon2 — SHA-256 is used for simplicity, appropriate for a local toy game, not for production credential storage.
- It does not transmit data over any network — all data remains on the local machine.
- It does not enforce password strength, account lockout, or session tokens.

See [DISCLAIMER.md](DISCLAIMER.md) and [docs/KNOWN_ISSUES.md](docs/KNOWN_ISSUES.md) for full scope documentation.

---

## Reporting a Vulnerability

If you discover a security issue in this project, please report it responsibly:

1. **Do not open a public GitHub Issue** for security vulnerabilities.
2. **Use GitHub's Private Security Advisory** feature:
   - Go to the repository → **Security** tab → **Advisories** → **New draft security advisory**.
3. **Alternatively**, email the maintainer directly (contact details on the GitHub profile).

Please include:
- A description of the vulnerability.
- Steps to reproduce it.
- The potential impact you see.
- Any suggested fix (optional but appreciated).

You will receive a response within **7 days**. Confirmed vulnerabilities will be patched in the next release and credited in the CHANGELOG (unless you prefer to remain anonymous).

---

*This policy applies to the source code in this repository. It does not apply to third-party dependencies (Pygame, Pillow, PyInstaller) — report those upstream.*
