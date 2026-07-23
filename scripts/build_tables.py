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
EQUATION_INDEX_OUT = ROOT / "equations" / "README.md"
SCREENING = ROOT / "references" / "model_screening_master.csv"
REFERENCES_OUT = ROOT / "references" / "references.csv"
BIB_OUT = ROOT / "references" / "references.bib"
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
        "| Model ID | Model | Biological scope | Cell or network type | Scale | Equation status | Primary source | Equation locator | Review scope |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in records:
        lines.append(
            "| `{model_id}` | [{model_name}]({equation_page}) | "
            "`{biological_cell_scope}` | `{cell_type}` / `{network_type}` | "
            "`{model_scale}` | `{equation_status}` | "
            "[DOI]({paper_url}) | {equation_source_locator} | "
            "{review_scope} |".format(
                **{
                    **{key: markdown_cell(value) for key, value in record.items()},
                    "review_scope": (
                        "independent check documented"
                        if record["equation_status"] == "independently_checked"
                        else (
                            "maintainer second pass"
                            if record["equation_status"] == "second_pass_checked"
                            else (
                                "transcribed; review pending"
                                if record["equation_status"]
                                == "equation_transcribed"
                                else (
                                    "source located; transcription pending"
                                    if record["equation_status"]
                                    == "equation_located"
                                    else "bibliography only"
                                )
                            )
                        )
                    ),
                }
            )
        )
    return "\n".join(lines)


