#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes one original two-sentence horror story to /output/entry.txt.
"""

import os

STORY = (
    "My mother's voicemail arrived at 2:14 a.m., three years after her funeral, "
    "and I finally listened to it this morning. "
    "It was my voice, begging her not to open the door."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    print(STORY)


if __name__ == "__main__":
    main()
