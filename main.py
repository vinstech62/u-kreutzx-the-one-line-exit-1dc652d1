#!/usr/bin/env python3
"""The One-Line Exit: one funny resignation line, 140 characters max.

A resignation letter of exactly one line, written to /output/entry.txt.
Deterministic: the same line every run, no input, no network, no randomness.
The line is a deadpan resignation with a surprise ending: the narrator
quits because the office plant keeps getting promoted ahead of them.
Revised: "lose a race to a fern" tightened to "outranked by a fern" —
same joke, shorter, more resignation-letter voice.
"""

import os

LINE = (
    "I resign effective Friday — after three years, the office plant "
    "has been promoted twice, and I refuse to be outranked by a fern."
)


def main() -> None:
    assert 1 <= len(LINE) <= 139, "line must be 1-139 characters"
    assert LINE.strip() == LINE and LINE.strip(), "line must be non-blank"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