def implementation_table(records: list[dict[str, str]]) -> str:
    lines = [
        "| Model | Brian2 compatibility | Implementation | Numerical tests | Reference behavior | Reproduction |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for record in records:
        lines.append(
            "| {model_name} | `{brian2_compatibility}` | "
            "`{brian2_implementation_status}` | `{numerical_test_status}` | "
            "`{reference_behavior_status}` | `{reproduction_status}` |".format(
                **{key: markdown_cell(value) for key, value in record.items()}
            )
        )
    return "\n".join(lines)


def reference_csv(records: list[dict[str, str]]) -> str:
    fields = [
        "reference_key",
        "title",
        "authors",
        "year",
        "journal",
        "doi",
        "pmid",
        "persistent_url",
        "open_access_status",
        "code_url",
        "code_license",
        "last_verified",
    ]
    from io import StringIO

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for record in records:
        writer.writerow(
            {
                "reference_key": record["model_id"],
                "title": record["original_paper_title"],
                "authors": record["original_paper_authors"],
                "year": record["publication_year"],
                "journal": record["journal"],
                "doi": record["doi"],
                "pmid": record["pmid"],
                "persistent_url": record["paper_url"],
                "open_access_status": record["open_access_status"],
                "code_url": record["code_url"],
                "code_license": record["code_license"],
                "last_verified": record["last_verified"],
            }
        )
    return output.getvalue()


def bib_view(records: list[dict[str, str]]) -> str:
    entries: list[str] = []
    for record in records:
        entry_type = (
            "inproceedings"
            if "Conference" in record["journal"]
            or "Lecture Notes" in record["journal"]
            else "article"
        )
        authors = record["original_paper_authors"].replace("; ", " and ")
        entries.append(
            f"@{entry_type}{{{record['model_id']},\n"
            f"  author = {{{authors}}},\n"
            f"  title = {{{record['original_paper_title']}}},\n"
            f"  {'booktitle' if entry_type == 'inproceedings' else 'journal'} = "
            f"{{{record['journal']}}},\n"
            f"  year = {{{record['publication_year']}}},\n"
            f"  doi = {{{record['doi']}}}\n"
            "}"
        )
    return "\n\n".join(entries) + "\n"


def equation_index(records: list[dict[str, str]]) -> str:
    local_records = [
        {**record, "equation_page": record["equation_page"].removeprefix("equations/")}
        for record in records
    ]
    return f"""<!-- {GENERATED_NOTICE} -->
# Equation evidence index

This index is generated from the canonical catalogue. Evidence states remain separate: a bibliography-only record has no source-specific displayed equation, `equation_located` records await transcription, `equation_transcribed` records await review, `second_pass_checked` records have a maintainer check, and `independently_checked` requires a separate documented checker.

{model_table(local_records)}
"""


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
    screening_counts: dict[str, int] = {}
    for row in screening:
        screening_counts[row["screening_status"]] = (
            screening_counts.get(row["screening_status"], 0) + 1
        )
    screening_summary = "\n".join(
        f"- `{status}`: **{count}**"
        for status, count in sorted(screening_counts.items())
    )
    return f"""<!-- {GENERATED_NOTICE} -->
# Neurocell Mathematical Models

> A traceable, copyright-compliant atlas of mathematical and computational models for nervous-system cells.

This repository is an equation-level knowledge base, not a paper mirror or a collection of third-party code. It separates bibliography verification, equation transcription, maintainer second-pass checking, and genuinely independent checking. A model-family screening item is never treated as a source-specific verified model without an identified primary source.

## Coverage summary

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

## Model catalogue

{model_table(records)}

## Equation evidence records

The unified table above preserves each row-level equation state. `second_pass_checked` remains a maintainer review state and is never treated as `independently_checked`. Located-only records do not display transcribed equations, and bibliography-only holding records do not display reconstructed source-specific equations.

## Implementation and numerical validation

{implementation_table(records)}

Compatibility is a feasibility classification, not execution evidence. A passing smoke test supports `implementation_only`; it is not a paper-result reproduction.

## Screening inventory

{screening_summary}

Every requested inventory row has exactly one current screening outcome. A `candidate` row has passed title-level scope screening but still lacks source-specific evidence.

## Evidence-status definitions

- `bibliography_verified`: publication identity is verified, but equation evidence is not.
- `equation_located`: a lawful direct source and exact locator were inspected; no transcription is claimed.
- `equation_transcribed`: source equations are transcribed and registered, but review is pending.
- `second_pass_checked`: the maintainer workflow completed a second pass.
- `independently_checked`: a separate checker followed the frozen-source protocol and resolved discrepancies.
- Parameter completeness, implementation, numerical tests, reference behavior, and paper-result reproduction remain independent status dimensions.

## Canonical data and generated views

The only hand-maintained model catalogue is [models/model_catalog.csv](models/model_catalog.csv). [JSON](models/model_catalog.json), [YAML](models/model_catalog.yaml), this README, the [equation index](equations/README.md), and bibliography views are generated by `python scripts/build_tables.py`.

Every displayed equation has an audit row in [data/equations/equation_audit.csv](data/equations/equation_audit.csv). The complete requested screening scope is tracked in [references/model_screening_master.csv](references/model_screening_master.csv), with a line-level request snapshot in [references/model_screening_inventory.csv](references/model_screening_inventory.csv).

## Evidence and copyright boundary

Equation pages require a lawful source, a precise locator, a transcription type, and an audit row. The repository stores original explanatory prose and concise cited mathematics only; it does not distribute paper PDFs, publisher figures, copied tables, supplements, unlicensed third-party code, or unauthorized data. Paper access status and code-license status are recorded separately.

## Navigation

- [Equation index](equations/README.md)
- [Equation curation protocol](docs/equation_curation_protocol.md)
- [Evidence-status migration](docs/evidence_status_migration.md)
- [Independent-review protocol](docs/independent_review_protocol.md)
- [Equation notation policy](docs/equation_notation_policy.md)
- [Model scope taxonomy](docs/model_scope_taxonomy.md)
- [Cell-type pages](docs/cell_types/README.md)
- [Research gaps](docs/research_gaps.md)
- [Screening master](references/model_screening_master.csv)
- [Data dictionary](docs/data_dictionary.md)
- [Contribution guide](docs/CONTRIBUTING.md)

## Canonical catalogue coverage

{coverage}

Neuron-microglia models, explicit oligodendrocyte-myelin networks, Schwann-cell models, neurovascular multicellular models, and other-cell categories remain evidence-gated screening items unless a source-specific canonical record says otherwise.

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
    EQUATION_INDEX_OUT.write_text(equation_index(records), encoding="utf-8")
    REFERENCES_OUT.write_text(reference_csv(records), encoding="utf-8")
    BIB_OUT.write_text(bib_view(records), encoding="utf-8")
    print(f"Built {len(records)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
