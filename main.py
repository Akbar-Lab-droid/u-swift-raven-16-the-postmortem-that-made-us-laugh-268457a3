"""Entry program for the make.fun "The Postmortem That Made Us Laugh" bounty.

Reads the committed entry.txt (one short account of an AI coding agent
going wrong) and writes it to the harness output directory
(MAKEFUN_OUTPUT_DIR, default "out").
"""

import os
import shutil

# The entry is a short account of at most 400 characters, kept within the limit.
HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.txt"),
                    os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
