#!/usr/bin/env python3
"""One Star for Monday.

Writes a single-line, one-star restaurant review of Monday to
``/output/entry.txt`` (override locally with ``ENTRY_OUTPUT_PATH``).

The review is built as a diner's complaint in four beats — seating,
the dish, the bill, and the special — each one a Monday-only grievance,
so the finished line stays short enough to retype into a group chat.
"""
import os
from pathlib import Path

# Each fragment is one beat of the complaint; joined they read as a
# single breathless one-star review.
BEATS = [
    "One star: seated Monday morning,",
    "waiter served cold Sunday leftovers,",
    "charged me five days,",
    "no sleep refills,",
    "and the special was meetings.",
]

REVIEW = " ".join(BEATS)


def render() -> str:
    """Return the review as one line of plain text."""
    return REVIEW


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
