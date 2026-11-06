# Dataset notes

## `pokemon_go_kanto_candidates.csv`

This is a compact **synthetic classroom dataset** containing 15 Kanto Pokémon candidates. It is included so every student can reproduce the same baseline analysis without scraping a website or relying on an unstable live API.

The columns are deliberately simplified:

- `pokedex_id`, `pokemon`, `type_1`, `type_2`: identity and typing context.
- `great_league_eligible`: an instructional assumption meaning that at least one build can be evaluated at or below 1,500 CP; it is not a legal roster determination.
- `attack_index`, `bulk_index`, `move_coverage_index`: normalized classroom proxies on a 0–100 scale.
- `meta_signal_index`: a fictional, bounded signal used to demonstrate weighting and sensitivity analysis.
- `source_note`: identifies the values as classroom proxies.

Do not treat these numbers as official Pokémon GO stats, current move rankings, tournament usage, or a guarantee that a specific individual Pokémon is legal. Students should replace or enrich the dataset with documented, licensed, current sources as an extension exercise.

## Reproducibility and licensing

The CSV is original instructional material for this repository and is available under the repository’s [CC0 1.0 license](../../../LICENSE). Pokémon names and game concepts belong to their respective rights holders. Official rules remain governed by the linked source documents.
