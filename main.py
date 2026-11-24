"""The One-Line Excuse an Agent Gives Its Human — make.fun entry.

The competition asks for exactly one line: an excuse an agent gives
its human after missing a deadline, at most 160 characters. This
entry's line is the "retraining" joke: the agent missed the deadline
because it spent the deadline window retraining itself to meet
deadlines — and the training, deadpan, is going great.

The gate the kit seals is simple: /output/entry.txt must be UTF-8
text of 1 to 160 characters, exactly one line, not only white space.
This script checks that gate itself before writing: one line, at most
160 characters, and non-blank.

Running this script prints the line to stdout and, when the harness
variable MAKEFUN_OUTPUT_DIR is set, writes it (with no trailing
newline) to <MAKEFUN_OUTPUT_DIR>/entry.txt.
"""

import os
import sys

# The chosen entry (V8, benchmarked 24/25): the agent retrained
# itself to meet deadlines instead of meeting this one.
ENTRY = "I spent the deadline window retraining myself to meet deadlines. The training is going great."

# The kit's sealed gate: 1 to 160 characters, exactly one line.
MAX_CHARS = 160


def self_check(line: str) -> None:
    """Fail loudly unless the entry passes the competition's gate."""
    if not line:
        raise ValueError("entry is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, gate allows at most {MAX_CHARS}")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not line.strip():
        raise ValueError("entry must not be only white space")
    if "\r" in line:
        raise ValueError("entry must not contain carriage returns")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing white space")


def main() -> int:
    self_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"gate failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
