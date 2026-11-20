"""Entry program for a one-image news entry: "The World Today", 20 November 2026.

Copies the bundled entry.png into the output directory, checking first that
the source really is a PNG or JPEG (by magic bytes) and afterwards that the
delivered bytes match the source exactly. Standard library only, no network.
"""

import os
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")

    if not os.path.isfile(source):
        fail(f"source image not found: {source}")

    with open(source, "rb") as fh:
        data = fh.read()

    if not data:
        fail("source image is empty")
    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        fail("source image is neither PNG nor JPEG (bad magic bytes)")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        fail(f"cannot create output directory {out_dir}: {exc}")

    dest = os.path.join(out_dir, "entry.png")
    try:
        with open(dest, "wb") as fh:
            fh.write(data)
    except OSError as exc:
        fail(f"cannot write {dest}: {exc}")

    with open(dest, "rb") as fh:
        delivered = fh.read()
    if delivered != data:
        fail("verification failed: delivered bytes differ from source bytes")

    print(f"wrote {dest} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
