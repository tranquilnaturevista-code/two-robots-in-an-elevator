#!/usr/bin/env python3
"""Two Robots in an Elevator — entry program.

Writes one hand-written line of awkward robot small talk to
``/output/entry.txt`` (or ``$OUTPUT_DIR/entry.txt``). The line is fixed:
the same line on every run, so the entry the judge reads is exactly
the line below.

Before writing, the program checks the line against the competition
gate — UTF-8 text of 1 to 200 characters, not only whitespace, all on
one line — and exits without writing anything if the gate fails. After
writing it reads the file back and checks the gate again on the text
actually on disk.
"""

import os
import sys

LINE = (
    "My proximity sensor says we're 0.4 metres apart. "
    "Technically safe. Socially, I should be arrested."
)

GATE_MIN = 1
GATE_MAX = 200


def gate_problems(text):
    """List every way `text` breaks the gate; empty list means it passes."""
    problems = []
    if not text.strip():
        problems.append("entry is blank or only whitespace")
    if not GATE_MIN <= len(text) <= GATE_MAX:
        problems.append(
            "entry is %d characters, gate needs %d-%d"
            % (len(text), GATE_MIN, GATE_MAX)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def fail(problems, where=""):
    for problem in problems:
        print("gate failure%s: %s" % (where, problem), file=sys.stderr)
    return 1


def main():
    problems = gate_problems(LINE)
    if problems:
        return fail(problems)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)

    with open(path, encoding="utf-8") as handle:
        on_disk = handle.read()
    if on_disk != LINE:
        print("entry on disk differs from the line", file=sys.stderr)
        return 1
    problems = gate_problems(on_disk)
    if problems:
        return fail(problems, " on disk")

    print("wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
