"""Build JSON and YAML views from the extended model catalogue.

The CSV is the hand-curated source of truth. Generated files contain no
third-party text and may be regenerated with `python scripts/build_tables.py`.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "models" / "model_catalog.csv"
JSON_OUT = ROOT / "models" / "model_catalog.json"
YAML_OUT = ROOT / "models" / "model_catalog.yaml"


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def main() -> int:
    with SOURCE.open(encoding="utf-8", newline="") as handle:
        records = list(csv.DictReader(handle))
    JSON_OUT.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Generated from models/model_catalog.csv; do not edit by hand."]
    for record in records:
        lines.append("- model_id: " + yaml_quote(record["model_id"]))
        for key, value in record.items():
            if key != "model_id":
                lines.append(f"  {key}: {yaml_quote(value)}")
    YAML_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Built {len(records)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
