# TI2006B Capstone Project Repository

Template for a reproducible business-intelligence, analytics, data-engineering, or machine-learning capstone project.

The repository should make a decision easy to review:

**business question → data → analysis → dashboard/model → decision → operation**

This template is designed for Visual Studio Code and Anaconda. Power BI and Tableau artifacts may remain in their native applications, but the repository must contain their metric definitions, screenshots or exports, refresh instructions, and limitations.

## Recommended workflow

1. Create an Anaconda environment from [`environment.yml`](environment.yml).
2. Open the repository folder in VS Code and install the recommended extensions.
3. Write the problem and success measures in [`docs/project-charter.md`](docs/project-charter.md).
4. Record important technical choices as ADRs in [`docs/adr/`](docs/adr/).
5. Keep exploratory work in [`notebooks/`](notebooks/); move reusable logic to [`src/`](src/).
6. Store only licensed, synthetic, anonymized, or small reproducible data samples in [`data/`](data/).
7. Publish the decision in [`reports/`](reports/) and document the dashboard in [`dashboards/`](dashboards/).
8. Run tests and notebook checks before opening a pull request.

## Repository map

```text
.
├── .github/workflows/       # CI checks; deployment is intentionally gated
├── .vscode/                 # shared editor and extension recommendations
├── assignments/             # capstone milestones and evidence
├── dashboards/              # BI metric catalog, exports, screenshots, refresh docs
│   ├── powerbi/             # PBIX/PBIT guidance and exported evidence
│   └── tableau/             # TWB/TWBX guidance and exported evidence
├── data/                    # raw, processed, external, and data documentation
├── docs/                    # charter, architecture, ADRs, governance, runbook
├── notebooks/               # analysis notebooks, ordered by execution flow
├── reports/                 # executive brief, technical report, figures
├── src/                     # tested reusable Python modules
├── tests/                   # unit and data-quality tests
├── environment.yml          # Anaconda environment definition
└── README.md
```

## Rules for a trustworthy capstone

- Never commit passwords, API keys, personal data, private company data, or unlicensed extracts.
- Every dataset must identify its source, license, retrieval date, transformations, and known limitations.
- Every KPI must have one definition, owner, grain, time zone, freshness target, and calculation.
- A dashboard is evidence for a decision, not the decision itself.
- A notebook should be runnable from the repository root and explain what its results do and do not support.
- Do not hide failed experiments; summarize them in the report or a decision log.

## Local setup

```bash
conda env create -f environment.yml
conda activate ti2006b-capstone
code .
jupyter lab
```

In VS Code, open a notebook and select the `ti2006b-capstone` kernel from the top-right kernel picker. The dashboard applications are installed and managed separately according to team or institution policy.

## Suggested capstone milestones

See [`assignments/README.md`](assignments/README.md) for the evidence expected at each stage. A project is complete when another student can understand the decision, reproduce the analysis, inspect the dashboard assumptions, and identify what should be monitored after delivery.
