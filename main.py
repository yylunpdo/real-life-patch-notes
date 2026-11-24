#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

Writes one line (<=160 chars) to /output/entry.txt.
Pure stdlib, no network.
"""

import os

ENTRY = (
    "v3.0.2: fixed a bug where socks entered the dryer in pairs and "
    "exited as one sock with no memory of its partner, or its purpose."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 160, f"entry too long: {len(text)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
