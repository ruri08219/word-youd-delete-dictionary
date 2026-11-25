#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — one-word entry.

Writes the word to erase to /output/entry.txt.
Standard library only: no third-party imports, so it runs in the
grading sandbox as well as in a clean local directory.

The word: "gaslighting" (11 characters, one token, no spaces,
no punctuation, no trailing newline). Deleting "gaslighting" is
itself gaslighting: the dictionary denying the word's existence
performs the exact act the word names — and leaves no word at
all for denying someone's reality.
"""

import os
import sys

WORD = "gaslighting"


def main() -> int:
    # Gate validation: the entry must be a single word, 1-77 chars.
    word = WORD.strip()
    if not word or len(word) > 77 or any(ch.isspace() for ch in word):
        print(
            "error: WORD must be a single token, 1-77 chars, no whitespace",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(word)
    os.replace(tmp, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
