# Activity 2 — VS Code + Anaconda workbench

Goal: set up a reproducible Python data-science workbench (VS Code + Anaconda +
Git), run beginner code in a project-specific conda environment, and sync a
tested change to GitHub from VS Code.

## Submission note

| Item | Value |
| --- | --- |
| Operating system | Windows 11 Home Single Language (build 26200), x64 |
| Anaconda Distribution | Anaconda Navigator 2.7.1, base Python 3.14.6 |
| conda version | 26.7.3 |
| Project environment | `ti2006b-workbench` |
| Python version (environment) | 3.12.16 |
| Selected interpreter (VS Code) | `Python 3.12.16 ('ti2006b-workbench')` |
| Selected notebook kernel | `ti2006b-workbench` (Python 3.12.16) |
| Key packages | pandas 3.1.0, matplotlib 3.11.2, ipykernel 7.3.0, notebook 7.6.3 |
| VS Code | 1.145.3 |
| VS Code extensions | Python, Pylance, Jupyter (Microsoft) |
| Git | 2.46.0.windows.1 |
| Workflow | Direct commit to `main` via VS Code Source Control (no branch / PR) |

## The parts of the workbench (and why they are separate)

| Part | What it does | Where it lives |
| --- | --- | --- |
| **Editor** (VS Code) | Edits files, shows diffs, runs terminals. It does not contain Python. | VS Code install |
| **Python interpreter** | Actually runs the code. This machine has *three*: a system Python 3.9, the Anaconda `base` (3.14) and the project env `ti2006b-workbench` (3.12). VS Code must be told which one to use. | `anaconda3\envs\ti2006b-workbench` |
| **conda** | Creates and manages isolated environments and packages. | Anaconda Distribution |
| **Git** | Tracks versions and syncs with GitHub. VS Code's Source Control view is only a UI on top of it. | Git for Windows |
| **Extensions** | Python (interpreter selection, debugging), Pylance (IntelliSense), Jupyter (run notebooks in VS Code). | VS Code marketplace |

## Files in this activity

- [`workbench_check.py`](workbench_check.py) — beginner pandas + matplotlib
  script; reads the Activity 2.6 dataset, prints a top 5 and descriptive
  statistics, and saves a chart.
- [`workbench_check.ipynb`](workbench_check.ipynb) — the same check as a
  notebook, executed with the `ti2006b-workbench` kernel (outputs kept).
- [`evidence/attack_vs_bulk.png`](evidence/attack_vs_bulk.png) — chart produced
  by the script.

The installation evidence (screenshots) is submitted as a separate PDF.

Repository-level files added for reproducibility:

- [`environment.yml`](../../environment.yml) — `conda env export --from-history`
  with the machine-specific `prefix:` line removed.
- [`requirements.txt`](../../requirements.txt) — pip mirror of the same
  packages, for CI or non-conda users.
- [`.vscode/extensions.json`](../../.vscode/extensions.json) — recommended
  extensions (no paths or secrets).
- [`.gitignore`](../../.gitignore) — ignores personal `.vscode` settings,
  `.env*` files, keys and caches.

## Reproduce

```bash
conda env create -f environment.yml
conda activate ti2006b-workbench
python activities/02-vscode-anaconda-workbench/workbench_check.py
```

In VS Code: `Ctrl+Shift+P` → **Python: Select Interpreter** →
`ti2006b-workbench`. Open the notebook and pick the same environment in
**Select Kernel**.

Expected output ends with:

```text
Top 5 by equal-weight mean score:
  pokemon type_1  mean_score
  Snorlax Normal        85.5
   Lapras  Water        84.8
Poliwrath  Water        82.8
Nidoqueen Poison        81.0
  Slowbro  Water        79.2
...
Workbench environment is ready
```

## Issues found and how they were fixed

1. **`conda` not recognized in a normal PowerShell terminal.** Anaconda was
   installed for the current user without adding it to `PATH`, so `python`
   pointed to an older system Python 3.9. Fix: use **Anaconda Prompt** /
   **Anaconda PowerShell Prompt**, or run `conda init powershell` once from
   the Anaconda Prompt and reopen VS Code.
2. **`conda env export` includes a local path.** The `prefix:` line contains
   the user's folder, so it was deleted from `environment.yml` before
   committing.
3. **pandas 3.x was installed.** `requirements.txt` was written with
   `pandas>=2.0,<4` so it matches what conda actually resolved.

## Security

No tokens, passwords, `.env` files or local paths are committed. GitHub
authentication is handled by Git Credential Manager, outside the repository.
