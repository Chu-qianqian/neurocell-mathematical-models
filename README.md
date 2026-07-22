# Neurocell Mathematical Models

A curated and reproducible atlas of mathematical and computational models for neurons, astrocytes, microglia, oligodendrocytes, Schwann cells, and other nervous-system cell types.

This repository is a literature-grounded catalogue of published mathematical and computational models. It records model scope, source identifiers, implementation availability, and verification status without redistributing papers or unclear-license code.

## Licensing

- Original source code is licensed under [Apache-2.0](LICENSE-CODE).
- Original documentation, tables, and explanatory text are licensed under [CC BY 4.0](LICENSE-DOCS).
- Third-party materials retain their own terms and are not relicensed; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

No paper full text or third-party implementation is included merely by being cited.

## Status

The working atlas is developed on `codex/neurocell-model-atlas` and reviewed through a draft pull request. Start with [PROJECT_PLAN.md](PROJECT_PLAN.md), then inspect the machine-readable [model catalogue](data/models/catalogue.csv).

## Repository map

- `data/models/` — curated model records and controlled vocabularies.
- `references/` — search protocol, sources, and verification reports.
- `docs/` — field definitions and curation rules.
- `scripts/` — local validation utilities.
- `examples/` — original minimal examples only; no copied third-party implementations.

## Curation status

The seed release contains **six bibliographically verified model records** across neurons, astrocytes, microglia, and oligodendrocytes. Schwann-cell coverage is in scope but has not yet passed the stricter source-and-equation screening gate. See [data/models/coverage_status.csv](data/models/coverage_status.csv).
