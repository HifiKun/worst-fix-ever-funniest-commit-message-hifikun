#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit-message line (at most 100 characters) for a bug fix
that made everything worse, to /output/entry.txt.
"""
import os
from pathlib import Path

MESSAGE = "fix: slow query fixed by caching the wrong answer forever"


def main() -> None:
    text = MESSAGE.strip()
    if not 1 <= len(text) <= 100:
        raise ValueError(f"commit message must be 1-100 chars, got {len(text)}")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
