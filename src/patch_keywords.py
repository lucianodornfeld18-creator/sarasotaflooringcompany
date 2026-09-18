#!/usr/bin/env python3
"""Idempotent editorial patches: (1) keyword-gap FAQs on the page that owns each query, (2) city-named stock sentences.
All dollar figures are computed from the §6 installed ranges with a 10% waste allowance.  python src/patch_keywords.py"""
import os, re, json, glob

HERE = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(HERE, "content")
def load(p): return json.load(open(os.path.join(C, p), encoding="utf-8"))
def save(p, d): json.dump(d, open(os.path.join(C, p), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
def money(x): return f"${x:,.0f}"
def rng(sf, lo, hi, waste=0.10): return f"{money(sf * (1 + waste) * lo)} to {money(sf * (1 + waste) * hi)}"

def add_faqs(path, key, faqs):
    d = load(path); o = d[key] if key else d
    have = {f["q"].lower() for f in o.setdefault("faqs", [])}
    n = 0
    for q, a in faqs:
        if q.lower() not in have: o["faqs"].append({"q": q, "a": a}); n += 1
    if n: save(path, d)
    return n

n = 0
n += add_faqs("home.json", None, [
    ("Are you a flooring store in Sarasota?",
     "No. We're a flooring installation company, not a flooring store. There's no showroom to visit: samples come to your home so you see them in your own light, next to your own cabinets. If you already bought material from a Sarasota flooring store or a big-box retailer, we install it, as long as it suits the slab and the room. People comparing local flooring companies usually find that difference matters more than the brand on the box."),
])
n += add_faqs("cost_guides/_index.json", "_index", [
    ("How much does it cost to install 1,000 sq ft of flooring in Sarasota?",
     f"At our 2026 installed ranges, with a 10% waste allowance, 1,000 sq ft runs about {rng(1000, 2.75, 5.50)} in mid-range SPC vinyl plank, {rng(1000, 3.25, 5.00)} in AC4 laminate, {rng(1000, 6, 10)} in 12 to 18 inch porcelain tile and {rng(1000, 9, 12)} in 5 inch engineered hardwood. Removing the old floor adds {money(1000 * 1.75)} to {money(1000 * 3.25)} for carpet or a floating floor, more for glued tile."),
    ("What is the labor cost to install flooring per square foot?",
     "We quote installed prices and show labor as its own line on the written quote, so you can see it. As a rule, labor is the larger share of a tile job, because of layout, cutting, setting and grouting, and the smaller share of a hardwood job, where the material carries the cost. Click vinyl plank and laminate sit at the low end for labor. If you supply the material yourself, ask for a labor-only quote at the estimate."),
    ("Is there affordable flooring installation near me that still holds up in Florida?",
     f"Yes. If you searched for affordable flooring installation near me from anywhere in Sarasota or Manatee County, the lowest-cost floor we'd still stand behind on a slab is a 12-mil or 20-mil SPC vinyl plank, at $1.75 to $5.50 per square foot installed in 2026. A 600 sq ft condo or bedroom wing lands around {rng(600, 2.75, 5.50)} in the mid-range product. <a href=\"/financing/\">Payment options</a> are covered on the financing page."),
])
n += add_faqs("cost_guides/vinyl-plank-flooring.json", "vinyl-plank-flooring", [
    ("What does it cost to replace carpet with LVP?",
     f"For 1,000 sq ft in 2026, carpet removal and haul-away runs {money(1000 * 1.75)} to {money(1000 * 3.25)}, and mid-range 20-mil SPC with a 10% waste allowance runs {rng(1000, 2.75, 5.50)}. That puts the cost to replace carpet with LVP at about {money(1000 * 1.75 + 1100 * 2.75)} to {money(1000 * 3.25 + 1100 * 5.50)}, before any slab leveling or new baseboard."),
    ("Is LVP installation labor cost quoted separately?",
     "Yes. Every written quote shows the LVP installation labor cost on its own line, apart from material, removal, slab prep and trim. Click-together SPC over a flat, dry slab is the fastest floor we install, so labor is a smaller share of the total than it is for tile. Glue-down vinyl takes longer and costs more in labor."),
])
n += add_faqs("cost_guides/hardwood-flooring.json", "hardwood-flooring", [
    ("What does it cost to install hardwood floors in a Sarasota home?",
     f"In 2026 the cost to install hardwood floors on a Sarasota slab is $9 to $15 per square foot for engineered plank glued down, and $14 to $19 for wide European white oak. For 800 sq ft of living area with 10% waste, that is {rng(800, 9, 12)} in 5 inch engineered and {rng(800, 11, 15)} in 7 to 9 inch plank, before removal of the old floor."),
])
n += add_faqs("cost_guides/tile-installation.json", "tile-installation", [
    ("What does it cost to install a tile floor in Florida?",
     f"Our 2026 range in Sarasota and Manatee counties is $6 to $10 per square foot installed for 12 to 18 inch porcelain, $9 to $15 for large-format and $8 to $13 for wood-look plank. So the cost to install a tile floor in a 500 sq ft Florida kitchen and living area, with 10% waste, is about {rng(500, 6, 10)} in standard porcelain. Removing old glued tile adds $2.50 to $4.50 per square foot."),
])
n += add_faqs("services_extra/vinyl-plank-flooring.json", "vinyl-plank-flooring", [
    ("Glue-down vs floating vinyl plank: which do you install more?",
     "Floating, by a wide margin. On a flat slab that passes its moisture test, a click-together SPC floor goes down fast and can be lifted if a plank is damaged. We use glue-down vinyl plank where rolling loads, heavy rental traffic or big sun-exposed rooms make a floating floor a risk. The glue down vs floating vinyl plank decision is made after the slab reading, not before."),
])
n += add_faqs("services_extra/tile-installation.json", "tile-installation", [
    ("Wood-look tile vs LVP: which makes more sense here?",
     "Wood-look tile wins in flood-exposed ground floors, lanais and homes that sit closed up all summer, because porcelain ignores water and heat. LVP wins on comfort, speed and price, at $2.75 to $5.50 per square foot installed against $8 to $13 for wood-look porcelain plank in 2026. The longer comparison is in <a href=\"/blog/lvp-vs-porcelain-tile-better-florida-house/\">LVP or porcelain tile for a Florida house</a>."),
])
n += add_faqs("landings/condo-flooring.json", None, [
    ("What is the best flooring for condos in Florida?",
     "For most upper-floor units, a rigid-core vinyl plank or an engineered hardwood over an acoustic underlayment that meets the association's IIC number. Porcelain tile works too, but it needs a sound mat under it and adds weight and height. The best flooring for condos in Florida is whichever assembly your documents approve, so start with the rules. <a href=\"/blog/best-flooring-florida-condo-upper-floor/\">More on upper-floor condo flooring</a>."),
    ("Can you put hardwood floors in a Florida condo?",
     "Usually yes, as engineered hardwood glued over an approved acoustic mat, never solid plank nailed down. You can put hardwood floors in a Florida condo when the association approves the assembly's IIC rating and the unit holds steady humidity year-round. Seasonal owners who turn the air conditioning up for the summer are better served by vinyl plank or tile."),
    ("What flooring works for a second floor condo in Florida?",
     "Flooring for a second floor condo in Florida has to satisfy the neighbor below as much as the owner. Most associations want a tested floor-and-underlayment assembly at IIC 50 or higher, and some ban floating floors outright. We match the product to your building's rule, put the test report in the approval packet and schedule around the elevator. Use the <a href=\"/tools/condo-flooring-approval-checklist/\">condo approval checklist</a> to see what your manager will ask for."),
])
# financing page: one natural paragraph
fp = "pages/financing.json"; d = load(fp)
add = "<p>People who search for flooring installation near me with financing are usually weighing a whole-house job against doing it room by room. Both work. We can phase a project so each stage is paid on completion, and we're glad to talk through payment timing at the free estimate.</p>"
if "near me with financing" not in d["financing"]["html"]:
    d["financing"]["html"] += add; save(fp, d); n += 1
# areas page: University Park and other close-in communities that have no page of their own
fp = "areas.json"; d = load(fp)
add = "<p>Several close-in communities don't have their own page because they sit inside a larger one. Flooring jobs in University Park, The Meadows, Fruitville and Bee Ridge are covered on the <a href=\"/sarasota/\">Sarasota page</a>; Palmer Ranch and Gulf Gate are there too. Lido Key and St. Armands follow the same condo rules described for <a href=\"/longboat-key/\">Longboat Key</a>.</p>"
if "University Park" not in d.get("intro_html", ""):
    d["intro_html"] = d.get("intro_html", "") + add; save(fp, d); n += 1

# ---- city-named stock sentences (guarantees no two city pages share them)
names = {c["slug"]: c["name"] for c in load("city_list.json")}
PAT = [(r"(?:Typical 2026 installed pricing here runs|Expect|In 2026 most installed floors here land between|Installed, 2026 jobs here usually price out at|Budget|Our 2026 installed range for the floors that suit these homes is|Most 2026 quotes we write here fall between|At 2026 prices, plan on|Figure|Installed cost in 2026 generally sits between) (\$[\d.,]+) (?:to|and) (\$[\d.,]+)[^.]*\.",
        lambda m, c: f"In {c}, 2026 installed pricing runs {m.group(1)} to {m.group(2)} per square foot."),
       (r"(?:See the cost guide or the flooring cost calculator for more worked examples\.|The cost guide and the calculator show more worked examples\.|More worked examples are in the cost guide; the calculator handles your own square footage\.|For other room sizes, run the numbers in the calculator or open the cost guide\.|The calculator and the cost guides cover other project sizes\.)",
        lambda m, c: f"The cost guides and the calculator cover other {c} project sizes."),
       (r"(?:New floor coverings don't normally need a building permit here\.|Replacing a floor covering is normally permit-exempt\.|A straight floor-covering swap usually needs no permit\.|Floor coverings alone rarely trigger a permit\.|Swapping the floor covering is generally exempt from permitting\.)",
        lambda m, c: f"Replacing a floor covering in {c} normally needs no building permit."),
       (r"Waterproof vinyl and tile, typical 2026 pricing from \$1\.75/sq ft\.", lambda m, c: f"Waterproof vinyl and tile for {c} homes, 2026 pricing from $1.75/sq ft.")]
for fp in glob.glob(os.path.join(C, "cities", "*.json")):
    d = json.load(open(fp, encoding="utf-8")); c = names.get(d.get("slug"), "")
    if not c: continue
    raw = json.dumps(d, ensure_ascii=False)
    new = raw
    for pat, fn in PAT: new = re.sub(pat, lambda m, fn=fn: fn(m, c).replace('"', '\\"'), new)
    if new != raw:
        json.dump(json.loads(new), open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1); n += 1
# cost guides: shared intro sentence to the worked examples
for s in ("hardwood-flooring", "laminate-flooring", "tile-installation"):
    fp = f"cost_guides/{s}.json"; d = load(fp); raw = json.dumps(d, ensure_ascii=False)
    label = {"hardwood-flooring": "hardwood", "laminate-flooring": "laminate", "tile-installation": "tile"}[s]
    new = re.sub(r"These three examples use our 2026 installed ranges from the price table above,", f"The three {label} examples below use our 2026 installed ranges from the price table above,", raw)
    new = new.replace("Run your own square footage through the flooring cost calculator for a same-day range.", f"Put your own {label} square footage into the flooring cost calculator for a range you can use today.") if s != "laminate-flooring" else new
    if new != raw: save(fp, json.loads(new)); n += 1
print("patches applied:", n)
