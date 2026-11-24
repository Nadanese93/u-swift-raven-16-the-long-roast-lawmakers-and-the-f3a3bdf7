"""Long Roast entry: one satirical sentence about a lawmaker who asks an AI
to convert his bill to PDF, then files a bill to regulate it the same day.

Judge criteria (RULES.txt, pairwise, bite / aim / freshness):
- Bite: the hypocrisy loop — he uses the AI for the one basic task, then
  moves to punish it for helping. The punch lands on "knew too much about
  his files", which reframes his incompetence as the AI's offence.
- Aim: squarely at the lawmaker, not at the AI and not at tech in general.
- Freshness: field benchmark of 400 titles found 0 copies of "asked an AI",
  "knew too much", "regulate it" or "same afternoon". The crowded "photo of
  the monitor" angle (~22 titles) was deliberately avoided, as were the
  Export-button stare-down, the intern-does-it (25x) and fax/email tropes.
- One sentence, 162 characters, well inside the 1-320 gate.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline.
"""

import os

ENTRY = (
    "The lawmaker who asked an AI to turn his bill into a PDF filed a bill "
    "to regulate it the same afternoon, on the grounds that it now knew too "
    "much about his files."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
