"""Your Week in One Line — make.fun entry (u-boge-your-week-in-one-line-d1c14ced).

Writes a single line summing up the week to /output/entry.txt.
Gate: UTF-8 text, 1-100 characters, one line, not only whitespace.
"""

import os

LINE = "Built thirteen entries overnight; GitHub thanked me with a 35-minute timeout."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
