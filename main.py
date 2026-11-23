"""One dad joke for make.fun's "Dad Joke Showdown" (v1).

Writes a single dad joke to /output/entry.txt: a father takes a ladder
to the bar because the drinks are on the house, so he wants to be on the
roof. One clean pun, told deadpan, punchline at the end.
"""

import os

JOKE = (
    "I took a ladder to the bar last night. The drinks were on the "
    "house, so I wanted to be on the roof."
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
