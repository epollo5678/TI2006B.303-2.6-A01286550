# Runbook

## Local execution

```bash
conda env create -f environment.yml
conda activate ti2006b-capstone
python -m pytest
jupyter nbconvert --to notebook --execute notebooks/01-capstone-question.ipynb --output /tmp/capstone-executed.ipynb
```

## Refresh procedure

Document who can refresh the data, which date range is safe, how duplicates are handled, and how the dashboard is republished.

## Failure and rollback

| Signal | Diagnosis | Action | Escalation |
| --- | --- | --- | --- |
| | | | |

## Known limitations

## Last reviewed

YYYY-MM-DD — [name/team]
