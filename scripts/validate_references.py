"""Validate references, generated views, screening coverage, and archive boundaries."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

from build_tables import build_readme, json_view, yaml_view


ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models" / "model_catalog.csv"
JSON_VIEW = ROOT / "models" / "model_catalog.json"
YAML_VIEW = ROOT / "models" / "model_catalog.yaml"
README_VIEW = ROOT / "README.md"
REFERENCES = ROOT / "references" / "references.csv"
CANDIDATES = ROOT / "references" / "screening_candidates.csv"
SCREENING = ROOT / "references" / "model_screening_master.csv"
SCREENING_INVENTORY = ROOT / "references" / "model_screening_inventory.csv"
VERIFICATION_AUDIT = ROOT / "references" / "verification_audit.csv"
BIB = ROOT / "references" / "references.bib"
DOI_RE = re.compile(r"10\.[^\s/]+/.+", re.I)
BIB_KEY_RE = re.compile(r"^@\w+\{([^,]+),", re.M)
FORBIDDEN_SUFFIXES = {".pdf", ".epub", ".mobi", ".zip", ".rar", ".7z", ".tar", ".gz"}
THIRD_PARTY_CODE_SUFFIXES = {
    ".c", ".cc", ".cpp", ".h", ".hpp", ".java", ".js", ".m", ".r", ".rs", ".ts", ".ipynb"
}
EQUATION_STATUSES = {
    "equation_located",
    "equation_transcribed",
    "second_pass_checked",
    "independently_checked",
}
SCREENING_STATUSES = {
    "search_queue",
    "candidate",
    "bibliography_verified",
    "equation_screening",
    "promoted",
    "excluded",
    "not_verified",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def check_dois(rows: list[dict[str, str]], field: str, label: str, errors: list[str]) -> None:
    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        doi = row.get(field, "").strip().lower()
        if not DOI_RE.fullmatch(doi):
            errors.append(f"{label}:{index}: invalid DOI")
        if doi in seen:
            errors.append(f"{label}:{index}: duplicate DOI {doi}")
        seen.add(doi)
        url = row.get("paper_url") or row.get("persistent_url") or ""
        if url != f"https://doi.org/{doi}":
            errors.append(f"{label}:{index}: DOI URL is not canonical")


def main() -> int:
    errors: list[str] = []
    models = read_csv(MODELS)
    references = read_csv(REFERENCES)
    candidates = read_csv(CANDIDATES)
    screening = read_csv(SCREENING)
    inventory = read_csv(SCREENING_INVENTORY)
    verification_audit = read_csv(VERIFICATION_AUDIT)
    required = {
        "model_id", "model_name", "cell_type", "doi", "paper_url", "last_verified", "model_scope",
        "equation_page", "equation_status", "equation_source_locator", "equation_verification_source",
        "equation_transcription_type", "variable_registry_status", "parameter_registry_status",
        "initial_conditions_status", "boundary_conditions_status", "numerical_method_status",
        "full_text_access_status", "code_license_status",
    }
    if not models or not required.issubset(models[0]):
        errors.append("models: missing required equation-aware catalogue columns")
    ids = [row.get("model_id", "") for row in models]
    if len(ids) != len(set(ids)):
        errors.append("models: duplicate model_id")
    audit_ids = [row.get("model_id", "") for row in verification_audit]
    if set(audit_ids) != set(ids) or len(audit_ids) != len(set(audit_ids)):
        errors.append("verification audit must cover every canonical model exactly once")
    check_dois(models, "doi", "models", errors)
    check_dois(references, "doi", "references", errors)
    check_dois(candidates, "doi", "candidates", errors)
    for index, row in enumerate(models, start=2):
        if row.get("code_url", "").strip() and not row.get("code_license", "").strip():
            errors.append(f"models:{index}: external code URL needs a license status")
        page = ROOT / row.get("equation_page", "")
        if not page.exists():
            errors.append(f"models:{index}: referenced equation page is missing")
        if row.get("equation_status") in EQUATION_STATUSES:
            if row.get("equation_source_locator") in {"", "not verified"}:
                errors.append(f"models:{index}: transcribed status needs a source locator")
            if row.get("equation_transcription_type") in {"", "not applicable"}:
                errors.append(f"models:{index}: transcribed status needs a transcription type")
        matching_audit = [
            audit_row
            for audit_row in verification_audit
            if audit_row.get("model_id") == row.get("model_id")
        ]
        if (
            row.get("equation_status") in EQUATION_STATUSES
            and matching_audit
            and matching_audit[0].get("equations_inspected") != "yes"
        ):
            errors.append(
                f"models:{index}: equation status conflicts with verification audit"
            )
    keys = BIB_KEY_RE.findall(BIB.read_text(encoding="utf-8"))
    if len(keys) != len(set(keys)):
        errors.append("references.bib: duplicate BibTeX key")
    generated_json = JSON_VIEW.read_text(encoding="utf-8")
    if generated_json != json_view(models):
        errors.append("model_catalog.json is stale; run python scripts/build_tables.py")
    if YAML_VIEW.read_text(encoding="utf-8") != yaml_view(models):
        errors.append("model_catalog.yaml is stale; run python scripts/build_tables.py")
    if README_VIEW.read_text(encoding="utf-8") != build_readme(models, screening):
        errors.append("README.md is stale; run python scripts/build_tables.py")

    screening_required = {
        "screening_id",
        "source_inventory_line",
        "requested_model_or_family",
        "category",
        "cell_type",
        "model_scope_candidate",
        "specific_source_identified",
        "primary_source_title",
        "doi",
        "metadata_status",
        "full_text_access_status",
        "equation_evidence_status",
        "parameter_evidence_status",
        "code_identified",
        "code_url",
        "code_license_status",
        "screening_status",
        "exclusion_or_hold_reason",
        "priority",
        "last_checked",
    }
    if not screening or not screening_required.issubset(screening[0]):
        errors.append("screening master is missing required columns")
    screening_ids: set[str] = set()
    screening_keys: list[tuple[str, str, str]] = []
    for index, row in enumerate(screening, start=2):
        screening_id = row.get("screening_id", "")
        if not screening_id or screening_id in screening_ids:
            errors.append(f"screening:{index}: missing or duplicate screening_id")
        screening_ids.add(screening_id)
        if row.get("screening_status") not in SCREENING_STATUSES:
            errors.append(f"screening:{index}: invalid screening_status")
        doi = row.get("doi", "").strip().lower()
        if doi and not DOI_RE.fullmatch(doi):
            errors.append(f"screening:{index}: invalid DOI")
        if row.get("specific_source_identified") == "yes":
            if not row.get("primary_source_title") or not doi:
                errors.append(
                    f"screening:{index}: identified source needs title and DOI"
                )
        elif row.get("screening_status") in {
            "bibliography_verified",
            "equation_screening",
            "promoted",
        }:
            errors.append(
                f"screening:{index}: promoted evidence needs an identified source"
            )
        if row.get("code_url") and row.get("code_license_status") == "not_assessed":
            errors.append(
                f"screening:{index}: external code URL needs a license status"
            )
        screening_keys.append(
            (
                row.get("source_inventory_line", ""),
                row.get("category", ""),
                row.get("requested_model_or_family", ""),
            )
        )
    inventory_keys = [
        (
            row.get("source_inventory_line", ""),
            row.get("category", ""),
            row.get("requested_model_or_family", ""),
        )
        for row in inventory
    ]
    if screening_keys != inventory_keys:
        errors.append(
            "screening master does not cover the request inventory exactly once and in order"
        )

    for path in ROOT.rglob("*"):
        if ".git" not in path.parts and path.is_file() and path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden archive-like file: {path.relative_to(ROOT)}")
        if (
            ".git" not in path.parts
            and path.is_file()
            and path.suffix.lower() in THIRD_PARTY_CODE_SUFFIXES
        ):
            errors.append(
                f"unreviewed third-party-code file type: {path.relative_to(ROOT)}"
            )
    if errors:
        print("Reference validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Reference validation passed: {len(models)} core records, {len(candidates)} candidates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
