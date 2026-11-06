# Activity 2.6 — GitHub Project Home

## Pokémon GO: should Charizard make the Kanto shortlist?

### Learning goal

Practice the complete evidence-to-decision loop in a small, reproducible analytics project:

1. inspect a dataset and its provenance;
2. define a selection rule before looking at the result;
3. calculate a transparent ranking;
4. test sensitivity to the weights and shortlist size;
5. separate a classroom proxy from official tournament legality;
6. publish a concise conclusion with assumptions and references.

### Decision question

> **Using the supplied Kanto candidate dataset and the stated classroom scoring rule, is Charizard among the five Pokémon selected for a tournament-preparation shortlist? What additional evidence would be required before entering an official Pokémon GO event?**

The notebook answers the first part reproducibly. The second part is deliberately open-ended: students must consult the current official rules and explain why a static analytical ranking cannot guarantee eligibility or competitive success.

### Important scope note

This activity uses a **classroom proxy dataset**, not an official Pokémon GO battle simulator or a current legal-roster database. The features are intentionally small and interpretable. They are suitable for practicing decision analysis, not for making a real tournament registration decision.

Official Play! Pokémon rules are a separate constraint. The current rules document says a tournament team can contain up to six Pokémon, players choose three for a game, and Great League Pokémon must be at or below 1,500 CP. Format-specific bans and rules can change. Students must verify the current rule set before drawing an operational conclusion.

### Files

- [`pokemon_go_kanto_candidates.csv`](data/pokemon_go_kanto_candidates.csv): included data students can inspect, copy, and extend.
- [`pokemon_go_kanto_analysis.ipynb`](pokemon_go_kanto_analysis.ipynb): guided analysis notebook.
- [`data/README.md`](data/README.md): provenance, license, and limitations.

### Suggested workflow

1. Open the notebook in JupyterLab, VS Code, or Google Colab.
2. Run all cells from top to bottom.
3. Change the weights in the sensitivity section and record when Charizard enters or leaves the top five.
4. Add at least one new feature or a new candidate and explain whether the decision changes.
5. Commit the notebook, data notes, and a short decision memo to your project repository.

### Deliverable

Submit a notebook and a one-page decision memo containing:

- the exact question and selection rule;
- the selected five and Charizard’s position;
- at least one sensitivity analysis;
- limitations of the dataset and proxy score;
- reviewed official references and the date they were checked;
- a recommendation for what to verify before an actual tournament.

### References reviewed

Reviewed 2026-11-06. These links are starting points, not a substitute for checking the event’s current rules:

- [Play! Pokémon Pokémon GO Tournament Rules](https://www.pokemon.com/static-assets/content-assets/cms2/pdf/play-pokemon/rules/play-pokemon-pokemon-go-tournament-rules-09292023-en.pdf) — team construction, Great League CP limit, and allowable Pokémon rules.
- [Play! Pokémon Resources and Documents](https://play.pokemon.com/en-gb/resources/documents/?filter=go) — current Pokémon GO rules, banned-Pokémon list, and team-list resources.
- [Play! Pokémon Competitive Rules & Formats](https://play.pokemon.com/en-us/resources/rules/?category=go) — official rules-and-formats entry point.
- [Pokémon GO Local Tournaments](https://play.pokemon.com/en-us/local-tournaments/go/) — context for local League Challenge and League Cup events.
