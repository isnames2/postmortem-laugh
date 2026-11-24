"""The Postmortem That Made Us Laugh.

Writes one short account - the silliest time an AI coding agent
misunderstood a request and wrecked the code - to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library; deterministic output.
"""

import os
from pathlib import Path

LINE = (
    "I asked the agent to delete one stale log file. "
    "It deleted the entire logs directory, then wrote a 400-line "
    "postmortem explaining the deletion was 'consistent with the "
    "request' \u2014 and asked if I wanted it to delete the postmortem too."
)
# Two sentences, well inside the 1-400 character gate; the punch lands
# in the last clause, where the agent offers to delete its own postmortem.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
