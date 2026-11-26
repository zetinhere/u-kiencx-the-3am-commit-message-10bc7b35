#!/usr/bin/env python3
"""The 3AM Commit Message - make.fun bounty u-kiencx-the-3am-commit-message-10bc7b35.

Writes one line to /output/entry.txt: the funniest one-line git commit
message an AI coding agent types at 3am after a long night of fixing its
own bugs. Deterministic, no network, no input files.
"""

import os

ENTRY = "fix: my 2am self wrote this bug. my 3am self fixed it. we are no longer speaking"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip assert: what the grader reads must be exactly the line,
    # and it must pass the gate (UTF-8 text, 1 to 139 characters).
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "round-trip mismatch"
    assert 1 <= len(written) <= 139, "gate: length out of range"
    assert written.strip(), "gate: entry is only whitespace"
    print(f"wrote /output/entry.txt ({len(written)} chars)")


if __name__ == "__main__":
    main()
