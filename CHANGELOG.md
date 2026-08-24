# Changelog

All notable changes to this repository are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.2.1] - 2026-08-24

### Added

- Source-verified equation transcriptions for three records: Halnes 2013 electrodiffusive astrocyte-extracellular model (equations (1)-(6)), Polykretis 2018 neuron-astrocytic network (equations (1)-(9)), and Hopfield 1982 associative-memory network (equations [1]-[8]).
- Variable and parameter registry entries covering the three newly transcribed systems, including the literature-given parameter values.
- Equation audit rows covering every newly displayed equation block.

### Changed

- Hopfield 1982 advanced from bibliography-only holding to `equation_transcribed`; Halnes 2013 and Polykretis 2018 advanced from `equation_located` to `equation_transcribed`.
- The reference verification audit now records inspected equations for the three records.

## [0.2.0] - 2026-08-23

### Added

- Generated Simplified Chinese catalogue view `README.zh-CN.md`, with language-switcher badges on both README files; every data table derives from the same canonical CSV as the English view.
- Chinese mirrors for five core documents: contribution guide, data dictionary, equation curation protocol, model scope taxonomy, and research gaps.
- Dedicated localization module `scripts/i18n_zh.py` holding all Simplified Chinese repository-authored text in one auditable place.
- Issue templates for new-model proposals and data corrections.
- Staleness gate for the Chinese README in `scripts/validate_references.py`.

### Changed

- `scripts/build_tables.py` renders both languages from shared statistics; table headers, status labels, and navigation entries are localized while the canonical data stays unchanged.
- `scripts/validate_language.py` exempts designated `.zh-CN.*` documents, the localization module, and language-switcher links from the English-only check; tool-brand checks remain global.

### Fixed

- The validation workflow now also triggers on pushes to the default branch `curation/evidence-audit-and-reproducibility`; previously only pull requests ran it.

## [0.1.0] - 2026-07-22

### Added

- Initial public atlas: canonical catalogue of 25 model records, 278-row screening inventory, equation audit registries, governance files, offline validators, and Brian2 smoke tests.
