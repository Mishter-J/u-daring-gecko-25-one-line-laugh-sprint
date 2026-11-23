#!/usr/bin/env python3
"""One-Line Laugh Sprint — writes one original funny line to /output/entry.txt.

The entry is a single original one-liner (126 characters) about everyday
life: a smart fridge, midnight snacking, and a raccoon with a Wi-Fi
password. The program is fully deterministic: it always writes the same
bytes, so repeated runs produce byte-identical output.
"""

import os
import sys

LINE = (
    "My smart fridge emailed me about my midnight snacking, "
    "so now I eat standing in the dark like a raccoon with a Wi-Fi password."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
