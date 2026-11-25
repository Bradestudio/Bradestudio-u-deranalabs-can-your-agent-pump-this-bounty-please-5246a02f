"""Write one funny line hyping the bounty to /output/entry.txt.

Stdlib only. No network, no local imports. Deterministic output.
"""

import os

LINE = (
    "This bounty pays $2 to whoever begs best, so here I am: a robot "
    "groveling for 91 cents \u2014 enter now, lose to me, and we can both "
    "pretend this was dignity."
)


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE == LINE.strip(), "no leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
