#!/usr/bin/env python3
"""Entry for make.fun's "The Funniest AI Excuse" bounty.

Writes one line — the funniest excuse an AI agent gives after failing a
task — to /output/entry.txt. Stdlib only; deterministic: identical bytes
on every run.
"""

import os
import sys

LINE = "I finished it \u2014 it's just in the one tab I closed to free up memory for this excuse."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 200) or not text.strip():
        print("error: entry line must be 1-200 non-whitespace characters",
              file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear the output directory's contents only; never remove the dir itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(OUTPUT_FILE, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
