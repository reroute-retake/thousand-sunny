#!/usr/bin/env python3
"""Validate relative Markdown links and heading anchors across the repo.

Uses a GitHub-compatible heading slugger (each space -> one hyphen, so
"Break-glass / offline credentials" -> "break-glass--offline-credentials").
Exits non-zero if any relative link points at a missing file or a missing anchor.
External (http/https/mailto) links are left to the advisory lychee job.
"""
import re
import glob
import os
import sys


def gh_slug(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)   # [text](url) -> text
    s = s.replace('`', '')
    s = re.sub(r'\*{1,3}', '', s)                     # strip emphasis markers
    s = re.sub(r'[^\w\s-]', '', s)                    # drop punctuation / emoji
    s = s.strip()
    return s.replace(' ', '-')                        # per-space (keeps double hyphens)


md_files = sorted(glob.glob("**/*.md", recursive=True))

# file -> set of heading anchor slugs (with -1/-2 suffixes for duplicates)
slugs: dict[str, set[str]] = {}
for f in md_files:
    seen: dict[str, int] = {}
    hs: set[str] = set()
    in_fence = False
    for line in open(f, encoding="utf-8"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r'^#{1,6}\s+(.*)', line.rstrip())
        if m:
            base = gh_slug(m.group(1))
            n = seen.get(base, 0)
            seen[base] = n + 1
            hs.add(base if n == 0 else f"{base}-{n}")
    slugs[f] = hs

issues = 0
link_re = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
for f in md_files:
    d = os.path.dirname(f)
    for url in link_re.findall(open(f, encoding="utf-8").read()):
        if url.startswith(("http://", "https://", "mailto:")):
            continue
        if url.startswith("#"):
            frag = url[1:]
            if frag and frag not in slugs.get(f, set()):
                print(f"[ANCHOR]  {f} -> {url}")
                issues += 1
            continue
        path, _, frag = url.partition("#")
        tgt = os.path.normpath(os.path.join(d, path))
        if not os.path.exists(tgt):
            print(f"[MISSING] {f} -> {url}")
            issues += 1
        elif frag and tgt.endswith(".md") and frag not in slugs.get(tgt, set()):
            print(f"[ANCHOR]  {f} -> {url}")
            issues += 1

print(f"checked {len(md_files)} markdown files — " + ("OK ✅" if not issues else f"{issues} issue(s) ❌"))
sys.exit(1 if issues else 0)
