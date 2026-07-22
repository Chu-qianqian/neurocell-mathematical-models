"""Validate reference metadata, generated catalogue views, and archive boundaries."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models" / "model_catalog.csv"
JSON_VIEW = ROOT / "models" / "model_catalog.json"
YAML_VIEW = ROOT / "models" / "model_catalog.yaml"
REFERENCES = ROOT / "references" / "references.csv"
CANDIDATES = ROOT / "references" / "screening_candidates.csv"
BIB = ROOT / "references" / "references.bib"
DOI_RE = re.compile(r"10\.[^\s/]+/.+", re.I)
BIB_KEY_RE = re.compile(r"^@\w+\{([^,]+),", re.M)
FORBIDDEN_SUFFIXES = {".pdf", ".epub", ".mobi", ".zip", ".rar", ".7z", ".tar", ".gz"}
EQUATION_STATUSES = {"equation_located", "equation_transcribed", "independently_checked"}


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


def yaml_view(records: list[dict[str, str]]) -> str:
    lines = ["# Generated from models/model_catalog.csv; do not edit by hand."]
    for record in records:
        lines.append("- model_id: " + json.dumps(record["model_id"], ensure_ascii=False))
        for key, value in record.items():
            if key != "model_id":
                lines.append(f"  {key}: {json.dumps(value, ensure_ascii=False)}")
    return "\n".join(lines) + "\n"


def main() -> int:
    errors: list[str] = []
    models = read_csv(MODELS)
    references = read_csv(REFERENCES)
    candidates = read_csv(CANDIDATES)
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
    keys = BIB_KEY_RE.findall(BIB.read_text(encoding="utf-8"))
    if len(keys) != len(set(keys)):
        errors.append("references.bib: duplicate BibTeX key")
    generated_json = json.loads(JSON_VIEW.read_text(encoding="utf-8"))
    if generated_json != models:
        errors.append("model_catalog.json is stale; run python scripts/build_tables.py")
    if YAML_VIEW.read_text(encoding="utf-8") != yaml_view(models):
        errors.append("model_catalog.yaml is stale; run python scripts/build_tables.py")
    for path in ROOT.rglob("*"):
        if ".git" not in path.parts and path.is_file() and path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden archive-like file: {path.relative_to(ROOT)}")
    if errors:
        print("Reference validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Reference validation passed: {len(models)} core records, {len(candidates)} candidates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
