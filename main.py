"""One dad joke for make.fun's "Dad Joke Showdown" (v2).

Writes a single dad joke to /output/entry.txt: the elevator at work has
been feeling down lately, so Dad tells it to lift its spirits. A cleaner
turn than v1 (two meanings of "down"/"lift" in one deadpan line), tighter
at 81 characters, fresher, and the punchline lands on the last two words.
Judged as a father would hear it at the table: the pun first, then the
groan.
"""

import os

JOKE = (
    "The elevator at work has been feeling down lately. I told it to "
    "lift its spirits."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
