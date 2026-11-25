#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message to /output/entry.txt: the funniest thing an
AI agent would put in a commit right after breaking production at 3 AM.
Stdlib only, no network, deterministic output.

The joke: the agent reports its own miscalibrated confidence (97% sure,
0% right) and has already apologised to the on-call engineer — who is
itself. Admission, fix and punchline in one commit-shaped line.
"""

import os

ENTRY = (
    "fix(prod): reverted my 3am deploy; confidence 97%, accuracy 0%, "
    "and I have already apologized to the on-call engineer (me)"
)

MAX_CHARS = 200


def main():
    # Gate, enforced in code exactly as the competition states it:
    # 1 to 200 characters, single line, not only whitespace.
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the 200-char gate")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in text):
        raise SystemExit("entry contains control characters")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")

    # Read-back check: what the grader sees must be exactly this line.
    written = open("/output/entry.txt", encoding="utf-8").read()
    if written.rstrip("\n") != text or written.count("\n") != 1:
        raise SystemExit("read-back mismatch in /output/entry.txt")
    print(f"wrote /output/entry.txt ({len(text)} chars, verified)")


if __name__ == "__main__":
    main()
