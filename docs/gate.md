# The repository gate

`tools/gate.py` reads every file tracked by git and fails when one of them is unfit for this public repository. It is the first code of the project, written before any browser code so that every later line passes through it.

## What it refuses

| Rule | Why |
|---|---|
| A binary file (a NUL byte, or not UTF-8 text) | Nobody can review a binary. The project promises that everything in the repository is readable. |
| A line longer than 2,000 characters | Minified or generated code cannot be reviewed either. |
| A file name reserved for secrets or local settings (`.env`, `*.keystore`, `*.jks`, `*.pem`, `*.key`, `*.p12`, `.claude/`, `CLAUDE.local.md`, `settings.local.json`) | Secrets and local tool settings never enter the repository. `.gitignore` stops accidents, the gate stops a forced add. |
| A symbolic link | A link can point outside the repository and hide what is really read. |
| An em-dash | Project writing rule. |

## How to run it

From the repository root, with Python 3 and git, nothing else to install:

```
python3 -m unittest discover -s tests -v
python3 tools/gate.py
```

The same two commands run on every pull request and on every push to `main` (`.github/workflows/gate.yml`). The workflow uses no third-party action: it fetches the commit with plain git and has no permissions and no secrets.

## Limits

- It does not search file contents for secrets. A password pasted into a text file passes. The file name rule only catches the usual containers.
- It reads the current files, not the history. A file added and then deleted stays in the git history.
- It runs on GitHub's hosted runners, a Microsoft service. The script itself needs none of that and gives the same answer on any machine.
- The size and patch rules of the future browser code (line budget, one purpose per patch) are not here yet: there are no patches to count.
