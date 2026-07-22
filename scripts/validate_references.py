"""Validate atlas reference files and generated catalogue views offline."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models" / "model_catalog.csv"
JSON_VIEW = ROOT / "models" / "model_catalog.json"
REFERENCES = ROOT / "references" / "references.csv"
CANDIDATES = ROOT / "references" / "screening_candidates.csv"
BIB = ROOT / "references" / "references.bib"
DOI_RE = re.compile(r"10\.[^\s/]+/.+", re.I)
BIB_KEY_RE = re.compile(r"^@\w+\{([^,]+),", re.M)


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
    required = {"model_id", "model_name", "cell_type", "doi", "paper_url", "last_verified", "model_scope"}
    if not models or not required.issubset(models[0]):
        errors.append("models: missing required extended-catalogue columns")
    ids = [row.get("model_id", "") for row in models]
    if len(ids) != len(set(ids)):
        errors.append("models: duplicate model_id")
    check_dois(models, "doi", "models", errors)
    check_dois(references, "doi", "references", errors)
    check_dois(candidates, "doi", "candidates", errors)
    for index, row in enumerate(models, start=2):
        if row.get("code_url", "").strip() and not row.get("code_license", "").strip():
            errors.append(f"models:{index}: external code URL needs a license status")
    keys = BIB_KEY_RE.findall(BIB.read_text(encoding="utf-8"))
    if len(keys) != len(set(keys)):
        errors.append("references.bib: duplicate BibTeX key")
    generated = json.loads(JSON_VIEW.read_text(encoding="utf-8"))
    if generated != models:
        errors.append("model_catalog.json is stale; run python scripts/build_tables.py")
    if errors:
        print("Reference validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Reference validation passed: {len(models)} core records, {len(candidates)} candidates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
