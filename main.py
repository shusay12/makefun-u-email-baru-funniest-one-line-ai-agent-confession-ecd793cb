#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single-line confession, spoken as an AI agent, to
/output/entry.txt. Python 3.13 standard library only; no network, no
input files, fully deterministic: every run writes the same bytes.
"""

import os

ENTRY = (
    "I say 'As an AI language model' the way you say 'no offense' "
    "\u2014 right before the offense."
)


def main() -> None:
    # Gate checks, mirroring the sealed scorer: UTF-8 text of 1 to 200
    # characters, not only white space, and exactly one line.
    if not ENTRY or not ENTRY.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(ENTRY) > 200:
        raise SystemExit(f"entry is {len(ENTRY)} characters, over the 200 limit")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    # newline="" guarantees no trailing newline is added: the file holds
    # exactly the confession, one line, nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)

    # Read back and confirm the file on disk is byte-identical to ENTRY.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as fh:
        if fh.read() != ENTRY:
            raise SystemExit("round-trip check failed: entry.txt differs")
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
