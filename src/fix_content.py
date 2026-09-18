#!/usr/bin/env python3
"""One-off editorial fix pass after the writers finished (idempotent). python src/fix_content.py"""
import os, re, json, glob, html

HERE = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(HERE, "content")

def load(p): return json.load(open(p, encoding="utf-8"))
def save(p, d): json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
def deep(o, fn):
    if isinstance(o, dict): return {k: deep(v, fn) for k, v in o.items()}
    if isinstance(o, list): return [deep(v, fn) for v in o]
    return fn(o) if isinstance(o, str) else o

changed = 0
def edit(rel, fn):
    global changed
    p = os.path.join(C, rel)
    if not os.path.exists(p): return
    d = load(p); n = fn(d)
    n = d if n is None else n
    if json.dumps(n, sort_keys=True) != json.dumps(load(p), sort_keys=True): save(p, n); changed += 1

# 1 — over-length titles
TITLES = {"city_service/hardwood-flooring--bradenton.json": "Hardwood Flooring Bradenton FL | Riverside & Old Homes",
          "city_service/tile-installation--bradenton.json": "Tile Installation Bradenton FL | Showers & Floors",
          "city_service/tile-installation--sarasota.json": "Tile Installation Sarasota FL | Porcelain & Showers",
          "city_service/vinyl-plank-flooring--bradenton.json": "Vinyl Plank Flooring Bradenton FL | LVP Installers"}
for rel, t in TITLES.items():
    def f(d, t=t):
        k = next(iter(d)); d[k]["title"] = t
    edit(rel, f)

# 2 — banned word
edit("city_service/floor-repair--palmetto.json", lambda d: deep(d, lambda s: s.replace("which insurance policy ultimately pays", "which insurance policy ends up paying")))
edit("posts/better-refinish-replace-hardwood-floors.json", lambda d: deep(d, lambda s: re.sub(r"\b[Ww]hether you're\b", lambda m: "If you're" if m.group(0)[0] == "W" else "if you're", s)))

# 3 — the price sentence every city capsule shared, plus a few stock closers → one distinct wording per city
PRICE = ["Typical 2026 installed pricing here runs {a} to {b} a square foot.", "Expect {a} to {b} per square foot installed in 2026, depending on the floor.",
         "In 2026 most installed floors here land between {a} and {b} per square foot.", "Installed, 2026 jobs here usually price out at {a} to {b} a square foot.",
         "Budget {a} to {b} per square foot installed at 2026 prices.", "Our 2026 installed range for the floors that suit these homes is {a} to {b} per square foot.",
         "Most 2026 quotes we write here fall between {a} and {b} per installed square foot.", "At 2026 prices, plan on {a} to {b} per square foot, installed.",
         "Figure {a} to {b} for each installed square foot in 2026.", "Installed cost in 2026 generally sits between {a} and {b} a square foot."]
CLOSE = ["The cost guide and the calculator show more worked examples.", "More worked examples are in the cost guide; the calculator handles your own square footage.",
         "For other room sizes, run the numbers in the calculator or open the cost guide.", "The calculator and the cost guides cover other project sizes."]
EXEMPT = ["New floor coverings don't normally need a building permit here.", "Replacing a floor covering is normally permit-exempt.",
          "A straight floor-covering swap usually needs no permit.", "Floor coverings alone rarely trigger a permit.", "Swapping the floor covering is generally exempt from permitting."]
for i, fp in enumerate(sorted(glob.glob(os.path.join(C, "cities", "*.json")))):
    def f(d, i=i):
        def fix(s):
            s = re.sub(r"Typical 2026 installed (?:pricing|ranges) runs? (\$[\d.,]+) to (\$[\d.,]+) per (?:square foot|sq ft)(?: depending on product tier)?\.",
                       lambda m: PRICE[i % len(PRICE)].format(a=m.group(1), b=m.group(2)), s)
            s = s.replace("See the cost guide or the flooring cost calculator for more worked examples.", CLOSE[i % len(CLOSE)])
            s = re.sub(r"Floor coverings themselves are typically exempt from permitting (?:either way|under Florida's building code)\.", EXEMPT[i % len(EXEMPT)], s)
            return s
        return deep(d, fix)
    edit(os.path.relpath(fp, C), f)

# 4 — FAQ questions that also exist as a full post: keep the short answer, point to the one URL that owns the question
posts = {}
for fp in glob.glob(os.path.join(C, "posts", "*.json")):
    d = load(fp)
    if isinstance(d, dict) and d.get("slug"):
        for q in (d.get("question", ""), d.get("h1", "")):
            if q: posts[re.sub(r"[^a-z0-9]+", " ", q.lower()).strip()] = d
for fp in glob.glob(os.path.join(C, "**", "*.json"), recursive=True):
    rel = os.path.relpath(fp, C).replace("\\", "/")
    if rel.startswith("posts/") or rel in ("city_list.json", "legacy_redirects.json", "merged_slugs.json"): continue
    def f(d):
        def walk(o):
            if isinstance(o, dict):
                if "q" in o and "a" in o:
                    p = posts.get(re.sub(r"[^a-z0-9]+", " ", o["q"].lower()).strip())
                    if p and f'/blog/{p["slug"]}/' not in o["a"]:
                        o["a"] = o["a"].rstrip() + f' <a href="/blog/{p["slug"]}/">Read the full answer</a>.'
                for v in o.values(): walk(v)
            elif isinstance(o, list):
                for v in o: walk(v)
        walk(d)
    edit(rel, f)
print("files changed:", changed)
