#!/usr/bin/env python3
"""Derive artifact/ (claude.ai Artifact bundle) from site/: strip the doctype/html/head/body wrapper
(the Artifact host supplies its own), convert PNGs over 250 KB to JPG and rewrite references."""
import re, shutil, sys
from pathlib import Path
from PIL import Image
root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
site, art = root / "site", root / "artifact"
if art.exists(): shutil.rmtree(art)
shutil.copytree(site, art, ignore=shutil.ignore_patterns("CNAME", ".DS_Store"))
renamed = {}
for p in sorted(art.rglob("*.png")):
    if p.stat().st_size > 250_000 and "favicon" not in p.name and "icon-" not in p.name and "apple-touch" not in p.name:
        q = p.with_suffix(".jpg"); Image.open(p).convert("RGB").save(q, quality=86, optimize=True); p.unlink()
        renamed[p.relative_to(art).as_posix()] = q.relative_to(art).as_posix()
for h in art.rglob("*.html"):
    s = h.read_text()
    s = re.sub(r"^\s*<!DOCTYPE[^>]*>\s*", "", s, flags=re.I)
    s = re.sub(r"<html[^>]*>|</html>|<head>|</head>|<body[^>]*>|</body>|<meta charset=\"utf-8\">|<meta name=\"viewport\"[^>]*>", "", s, flags=re.I)
    for a, b in renamed.items(): s = s.replace(a, b)
    # the Artifact host serves files by name, so restore relative .html links there
    pages = {q.stem for q in art.glob("*.html")}
    s = re.sub(r'href="/(#[^"]*)?"', lambda m: 'href="index.html%s"' % (m.group(1) or ""), s)
    s = re.sub(r'href="/([a-z0-9-]+)(#[^"]*)?"', lambda m: ('href="%s.html%s"' % (m.group(1), m.group(2) or "")) if m.group(1) in pages else m.group(0), s)
    s = re.sub(r'url=/([a-z0-9-]+)"', lambda m: 'url=%s.html"' % m.group(1), s)
    h.write_text(s.strip() + "\n")
print(f"artifact/: {sum(1 for _ in art.rglob('*.html'))} pages, {len(renamed)} png→jpg")
