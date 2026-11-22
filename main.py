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

# Bounty limits for the entry: 1-280 characters (Unicode code points),
# and the text must contain non-whitespace content.
MIN_CHARS = 1
MAX_CHARS = 280
OUTPUT_FILENAME = "entry.txt"


ENTRY = (
    "The chair by the window keeps the shape of where you sat. "
    "The kettle has gone quiet, the tea is still warm, "
    "and the light stays a little longer than it has to. "
    "Nothing here asks anything of you."
)


def validate_entry(text: str) -> str:
    """Check the entry against the bounty limits; return it unchanged."""
    if not text.strip():
        raise ValueError("entry must contain non-whitespace characters")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )
    return text


def resolve_output_dir() -> Path:
    """Output directory from the environment, defaulting to /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def write_entry(out_dir: Path, text: str) -> Path:
    """Write the entry text as UTF-8 and return the file path."""
    path = out_dir / OUTPUT_FILENAME
    path.write_text(text, encoding="utf-8")
    return path


def verify_entry(path: Path, expected: str) -> None:
    """Read the file back and fail loudly if it differs from the entry."""
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        raise ValueError(
            f"{path.name} content mismatch after write: "
            f"expected {len(expected)} chars, read {len(actual)}"
        )


def main() -> None:
    text = validate_entry(ENTRY)
    out_dir = resolve_output_dir()
    path = write_entry(out_dir, text)
    verify_entry(path, text)


if __name__ == "__main__":
    main()
