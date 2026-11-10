#!/usr/bin/env python3
"""Repository gate: fails when a tracked file is unfit for this public repository.

Run from the repository root: python3 tools/gate.py
Standard library only. Rules and limits: docs/gate.md
"""
import fnmatch
import os
import subprocess
import sys

MAX_LINE = 2000  # longer lines are minified or generated, nobody can review them
EM_DASH = chr(0x2014)  # written as a number so this file passes its own rule

# Same names as .gitignore: the ignore file stops accidents, the gate stops "git add -f".
FORBIDDEN_NAMES = (
    ".env", ".env.*", ".dev.vars", "*.keystore", "*.jks", "*.pem", "*.key", "*.p12",
    "CLAUDE.local.md", "settings.local.json",
)
FORBIDDEN_DIRS = (".claude",)


def check(path, data):
    """Return the list of problems for one tracked file (path with /, content as bytes)."""
    problems = []
    parts = path.split("/")
    if any(fnmatch.fnmatchcase(parts[-1], pattern) for pattern in FORBIDDEN_NAMES):
        problems.append("file name reserved for secrets or local settings")
    if any(part in FORBIDDEN_DIRS for part in parts[:-1]):
        problems.append("inside a local settings folder")
    if b"\0" in data:
        return problems + ["binary file"]
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return problems + ["binary file (not UTF-8 text)"]
    for number, line in enumerate(text.splitlines(), 1):
        if len(line) > MAX_LINE:
            problems.append(f"line {number} is longer than {MAX_LINE} characters (minified or generated)")
        if EM_DASH in line:
            problems.append(f"line {number} contains an em-dash")
    return problems


def main():
    # -z: git prints names raw, so a strange file name cannot hide from the gate
    names = subprocess.run(
        ["git", "ls-files", "-z"], check=True, capture_output=True
    ).stdout.decode("utf-8", "surrogateescape").split("\0")
    failed = 0
    for path in filter(None, names):
        if os.path.islink(path):
            problems = ["symbolic link"]
        else:
            with open(path, "rb") as file:
                problems = check(path, file.read())
        for problem in problems:
            failed += 1
            print(f"{path!r}: {problem}")
    print(f"gate: {failed} problem(s)" if failed else "gate: OK")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
