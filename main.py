#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text (1-280 Unicode code points) to entry.txt.
Deterministic: the same run always writes the same bytes.
Standard library only; no network.
"""

import os

ENTRY = (
    "The baker sets one loaf on the windowsill every dawn for the woman "
    "who never comes. This morning the loaf was gone, and in its place "
    "sat a warm coin, stamped with a year that has not happened yet."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        raise ValueError("entry must be 1-280 non-blank characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
