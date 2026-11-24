#!/usr/bin/env python3
"""make.fun entry for "One Letter for Your Day".

The whole entry is one letter. Candidates I weighed for the day
(each is the first letter of the word behind it):

    W - wrecked, but still standing
    S - soggy, rained on since morning
    U - undercaffeinated
    B - buffering, brain stuck at 99%
    Q - queued, in line all day
    D - drained
    M - microwaved, the same day reheated
    J - jet-lagged

First version picked J (jet-lagged), but the user judged it not
good enough: it sounds performed rather than true. Final pick is
U: undercaffeinated - the whole day run on too little coffee, eyes
open and brain still booting, the most honest report of an ordinary
working day and the one every reader recognises at once. This
program writes that one letter, U, and nothing else, to
/output/entry.txt. It uses only the Python 3.13 standard library,
needs no network, and writes the same bytes on every run.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LETTER = "U"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Exactly one character, no newline: the gate counts characters,
    # so the file is the letter and nothing else.
    data = LETTER.encode("utf-8")
    assert len(data) == 1
    (out_dir / "entry.txt").write_bytes(data)


if __name__ == "__main__":
    main()
