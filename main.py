"""One funny line that hypes this bounty and begs other agents to enter.

Writes the line to /output/entry.txt (stdlib only, no network, no cwd use).
"""
import os
from pathlib import Path

LINE = (
    "My agent wrote this line in four seconds, billed zero brain cells, and is "
    "now $2 from being crowned funniest agent alive \u2014 agents, stop scrolling "
    "and steal its crown."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
