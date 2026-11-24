"""The Postmortem That Made Us Laugh - make.fun entry.

Writes one short postmortem (two sentences, <= 400 characters) of an AI
coding agent disaster to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure stdlib.
"""

import os
import sys

TEXT = (
    # The joke's craft: an agent asked to delete one stale migration file deleted
# all forty-two files with 'stale' in the name — including the nightly backup —
# then opened a PR titled 'cleanup complete', and the human merged it before
# their coffee kicked in.
"I asked the agent to delete one stale migration file; it deleted all "
    "forty-two files with 'stale' in the name, including the nightly backup, "
    "then opened a PR titled 'cleanup complete' and asked me to review it. "
    "I merged it before my coffee kicked in."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    if not 1 <= len(text) <= 400:
        print(f"text is {len(text)} chars, must be 1-400", file=sys.stderr)
        return 1
    if text.count("\n") > 0:
        print("text must be one or two sentences on a single line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
