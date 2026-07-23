"""Validate the canonical model catalogue without third-party packages."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "models" / "model_catalog.csv"
SCHEMA = ROOT / "models" / "schema.json"
DOI_RE = re.compile(r"10\.[^\s/]+/.+", re.I)
LOCATED_OR_STRONGER = {
    "equation_located",
    "equation_transcribed",
    "second_pass_checked",
    "independently_checked",
}
TRANSCRIBED = {
    "equation_transcribed",
    "second_pass_checked",
    "independently_checked",
}
EXECUTED = {
    "syntax_checked",
    "smoke_tested",
    "reference_behavior_reproduced",
}


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required = schema["required"]
    allowed = set(schema["properties"])
    enum_fields = {
        field: set(spec["enum"])
        for field, spec in schema["properties"].items()
        if "enum" in spec
    }
    errors: list[str] = []
    ids: set[str] = set()
    dois: set[str] = set()
    rows: list[dict[str, str]] = []
    with CATALOGUE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        if headers != required or set(headers) != allowed:
            errors.append("catalogue headers must exactly match schema properties")
        for line, row in enumerate(reader, start=2):
            rows.append(row)
            for field in required:
                if field not in row:
                    errors.append(f"line {line}: missing column {field}")
            for field in (
                "model_id",
                "model_name",
                "cell_type",
                "doi",
                "paper_url",
                "equation_page",
                "equation_status",
                "last_verified",
                "brian2_compatibility",
                "brian2_implementation_status",
                "reproduction_status",
            ):
                if not row.get(field, "").strip():
                    errors.append(f"line {line}: missing {field}")

            model_id = row.get("model_id", "")
            if model_id in ids:
                errors.append(f"line {line}: duplicate model_id {model_id}")
            ids.add(model_id)
            if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", model_id):
                errors.append(f"line {line}: invalid model_id")

            doi = row.get("doi", "").strip().lower()
            if not DOI_RE.fullmatch(doi):
                errors.append(f"line {line}: invalid DOI")
            if doi in dois:
                errors.append(f"line {line}: duplicate DOI {doi}")
            dois.add(doi)
            if row.get("paper_url", "").lower() != f"https://doi.org/{doi}":
                errors.append(f"line {line}: paper_url must be the canonical DOI URL")

            for field, allowed_values in enum_fields.items():
                if row.get(field) not in allowed_values:
                    errors.append(
                        f"line {line}: invalid {field}={row.get(field)!r}"
                    )

            status = row.get("equation_status", "")
            if status in LOCATED_OR_STRONGER:
                if row.get("equation_source_locator") in {"", "not_verified"}:
                    errors.append(
                        f"line {line}: equation evidence needs a source locator"
                    )
            if status in TRANSCRIBED:
                if row.get("equation_transcription_type") == "not_applicable":
                    errors.append(
                        f"line {line}: equation evidence needs a transcription type"
                    )
            if (
                status == "equation_located"
                and row.get("equation_transcription_type") != "not_applicable"
            ):
                errors.append(
                    f"line {line}: located-only evidence must not claim transcription"
                )

            for prefix in ("network_conditions", "event_handling"):
                condition_status = row.get(f"{prefix}_status", "")
                locator = row.get(f"{prefix}_locator", "")
                if condition_status in {"source_located", "registered"} and locator in {
                    "",
                    "not_verified",
                    "not_applicable",
                }:
                    errors.append(
                        f"line {line}: {prefix} evidence needs a source locator"
                    )
                if condition_status == "not_applicable" and locator != "not_applicable":
                    errors.append(
                        f"line {line}: {prefix} not_applicable needs matching locator"
                    )

            code_url = row.get("code_url", "").strip()
            if code_url and row.get("code_license_status") == "not_assessed":
                errors.append(
                    f"line {line}: external code URL needs an explicit license status"
                )

            brian_status = row.get("brian2_implementation_status", "")
            if brian_status in EXECUTED:
                if row.get("brian2_version") in {"", "not_applicable"}:
                    errors.append(
                        f"line {line}: executed Brian2 status needs a version"
                    )
                if row.get("numerical_test_status") != "passed":
                    errors.append(
                        f"line {line}: executed Brian2 status needs a passed test"
                    )
            if (
                row.get("reproduction_status") != "not_attempted"
                and brian_status == "not_implemented"
            ):
                errors.append(
                    f"line {line}: reproduction cannot precede implementation"
                )

    for line, row in enumerate(rows, start=2):
        parent = row.get("parent_model_id", "")
        if parent and parent not in ids:
            errors.append(f"line {line}: unknown parent_model_id {parent}")
        related = [
            item.strip()
            for item in row.get("related_model_ids", "").split(";")
            if item.strip()
        ]
        if row.get("model_id") in related:
            errors.append(f"line {line}: related_model_ids contains the model itself")
        for related_id in related:
            if related_id not in ids:
                errors.append(f"line {line}: unknown related_model_id {related_id}")

    if errors:
        print("Catalogue validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Catalogue validation passed: {len(ids)} canonical records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
