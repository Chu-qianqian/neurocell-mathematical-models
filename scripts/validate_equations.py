"""Validate source-traceable equation pages and registry rows."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models" / "model_catalog.csv"
AUDIT = ROOT / "data" / "equations" / "equation_audit.csv"
VARIABLES = ROOT / "data" / "equations" / "variable_registry.csv"
PARAMETERS = ROOT / "data" / "equations" / "parameter_registry.csv"
DISPLAYED = {"equation_located", "equation_transcribed", "independently_checked"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    models = read_csv(MODELS)
    audit = read_csv(AUDIT)
    variables = read_csv(VARIABLES)
    parameters = read_csv(PARAMETERS)
    errors: list[str] = []
    ids = {row["model_id"] for row in models}
    audit_ids: set[str] = set()
    audited_models: set[str] = set()
    for line, row in enumerate(audit, start=2):
        equation_id = row.get("equation_id", "")
        if not equation_id or equation_id in audit_ids:
            errors.append(f"audit:{line}: missing or duplicate equation_id")
        audit_ids.add(equation_id)
        if row.get("model_id") not in ids:
            errors.append(f"audit:{line}: unknown model_id")
        audited_models.add(row.get("model_id", ""))
        for field in ("equation_page", "source_locator", "equation_verification_source", "equation_transcription_type", "verification_status"):
            if not row.get(field, "").strip():
                errors.append(f"audit:{line}: missing {field}")
    for label, rows in (("variables", variables), ("parameters", parameters)):
        for line, row in enumerate(rows, start=2):
            if row.get("model_id") not in ids:
                errors.append(f"{label}:{line}: unknown model_id")
            if not row.get("source_status") and label == "variables":
                errors.append(f"{label}:{line}: missing source_status")
            if not row.get("status") and label == "parameters":
                errors.append(f"{label}:{line}: missing status")
    for row in models:
        page = ROOT / row["equation_page"]
        if not page.exists():
            errors.append(f"models:{row['model_id']}: missing equation page")
            continue
        page_text = page.read_text(encoding="utf-8")
        for heading in ("## Verification status", "## Source citation", "## Variables", "## Parameters", "## Equations"):
            if heading not in page_text:
                errors.append(f"models:{row['model_id']}: missing {heading}")
        if row["equation_status"] in DISPLAYED and row["model_id"] not in audited_models:
            errors.append(f"models:{row['model_id']}: displayed equation status needs audit rows")
    if errors:
        print("Equation validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Equation validation passed: {len(audit)} equations, {len(variables)} variables, {len(parameters)} parameters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
