#!/usr/bin/env python3
"""One-Line Laugh Sprint — writes one original funny line to /output/entry.txt.

The entry is a single original one-liner about everyday life: a smart
fridge that snitches on its owner's midnight snacking. The line is built
from a setup and a punchline by build_line(), then checked by
validate_line() before anything is written, so the output always satisfies
the 1-200 character, single-line gate. The program is fully deterministic:
it always writes the same bytes, so repeated runs are byte-identical.
"""

import os
import sys

SETUP = "My smart fridge emailed my doctor about my midnight snacking,"
PUNCHLINE = (
    "so now I eat standing in the dark like a raccoon "
    "with a Wi-Fi password and a guilty conscience."
)


def build_line() -> str:
    """Join the setup and punchline into the single entry line."""
    return SETUP + " " + PUNCHLINE


def validate_line(line: str) -> None:
    """Enforce the entry gate: one line, 1-200 chars, no stray whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    if line != line.strip() or "  " in line:
        raise ValueError("entry must not have leading/trailing/double spaces")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry must not contain control characters")
    if not line.endswith("."):
        raise ValueError("entry must end with a period")


LINE = build_line()
validate_line(LINE)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
