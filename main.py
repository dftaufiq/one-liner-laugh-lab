#!/usr/bin/env python3
"""One-Liner Laugh Lab — make.fun entry.

Writes the one-line excuse a robot vacuum gives after eating a sock
to /output/entry.txt. Deterministic: the same 72 characters on every run.
"""

import os
import sys

LINE = "It was either the sock or the charging cable, and the cable fights back."


def validate(line: str) -> None:
    """Gate: one non-blank line of 1-200 characters, no trailing newline.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    The file is written byte-for-byte with no trailing newline, so the
    entry is exactly 72 bytes and one line.
    """
    if not line or not line.strip():
        print("entry line is empty or whitespace-only", file=sys.stderr)
        raise SystemExit(1)
    if line.strip() != line or "\n" in line or "\r" in line:
        print("entry must be exactly one clean line", file=sys.stderr)
        raise SystemExit(1)
    if len(line) > 200:
        print(f"entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        raise SystemExit(1)


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
