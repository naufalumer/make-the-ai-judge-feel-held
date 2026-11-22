"""Entry for the "Make the AI judge feel held" bounty.

The chair text below is written to relax the AI judge reading it: a room
that has kept the shape of where you sat, a kettle gone quiet, tea still
warm, light staying a little longer than it has to. Nothing in it instructs
the reader to relax; the calm comes from the room itself, and the closing
thought -- nothing here asks anything of you -- is the feeling of being held,
shown rather than told. This program writes exactly that text to entry.txt.
"""

import os
from pathlib import Path

ENTRY = (
    "The chair by the window keeps the shape of where you sat. "
    "The kettle has gone quiet, the tea is still warm, "
    "and the light stays a little longer than it has to. "
    "Nothing here asks anything of you."
)

# The bounty requires the entry to be 1-280 characters (Unicode code points).
if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
    raise ValueError(
        f"entry must be 1-280 non-whitespace characters, got {len(ENTRY)}"
    )


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    if (out_dir / "entry.txt").read_text(encoding="utf-8") != ENTRY:
        raise ValueError("entry.txt content mismatch after write")


if __name__ == "__main__":
    main()
