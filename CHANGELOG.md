# Changelog

## Unreleased

- First code: `tools/gate.py`, the repository gate. It fails when a tracked file is a binary, has a minified line, carries a name reserved for secrets or local settings, is a symbolic link, or contains an em-dash. Tests in `tests/`, run on every pull request by `.github/workflows/gate.yml` without any third-party action. Described in `docs/gate.md`. The code has no licence yet.
- Repository created with README, security policy and changelog. No code.
- Phase 1 draft: `docs/profile/android.md`, the Cromite setup checklist and the ten minute self-check with PCAPdroid. Not yet verified by measurement.
- Principles written in the README: free of charge, nobody earns money from it, reasons stated, open to checking, created in Italy, as little borrowed as possible. Each sentence carries its limit.
- `docs/dependencies.md`: the public list of everything the project relies on and did not write, with who is behind each part, whether it fits the project's rules, and why it stays. Facts read on 2026-11-10.
- Phase 1 draft corrected with facts checked on 2026-11-10: Cromite's latest release is about two months behind the engine's security fixes, stock Cromite makes connections of its own (listed), MetaGer is withdrawn as search engine because it needs a paid key, PCAPdroid and the hash check are described with their limits.
- README: the licence note now says what the missing licence means, and the engine is named (Chromium, through Cromite).
- README opens with the pitch: what the project wants to give, with thanks to the people who built the engine.
- Completeness pass of 2026-11-10 applied to the three public documents. Dependency list: rows added for what was missing (Google Play Protect, Cromite's own servers and contacts, the data lists and decoders built into the engine, Windows and the laptop, adb, a signing program, an app that shows who signed a package, the fingerprint test, the screen reader, the iPhone guide, the lists left out); "exception" now reads "exception proposed" wherever the author has not decided; Cromite, Phishing.Database, Git, Python, Vercel and Android rows corrected. README: the heading "Nobody earns money from it" becomes "The project earns no money", and the limits now say what is not public yet, what is not built yet and where the design still breaks its own rule. Guide: "Install without Google" becomes "Install without the Play Store", the file to download is named, the limits of switching Safe Browsing off and of secure DNS are stated, and the expected connections are complete.
