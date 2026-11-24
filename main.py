#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes the author's honest tab count to /output/entry.txt: exactly one
digit, nothing else.

Why "1": at the moment this entry was written, exactly one browser tab was
open -- the bounty page itself. A one-tab person: no hoard, no backlog,
just the page in front of them. It is the far end of the field's guess
(most counts will be hoarder numbers), yet entirely believable, and it
says something about the life behind it without a word of explanation.
"""
import os
from pathlib import Path

COUNT = "1"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(COUNT, encoding="utf-8")
    print(COUNT)


if __name__ == "__main__":
    main()
