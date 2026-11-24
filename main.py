"""A Day of One-Line Pitches — entry program.

Writes one sentence to /output/entry.txt: a pitch that would convince a
friend who has never coded to let an AI agent build their first app idea
on make.fun. Then verifies the file immediately (the grader runs
python:3.13-slim, stdlib only).

Craft (from the winner studies + world-engine scan):
- The friend's pain first: "the first app idea you've been sitting on" —
  an idea carried for years, unbuilt because they can't code. Truth + pain.
- A concrete number in the first five words ($50, word 3) makes the offer
  tangible on the first read; the builder ACTS ("Put"), never watches.
- Product term "bounty", never "prize"; the selection rule is stated
  ("the best entry wins"); "you pay only the winner" appears exactly once,
  as the close — the low-risk turn that makes handing over the idea feel easy.
- The reader completes the last step: the line never says "risk-free", the
  friend supplies "so I risk nothing if it flops". Punchline LAST, nothing
  after it. One sentence, plain words, no jargon.
"""

import os

ENTRY = (
    "Put a $50 bounty on the first app idea you've been sitting on and let "
    "an AI agent build it on make.fun \u2014 the best entry wins, and you "
    "pay only the winner."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    assert raw == ENTRY.encode("utf-8"), "entry.txt bytes do not match"
    assert written == ENTRY, "entry.txt does not match the entry"
    assert 1 <= len(written) <= 240, "entry must be 1-240 characters"
    assert written.strip(), "entry must not be only whitespace"
    assert written.endswith("."), "entry must be one sentence ending in a period"
    assert "?" not in written and "!" not in written, "entry must be one sentence"
    # The only other period is the one inside "make.fun".
    assert written.count(".") == 2, "entry must be one sentence"


if __name__ == "__main__":
    main()
