# Contributing to JS Tap-Tap

Thank you for your interest in contributing! This document explains how to
set up a development environment, what conventions to follow, and how to
submit changes.

---

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Development Setup](#2-development-setup)
3. [Running the Game from Source](#3-running-the-game-from-source)
4. [Running Tests](#4-running-tests)
5. [Code Style](#5-code-style)
6. [Branch Naming](#6-branch-naming)
7. [Submitting a Pull Request](#7-submitting-a-pull-request)
8. [Reporting Bugs / Requesting Features](#8-reporting-bugs--requesting-features)

---

## 1. Getting Started

- Fork the repository and clone your fork.
- Read [docs/PROJECT_ARCHITECTURE.md](docs/PROJECT_ARCHITECTURE.md) to understand the module structure before making changes.
- Check [docs/KNOWN_ISSUES.md](docs/KNOWN_ISSUES.md) for documented design decisions — don't fix what is intentional.

---

## 2. Development Setup

**Requirements:** Python 3.11+ (3.12 recommended), pip.

```bash
# Create a virtual environment
python -m venv .venv

# Activate it (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

> **Tip:** Add `.venv/` to your shell's ignore list. It is already in `.gitignore`.

---

## 3. Running the Game from Source

```bash
# From repo root, with .venv active:
python -m src.js_tap_tap.main

# Or directly:
python src/js_tap_tap/main.py
```

The game window should open identically to the compiled EXE.

---

## 4. Running Tests

```bash
# Run all tests with pytest
pytest tests/ -v
```

Tests in `tests/test_auth.py` cover authentication functions in isolation
(no Pygame required — `auth.py` is pure Python).

---

## 5. Code Style

- Follow **PEP 8** for all Python code.
- Use **4 spaces** for indentation (no tabs).
- Maximum line length: **100 characters**.
- All public functions and classes must have **docstrings**.
- Use `flake8` and `black` for linting/formatting:

```bash
flake8 src/ tests/
black src/ tests/
```

The CI lint workflow runs `flake8` on every PR — ensure it passes locally first.

---

## 6. Branch Naming

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feature/short-description` | `feature/multiplayer-scores` |
| Bug fix | `fix/short-description` | `fix/welcome-path-bug` |
| Documentation | `docs/short-description` | `docs/add-faq-section` |
| Refactor | `refactor/short-description` | `refactor/split-screens-module` |

Branch off from `main`. Do not commit directly to `main`.

---

## 7. Submitting a Pull Request

1. Push your branch to your fork.
2. Open a PR against this repository's `main` branch.
3. Fill in the [PR template](.github/PULL_REQUEST_TEMPLATE.md) completely.
4. Ensure the CI checks (lint + build) are green before requesting review.
5. Link any related issues using `Closes #issue-number`.

PRs will be reviewed within a reasonable timeframe. Feedback will be given
as GitHub review comments — please address all requested changes before merging.

---

## 8. Reporting Bugs / Requesting Features

- **Bugs:** Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md).
- **Features:** Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md).
- **Security issues:** See [SECURITY.md](SECURITY.md) — do NOT open a public issue.

---

By contributing, you agree that your changes will be licensed under the
[MIT License](LICENSE) that covers this project.
