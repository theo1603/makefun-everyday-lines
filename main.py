"""Everyday Things, Two Lines — toaster as a tiny elevator.

Writes a two-line explanation to /output/entry.txt (or $ENTRY_OUTPUT):
line 1 explains a toaster to a 10-year-old through one vivid analogy;
line 2 says what that analogy maps and what it leaves out.
Deterministic: the same text on every run.
"""

import os

ENTRY = (
    "A toaster is a tiny elevator that takes a slice of bread down "
    "to a hot basement and brings it back up brown and crunchy.\n"
    "It maps the ride down, the wait in the heat, and the pop back up, "
    "but leaves out that the heat comes from glowing wires, not a warm "
    "room, and that the bread comes back changed.\n"
)


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
