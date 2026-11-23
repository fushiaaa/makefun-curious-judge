#!/usr/bin/env python3
"""Write one short text to /output/entry.txt."""

from pathlib import Path

# Constant so a second run writes the same file.
TEXT = 'The archive tape ends mid-sentence. In the last clear frame a woman turns, not toward the camera, and speaks a name no one wrote down. The next reel is marked only: her answer.'


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
