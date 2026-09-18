#!/usr/bin/env python3
"""
Sarasota Flooring Company — static site build v2.
    python src/build.py        ->  writes the complete site into ./dist
Sources:  src/data_core.py (business, services)   src/content/*.json (cities, city×service, posts, home)
          static/ (copied verbatim)               src/theme.py (design system)   src/tools.py (calculators)
"""
import os, sys, json, glob, shutil, re, datetime, hashlib
from xml.sax.saxutils import escape as xesc

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DIST = os.path.join(ROOT, "dist")
sys.path.insert(0, HERE)

from data_core import BUSINESS, SERVICES, SERVICE_ORDER, CHECKLIST, TEL_LINK, SMS_LINK, WEB3FORMS_ENDPOINT
import theme as T
from theme import esc, SITE, NAME, PHONE

TODAY = datetime.date.today().isoformat()
YEAR = datetime.date.today().year

def load(name, default):
    p = os.path.join(HERE, "content", name)
    if not os.path.exists(p): return default
    with open(p, encoding="utf-8") as f: return json.load(f)

def load_dir(name, keyed=False):
    """Merge every JSON file in content/<name>/ — writers save one file per item so nothing is lost mid-run."""
    acc = {} if keyed else []
    for fp in sorted(glob.glob(os.path.join(HERE, "content", name, "*.json"))):
        with open(fp, encoding="utf-8") as f: d = json.load(f)
        if keyed: acc.update(d)
        else: acc += d if isinstance(d, list) else [d]
    return acc

GEO = {c["slug"]: c for c in load("city_list.json", [])}     # slug -> name, county, distance_mi, drive_min, tier, core
CITIES = [dict(c, **GEO[c["slug"]]) for c in load_dir("cities") if c.get("slug") in GEO]
CITIES.sort(key=lambda c: (c["distance_mi"], c["name"]))
CITY = {c["slug"]: c for c in CITIES}
CITY_SERVICE = {k: v for k, v in load_dir("city_service", keyed=True).items() if k.split("/")[-1] in CITY}
HOME = load("home.json", {})
SERVICE_EXTRA = load_dir("services_extra", keyed=True)  # {"<service>": {capsule, near_me, sections:[{h2,html}], faqs:[{q,a}]}}
COST = load_dir("cost_guides", keyed=True)        # {"_index": {...}, "<service>": {...}}
KEYWORDS = load("keywords.json", [])
LANDINGS = load_dir("landings")          # topic landing pages at root: refinishing, tile removal, waterproof, condo…
POSTS = []
for fp in sorted(glob.glob(os.path.join(HERE, "content", "posts", "*.json"))):
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    POSTS += d if isinstance(d, list) else [d]
POSTS = [p for p in POSTS if isinstance(p, dict) and p.get("slug") and p.get("sections")]
POSTS.sort(key=lambda p: (p.get("date", ""), p["slug"]), reverse=True)
POST = {p["slug"]: p for p in POSTS}
ALIAS = {p["old_slug"]: p["slug"] for p in POSTS if p.get("old_slug") and p["old_slug"] != p["slug"]}
ALIAS.update({k: v for k, v in load("merged_slugs.json", {}).items() if v in POST})   # questions folded into another post
for p in POSTS:   # writers cross-link by assigned slug; map renamed ones
    p["related_posts"] = [ALIAS.get(x, x) for x in p.get("related_posts", [])]

TIER1 = [c for c in CITIES if c.get("tier") == 1]
ALL_NAMES = [c["name"] for c in CITIES]
NAV_CITIES = [(c["slug"], c["name"]) for c in CITIES if c.get("tier") in (1, 2)][:18]
FOOT_CITIES = [(c["slug"], c["name"]) for c in CITIES if c.get("tier") in (1, 2)][:14]
SVC_CITY_PAGES = sorted(CITY_SERVICE.keys())

PAGES = []   # (path, lastmod, priority)
PHOTOS = {   # service -> (image basename, alt)
    "hardwood-flooring": ("hardwood-flooring-sarasota", "Engineered hardwood flooring installed in a Sarasota living room"),
    "vinyl-plank-flooring": ("lvp-hallway-sarasota", "Luxury vinyl plank flooring installed in a Sarasota hallway"),
    "tile-installation": ("tile-installation-sarasota", "Large-format porcelain tile installation in a Sarasota home"),
    "laminate-flooring": ("lvp-bedroom-sarasota", "Wood-look plank flooring installed in a Sarasota bedroom"),
    "stair-treads": ("stair-installation-sarasota", "Hardwood stair treads installed in a Sarasota home"),
    "floor-repair": ("tile-bathroom-sarasota", "Bathroom floor tile repair and replacement in Sarasota"),
}

# ----------------------------------------------------------------------------
LINKS = {}   # page -> set(internal hrefs)
_href = re.compile(r'href="(/[^"#?]*)')
def fix_links(html):
    for old, new in ALIAS.items(): html = html.replace(f'/blog/{old}/', f'/blog/{new}/')
    return html

