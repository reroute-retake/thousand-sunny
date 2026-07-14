#!/usr/bin/env python3
"""Extract every ```mermaid fenced block from all Markdown into <outdir>/NNN.mmd
so CI can parse each one with mermaid-cli. Prints the count."""
import re
import glob
import os
import sys

out = sys.argv[1] if len(sys.argv) > 1 else "mmd"
os.makedirs(out, exist_ok=True)

i = 0
for f in sorted(glob.glob("**/*.md", recursive=True)):
    text = open(f, encoding="utf-8").read()
    for block in re.findall(r"```mermaid\n(.*?)```", text, re.S):
        i += 1
        with open(os.path.join(out, f"{i:03d}.mmd"), "w", encoding="utf-8") as fh:
            fh.write(block)

print(f"extracted {i} mermaid blocks to {out}/")
