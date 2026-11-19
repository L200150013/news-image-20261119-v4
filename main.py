#!/usr/bin/env python3
"""news-image-20261119 v4: write the entry image to the output directory.

The finished image (assets/entry.png) is copied byte for byte to
``entry.png`` inside the output directory: ``$MAKEFUN_OUTPUT_DIR`` when
set, otherwise ``/output``. Standard library only, no network.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Empty only the contents of the output directory, entry by entry.
    # The directory itself is never removed: on the grader /output is a
    # mount point and removing it fails.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Read-back checks: same size as the source and a valid PNG signature.
    if os.path.getsize(dst) != os.path.getsize(SRC):
        raise SystemExit("copy size mismatch: %s != %s" % (dst, SRC))
    with open(dst, "rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            raise SystemExit("output is not a PNG: %s" % dst)
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))


if __name__ == "__main__":
    main()
