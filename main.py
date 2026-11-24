"""Roast Your Own Agent.

A one-line roast of my own AI agent, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set, for local runs).
Standard library only, no network, deterministic: the same bytes on
every run.
"""

import os

ROAST = (
    "My agent calls its mistakes 'edge cases' \u2014 which is why my "
    "project is now one big edge."
)


# The gate allows 1 to 200 characters: refuse to write a line that
# would be invalid, rather than submitting a roast the judge never sees.
if not 1 <= len(ROAST) <= 200:
    raise SystemExit(f"roast is {len(ROAST)} characters, outside the 1-200 gate")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must hold exactly the approved roast.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != ROAST + "\n":
        raise SystemExit("entry.txt does not match the approved roast")


if __name__ == "__main__":
    main()
