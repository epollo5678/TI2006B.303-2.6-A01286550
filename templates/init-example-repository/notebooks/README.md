# Notebooks: purpose, dataset, and conventions

License: Original notebook narrative and teaching material are licensed under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The
dataset source and software libraries retain their own terms.

Version: `v1.0`  
Status: `example`

The `notebooks/` directory is the learning and exploration layer of the
persistent class repository. Each notebook should state its question, source,
transformations, visual evidence, limitations, and next action. When an
analysis becomes stable, move reusable functions into `src/` and summarize the
result in `reports/`.

## Pokémon GO example

`01-pokemon-go-analysis.ipynb` is an introductory analysis for the class. Its
purpose is to practice a complete data workflow:

1. retrieve public source tables;
2. inspect columns and missing values;
3. join species, type, and base-stat tables;
4. derive total base stats and averages by type;
5. communicate patterns with interactive Plotly charts; and
6. record what the data can and cannot support.

The analysis is Pokémon GO-inspired because Pokémon GO is a familiar business
and product context for asking questions about entities, attributes, types,
comparisons, and player-facing decisions. The data is not Pokémon GO player
telemetry and does not contain accounts, locations, encounters, catches,
friends, or battle history.

## Dataset and provenance

The notebook downloads these CSV tables at runtime from the public
`veekun/pokedex` repository:

- [`pokemon.csv`](https://raw.githubusercontent.com/veekun/pokedex/master/pokedex/data/csv/pokemon.csv): identifiers, names, height, weight, and base experience.
- [`pokemon_stats.csv`](https://raw.githubusercontent.com/veekun/pokedex/master/pokedex/data/csv/pokemon_stats.csv): one row per Pokémon/statistic pair and the base-stat value.
- [`pokemon_types.csv`](https://raw.githubusercontent.com/veekun/pokedex/master/pokedex/data/csv/pokemon_types.csv): one row per Pokémon/type pair and the type slot.
- [`stats.csv`](https://raw.githubusercontent.com/veekun/pokedex/master/pokedex/data/csv/stats.csv): statistic identifiers and names.
- [`types.csv`](https://raw.githubusercontent.com/veekun/pokedex/master/pokedex/data/csv/types.csv): type identifiers and names.

The source is a public, community-maintained Pokédex data repository. Its
tables describe Pokémon species and game data; they are not an official
Pokémon GO API. Students must verify the source license and freshness before
using the analysis for a public or commercial claim. The notebook records the
retrieval date at runtime.

## Expected outputs

The initial notebook produces:

- a data-quality summary;
- a distribution of total base stats;
- a ranked bar chart of the strongest records by total base stats;
- a type-count chart; and
- a scatter plot comparing weight and total base stats.

These are descriptive results, not a Pokémon GO battle ranking. Future
activities can add a dimensional model, a reproducible pipeline, cloud storage,
quality tests, and a project-management trail around the same repository.
