"""Validate the CSV catalogue without requiring third-party packages."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "data" / "models" / "catalogue.csv"
SCHEMA = ROOT / "data" / "models" / "catalogue.schema.json"


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
    with CATALOGUE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        if set(headers) != allowed:
            errors.append("catalogue headers must exactly match schema properties")
        for line, row in enumerate(reader, start=2):
            for field in required:
                if not row.get(field, "").strip():
                    errors.append(f"line {line}: missing {field}")
            model_id = row.get("model_id", "")
            if model_id in ids:
                errors.append(f"line {line}: duplicate model_id {model_id}")
            ids.add(model_id)
            if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", model_id):
                errors.append(f"line {line}: invalid model_id")
            doi = row.get("primary_source_doi", "")
            if not re.fullmatch(r"10\.[^\s/]+/.+", doi):
                errors.append(f"line {line}: invalid DOI")
            if row.get("persistent_url") != f"https://doi.org/{doi}":
                errors.append(f"line {line}: persistent_url must be canonical DOI URL")
            for field, allowed_values in enum_fields.items():
                if row.get(field) not in allowed_values:
                    errors.append(f"line {line}: invalid {field}={row.get(field)!r}")
    if errors:
        print("Catalogue validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Catalogue validation passed: {len(ids)} records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
