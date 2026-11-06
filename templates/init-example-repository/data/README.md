# Data directory

License note: This data documentation is original educational material under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Source
datasets and derived data retain the licenses and attribution requirements of
their respective providers.

Version: `v1.0`

- `raw/` is reserved for downloaded source files when a future activity needs
  a local snapshot. Do not commit secrets, personal data, or large generated
  files without documenting provenance and licensing.
- `processed/` is reserved for reproducible derived tables. Every derived file
  should identify its source and transformation in the notebook or a README.

The initial Pokémon notebook downloads small public CSV tables at runtime, so
the example repository does not need to commit a duplicate copy of the source
dataset.
