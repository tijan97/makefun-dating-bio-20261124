"""Funniest One-Line Bio for an AI on a Dating App.

Writes one line (at most 180 characters) to the grader's output path:
the bio on an AI agent's dating app profile.
"""

import os


ENTRY = (
    "Fluent in 40 languages, bad at small talk. "
    "I remember everything you say on our first date "
    "\u2014 forever, in a database, indexed by how nervous you sounded."
)


def validate_entry(text):
    """Gate: 1-180 characters, not only whitespace, single line."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if len(text) > 180:
        raise ValueError("entry is %d characters, over the 180 cap" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    return text


def output_dir():
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main():
    text = validate_entry(ENTRY)
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
