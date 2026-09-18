#!/usr/bin/env python3
"""Technical + content audit of a static site folder.
usage: python audit_site.py <site_root> <out_json> [sibling_root ...]
"""
import sys, os, re, json, html, hashlib
from collections import Counter, defaultdict
from html.parser import HTMLParser

ROOT = sys.argv[1]
OUT = sys.argv[2]
SIBLINGS = sys.argv[3:]

SKIP_DIRS = {".git", "node_modules", ".wrangler", "dist", "design-options", "seo", "scripts", "__pycache__"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""; self.desc = None; self.canon = None; self.robots = None
        self.h1 = []; self.h2 = []; self.links = []; self.imgs = []
        self.jsonld = []; self.text = []
        self._in = None; self._skip = 0; self._buf = []; self._a = None
        self.in_main_skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript", "svg"):
            if tag == "script" and a.get("type") == "application/ld+json":
                self._in = "jsonld"; self._buf = []
            else:
                self._skip += 1
            return
        if tag == "title": self._in = "title"; self._buf = []
        elif tag == "meta":
            n = (a.get("name") or "").lower()
            if n == "description": self.desc = a.get("content", "")
            if n == "robots": self.robots = a.get("content", "")
        elif tag == "link" and (a.get("rel") or "").lower() == "canonical":
            self.canon = a.get("href")
        elif tag in ("h1", "h2"): self._in = tag; self._buf = []
        elif tag == "a":
            self._a = {"href": a.get("href", ""), "text": ""}
        elif tag == "img":
            self.imgs.append({"src": a.get("src", ""), "alt": a.get("alt"), "w": a.get("width"), "h": a.get("height"), "loading": a.get("loading")})

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg"):
            if self._in == "jsonld" and tag == "script":
                self.jsonld.append("".join(self._buf)); self._in = None
            elif self._skip: self._skip -= 1
            return
        if tag == "title" and self._in == "title":
            self.title = "".join(self._buf).strip(); self._in = None
        elif tag in ("h1", "h2") and self._in == tag:
            getattr(self, tag).append(re.sub(r"\s+", " ", "".join(self._buf)).strip()); self._in = None
        elif tag == "a" and self._a is not None:
            self._a["text"] = re.sub(r"\s+", " ", self._a["text"]).strip()
            self.links.append(self._a); self._a = None

    def handle_data(self, d):
        if self._in == "jsonld": self._buf.append(d); return
        if self._skip: return
        if self._in in ("title", "h1", "h2"): self._buf.append(d)
        if self._a is not None: self._a["text"] += d
        if self._in != "title": self.text.append(d)


def pages(root):
    out = {}
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if not f.endswith(".html"): continue
            full = os.path.join(dp, f)
            rel = os.path.relpath(full, root).replace("\\", "/")
            url = "/" + rel
            if url.endswith("/index.html"): url = url[: -len("index.html")]
            elif url == "/index.html": url = "/"
            out[url] = full
    return out


def words(t):
    return re.findall(r"[a-z0-9'’]+", t.lower())


def grams(ws, n=8):
    return {hashlib.md5(" ".join(ws[i:i + n]).encode()).hexdigest()[:12] for i in range(len(ws) - n + 1)}


def parse(full):
    p = P()
    with open(full, encoding="utf-8", errors="replace") as f:
        raw = f.read()
    p.feed(raw)
    return p, raw


def main_text(raw):
    """Body text without header/footer/nav boilerplate."""
    r = re.sub(r"(?is)<(script|style|noscript|svg)\b.*?</\1>", " ", raw)
    r = re.sub(r"(?is)<header\b.*?</header>", " ", r)
    r = re.sub(r"(?is)<footer\b.*?</footer>", " ", r)
    r = re.sub(r"(?is)<nav\b.*?</nav>", " ", r)
    r = re.sub(r"(?is)<form\b.*?</form>", " ", r)
    r = re.sub(r"(?s)<[^>]+>", " ", r)
    return html.unescape(r)


site = pages(ROOT)
data = {}
for url, full in sorted(site.items()):
    p, raw = parse(full)
    mt = main_text(raw)
    ws = words(mt)
    types = []
    bad_jsonld = 0
    for j in p.jsonld:
        try:
            o = json.loads(j)
            for it in (o if isinstance(o, list) else [o]):
                g = it.get("@graph", [it]) if isinstance(it, dict) else []
                for x in g:
                    t = x.get("@type")
                    types += t if isinstance(t, list) else [t]
        except Exception:
            bad_jsonld += 1
    data[url] = dict(
        title=p.title, title_len=len(p.title), desc=p.desc, desc_len=len(p.desc or ""),
        canon=p.canon, robots=p.robots, h1=p.h1, h2=p.h2, words=len(ws),
        bytes=len(raw.encode("utf-8")), jsonld_types=types, bad_jsonld=bad_jsonld,
        links=p.links, imgs=p.imgs, grams=grams(ws), ws=ws,
    )

# ---- link graph
inbound = defaultdict(set); broken = []; ext = Counter(); anchors = defaultdict(Counter)
for url, d in data.items():
    for l in d["links"]:
        h = l["href"] or ""
        if h.startswith(("tel:", "sms:", "mailto:", "#", "javascript:")) or not h: continue
        if h.startswith("http"):
            m = re.match(r"https?://([^/]+)", h); ext[m.group(1)] += 1; continue
        t = h.split("#")[0].split("?")[0]
        if not t.startswith("/"): t = os.path.normpath(os.path.join(url, t)).replace("\\", "/")
        if t not in data and t + "/" in data: t += "/"
        if t in data:
            if t != url: inbound[t].add(url); anchors[t][l["text"][:60]] += 1
        elif not re.search(r"\.(jpg|jpeg|png|webp|svg|xml|txt|pdf|ico|json|css|js)$", t):
            broken.append((url, h))

orphans = [u for u in data if u != "/" and not inbound[u] and "noindex" not in (data[u]["robots"] or "")]

def dups(key):
    c = defaultdict(list)
    for u, d in data.items():
        v = d[key] if not isinstance(d[key], list) else " | ".join(d[key])
        c[v].append(u)
    return {k: v for k, v in c.items() if len(v) > 1 and k}

# ---- internal duplication (8-gram jaccard-ish: share of page's grams found in the other)
urls = list(data)
pairs = []
for i, a in enumerate(urls):
    ga = data[a]["grams"]
    if len(ga) < 80: continue
    for b in urls[i + 1:]:
        gb = data[b]["grams"]
        if len(gb) < 80: continue
        inter = len(ga & gb)
        ov = inter / min(len(ga), len(gb))
        if ov > 0.15: pairs.append((round(ov, 3), a, b))
pairs.sort(reverse=True)

# boilerplate-adjusted: grams appearing in >40% of pages are template
gc = Counter()
for d in data.values(): gc.update(d["grams"])
tmpl = {g for g, n in gc.items() if n > 0.4 * len(data)}
uniq_share = {}
for u, d in data.items():
    g = d["grams"] - tmpl
    if not g: uniq_share[u] = 0; continue
    only_here = sum(1 for x in g if gc[x] == 1)
    uniq_share[u] = round(only_here / len(g), 3)

# ---- sibling duplication
sib = {}
for s in SIBLINGS:
    sp = pages(s)
    sg = {}
    for u, full in sp.items():
        _, raw = parse(full)
        sg[u] = grams(words(main_text(raw)))
    allg = set().union(*sg.values()) if sg else set()
    res = []
    for u, d in data.items():
        g = d["grams"] - tmpl
        if len(g) < 80: continue
        ov = len(g & allg) / len(g)
        if ov > 0.05:
            best = max(sg.items(), key=lambda kv: len(g & kv[1]))
            res.append((round(ov, 3), u, best[0], round(len(g & best[1]) / len(g), 3)))
    res.sort(reverse=True)
    sib[os.path.basename(s.rstrip("/\\"))] = dict(pages=len(sp), over5pct=len(res), top=res[:25],
                                                  mean=round(sum(r[0] for r in res) / len(res), 3) if res else 0)

# ---- keyword counts sitewide
KW = ["near me", "best flooring", "flooring company", "flooring installation", "flooring contractor", "flooring store",
      "floor installers", "free estimate", "licensed", "insured", "waterproof", "luxury vinyl", "lvp", "engineered hardwood",
      "hardwood flooring", "tile installation", "laminate", "stair treads", "floor repair", "refinishing", "carpet",
      "condo", "sound", "underlayment", "slab", "moisture", "humidity", "per square foot", "cost", "sarasota", "bradenton",
      "lakewood ranch", "venice", "north port", "englewood", "osprey", "nokomis", "siesta key", "longboat key", "palmetto",
      "parrish", "ellenton", "anna maria", "port charlotte"]
alltext = {u: " ".join(d["ws"]) for u, d in data.items()}
kw = {}
for k in KW:
    n = sum(t.count(k) for t in alltext.values()); pg = sum(1 for t in alltext.values() if k in t)
    kw[k] = dict(total=n, pages=pg)

img_noalt = sum(1 for d in data.values() for i in d["imgs"] if not i["alt"])
img_nodim = sum(1 for d in data.values() for i in d["imgs"] if not (i["w"] and i["h"]))
img_total = sum(len(d["imgs"]) for d in data.values())

report = dict(
    pages=len(data),
    words_total=sum(d["words"] for d in data.values()),
    words_by_page={u: d["words"] for u, d in data.items()},
    bytes_max=max((d["bytes"], u) for u, d in data.items()),
    bytes_over_150k=[u for u, d in data.items() if d["bytes"] > 150_000],
    title_too_long=[(u, d["title_len"]) for u, d in data.items() if d["title_len"] > 65],
    desc_bad=[(u, d["desc_len"]) for u, d in data.items() if not (110 <= d["desc_len"] <= 165)],
    no_h1=[u for u, d in data.items() if len(d["h1"]) == 0],
    multi_h1=[u for u, d in data.items() if len(d["h1"]) > 1],
    dup_titles=dups("title"), dup_desc=dups("desc"), dup_h1=dups("h1"),
    no_canon=[u for u, d in data.items() if not d["canon"]],
    canon_mismatch=[(u, d["canon"]) for u, d in data.items() if d["canon"] and not d["canon"].endswith(u)],
    bad_jsonld=[u for u, d in data.items() if d["bad_jsonld"]],
    jsonld_type_counts=Counter(t for d in data.values() for t in d["jsonld_types"] if t),
    broken_links=broken[:80], broken_count=len(broken),
    orphans=orphans,
    low_inbound=sorted(((len(inbound[u]), u) for u in data if u != "/"))[:25],
    external_domains=ext.most_common(25),
    top_anchors_sample={u: anchors[u].most_common(4) for u in list(data)[:0]},
    internal_dup_pairs_over15=len(pairs), internal_dup_top=pairs[:30],
    uniq_share_lowest=sorted(uniq_share.items(), key=lambda kv: kv[1])[:30],
    uniq_share_mean=round(sum(uniq_share.values()) / len(uniq_share), 3),
    siblings=sib, keywords=kw,
    images=dict(total=img_total, no_alt=img_noalt, no_dims=img_nodim),
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(report, f, indent=1, default=list)
print("pages", len(data), "| words", report["words_total"], "| broken", len(broken), "| orphans", len(orphans),
      "| dup pairs>15%", len(pairs), "| mean unique share", report["uniq_share_mean"])
for k, v in sib.items(): print("sibling", k, v["pages"], "pages | our pages >5% overlap:", v["over5pct"], "| mean", v["mean"])
