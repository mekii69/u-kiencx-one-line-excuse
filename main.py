#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

The competition gate requires /output/entry.txt to be UTF-8 text of
1 to 160 characters, not only white space. This program is fully
deterministic: it always writes the same single line, with no trailing
newline, no network access, no environment input and no randomness.
"""

import os

ENTRY = (
    "Sorry, it's late: I put it in a branch called later, "
    "merged it into someday, and tagged the release 'eventually'."
)


def main() -> None:
    # Enforce the gate contract in code: 1 to 160 characters, never blank.
    if not 1 <= len(ENTRY) <= 160 or ENTRY.isspace():
        raise ValueError("entry must be 1 to 160 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
