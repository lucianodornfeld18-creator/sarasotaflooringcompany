#!/usr/bin/env python3
"""Keyword coverage over the BUILT site (dist/).  python src/kw_report.py
For every researched keyword: exact-phrase hits, loose hits (all words inside one sentence), pages, and whether it
appears in any <title> or <h1>. Writes docs/keyword-coverage.md + .json."""
import os, re, csv, json, html, glob

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); DIST = os.path.join(ROOT, "dist")
rows = list(csv.DictReader(open(os.path.join(ROOT, "docs", "keywords.csv"), encoding="utf-8")))

pages = {}
for fp in glob.glob(os.path.join(DIST, "**", "*.html"), recursive=True):
    raw = open(fp, encoding="utf-8").read()
    t = re.search(r"<title>(.*?)</title>", raw, re.S); h = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S)
    body = re.sub(r"(?is)<(script|style|svg|noscript)\b.*?</\1>", " ", raw)
    body = re.sub(r"(?is)<(header|footer)\b.*?</\1>", " ", body)          # boilerplate nav excluded
    body = html.unescape(re.sub(r"<[^>]+>", " ", body)).lower()
    body = re.sub(r"[^a-z0-9$%.,?'\s-]", " ", body)
    pages[os.path.relpath(fp, DIST).replace("\\", "/")] = dict(
        text=re.sub(r"\s+", " ", body), sents=[set(re.findall(r"[a-z0-9']+", s)) for s in re.split(r"[.?!]\s", body)],
        head=html.unescape(re.sub(r"<[^>]+>", " ", (t.group(1) if t else "") + " " + (h.group(1) if h else ""))).lower())

STOP = {"fl", "in", "for", "the", "a", "to", "of", "near", "me"}
out = []
for r in rows:
    k = r["keyword"].lower().strip()
    ws = [w for w in re.findall(r"[a-z0-9']+", k)]
    core = set(w for w in ws if w not in STOP) or set(ws)
    exact = sum(p["text"].count(k) for p in pages.values())
    ex_pages = sum(1 for p in pages.values() if k in p["text"])
    loose = sum(sum(1 for s in p["sents"] if core <= s) for p in pages.values())
    lo_pages = sum(1 for p in pages.values() if any(core <= s for s in p["sents"]))
    inhead = sum(1 for p in pages.values() if core <= set(re.findall(r"[a-z0-9']+", p["head"])))
    out.append(dict(keyword=k, cluster=r["cluster"], demand=r["demand"][:6].strip(), exact=exact, exact_pages=ex_pages, loose=loose, loose_pages=lo_pages, title_h1_pages=inhead))

out.sort(key=lambda x: ({"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(x["demand"].upper().split()[0] if x["demand"] else "LOW", 3), -x["loose"]))
covered = sum(1 for x in out if x["loose_pages"] > 0); strong = sum(1 for x in out if x["loose_pages"] >= 5)
md = [f"# Keyword coverage — built site ({len(pages)} pages)", "",
      f"{len(out)} researched keywords · **{covered} present on the site** · {strong} present on 5+ pages · {sum(1 for x in out if x['title_h1_pages'])} matched in a title/H1.",
      "Exact = the literal phrase. Loose = every meaningful word of the keyword inside one sentence (how Google actually matches). Header/footer navigation is excluded.", "",
      "| Keyword | Demand | Exact hits | Exact pages | Loose hits | Loose pages | In title/H1 (pages) |", "|---|---|---|---|---|---|---|"]
md += [f"| {x['keyword']} | {x['demand']} | {x['exact']} | {x['exact_pages']} | {x['loose']} | {x['loose_pages']} | {x['title_h1_pages']} |" for x in out]
open(os.path.join(ROOT, "docs", "keyword-coverage.md"), "w", encoding="utf-8").write("\n".join(md))
json.dump(out, open(os.path.join(ROOT, "docs", "keyword-coverage.json"), "w", encoding="utf-8"), indent=1)
print(f"keywords {len(out)} | present {covered} | on 5+ pages {strong} | missing: {[x['keyword'] for x in out if x['loose_pages'] == 0][:25]}")
nm = sum(p["text"].count("near me") for p in pages.values()); print("'near me' occurrences:", nm, "on", sum(1 for p in pages.values() if "near me" in p["text"]), "pages")
