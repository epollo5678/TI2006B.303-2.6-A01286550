# BI dashboards

This directory is the dashboard documentation layer. The native Power BI or Tableau file may be stored outside Git when it is large, proprietary, or contains embedded data. The repository must still contain enough evidence to review the work.

For every dashboard, document:

- audience and decision supported;
- page/story map and interaction design;
- KPI definitions linked to [`docs/data-dictionary.md`](../docs/data-dictionary.md);
- data source, grain, refresh cadence, and filters;
- screenshots or small PDF/PNG exports with a date;
- accessibility decisions and known limitations;
- publication, permissions, and rollback instructions.

See the tool-specific guidance in [`powerbi/README.md`](powerbi/README.md) and [`tableau/README.md`](tableau/README.md).
