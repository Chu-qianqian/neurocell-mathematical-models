"""Check local Markdown links without fetching external resources."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    checked = 0
    for path in ROOT.rglob("*.md"):
        if any(part == ".git" for part in path.parts):
            continue
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0].strip().strip("<>")
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            checked += 1
            destination = (path.parent / target).resolve()
            if not destination.exists():
                errors.append(f"{path.relative_to(ROOT)} -> {target}")
    if errors:
        print("Local link validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Local link validation passed: {checked} links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
