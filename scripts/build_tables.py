"""Build all generated catalogue views from the canonical model CSV."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "models" / "model_catalog.csv"
JSON_OUT = ROOT / "models" / "model_catalog.json"
YAML_OUT = ROOT / "models" / "model_catalog.yaml"
README_OUT = ROOT / "README.md"
SCREENING = ROOT / "references" / "model_screening_master.csv"
GENERATED_NOTICE = "Generated from models/model_catalog.csv; do not edit by hand."


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def json_view(records: list[dict[str, str]]) -> str:
    payload = {"_generated_notice": GENERATED_NOTICE, "records": records}
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def yaml_view(records: list[dict[str, str]]) -> str:
    lines = [f"# {GENERATED_NOTICE}", "records:"]
    for record in records:
        lines.append("  - model_id: " + yaml_quote(record["model_id"]))
        for key, value in record.items():
            if key != "model_id":
                lines.append(f"    {key}: {yaml_quote(value)}")
    return "\n".join(lines) + "\n"


def markdown_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ")


def model_table(records: list[dict[str, str]]) -> str:
    if not records:
        return "No records currently meet this evidence state."
    lines = [
        "| Cell type | Model | Equation status | Brian2 compatibility | Equation page |",
        "| --- | --- | --- | --- | --- |",
    ]
    for record in records:
        lines.append(
            "| {cell_type} | {model_name} | `{equation_status}` | "
            "`{brian2_compatibility}` | [record]({equation_page}) |".format(
                **{key: markdown_cell(value) for key, value in record.items()}
            )
        )
    return "\n".join(lines)


def build_readme(
    records: list[dict[str, str]], screening: list[dict[str, str]]
) -> str:
    statuses = {
        status: sum(record["equation_status"] == status for record in records)
        for status in {
            "bibliography_verified",
            "equation_located",
            "equation_transcribed",
            "second_pass_checked",
            "independently_checked",
        }
    }
    equation_located_or_beyond = sum(
        record["equation_status"]
        in {
            "equation_located",
            "equation_transcribed",
            "second_pass_checked",
            "independently_checked",
        }
        for record in records
    )
    parameters_incomplete = sum(
        record["parameter_registry_status"] == "parameters_incomplete"
        for record in records
    )
    full_text_unavailable = sum(
        record["full_text_access_status"] == "full_text_unavailable"
        for record in records
    )
    uninspected_full_text = sum(
        record["full_text_access_status"] != "source_inspected"
        for record in records
    )
    license_unclear = sum(
        record["code_license_status"] == "license_unclear" for record in records
    )
    promoted_screening = sum(
        row["screening_status"] == "promoted" for row in screening
    )
    cell_counts: dict[str, int] = {}
    for record in records:
        cell_counts[record["cell_type"]] = cell_counts.get(record["cell_type"], 0) + 1
    coverage = "\n".join(
        f"- {cell_type}: **{count}**"
        for cell_type, count in sorted(cell_counts.items())
    )
    latest = max(record["last_verified"] for record in records)
    by_status = {
        status: [
            record for record in records if record["equation_status"] == status
        ]
        for status in statuses
    }
    brian_table = model_table(records)
    return f"""<!-- {GENERATED_NOTICE} -->
# Neurocell Mathematical Models

> A traceable, copyright-compliant atlas of mathematical and computational models for nervous-system cells.

This repository is an equation-level knowledge base, not a paper mirror or a collection of third-party code. It separates bibliography verification, equation transcription, maintainer second-pass checking, and genuinely independent checking. A model-family screening item is never treated as a source-specific verified model without an identified primary source.

## Current evidence counts

