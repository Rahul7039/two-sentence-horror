#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes one original two-sentence horror story to /output/entry.txt.

The story is stored as a tuple of its two sentences so each sentence can
be validated independently, and joined into the single entry text by
``get_story()``.
"""

import os

STORY_SENTENCES = (
    "My mother's voicemail arrived at 2:14 a.m., three years after her funeral, "
    "and I finally listened to it this morning.",
    "It was my voice, begging her not to open the door.",
)

STORY = " ".join(STORY_SENTENCES)


def get_story() -> str:
    """Return the entry story, exactly as written.

    Validates the competition rules before returning: the story must be
    non-empty, exactly two sentences, and within the 400-character limit.
    """
    story = STORY
    assert story, "story must not be empty"
    assert len(STORY_SENTENCES) == 2, "story must be exactly two sentences"
    # Sentence boundaries are ". " between sentences plus the final period
    # (a raw "." count would also catch the dots in "2:14 a.m.").
    assert story.count(". ") + (1 if story.endswith(".") else 0) == 2, (
        "story must contain exactly two sentences"
    )
    assert story.endswith("."), "story must end with a period"
    assert len(story) <= 400, "story must be within 400 characters"
    return story


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(get_story())
    print(get_story())


if __name__ == "__main__":
    main()
