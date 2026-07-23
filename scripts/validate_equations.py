"""Validate equation pages, audit evidence, and registry coverage."""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models" / "model_catalog.csv"
AUDIT = ROOT / "data" / "equations" / "equation_audit.csv"
VARIABLES = ROOT / "data" / "equations" / "variable_registry.csv"
PARAMETERS = ROOT / "data" / "equations" / "parameter_registry.csv"
INDEPENDENT_TEMPLATE = (
    ROOT / "data" / "equations" / "independent_review_template.csv"
)
LOCATED = {
    "equation_located",
    "equation_transcribed",
    "second_pass_checked",
    "independently_checked",
}
DISPLAYED = {
    "equation_transcribed",
    "second_pass_checked",
    "independently_checked",
}
NO_DISPLAY = {
    "not_verified",
    "bibliography_verified",
    "full_text_unavailable",
    "license_unclear",
}
AUDIT_FIELDS = {
    "equation_id",
    "model_id",
    "equation_page",
    "source_locator",
    "equation_verification_source",
    "equation_transcription_type",
    "verification_status",
    "source_version",
    "source_access_date",
    "checker_name",
    "checker_role",
    "check_date",
    "check_method",
    "source_identifier",
    "frozen_commit_sha",
    "discrepancies_found",
    "discrepancy_resolution",
    "resolution_date",
}
INDEPENDENT_FIELDS = {
    "checker_name",
    "checker_role",
    "check_date",
    "check_method",
    "source_identifier",
    "source_version",
    "source_access_date",
    "frozen_commit_sha",
    "discrepancies_found",
    "discrepancy_resolution",
    "resolution_date",
}
PLACEHOLDERS = {"", "not_verified", "not verified", "not_applicable"}
INDEPENDENT_TEMPLATE_FIELDS = [
    "equation_id",
    "model_id",
    "checker_name",
    "checker_role",
    "check_date",
    "check_method",
    "source_identifier",
    "source_version",
    "source_access_date",
    "frozen_commit_sha",
    "discrepancies_found",
    "discrepancy_resolution",
    "resolution_date",
]


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
    audit_counts: Counter[str] = Counter()

    with INDEPENDENT_TEMPLATE.open(encoding="utf-8", newline="") as handle:
        template_fields = csv.DictReader(handle).fieldnames or []
    if template_fields != INDEPENDENT_TEMPLATE_FIELDS:
        errors.append("independent review template has unexpected fields")

    if audit and not AUDIT_FIELDS.issubset(audit[0]):
        errors.append("audit: missing strict provenance or independent-check columns")
    for line, row in enumerate(audit, start=2):
        equation_id = row.get("equation_id", "")
        if not equation_id or equation_id in audit_ids:
            errors.append(f"audit:{line}: missing or duplicate equation_id")
        audit_ids.add(equation_id)
        model_id = row.get("model_id", "")
        if model_id not in ids:
            errors.append(f"audit:{line}: unknown model_id")
        audited_models.add(model_id)
        audit_counts[model_id] += 1
        for field in (
            "equation_page",
            "source_locator",
            "equation_verification_source",
            "equation_transcription_type",
            "verification_status",
            "source_version",
            "source_access_date",
        ):
            if not row.get(field, "").strip():
                errors.append(f"audit:{line}: missing {field}")
        if row.get("verification_status") == "independently_checked":
            unconditional = INDEPENDENT_FIELDS - {
                "discrepancy_resolution",
                "resolution_date",
            }
            for field in unconditional:
                if row.get(field, "").strip() in PLACEHOLDERS:
                    errors.append(
                        f"audit:{line}: independently checked row needs {field}"
                    )
            discrepancy = row.get("discrepancies_found", "").strip()
            if discrepancy not in {"yes", "no"}:
                errors.append(
                    f"audit:{line}: independently checked row needs yes/no discrepancies_found"
                )
            if discrepancy == "yes":
                for field in ("discrepancy_resolution", "resolution_date"):
                    if row.get(field, "").strip() in PLACEHOLDERS:
                        errors.append(
                            f"audit:{line}: resolved discrepancy needs {field}"
                        )

    variable_models = {row.get("model_id", "") for row in variables}
    parameter_models = {row.get("model_id", "") for row in parameters}
    for label, rows in (("variables", variables), ("parameters", parameters)):
        seen: set[tuple[str, str]] = set()
        key_field = "symbol" if label == "variables" else "parameter"
        for line, row in enumerate(rows, start=2):
            model_id = row.get("model_id", "")
            if model_id not in ids:
                errors.append(f"{label}:{line}: unknown model_id")
            key = (model_id, row.get(key_field, ""))
            if not key[1] or key in seen:
                errors.append(f"{label}:{line}: missing or duplicate {key_field}")
            seen.add(key)
            if label == "variables" and not row.get("source_status"):
                errors.append(f"{label}:{line}: missing source_status")
            if label == "parameters" and not row.get("status"):
                errors.append(f"{label}:{line}: missing status")

    for row in models:
        model_id = row["model_id"]
        page = ROOT / row["equation_page"]
        if not page.exists():
            errors.append(f"models:{model_id}: missing equation page")
            continue
        page_text = page.read_text(encoding="utf-8")
        for heading in (
            "## Verification status",
            "## Source citation",
            "## Variables",
            "## Parameters",
            "## Equations",
            "## Inputs, outputs, and conditions",
            "## Assumptions and limitations",
            "## Reproducibility and code",
        ):
            if heading not in page_text:
                errors.append(f"models:{model_id}: missing {heading}")
        status = row["equation_status"]
        displayed_blocks = len(re.findall(r"(?m)^\$\$\s*$", page_text)) // 2
        if status in DISPLAYED:
            if model_id not in audited_models:
                errors.append(f"models:{model_id}: equation status needs audit rows")
            if model_id not in variable_models:
                errors.append(f"models:{model_id}: displayed equations need variables")
            if model_id not in parameter_models:
                errors.append(f"models:{model_id}: displayed equations need parameters")
            if displayed_blocks == 0:
                errors.append(f"models:{model_id}: equation status needs displayed math")
            if audit_counts[model_id] < displayed_blocks:
                errors.append(
                    f"models:{model_id}: fewer audit rows than displayed equation blocks"
                )
        if status == "equation_located":
            if model_id not in audited_models:
                errors.append(f"models:{model_id}: located status needs audit rows")
            if displayed_blocks:
                errors.append(
                    f"models:{model_id}: located-only status must not display equations"
                )
            model_audit = [
                audit_row
                for audit_row in audit
                if audit_row.get("model_id") == model_id
            ]
            if not model_audit or any(
                audit_row.get("verification_status") != "equation_located"
                or audit_row.get("equation_transcription_type") != "not_applicable"
                for audit_row in model_audit
            ):
                errors.append(
                    f"models:{model_id}: located-only audit rows claim stronger evidence"
                )
        if status in NO_DISPLAY and displayed_blocks:
            errors.append(
                f"models:{model_id}: {status} page must not display model-specific equations"
            )
        if status == "independently_checked":
            model_audit = [
                audit_row
                for audit_row in audit
                if audit_row.get("model_id") == model_id
            ]
            if not model_audit or any(
                audit_row.get("verification_status") != "independently_checked"
                for audit_row in model_audit
            ):
                errors.append(
                    f"models:{model_id}: independent status is not supported by every audit row"
                )

    if errors:
        print("Equation validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(
        "Equation validation passed: "
        f"{len(audit)} equations, {len(variables)} variables, "
        f"{len(parameters)} parameters"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
