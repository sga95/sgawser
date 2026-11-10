# Changelog

## Unreleased

- First code: `tools/gate.py`, the repository gate. It fails when a tracked file is a binary, has a minified line, carries a name reserved for secrets or local settings, is a symbolic link, or contains an em-dash. Tests in `tests/`, run on every pull request by `.github/workflows/gate.yml` without any third-party action. Described in `docs/gate.md`. The code has no licence yet.
- Repository created with README, security policy and changelog. No code.
