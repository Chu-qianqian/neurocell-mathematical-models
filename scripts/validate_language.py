"""Ensure repository-authored project text contains no Chinese characters."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGETS = (ROOT / "README.md", ROOT / "PROJECT_PLAN.md", ROOT / "CITATION.cff", ROOT / "CODE_OF_CONDUCT.md")
DIRECTORIES = (ROOT / "docs", ROOT / "equations", ROOT / "references", ROOT / "models", ROOT / "data", ROOT / "scripts", ROOT / ".github")
HAN_RE = re.compile(r"[\u4e00-\u9fff]")


def files_to_check() -> list[Path]:
    files = [path for path in TARGETS if path.exists()]
    for directory in DIRECTORIES:
        if directory.exists():
            files.extend(path for path in directory.rglob("*") if path.is_file())
    return files


def main() -> int:
    errors: list[str] = []
    for path in files_to_check():
        if path.suffix.lower() not in {".md", ".csv", ".json", ".yaml", ".yml", ".py", ".bib", ".cff"}:
            continue
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if HAN_RE.search(line):
                errors.append(f"{path.relative_to(ROOT)}:{line_no}")
    if errors:
        print("Language validation failed: Chinese characters found in repository text")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Language validation passed: repository-authored text is English-only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