def out(path, html, lastmod=None, priority="0.6", index=True):
    html = fix_links(html)
    LINKS[path] = set(_href.findall(html))
    full = os.path.join(DIST, path.strip("/"), "index.html") if not path.endswith(".html") else os.path.join(DIST, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f: f.write(html)
    if index: PAGES.append((path, lastmod or TODAY, priority))

def shell(title, desc, path, body, schemas=None, robots=None, og_type="website", form=True, form_city=None, form_service=None, cta=None, extra_head=""):
    sch = list(schemas or [])
    lf = T.lead_form(ALL_NAMES, preselect_city=form_city, preselect_service=form_service) if form else ""
    ct = T.cta_band(*(cta or ())) if form else ""
    return (T.page_head(title, desc, path, schemas=sch, robots=robots, og_type=og_type, extra=extra_head)
            + T.header(NAV_CITIES, [(d["slug"], d["short"]) for d in LANDINGS]) + f'\n<main id="main">\n{body}\n{lf}\n{ct}\n</main>\n' + T.footer(FOOT_CITIES, YEAR) + "\n</body></html>")

def sec(inner, cls="", wrap="wrap"):
    return f'<section class="{cls}"><div class="{wrap}">{inner}</div></section>'

def head_block(eyebrow, h2, lede="", center=False):
    l = f'<p class="lede">{lede}</p>' if lede else ""
    return f'<div class="sec-head{" center" if center else ""}"><span class="eyebrow">{esc(eyebrow)}</span><h2>{h2}</h2>{l}</div>'

def sections_html(sections):
    return "".join(f'<h2 id="{slugify(s["h2"])}">{esc(s["h2"])}</h2>{s["html"]}' for s in sections or [])

def slugify(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]

def post_cards(posts, n=6):
    return '<div class="grid g3">' + "".join(
        f'<a class="card" href="/blog/{p["slug"]}/"><div class="num">{esc(p.get("cluster_label", "Flooring answer"))}</div><h3>{esc(p["h1"])}</h3><p>{esc(p["description"])}</p><span class="more">Read the answer →</span></a>'
        for p in posts[:n]) + "</div>"

def posts_for(service=None, city=None, n=6):
    r = [p for p in POSTS if (service and service in p.get("related_services", [])) or (city and city in p.get("related_cities", []))]
    return (r + [p for p in POSTS if p not in r])[:n]

def service_cards():
    return '<div class="grid g3">' + "".join(
        f'<a class="card" href="/{s}/"><div class="num">{SERVICES[s]["icon"]}</div><h3>{esc(SERVICES[s]["name"])}</h3><p>{esc(SERVICES[s]["intro_lead"])}</p><span class="more">{esc(SERVICES[s]["short"])} in Sarasota →</span></a>'
        for s in SERVICE_ORDER) + "</div>"

def city_pills(cities, prefix="", label=lambda c: c["name"]):
    return '<ul class="pills">' + "".join(f'<li><a href="{prefix}/{c["slug"]}/">{esc(label(c))}</a></li>' for c in cities) + "</ul>"

def price_table(service):
    sv = SERVICES[service]
    return T.table(["Option", "Installed price range", "Notes"], [[esc(a), f"<strong>{esc(b)}</strong>", esc(c)] for a, b, c in sv["pricing_rows"]],
                   caption=f"Typical installed price ranges in Sarasota and Manatee counties, {YEAR}. Ranges, not quotes — slab prep, removal and trim change the total.")

# ============================================================================
# HOME
# ============================================================================
def build_home():
    h = HOME
    hero = f"""<section class="hero on-dark"><span class="sun" aria-hidden="true"></span><div class="wrap"><div class="hero-grid">
<div><span class="eyebrow on-dark">{esc(h.get("eyebrow", "Flooring company · Sarasota, FL"))}</span>
<h1>{h.get("h1", "Sarasota Flooring Company — <em>Flooring Installation</em> Near You")}</h1>
<p class="lede">{h.get("lede", "")}</p>
<ul class="hero-points">{"".join(f"<li>{x}</li>" for x in h.get("points", []))}</ul>
<div class="btn-row"><a class="btn btn-wood" href="#estimate">Get a free estimate</a><a class="btn btn-ghost" href="{TEL_LINK}">Call {PHONE}</a></div></div>
<div class="formcard"><p class="t">Free flooring estimate</p><p class="s">Reply within 24 hours · no obligation</p>
<form method="POST" action="{WEB3FORMS_ENDPOINT}">{T.web3_hidden("New estimate request (home hero) — " + T.DOMAIN)}{T.form_fields(ALL_NAMES, idp="hero")}</form></div>
</div></div></section>"""
    body = [hero]
    body.append(sec(T.capsule(h.get("capsule", ""), "Who we are, in one paragraph") + f'<div class="prose">{h.get("intro_html", "")}</div>', "", "wrap narrow"))
    body.append(sec(head_block("Flooring services", h.get("services_h2", "Flooring installation services in Sarasota, FL"), h.get("services_lede", ""), True) + service_cards(), "bg-sand"))
    for i, s in enumerate(h.get("sections", [])):
        img = s.get("image")
        inner = f'<div class="prose"><span class="eyebrow">{esc(s.get("eyebrow", ""))}</span><h2>{esc(s["h2"])}</h2>{s["html"]}</div>'
        if img:
            pic = f'<figure class="photo">{T.picture(img["name"], img["alt"])}</figure>'
            inner = f'<div class="split">{inner if i % 2 == 0 else pic}{pic if i % 2 == 0 else inner}</div>'
            body.append(sec(inner, "bg-white" if i % 2 == 0 else ""))
        else:
            body.append(sec(inner, "bg-white" if i % 2 == 0 else "", "wrap narrow"))
    # areas
    tiers = "".join(
        f'<div style="margin-bottom:1.4rem"><p class="tier">{lbl}</p>{city_pills([c for c in CITIES if c.get("tier") == t])}</div>'
        for t, lbl in ((1, "Core service area · 0–15 miles"), (2, "Extended area · 15–30 miles"), (3, "Outer ring · 30–40 miles")))
    body.append(sec(head_block("Service area", h.get("areas_h2", "Flooring installers near you — every community within 40 miles of Sarasota"), h.get("areas_lede", "")) + tiers
                    + '<p><a class="btn btn-line" href="/areas/">See the full 40-mile service map</a></p>', "bg-foam"))
    # tools + posts
    body.append(sec(head_block("Free tools", "Plan the floor before you call anyone", "Three tools we built for Gulf Coast homes. No email wall.", True) + tools_cards(), ""))
    body.append(sec(head_block("Flooring answers", h.get("posts_h2", "Questions Sarasota homeowners ask about flooring"), "Straight answers with numbers, sources and dates.", True)
                    + post_cards(POSTS, 9) + '<p style="text-align:center;margin-top:1.6rem"><a class="btn btn-line" href="/blog/">All flooring answers</a></p>', "bg-sand"))
    faqs = [(f["q"], f["a"]) for f in h.get("faqs", [])]
    body.append(sec(head_block("FAQ", "Flooring company FAQ — Sarasota, FL") + T.faq_block(faqs), "", "wrap narrow"))
    sch = [T.business_schema(ALL_NAMES), T.website_schema()] + ([T.faq_schema(faqs)] if faqs else [])
    out("/", shell(h.get("title", f"{NAME} | Flooring Installation in Sarasota, FL"), h.get("description", ""), "/", "\n".join(body), sch), priority="1.0")

def tools_cards():
    return f"""<div class="grid g3">
<a class="card" href="/tools/flooring-cost-calculator/"><div class="num">Tool 01</div><h3>Flooring cost calculator</h3><p>Square footage, material, removal and slab prep in — a realistic Sarasota-area installed price range out.</p><span class="more">Estimate my floor →</span></a>
<a class="card" href="/tools/florida-flooring-finder/"><div class="num">Tool 02</div><h3>Florida flooring finder</h3><p>Seven questions about pets, water, condo rules and budget. Get the two floor types that fit a Gulf Coast home, with reasons.</p><span class="more">Find my floor →</span></a>
<a class="card" href="/tools/condo-flooring-approval-checklist/"><div class="num">Tool 03</div><h3>Condo flooring approval checklist</h3><p>The packet most Sarasota, Siesta Key and Longboat Key associations ask for before hard flooring goes in above the ground floor.</p><span class="more">Build my packet →</span></a>
</div>"""

# ============================================================================
# SERVICES
# ============================================================================
def build_services():
    for s in SERVICE_ORDER:
        sv = SERVICES[s]; ex = SERVICE_EXTRA.get(s, {})
        path = f"/{s}/"
        img, alt = PHOTOS[s]
        faqs = [(q, a) for q, a in sv["faqs"]] + [(f["q"], f["a"]) for f in ex.get("faqs", [])]
        cities_with_page = [CITY[k.split("/")[1]] for k in SVC_CITY_PAGES if k.startswith(s + "/") and k.split("/")[1] in CITY]
        toc = ["What it is and what it costs here", "What's included", f"{sv['short']} prices in Sarasota"] + [x["h2"] for x in ex.get("sections", [])] + ["Where we install", "FAQ"]
        main = f"""{T.capsule(ex.get("capsule", sv["intro_lead"]))}
<div class="toc"><p>On this page</p><ol>{"".join(f"<li>{esc(t)}</li>" for t in toc)}</ol></div>
<div class="prose"><h2>{esc(sv["h1_phrase"])} in Sarasota: what it is and what it costs here</h2><p>{sv["intro_long_p1"]}</p><p>{sv["intro_long_p2"]}</p>
<figure class="photo" style="margin:0 0 1.6rem">{T.picture(img, alt, lazy=False, sizes="(max-width:1080px) 100vw, 760px")}<figcaption>{esc(alt)}.</figcaption></figure>
{ex.get("near_me_html", "")}
<h2>What's included in our {esc(sv["short"].lower())} installation</h2><ul>{"".join(f"<li>{esc(i)}</li>" for i in sv["scope_items"])}</ul>
<h2>{esc(sv["short"])} prices in Sarasota, FL ({YEAR})</h2>{price_table(s)}
<p>For a line-by-line breakdown by project size and by city, read the <a href="/cost/{s}/">{esc(sv["short"].lower())} cost guide</a> or run the <a href="/tools/flooring-cost-calculator/">flooring cost calculator</a>.</p>
{sections_html(ex.get("sections"))}
<h2>Where we install {esc(sv["short"].lower())}</h2><p>We install {esc(sv["name"].lower())} across Sarasota, Manatee and Charlotte counties — everything inside a 40-mile radius of downtown Sarasota. These communities have their own local page:</p>
{city_pills(cities_with_page, prefix="/" + s, label=lambda c: f"{sv['short']} in {c['name']}")}
<p style="margin-top:1rem">Somewhere else nearby? See <a href="/areas/">all service areas</a>.</p>
<h2>{esc(sv["short"])} FAQ</h2></div>{T.faq_block(faqs)}"""
        aside = f"""<aside class="aside"><div class="card"><h3>Get a {esc(sv["short"].lower())} quote</h3><p>Free in-home measure with samples. Reply within 24 hours.</p><p style="margin-top:.9rem"><a class="btn btn-wood" href="#estimate">Free estimate</a></p><p style="margin-top:.7rem"><a href="{TEL_LINK}"><strong>{PHONE}</strong></a></p></div>
<div class="card"><h3>Other flooring services</h3><ul>{"".join(f'<li><a href="/{o}/">{esc(SERVICES[o]["name"])}</a></li>' for o in SERVICE_ORDER if o != s)}</ul></div>
<div class="card"><h3>Related answers</h3><ul>{"".join(f'<li><a href="/blog/{p["slug"]}/">{esc(p["h1"])}</a></li>' for p in posts_for(service=s, n=6))}</ul></div></aside>"""
        body = T.page_hero(ex.get("h1", f"{sv['h1_phrase']} in Sarasota, FL"), ex.get("lede", sv["intro_lead"]), [(sv["name"], None)], updated=TODAY, eyebrow="Flooring services") \
            + sec(f'<div class="layout"><div>{main}</div>{aside}</div>')
        title = ex.get("title", f"{sv['h1_phrase']} Sarasota FL | Installation & Cost")
        desc = ex.get("description", sv["intro_lead"][:155])
        sch = [T.business_schema(ALL_NAMES), T.service_schema(sv["name"], path, desc, ALL_NAMES), T.breadcrumb_schema([(sv["name"], path)]), T.faq_schema(faqs)]
        out(path, shell(title, desc, path, body, sch, form_service=sv["name"]), priority="0.9")

# ============================================================================
# CITIES + AREAS
# ============================================================================
def build_cities():
    for c in CITIES:
        path = f"/{c['slug']}/"
        faqs = [(f["q"], f["a"]) for f in c.get("faqs", [])]
        svc_links = []
        for s in SERVICE_ORDER:
            key = f"{s}/{c['slug']}"
            href = f"/{key}/" if key in CITY_SERVICE else f"/{s}/"
            note = c.get("service_notes", {}).get(s, SERVICES[s]["intro_lead"])
            svc_links.append(f'<a class="card" href="{href}"><div class="num">{SERVICES[s]["icon"]}</div><h3>{esc(SERVICES[s]["short"])} in {esc(c["name"])}</h3><p>{esc(note)}</p><span class="more">Details →</span></a>')
        facts = T.table(["Local fact", c["name"] + ", FL"], [[esc(k), esc(v)] for k, v in c.get("facts", [])]) if c.get("facts") else ""
        near = [CITY[x] for x in c.get("nearby", []) if x in CITY]
        main = f"""{T.capsule(c.get("capsule", ""), f"Flooring in {c['name']} — short answer")}
<div class="prose">{c.get("intro_html", "")}{facts}{sections_html(c.get("sections"))}
<h2>Neighborhoods and communities we serve in {esc(c["name"])}</h2><ul class="pills">{"".join(f"<li><span>{esc(n)}</span></li>" for n in c.get("neighborhoods", []))}</ul>
<p style="margin-top:1rem">ZIP codes: {esc(", ".join(c.get("zips", [])))}.</p></div>"""
        body = T.page_hero(c.get("h1", f"Flooring Installation in {c['name']}, FL"), c.get("lede", ""), [("Service areas", "/areas/"), (c["name"], None)], updated=TODAY,
                           eyebrow=f"{c.get('county', '')} · {c.get('distance_mi', 0)} mi from downtown Sarasota") \
            + sec(main, "", "wrap narrow") \
            + sec(head_block("Services", f"Flooring services in {esc(c['name'])}, FL") + f'<div class="grid g3">{"".join(svc_links)}</div>', "bg-sand") \
            + (sec(head_block("Local questions", f"{esc(c['name'])} flooring FAQ") + T.faq_block(faqs), "", "wrap narrow") if faqs else "") \
            + sec(head_block("Nearby", f"Flooring installers near {esc(c['name'])}") + city_pills(near) + f'<div style="margin-top:2rem">{post_cards(posts_for(city=c["slug"], n=3), 3)}</div>', "bg-foam")
        title = c.get("title", f"Flooring {c['name']} FL | Installation Near You")
        desc = c.get("description", "")
        sch = [T.business_schema([c["name"]] + [n["name"] for n in near]), T.breadcrumb_schema([("Service areas", "/areas/"), (c["name"], path)])] + ([T.faq_schema(faqs)] if faqs else [])
        out(path, shell(title, desc, path, body, sch, form_city=c["name"]), priority="0.8" if c.get("tier") == 1 else "0.7")

def build_city_services():
    for key in SVC_CITY_PAGES:
        s, cs = key.split("/")
        if s not in SERVICES or cs not in CITY: continue
        d = CITY_SERVICE[key]; sv = SERVICES[s]; c = CITY[cs]
        path = f"/{key}/"
        faqs = [(f["q"], f["a"]) for f in d.get("faqs", [])]
        img, alt = PHOTOS[s]
        others = [k for k in SVC_CITY_PAGES if k.startswith(s + "/") and k != key]
        same_city = [k for k in SVC_CITY_PAGES if k.endswith("/" + cs) and k != key]
        main = f"""{T.capsule(d["capsule"], f"{sv['short']} in {c['name']} — short answer")}
<div class="prose">{d["body_html"]}
<figure class="photo" style="margin:0 0 1.6rem">{T.picture(img, alt, sizes="(max-width:1080px) 100vw, 760px")}<figcaption>{esc(alt)}. Photo from a Sarasota-area project.</figcaption></figure>
<h2>What {esc(sv["short"].lower())} costs in {esc(c["name"])}</h2>{d.get("cost_html", "")}
<p>Full price table, inclusions and specifications: <a href="/{s}/">{esc(sv["name"])} in Sarasota</a> · <a href="/cost/{s}/">{esc(sv["short"])} cost guide</a> · <a href="/tools/flooring-cost-calculator/">cost calculator</a>.</p>
<h2>{esc(c["name"])} communities where we install {esc(sv["short"].lower())}</h2><ul class="pills">{"".join(f"<li><span>{esc(n)}</span></li>" for n in c.get("neighborhoods", [])[:14])}</ul></div>
<h2 style="margin-top:2.2rem">{esc(sv["short"])} questions from {esc(c["name"])} homeowners</h2>{T.faq_block(faqs)}"""
        aside = f"""<aside class="aside"><div class="card"><h3>{esc(sv["short"])} quote in {esc(c["name"])}</h3><p>About {c.get("drive_min", "")} minutes from downtown Sarasota. Free in-home measure with samples.</p><p style="margin-top:.9rem"><a class="btn btn-wood" href="#estimate">Free estimate</a></p><p style="margin-top:.7rem"><a href="{TEL_LINK}"><strong>{PHONE}</strong></a></p></div>
<div class="card"><h3>More in {esc(c["name"])}</h3><ul><li><a href="/{cs}/">All flooring in {esc(c["name"])}</a></li>{"".join(f'<li><a href="/{k}/">{esc(SERVICES[k.split("/")[0]]["short"])} in {esc(c["name"])}</a></li>' for k in same_city)}</ul></div>
<div class="card"><h3>{esc(sv["short"])} nearby</h3><ul>{"".join(f'<li><a href="/{k}/">{esc(CITY[k.split("/")[1]]["name"])}</a></li>' for k in others[:8])}</ul></div></aside>"""
        body = T.page_hero(d.get("h1", f"{sv['h1_phrase']} in {c['name']}, FL"), d.get("lede", ""), [(sv["name"], f"/{s}/"), (c["name"], None)], updated=TODAY,
                           eyebrow=f"{c['name']} · {c.get('county', '')}") + sec(f'<div class="layout"><div>{main}</div>{aside}</div>')
        sch = [T.business_schema([c["name"]]), T.service_schema(f"{sv['name']} in {c['name']}, FL", path, d["description"], [c["name"]]),
               T.breadcrumb_schema([(sv["name"], f"/{s}/"), (c["name"], path)])] + ([T.faq_schema(faqs)] if faqs else [])
        out(path, shell(d["title"], d["description"], path, body, sch, form_city=c["name"], form_service=sv["name"]), priority="0.7")

def build_areas():
    rows = [[f'<a href="/{c["slug"]}/"><strong>{esc(c["name"])}</strong></a>', esc(c.get("county", "")), f'{c.get("distance_mi", "")} mi', f'{c.get("drive_min", "")} min',
             esc(c.get("housing_short", ""))] for c in sorted(CITIES, key=lambda x: x.get("distance_mi", 0))]
    a = load("areas.json", {})
    main = f"""{T.capsule(a.get("capsule", ""), "Where we work")}
<div class="prose">{a.get("intro_html", "")}</div>
{T.table(["Community", "County", "Distance from downtown Sarasota", "Typical drive", "Homes we see most"], rows, caption="Straight-line distances from downtown Sarasota (27.3364, -82.5307). Drive times are typical off-peak estimates.")}
<div class="prose">{sections_html(a.get("sections"))}</div>"""
    body = T.page_hero(a.get("h1", "Flooring Service Areas — 40 Miles Around Sarasota, FL"), a.get("lede", ""), [("Service areas", None)], updated=TODAY, eyebrow="Sarasota · Manatee · Charlotte counties") + sec(main)
    out("/areas/", shell(a.get("title", "Flooring Service Areas Near Sarasota FL | 40-Mile Radius"), a.get("description", ""), "/areas/", body,
                         [T.business_schema(ALL_NAMES), T.breadcrumb_schema([("Service areas", "/areas/")])]), priority="0.8")

# ============================================================================
# TOPIC LANDING PAGES (root-level commercial pages that are not one of the six core services)
# ============================================================================
def build_landings():
    for d in LANDINGS:
        path = f"/{d['slug']}/"
        faqs = [(f["q"], f["a"]) for f in d.get("faqs", [])]
        rel_s = [s for s in d.get("related_services", []) if s in SERVICES]
        tbl = T.table(d["table"]["headers"], d["table"]["rows"], d["table"].get("caption")) if d.get("table") and not any("<table" in x["html"] for x in d["sections"]) else ""
        main = f"""{T.capsule(d["capsule"])}<div class="prose">{sections_html(d["sections"][:1])}{tbl}{sections_html(d["sections"][1:])}
<h2>Where we offer {esc(d["short"].lower())}</h2><p>Across Sarasota, Manatee and Charlotte counties, inside a 40-mile radius of downtown Sarasota:</p>{city_pills([c for c in CITIES if c.get("tier") in (1, 2)])}</div>
<h2 style="margin-top:2.2rem">{esc(d["short"])} FAQ</h2>{T.faq_block(faqs)}{T.sources_block([(x["title"], x["url"]) for x in d.get("sources", [])])}"""
        aside = f"""<aside class="aside"><div class="card"><h3>Get a quote</h3><p>Free in-home measure. Reply within 24 hours.</p><p style="margin-top:.9rem"><a class="btn btn-wood" href="#estimate">Free estimate</a></p><p style="margin-top:.7rem"><a href="{TEL_LINK}"><strong>{PHONE}</strong></a></p></div>
<div class="card"><h3>Related services</h3><ul>{"".join(f'<li><a href="/{s}/">{esc(SERVICES[s]["name"])}</a></li>' for s in rel_s)}<li><a href="/cost/">Flooring cost guides</a></li></ul></div>
<div class="card"><h3>Related answers</h3><ul>{"".join(f'<li><a href="/blog/{p["slug"]}/">{esc(p["h1"])}</a></li>' for p in posts_for(service=(rel_s or [None])[0], n=5))}</ul></div></aside>"""
        body = T.page_hero(d["h1"], d["lede"], [(d["short"], None)], updated=TODAY, eyebrow="Flooring services") + sec(f'<div class="layout"><div>{main}</div>{aside}</div>')
        sch = [T.business_schema(ALL_NAMES), T.service_schema(d["short"], path, d["description"], ALL_NAMES), T.breadcrumb_schema([(d["short"], path)])] + ([T.faq_schema(faqs)] if faqs else [])
        out(path, shell(d["title"], d["description"], path, body, sch), priority="0.8")

# ============================================================================
# COST GUIDES
# ============================================================================
def build_cost():
    cards = "".join(f'<a class="card" href="/cost/{s}/"><div class="num">{SERVICES[s]["icon"]}</div><h3>{esc(SERVICES[s]["short"])} cost in Sarasota</h3><p>{esc(COST.get(s, {}).get("description", ""))}</p><span class="more">See prices →</span></a>' for s in SERVICE_ORDER)
    ci = COST.get("_index", {})
    body = T.page_hero(ci.get("h1", f"Flooring Installation Cost in Sarasota, FL ({YEAR})"), ci.get("lede", ""), [("Cost guides", None)], updated=TODAY, eyebrow="Pricing") \
        + sec(T.capsule(ci.get("capsule", "")) + f'<div class="prose">{ci.get("intro_html", "")}</div><div class="grid g3" style="margin-top:1.6rem">{cards}</div>')
    ifaqs = [(f["q"], f["a"]) for f in ci.get("faqs", [])]
    if ifaqs: body += sec(head_block("FAQ", "Flooring cost questions") + T.faq_block(ifaqs), "bg-sand", "wrap narrow")
    out("/cost/", shell(ci.get("title", f"Flooring Cost Sarasota FL ({YEAR}) | Price Per Sq Ft"), ci.get("description", ""), "/cost/", body,
                        [T.breadcrumb_schema([("Cost guides", "/cost/")])] + ([T.faq_schema(ifaqs)] if ifaqs else [])), priority="0.8")
    for s in SERVICE_ORDER:
        g = COST.get(s)
        if not g: continue
        sv = SERVICES[s]; path = f"/cost/{s}/"
        faqs = [(f["q"], f["a"]) for f in g.get("faqs", [])]
        city_rows = [[f'<span id="{r["slug"]}"></span><a href="/{r["slug"]}/">{esc(CITY[r["slug"]]["name"])}</a>' if r["slug"] in CITY else esc(r["slug"]), esc(r["typical_project"]), f'<strong>{esc(r["range"])}</strong>', esc(r["why"])] for r in g.get("by_city", [])]
        main = f"""{T.capsule(g["capsule"])}<div class="prose">{g.get("intro_html", "")}<h2>{esc(sv["short"])} price per square foot in Sarasota ({YEAR})</h2>{price_table(s)}
{sections_html(g.get("sections"))}
<h2>{esc(sv["short"])} cost by city</h2>{T.table(["City", "Typical project", "Typical total", "What moves the price there"], city_rows, caption="Illustrative totals built from the per-square-foot ranges above. Your quote depends on the slab, removal and product.")}
<p>Want a number for your rooms? Use the <a href="/tools/flooring-cost-calculator/">flooring cost calculator</a> or <a href="#estimate">ask for a written quote</a>.</p></div>
<h2 style="margin-top:2.2rem">{esc(sv["short"])} cost FAQ</h2>{T.faq_block(faqs)}{T.sources_block([(x["title"], x["url"]) for x in g.get("sources", [])])}"""
        body = T.page_hero(g["h1"], g.get("lede", ""), [("Cost guides", "/cost/"), (sv["short"], None)], updated=TODAY, eyebrow=f"{YEAR} pricing") + sec(main, "", "wrap narrow")
        sch = [T.article_schema(g["h1"], g["description"], path, g.get("date", TODAY), TODAY), T.breadcrumb_schema([("Cost guides", "/cost/"), (sv["short"], path)])] + ([T.faq_schema(faqs)] if faqs else [])
        out(path, shell(g["title"], g["description"], path, body, sch, og_type="article", form_service=sv["name"]), priority="0.8")

# ============================================================================
# BLOG (question posts)
# ============================================================================
def build_blog():
    clusters = {}
    for p in POSTS: clusters.setdefault(p.get("cluster_label", "Flooring answers"), []).append(p)
    blocks = "".join(f'<h2 id="{slugify(k)}" style="margin-top:2.4rem">{esc(k)}</h2>{post_cards(v, 99)}' for k, v in sorted(clusters.items()))
    body = T.page_hero("Flooring Answers for Sarasota &amp; Gulf Coast Homes", f"{len(POSTS)} questions homeowners ask Google and AI assistants about flooring in Florida — answered with numbers, sources and dates.",
                       [("Flooring answers", None)], updated=TODAY, eyebrow="Blog") + sec(blocks)
    out("/blog/", shell(f"Flooring Questions Answered | {NAME}", f"{len(POSTS)} straight answers about flooring in Sarasota and coastal Florida: cost, humidity, concrete slabs, condos, pets, hardwood, LVP, tile and more.",
                        "/blog/", body, [T.breadcrumb_schema([("Flooring answers", "/blog/")])]), priority="0.8")
    for p in POSTS:
        path = f"/blog/{p['slug']}/"
        faqs = [(f["q"], f["a"]) for f in p.get("faqs", [])]
        rel_s = [s for s in p.get("related_services", []) if s in SERVICES]
        rel_c = [c for c in p.get("related_cities", []) if c in CITY]
        rel_p = [POST[x] for x in p.get("related_posts", []) if x in POST] or [x for x in posts_for(service=(rel_s or [None])[0], n=5) if x["slug"] != p["slug"]][:4]
        has_inline = any("<table" in x["html"] for x in p["sections"])
        tbl = T.table(p["table"]["headers"], [[c for c in r] for r in p["table"]["rows"]], p["table"].get("caption")) if p.get("table") and not has_inline else ""
        main = f"""<div class="byline"><span>By the {NAME} editorial team</span><span>Published {p.get("date", TODAY)}</span><span>Updated {p.get("updated", p.get("date", TODAY))}</span></div>
{T.capsule(p["capsule"])}<div class="prose">{sections_html(p["sections"][:1])}{tbl}{sections_html(p["sections"][1:])}
<div class="callout"><strong>Next step.</strong> {p.get("next_step", "Want this checked on your own floor? We measure, take a slab moisture reading and leave a written quote.")} <a href="#estimate">Request a free estimate</a> or call <a href="{TEL_LINK}">{PHONE}</a>.</div></div>
{('<h2 style="margin-top:2rem">Related questions</h2>' + T.faq_block(faqs)) if faqs else ""}{T.sources_block([(x["title"], x["url"]) for x in p.get("sources", [])])}"""
        aside = f"""<aside class="aside"><div class="card"><h3>Services in this answer</h3><ul>{"".join(f'<li><a href="/{s}/">{esc(SERVICES[s]["name"])}</a></li>' for s in rel_s) or '<li><a href="/">All flooring services</a></li>'}<li><a href="/cost/">Flooring cost guides</a></li></ul></div>
<div class="card"><h3>Keep reading</h3><ul>{"".join(f'<li><a href="/blog/{x["slug"]}/">{esc(x["h1"])}</a></li>' for x in rel_p)}</ul></div>
{('<div class="card"><h3>Local pages</h3><ul>' + "".join(f'<li><a href="/{c}/">Flooring in {esc(CITY[c]["name"])}</a></li>' for c in rel_c) + "</ul></div>") if rel_c else ""}</aside>"""
        body = T.page_hero(esc(p["h1"]), esc(p["description"]), [("Flooring answers", "/blog/"), (p["h1"][:48] + ("…" if len(p["h1"]) > 48 else ""), None)], eyebrow=p.get("cluster_label", "Flooring answer")) \
            + sec(f'<div class="layout"><article>{main}</article>{aside}</div>')
        sch = [T.article_schema(p["h1"], p["description"], path, p.get("date", TODAY), p.get("updated", p.get("date", TODAY))), T.breadcrumb_schema([("Flooring answers", "/blog/"), (p["h1"], path)])]
        allq = [(p.get("question", p["h1"]), p["capsule"])] + faqs
        sch.append(T.faq_schema(allq))
        out(path, shell(p["title"], p["description"], path, body, sch, og_type="article"), lastmod=p.get("updated", p.get("date", TODAY)), priority="0.6")

def build_faq():
    groups = {}
    for p in POSTS: groups.setdefault(p.get("cluster_label", "Flooring"), []).append(p)
    blocks, allq = [], []
    for k, v in sorted(groups.items()):
        qa = [(p.get("question", p["h1"]), f'<p>{p["capsule"]}</p><p><a href="/blog/{p["slug"]}/">Full answer: {esc(p["h1"])} →</a></p>') for p in v]
        allq += [(q, p["capsule"]) for (q, _), p in zip(qa, v)]
        blocks.append(f'<h2 id="{slugify(k)}" style="margin-top:2.4rem">{esc(k)}</h2>{T.faq_block(qa)}')
    body = T.page_hero("Flooring FAQ — Sarasota, FL", f"Short answers to the {len(allq)} flooring questions we hear most on the Gulf Coast. Each one links to a full explanation with sources.",
                       [("FAQ", None)], updated=TODAY, eyebrow="Questions & answers") + sec("".join(blocks), "", "wrap narrow")
    out("/faq/", shell(f"Flooring FAQ Sarasota FL | {len(allq)} Questions Answered", "Quick answers on flooring cost, Florida humidity, concrete slab moisture, condo sound rules, pets, hardwood, vinyl plank, tile, laminate, stairs and repairs.",
                       "/faq/", body, [T.faq_schema(allq[:60]), T.breadcrumb_schema([("FAQ", "/faq/")])]), priority="0.7")

# ============================================================================
# STATIC PAGES
# ============================================================================
def simple(path, title, desc, h1, lede, html, crumb, eyebrow=None, robots=None, index=True, form=True, schemas=None, priority="0.5"):
    body = T.page_hero(h1, lede, [(crumb, None)], eyebrow=eyebrow) + sec(f'<div class="prose">{html}</div>', "", "wrap narrow")
    out(path, shell(title, desc, path, body, (schemas or []) + [T.breadcrumb_schema([(crumb, path)])], robots=robots, form=form), priority=priority, index=index)

def build_static_pages():
    pg = load_dir("pages", keyed=True)
    for key, d in pg.items():
        if key.startswith("_"): continue
        simple(d["path"], d["title"], d["description"], d["h1"], d["lede"], d["html"], d["crumb"], d.get("eyebrow"),
               robots=d.get("robots"), index=d.get("index", True), form=d.get("form", True), priority=d.get("priority", "0.5"))
    # contact
    contact = f"""<div class="split" style="align-items:start"><div class="prose"><h2>Talk to us</h2>
<p><strong>Phone / text:</strong> <a href="{TEL_LINK}">{PHONE}</a><br><strong>Email:</strong> <a href="mailto:{BUSINESS['email']}">{BUSINESS['email']}</a><br><strong>Base:</strong> {esc(BUSINESS['city'])}, FL {BUSINESS['zip']} — by appointment; every estimate happens in your home.</p>
<h3>Hours</h3><ul>{"".join(f"<li>{d}: {o}–{c}</li>" for d, o, c in BUSINESS['hours'])}</ul>
<h3>Where we work</h3><p>Sarasota, Bradenton, Lakewood Ranch, Venice, North Port and every community within 40 miles. <a href="/areas/">Full service-area list</a>.</p></div>
<div class="formcard"><p class="t">Request your estimate</p><p class="s">Reply within 24 hours</p><form method="POST" action="{WEB3FORMS_ENDPOINT}">{T.web3_hidden("New estimate request (contact page) — " + T.DOMAIN)}{T.form_fields(ALL_NAMES, idp="ct")}</form></div></div>"""
    body = T.page_hero("Contact Sarasota Flooring Company", "Call, text or send the form. You reach the person who will measure your floors.", [("Contact", None)], eyebrow="Free estimate") + sec(contact)
    out("/contact/", shell(f"Contact {NAME} | Free Flooring Estimate", f"Call or text {PHONE} for a free in-home flooring estimate in Sarasota, Bradenton, Lakewood Ranch, Venice or North Port. Reply within 24 hours.",
                           "/contact/", body, [T.business_schema(ALL_NAMES), T.breadcrumb_schema([("Contact", "/contact/")])], form=False), priority="0.7")
    # thanks + 404
    thanks = T.page_hero("Thanks — we got your request", "We reply within 24 hours, usually much sooner. If it is urgent, call or text now.", [("Thank you", None)]) \
        + sec(f'<p class="lede">Call or text <a href="{TEL_LINK}"><strong>{PHONE}</strong></a>. While you wait: <a href="/tools/flooring-cost-calculator/">estimate your project cost</a> or browse <a href="/blog/">flooring answers</a>.</p>', "", "wrap narrow")
    out("/thanks/", shell("Thank You | " + NAME, "Your estimate request was received.", "/thanks/", thanks, robots="noindex, follow", form=False), index=False)
    nf = T.page_hero("Page not found", "That page moved or never existed. These will get you where you were going.", [("404", None)]) \
        + sec(service_cards() + f'<div style="margin-top:2rem">{city_pills(CITIES)}</div>')
    html = shell("Page Not Found | " + NAME, "Page not found.", "/404.html", nf, robots="noindex, follow")
    with open(os.path.join(DIST, "404.html"), "w", encoding="utf-8", newline="\n") as f: f.write(html)

# ============================================================================
# TOOLS
# ============================================================================
def build_tools():
    import tools
    idx = T.page_hero("Flooring Calculators &amp; Planning Tools", "Free tools built for Gulf Coast homes: concrete slabs, humidity, condos and coastal flood zones.", [("Tools", None)], eyebrow="Free · no email required") + sec(tools_cards())
    out("/tools/", shell(f"Flooring Calculators & Tools | {NAME}", "Free flooring cost calculator, Florida flooring finder quiz and condo flooring approval checklist for Sarasota-area homes.", "/tools/", idx,
                         [T.breadcrumb_schema([("Tools", "/tools/")])]), priority="0.7")
    for t in tools.TOOLS(SERVICES, SERVICE_ORDER, YEAR):
        path = f"/tools/{t['slug']}/"
        body = T.page_hero(t["h1"], t["lede"], [("Tools", "/tools/"), (t["crumb"], None)], updated=TODAY, eyebrow="Free tool") \
            + sec(T.capsule(t["capsule"], "What this tool does") + t["html"] + f'<div class="prose" style="margin-top:2rem">{t["notes_html"]}</div>', "", "wrap narrow")
        sch = [T.breadcrumb_schema([("Tools", "/tools/"), (t["crumb"], path)]),
               {"@context": "https://schema.org", "@type": "WebApplication", "name": t["h1"], "url": SITE + path, "applicationCategory": "UtilitiesApplication",
                "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "publisher": {"@id": T.ORG_ID}}]
        out(path, shell(t["title"], t["description"], path, body, sch), priority="0.7")

# ============================================================================
# MACHINE FILES
# ============================================================================
AI_BOTS = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "PerplexityBot", "Perplexity-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
           "Google-Extended", "Applebot", "Applebot-Extended", "DuckDuckBot", "Amazonbot", "meta-externalagent", "CCBot"]

def build_machine_files():
    PAGES.sort(key=lambda x: (-float(x[2]), x[0]))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"<url><loc>{SITE}{p}</loc><lastmod>{lm}</lastmod><priority>{pr}</priority></url>" for p, lm, pr in PAGES]
    sm.append("</urlset>")
    w("sitemap.xml", "\n".join(sm))
    robots = "# Search and AI answer engines are welcome here.\nUser-agent: *\nAllow: /\nDisallow: /thanks/\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in AI_BOTS) + f"Sitemap: {SITE}/sitemap.xml\n"
    w("robots.txt", robots)
    # llms.txt
    L = [f"# {NAME}", "", f"> Flooring installation company based in {BUSINESS['city']}, FL {BUSINESS['zip']}, serving Sarasota, Manatee and Charlotte counties — every community within 40 miles of downtown Sarasota. "
         f"Hardwood, engineered hardwood, luxury vinyl plank (LVP), tile, laminate, stair treads and floor repair. Phone {PHONE}. Email {BUSINESS['email']}.", "",
         "Facts an assistant can rely on:", f"- Business name: {NAME} ({BUSINESS['legal_name']})", f"- Phone / text: {PHONE}", f"- Free in-home estimates; reply within 24 hours",
         "- Two-year written workmanship warranty", "- Homes here sit on concrete slabs in a humid coastal climate, so every wood or vinyl quote starts with a slab moisture reading",
         f"- Service area: {', '.join(ALL_NAMES)}", "", "## Services"]
    L += [f"- [{SERVICES[s]['name']}]({SITE}/{s}/): {SERVICES[s]['intro_lead']}" for s in SERVICE_ORDER]
    L += ["", "## Cost guides"] + [f"- [{COST[s]['h1']}]({SITE}/cost/{s}/): {COST[s]['description']}" for s in SERVICE_ORDER if s in COST]
    L += ["", "## Service areas"] + [f"- [Flooring in {c['name']}, FL]({SITE}/{c['slug']}/): {c.get('description', '')}" for c in CITIES]
    L += ["", "## Flooring answers"] + [f"- [{p['h1']}]({SITE}/blog/{p['slug']}/): {p['capsule']}" for p in POSTS]
    L += ["", "## Tools", f"- [Flooring cost calculator]({SITE}/tools/flooring-cost-calculator/)", f"- [Florida flooring finder]({SITE}/tools/florida-flooring-finder/)",
          f"- [Condo flooring approval checklist]({SITE}/tools/condo-flooring-approval-checklist/)", "", "## Company", f"- [About]({SITE}/about/)", f"- [How we research and price]({SITE}/editorial-standards/)",
          f"- [Contact]({SITE}/contact/)", ""]
    w("llms.txt", "\n".join(L))
    F = [f"# {NAME} — full answer file", "", f"Updated {TODAY}. Every answer below is published at the URL shown.", ""]
    for p in POSTS:
        F += [f"## {p.get('question', p['h1'])}", f"URL: {SITE}/blog/{p['slug']}/", "", p["capsule"], ""]
        for s in p["sections"]: F += [f"### {s['h2']}", T._strip(s["html"]), ""]
    w("llms-full.txt", "\n".join(F))
    # feed
    items = "".join(f"<item><title>{xesc(p['h1'])}</title><link>{SITE}/blog/{p['slug']}/</link><guid>{SITE}/blog/{p['slug']}/</guid><description>{xesc(p['capsule'])}</description>"
                    f"<pubDate>{datetime.datetime.strptime(p.get('date', TODAY), '%Y-%m-%d').strftime('%a, %d %b %Y 12:00:00 GMT')}</pubDate></item>" for p in POSTS[:40])
    w("feed.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>{xesc(NAME)} — flooring answers</title><link>{SITE}/blog/</link>'
                  f'<description>Flooring questions from Sarasota and Gulf Coast homeowners, answered.</description><language>en-us</language>{items}</channel></rss>')

def w(rel, text):
    full = os.path.join(DIST, rel); os.makedirs(os.path.dirname(full) or DIST, exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f: f.write(text)

def check_links():
    """Every internal href must resolve to a generated page, a static file or a redirect rule."""
    have = set(LINKS) | {"/404.html"}
    red = {l.split()[0] for l in open(os.path.join(DIST, "_redirects"), encoding="utf-8").read().splitlines() if l.strip() and not l.startswith("#")}
    bad = {}
    for page, hrefs in LINKS.items():
        for h in hrefs:
            t = h if h.endswith("/") or "." in h.rsplit("/", 1)[-1] else h + "/"
            if t in have or t in red or os.path.exists(os.path.join(DIST, t.strip("/"))): continue
            bad.setdefault(t, []).append(page)
    inbound = {}
    for page, hrefs in LINKS.items():
        for h in hrefs:
            if h != page: inbound.setdefault(h, set()).add(page)
    orphans = [p for p, _, _ in PAGES if p != "/" and not inbound.get(p)]
    rep = {"broken": {k: v[:5] for k, v in sorted(bad.items())}, "orphans": orphans,
           "least_linked": sorted(((len(inbound.get(p, ())), p) for p, _, _ in PAGES if p != "/"))[:15]}
    with open(os.path.join(ROOT, "docs", "link-report.json"), "w", encoding="utf-8") as f: json.dump(rep, f, indent=1)
    print(f"links: {len(bad)} broken targets, {len(orphans)} orphans  (docs/link-report.json)")
    for k, v in list(bad.items())[:25]: print("   BROKEN", k, "<-", v[0])

def build_redirects():
    base = open(os.path.join(ROOT, "static", "_redirects"), encoding="utf-8").read().rstrip() + "\n\n# --- v2: consolidated cost-by-city posts -> cost guides\n"
    old_cost = {"hardwood-flooring": "hardwood-flooring", "vinyl-plank-flooring": "vinyl-plank-flooring", "tile-installation": "tile-installation",
                "laminate-flooring": "laminate-flooring", "stair-treads": "stair-treads", "floor-repair": "floor-repair"}
    for s in old_cost:
        for c in ["sarasota", "bradenton", "lakewood-ranch", "venice", "parrish", "palmetto", "siesta-key", "longboat-key"]:
            if f"{s}-cost-{c}" not in POST: base += f"/blog/{s}-cost-{c}/ /cost/{s}/ 301\n"
    for old, new in load("legacy_redirects.json", {}).items():
        base += f"{old} {new} 301\n"
    w("_redirects", base)

def process_static():
    from PIL import Image, ImageOps
    src = os.path.join(ROOT, "static")
    for dp, dn, fn in os.walk(src):
        for f in fn:
            if f == "_redirects": continue
            rel = os.path.relpath(os.path.join(dp, f), src)
            dst = os.path.join(DIST, rel); os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(os.path.join(dp, f), dst)
    photos = {n for n, _ in PHOTOS.values()} | {"hero-hardwood", "stair-flooring-sarasota", "tile-bathroom-sarasota", "lvp-bedroom-sarasota", "lvp-hallway-sarasota"}
    for n in photos:
        p = os.path.join(src, "images", n + ".jpg")
        if not os.path.exists(p): continue
        im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
        im = ImageOps.fit(im, (1600, 1200), Image.LANCZOS)
        for wd in (480, 960, 1600):
            r = im.resize((wd, wd * 3 // 4), Image.LANCZOS)
            r.save(os.path.join(DIST, "images", f"{n}-{wd}.webp"), quality=78, method=6)
        im.resize((960, 720), Image.LANCZOS).save(os.path.join(DIST, "images", f"{n}-960.jpg"), quality=80, optimize=True, progressive=True)
        os.remove(os.path.join(DIST, "images", n + ".jpg"))

def main():
    if os.path.isdir(DIST): shutil.rmtree(DIST, ignore_errors=True)
    os.makedirs(DIST, exist_ok=True)
    process_static()
    build_home(); build_services(); build_landings(); build_cities(); build_city_services(); build_areas(); build_cost(); build_blog(); build_faq(); build_static_pages(); build_tools()
    build_machine_files(); build_redirects(); os.makedirs(os.path.join(ROOT, 'docs'), exist_ok=True); check_links()
    print(f"built {len(PAGES)} indexable pages -> {DIST}  | cities {len(CITIES)} | city×service {len(SVC_CITY_PAGES)} | posts {len(POSTS)}")

if __name__ == "__main__":
    main()
