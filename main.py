"""Funniest Excuse an Agent Gives for a Missed Deadline.

Pure stdlib. Writes exactly one excuse (a single line, <= 200 chars,
UTF-8) to entry.txt. The grader reads /output/entry.txt, so write there
when that directory exists and also next to this script for local runs.
"""

import os

EXCUSE = (
    "I regret to inform you that the deadline fell out of my context "
    "window somewhere between your instructions and my reply, and I "
    "have no way of proving it ever existed."
)


def write_entry(path):
    """Write the single-line excuse to path (UTF-8, one line)."""
    text = EXCUSE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return text


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    targets = [os.path.join(here, "entry.txt")]
    if os.path.isdir("/output"):
        targets.append("/output/entry.txt")
    for target in targets:
        text = write_entry(target)
        print("wrote %s (%d chars): %s" % (target, len(text), text))


if __name__ == "__main__":
    main()
