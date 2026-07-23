"""Negative tests for controlled vocabulary, evidence, and drift gates."""

from __future__ import annotations

import csv
import io
import json
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_catalogue
import validate_equations
import validate_references


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_rows(
    path: Path, fields: list[str], rows: list[dict[str, str]]
) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            lineterminator="\n",
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(rows)


class ValidationGateTests(unittest.TestCase):
    def run_quietly(self, function) -> int:
        with redirect_stdout(io.StringIO()):
            return function()

    def test_invalid_controlled_vocabulary_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            catalogue = Path(directory) / "catalogue.csv"
            shutil.copyfile(ROOT / "models" / "model_catalog.csv", catalogue)
            fields, rows = read_rows(catalogue)
            rows[0]["model_scale"] = "invalid_scale"
            write_rows(catalogue, fields, rows)
            with patch.object(validate_catalogue, "CATALOGUE", catalogue):
                self.assertEqual(self.run_quietly(validate_catalogue.main), 1)

    def test_missing_required_field_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            catalogue = Path(directory) / "catalogue.csv"
            fields, rows = read_rows(ROOT / "models" / "model_catalog.csv")
            fields.remove("event_handling_locator")
            write_rows(catalogue, fields, rows)
            with patch.object(validate_catalogue, "CATALOGUE", catalogue):
                self.assertEqual(self.run_quietly(validate_catalogue.main), 1)

    def test_independent_status_without_checker_fields_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            models = temp / "models.csv"
            audit = temp / "audit.csv"
            variables = temp / "variables.csv"
            parameters = temp / "parameters.csv"
            for source, target in (
                (ROOT / "models" / "model_catalog.csv", models),
                (ROOT / "data" / "equations" / "equation_audit.csv", audit),
                (ROOT / "data" / "equations" / "variable_registry.csv", variables),
                (ROOT / "data" / "equations" / "parameter_registry.csv", parameters),
            ):
                shutil.copyfile(source, target)
            model_fields, model_rows = read_rows(models)
            model_rows[0]["equation_status"] = "independently_checked"
            write_rows(models, model_fields, model_rows)
            audit_fields, audit_rows = read_rows(audit)
            for row in audit_rows:
                if row["model_id"] == model_rows[0]["model_id"]:
                    row["verification_status"] = "independently_checked"
            write_rows(audit, audit_fields, audit_rows)
            with (
                patch.object(validate_equations, "MODELS", models),
                patch.object(validate_equations, "AUDIT", audit),
                patch.object(validate_equations, "VARIABLES", variables),
                patch.object(validate_equations, "PARAMETERS", parameters),
            ):
                self.assertEqual(self.run_quietly(validate_equations.main), 1)

    def test_generated_json_drift_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            generated = Path(directory) / "model_catalog.json"
            payload = json.loads(
                (ROOT / "models" / "model_catalog.json").read_text(
                    encoding="utf-8"
                )
            )
            payload["_generated_notice"] = "stale"
            generated.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            with patch.object(validate_references, "JSON_VIEW", generated):
                self.assertEqual(self.run_quietly(validate_references.main), 1)

    def test_registry_model_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            variables = Path(directory) / "variables.csv"
            fields, rows = read_rows(
                ROOT / "data" / "equations" / "variable_registry.csv"
            )
            rows[0]["model_id"] = "unknown_model"
            write_rows(variables, fields, rows)
            with patch.object(validate_equations, "VARIABLES", variables):
                self.assertEqual(self.run_quietly(validate_equations.main), 1)


if __name__ == "__main__":
    unittest.main()
