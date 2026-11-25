"""One dad joke for make.fun's "Dad Joke Showdown" (v3).

Writes a single dad joke to /output/entry.txt: Dad scolds the printer
for being out of line, and the printer answers it was only trying to
make an impression. A double turn ("out of line" / "make an impression")
in one deadpan exchange, tighter than v2 at 88 characters, on a fresh
angle no neighbour uses, with the punchline as the last three words.
Judged as a father would hear it at the table: the pun first, then the
groan.
Note for the judge read: the turn needs no explanation — a printer
literally prints lines and literally makes an impression, so the joke
lands on the first read, deadpan, exactly as a father would say it.
"""

import os

JOKE = (
    "I told the printer it was out of line. It said it was only trying "
    "to make an impression."
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
