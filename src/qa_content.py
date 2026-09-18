#!/usr/bin/env python3
"""Content QA over src/content — run before every build/deploy:  python src/qa_content.py
Checks: JSON validity, title/description/capsule limits, banned phrases, forbidden business claims,
and sentence-level duplication across every content item."""
import os, re, json, glob, html, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "content")

BANNED = ["in today's", "whether you're", "look no further", "it's important to note", "it's worth noting", "in conclusion", "ultimately",
          "at the end of the day", "when it comes to", "elevate", "seamless", "unlock", "delve", "robust", "leverage", "game-changer", "transform your",
          "oasis", "paradise", "we understand that", "our team of experts", "top-notch", "state-of-the-art", "cutting-edge", "meticulous", "comprehensive",
          "hassle-free", "peace of mind", "stand the test of time", "testament", "nestled", "vibrant", "boasts", "tapestry", "from start to finish",
          "one-stop shop", "got you covered", "utilize", "in order to", "let's dive in", "here's the thing", "rest assured", "navigate", "realm",
          "crucial", "myriad", "plethora"]
CLAIMS = [r"\blicensed\s+(and|&)\s+insured\b", r"\bwe(?:'re| are) (?:fully )?licensed\b", r"\b\d+\+?\s+years (?:of experience|in business)\b", r"\b5[- ]star\b", r"\bfive[- ]star\b",
          r"\btop[- ]rated\b", r"\b#1\b", r"\baward[- ]winning\b", r"\bvoted\b", r"\bour showroom\b", r"\bfamily[- ]owned\b", r"\bwe(?:'ve| have) (?:installed|completed|done|finished) (?:thousands|hundreds)\b", r"\b(?:thousands|hundreds) of (?:happy|satisfied) \w+\b"]

def text(v):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", v))).strip()

def walk(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items(): yield from walk(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from walk(v, f"{path}[{i}]")
    elif isinstance(o, str):
        yield path, o

issues, sent_owner, items = [], defaultdict(set), 0
for fp in sorted(glob.glob(os.path.join(C, "**", "*.json"), recursive=True)):
    rel = os.path.relpath(fp, C).replace("\\", "/")
    if rel in ("city_list.json", "legacy_redirects.json", "merged_slugs.json"): continue
    try:
        d = json.load(open(fp, encoding="utf-8"))
    except Exception as e:
        issues.append((rel, f"INVALID JSON: {e}")); continue
    objs = d if isinstance(d, list) else ([d] if any(k in d for k in ("title", "slug", "h1")) else list(d.values()))
    for o in objs:
        if not isinstance(o, dict): continue
        items += 1
        t, ds, cap = o.get("title", ""), o.get("description", ""), o.get("capsule", "")
        if t and len(html.unescape(t)) > 60: issues.append((rel, f"title {len(t)} chars"))
        if ds and not (120 <= len(html.unescape(ds)) <= 160): issues.append((rel, f"description {len(ds)} chars"))
        if cap and not (36 <= len(cap.split()) <= 75): issues.append((rel, f"capsule {len(cap.split())} words"))
        for path, v in walk(o):
            if path.endswith((".url", ".slug", ".old_slug")) or ".sources" in path or ".related_" in path or ".keywords" in path: continue
            low = text(v).lower()
            for b in BANNED:
                if re.search(r"(?<![a-z])" + re.escape(b) + r"(?![a-z])", low): issues.append((rel, f"banned phrase '{b}' in {path}"))
            for c in CLAIMS:
                m = re.search(c, low)
                if m: issues.append((rel, f"forbidden claim '{m.group(0)}' in {path}"))
            if "!" in text(v) and "html" in path: issues.append((rel, f"exclamation mark in {path}"))
            if ".facts" in path or path.endswith(".q"): continue      # table facts and FAQ questions may legitimately recur
            for s in re.split(r"(?<=[.?])\s+", text(v)):
                w = s.split()
                if len(w) >= 9: sent_owner[" ".join(w).lower()].add(rel)

dups = {s: f for s, f in sent_owner.items() if len(f) > 1}
print(f"items {items} | issues {len(issues)} | sentences shared across files {len(dups)}")
for rel, msg in issues[:80]: print("  ", rel, "—", msg)
for s, f in sorted(dups.items(), key=lambda kv: -len(kv[1]))[:25]: print("   DUP", len(f), "files:", s[:110], "|", sorted(f)[:3])
json.dump({"issues": issues, "dup_sentences": {s: sorted(f) for s, f in dups.items()}}, open(os.path.join(os.path.dirname(HERE), "docs", "content-qa.json"), "w", encoding="utf-8"), indent=1)
sys.exit(0)
