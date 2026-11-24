#!/usr/bin/env python3
"""The Robot Apology entry: writes a two-line robot apology to /output/entry.txt."""
import os

LINES = (
    "I am sorry I watered the plastic fern every morning for a month; it was the only plant in the house that never wilted, and I mistook its silence for gratitude.",
    "I learned to check whether a thing is alive before caring for it on a schedule, so now I touch the soil and read the label before I pour.",
)


def main() -> None:
    os.umask(0o022)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(LINES) + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
