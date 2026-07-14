## What Changed

<!-- Describe what this PR does. Be specific — which module(s) were changed and how? -->

## Why

<!-- Explain the motivation. Link the issue this resolves if applicable. -->
Closes #

## Type of Change

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would change existing behaviour)
- [ ] Documentation update
- [ ] Refactor (no functional change)
- [ ] CI / tooling change

## Testing Performed

<!-- How did you verify this change works? -->
- [ ] Ran `python -m src.js_tap_tap.main` and confirmed gameplay is unchanged
- [ ] Ran `pytest tests/ -v` — all tests pass
- [ ] Ran `flake8 src/ tests/` — no lint errors
- [ ] Built EXE with `pyinstaller packaging/game.spec` and tested the output

## Checklist

- [ ] My code follows the PEP 8 style guidelines
- [ ] I have added docstrings to any new public functions or classes
- [ ] I have updated relevant documentation (README, docs/, CHANGELOG)
- [ ] I have added or updated tests where appropriate
- [ ] My changes do not introduce new warnings