- Canonical model records: **{len(records)}**
- Bibliography-only holding records: **{statuses["bibliography_verified"]}**
- Equation-located or stronger records: **{equation_located_or_beyond}**
- Equation-transcribed records awaiting a second pass: **{statuses["equation_transcribed"]}**
- Maintainer second-pass checked records: **{statuses["second_pass_checked"]}**
- Independently checked records: **{statuses["independently_checked"]}**
- Records with incomplete parameter registries: **{parameters_incomplete}**
- Records explicitly marked full text unavailable: **{full_text_unavailable}**
- Records whose source full text is unavailable or not yet inspected: **{uninspected_full_text}**
- Records with unclear external-code licensing: **{license_unclear}**
- Screening inventory rows: **{len(screening)}** ({promoted_screening} promoted to the canonical catalogue)

## Independently checked equations

{model_table(by_status["independently_checked"])}

Independent status requires a named checker, check date, method, verification source, source version, access date, and discrepancy resolution in the equation audit. No record currently satisfies that contract.

## Maintainer second-pass checked equations

{model_table(by_status["second_pass_checked"])}

These records received a second check within the maintainer workflow. They are deliberately not described as independently checked.

## Equation-transcribed models

{model_table(by_status["equation_transcribed"])}

These transcriptions have exact source locators and equation-audit rows but still await a documented second pass.

## Bibliography-verified holding records

{model_table(by_status["bibliography_verified"])}

Holding records do not display reconstructed source-specific equations.

## Brian2 feasibility and implementation evidence

{brian_table}

Compatibility is a feasibility classification, not execution evidence. Every current record remains `not_implemented`, with `numerical_test_status=not_run`, `reference_behavior_status=not_assessed`, and `reproduction_status=not_attempted`.

## Canonical data and generated views

The only hand-maintained model catalogue is [models/model_catalog.csv](models/model_catalog.csv). [JSON](models/model_catalog.json), [YAML](models/model_catalog.yaml), and this README are generated by `python scripts/build_tables.py`. The legacy `data/models/catalogue.csv` index was removed after its six records were confirmed to be represented in the canonical catalogue.

Every displayed equation has an audit row in [data/equations/equation_audit.csv](data/equations/equation_audit.csv). The complete requested screening scope is tracked in [references/model_screening_master.csv](references/model_screening_master.csv), with a line-level request snapshot in [references/model_screening_inventory.csv](references/model_screening_inventory.csv).

## Evidence and copyright boundary

Equation pages require a lawful source, a precise locator, a transcription type, and an audit row. The repository stores original explanatory prose and concise cited mathematics only; it does not distribute paper PDFs, publisher figures, copied tables, supplements, unlicensed third-party code, or unauthorized data. Paper access status and code-license status are recorded separately.

## Navigation

- [Equation index](equations/README.md)
- [Equation curation protocol](docs/equation_curation_protocol.md)
- [Evidence-status migration](docs/evidence_status_migration.md)
- [Equation notation policy](docs/equation_notation_policy.md)
- [Model scope taxonomy](docs/model_scope_taxonomy.md)
- [Cell-type pages](docs/cell_types/README.md)
- [Research gaps](docs/research_gaps.md)
- [Screening master](references/model_screening_master.csv)
- [Data dictionary](docs/data_dictionary.md)
- [Contribution guide](docs/CONTRIBUTING.md)

## Canonical catalogue coverage

{coverage}

Synaptic models, neuron-microglia models, myelinated-axon and myelin-plasticity models, Schwann-cell models, neurovascular multicellular models, and other-cell categories remain evidence-gated screening items unless a source-specific canonical record says otherwise.

## Licenses and disclaimer

- Original code: Apache-2.0, see [LICENSE-CODE](LICENSE-CODE).
- Original documentation, tables, and explanations: CC BY 4.0, see [LICENSE-DOCS](LICENSE-DOCS).
- Third-party material is not relicensed; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
- This repository is a literature-navigation and educational resource; see [DISCLAIMER.md](DISCLAIMER.md).

Last verified: {latest}.
"""


def main() -> int:
    records = read_csv(SOURCE)
    screening = read_csv(SCREENING)
    JSON_OUT.write_text(json_view(records), encoding="utf-8")
    YAML_OUT.write_text(yaml_view(records), encoding="utf-8")
    README_OUT.write_text(build_readme(records, screening), encoding="utf-8")
    print(f"Built {len(records)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
