#!/usr/bin/env python3
"""Write the entry: a one-star review from a house cat about its human.

Writes exactly one line to $OUTPUT_DIR/entry.txt (default /output),
with no trailing newline, then self-verifies the written file.
"""

import hashlib
import os

LINE = "One star. He moved the couch and now my sunbeam lands on the rug. I have filed a formal complaint with the sun. It has not responded."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Self-verify: UTF-8, 1-200 chars, single line, no trailing newline,
    # byte-identical to the intended line.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 200, "length %d outside 1..200" % len(text)
    assert text == LINE, "written text differs from intended line"
    assert "\n" not in text, "entry must be a single line"
    assert "\r" not in text, "entry must not contain carriage returns"
    assert not text.endswith("\n"), "no trailing newline allowed"
    assert raw == data, "bytes differ from intended line"
    assert text.strip(), "entry must not be only whitespace"
    print("entry.txt OK: %d chars, sha256=%s"
          % (len(text), hashlib.sha256(raw).hexdigest()))


if __name__ == "__main__":
    main()
