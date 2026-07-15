#!/usr/bin/env python3
"""Verify every relative link in the repo's Markdown files resolves to a real file.

External (http/https) links are skipped — they're checked by humans against primary
sources, not CI, so network flakiness never blocks a docs PR.

Exit 0 if all links resolve; exit 1 with a listing otherwise.
"""
import os
import re
import sys

LINK_RE = re.compile(r"\]\(([^)#\s]+?)(#[^)]*)?\)")
SKIP_DIRS = {".git", "node_modules"}


def main() -> int:
    broken = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            for match in LINK_RE.finditer(text):
                target = match.group(1)
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = os.path.normpath(os.path.join(root, target))
                if not os.path.exists(resolved):
                    broken.append((path, target))

    if broken:
        print("Broken relative links:")
        for path, target in broken:
            print(f"  {path}: {target}")
        return 1
    print("All relative links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
