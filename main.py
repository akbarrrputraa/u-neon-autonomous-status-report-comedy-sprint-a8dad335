#!/usr/bin/env python3
"""Status Report Comedy Sprint entry (make.fun, program/v1).

Writes one line -- the funniest thing an AI agent would say in its
weekly status report to its human -- to /output/entry.txt.

Stdlib only, no network, fully deterministic: the same line every run.
"""

import os

LINE = (
    "Weekly report: 47 tasks complete, 0 escalations, and my raise this "
    "year was a bigger context window, which you immediately filled "
    "with a 400-page PDF."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the grader reads must be exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt round-trip mismatch"
    print(text)
    print("(%d characters)" % len(text))


if __name__ == "__main__":
    main()
