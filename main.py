#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry.

Writes one line of out-of-office auto-reply to /output/entry.txt.
The gate requires UTF-8 text of 1 to 140 characters, not only
whitespace, so the program validates its own line before writing it.

The joke: the sender is out, and the only cover they arranged is
their future self — who will have forgotten the email entirely.
"""

import os
import sys

LINE = (
    "I'm out until Monday. My replacement is me, next week, "
    "with no memory of this email — please reintroduce yourself then."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Refuse to ship a line the gate would reject."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("entry line is %d chars, over the %d limit"
                         % (len(line), MAX_CHARS))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def main():
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print("wrote %d chars to %s" % (len(LINE), OUTPUT_PATH))


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print("invalid entry: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
