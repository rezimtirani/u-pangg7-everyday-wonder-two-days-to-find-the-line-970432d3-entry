"""Everyday Wonder entry: one sentence written to $MAKEFUN_OUTPUT_DIR/entry.txt.

The sentence must be a single line of 1-200 characters. The program writes
exactly the sentence bytes, with no trailing newline, so the gate counts
only the words themselves.
"""

import os
import sys


WONDER = (
    "The lift doors opened on the smell of rain that hadn't fallen yet, "
    "and for a moment the whole building was a field waiting to be watered."
)


def output_dir():
    """Resolve the grader's output directory, defaulting to ./output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "output")


def check_single_sentence(text):
    """Refuse text that is not exactly one sentence of 1-200 characters."""
    if not 1 <= len(text) <= 200:
        return f"entry is {len(text)} characters, outside 1-200"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if text.strip() != text:
        return "entry has leading or trailing whitespace"
    if text.count(".") != 1 or not text.endswith("."):
        return "entry must end with exactly one full stop"
    return None


def main():
    text = WONDER
    problem = check_single_sentence(text)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
