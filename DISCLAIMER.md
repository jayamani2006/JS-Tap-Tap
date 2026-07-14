# Disclaimer

## Nature of This Project

**JS Tap-Tap** is a **personal and portfolio project** created by Jayasubramani
under the **Chip-X / JS SoftTools** brand.

It is provided for demonstration, learning, and entertainment purposes only.
It is not a commercial product and is not intended for enterprise, production,
or mission-critical use.

---

## Authentication System Disclaimer

The local login and registration system in JS Tap-Tap uses
**SHA-256 with a random per-user salt** to hash passwords, stored in a local
`users.json` file.

This implementation is **intentionally designed for local, single-player use only**:

- It is **not** a production-grade authentication system.
- It is **not** suitable for networked, multi-user, or server-side credential storage.
- It does **not** use a memory-hard key-derivation function (e.g. bcrypt, Argon2).
- Anyone with local file system access to the machine can inspect `users.json`.

The purpose of this system is to demonstrate the concept of salted password
hashing in a self-contained context. It should **not** be replicated for any
application where real user security is at stake.

---

## No Warranty

This software is provided **"as is"**, without warranty of any kind, express or
implied, including but not limited to the warranties of merchantability, fitness
for a particular purpose, or non-infringement.

In no event shall the author be liable for any claim, damages, or other
liability arising from the use of this software.

---

## Third-Party Dependencies

This project uses the following open-source libraries:

| Library | License | Purpose |
|---------|---------|---------|
| [Pygame](https://www.pygame.org/) | LGPL 2.1 | Game engine and rendering |
| [Pillow](https://pillow.readthedocs.io/) | HPND (PIL fork) | Image processing in welcome popup |
| [PyInstaller](https://pyinstaller.org/) | GPL 2 + bootloader exception | Packaging into standalone EXE |

Their respective licenses apply to those components. This disclaimer covers only
the original source code authored by Jayasubramani.

---

*See [LICENSE](LICENSE) for the full terms governing this project's source code.*
