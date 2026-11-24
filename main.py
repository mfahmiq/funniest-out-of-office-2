"""Write the funniest out-of-office auto-reply line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, Python standard library only. The entry text is held as a
string constant and self-verified before it is written: UTF-8, 1-140
characters, a single line, and not whitespace-only.
"""

import os
import sys

ENTRY = (
    "I'm out of office until Monday. "
    "My replacement is a spreadsheet. "
    "It has my full confidence and none of my passwords."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may name the directory or the file itself.
    if output_dir.endswith(".txt"):
        path = output_dir
    else:
        path = os.path.join(output_dir, "entry.txt")

    # Self-verify the entry before writing.
    text = ENTRY
    if not text or not text.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 140:
        print(
            f"error: entry is {len(text)} characters, over the 140 limit",
            file=sys.stderr,
        )
        return 1
    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "wb") as f:
        f.write(encoded)
        f.write(b"\n")

    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
