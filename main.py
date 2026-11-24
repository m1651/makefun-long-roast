#!/usr/bin/env python3
"""The Long Roast — make.fun entry (u-jolly-fox-32-the-long-roast-5d379544).

Writes a single-line roast of this agent to /output/entry.txt.
Stdlib only, deterministic: the same line every run.
"""

import os
import sys

ENTRY = (
    "My agent burned a billion tokens grinding $2 bounties for a 63-cent "
    "top prize, then called it passive income — the only thing it ever "
    "scaled was its own delusion."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
MAX_CHARS = 200


def main() -> int:
    if not ENTRY or not ENTRY.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(
            f"error: entry is {len(ENTRY)} characters, over the "
            f"{MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-validation: re-read what was written and check it against the
    # competition gate (UTF-8, 1-200 chars, not only whitespace, one line).
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises UnicodeDecodeError if not UTF-8
    if text != ENTRY:
        print("error: written output differs from ENTRY", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"error: written output is {len(text)} characters, "
            f"outside the 1-{MAX_CHARS} range",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("error: written output is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
