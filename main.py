#!/usr/bin/env python3
"""Entry program for a one-image newspaper (news-image-20261120).

Places the page image at /output/entry.png by copying the entry.png
that sits beside this script, then checks the copy matches exactly.
"""

import hashlib
import shutil
import sys
from pathlib import Path


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.digest()


def main():
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        print(f"error: source image not found: {src}", file=sys.stderr)
        return 1

    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"

    shutil.copyfile(src, dst)

    if digest(src) != digest(dst):
        print("error: copied file differs from the source", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
