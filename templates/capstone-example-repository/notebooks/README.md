# Notebooks

Use numbered notebooks to make the intended execution order clear. Each notebook should include its question, data sources, retrieval date, assumptions, quality checks, transformations, visual evidence, limitations, and next action.

- `01-capstone-question.ipynb`: minimal runnable starting point.
- `02-data-quality.ipynb`: profiling, schema checks, and missingness.
- `03-analysis.ipynb`: analysis or model development after the question is stable.
- `04-dashboard-dataset.ipynb`: reproducible table prepared for BI consumption.

When code becomes reusable, move it into `src/` and test it. Keep notebooks focused on exploration, explanation, and evidence rather than hiding an entire production pipeline in one cell.
