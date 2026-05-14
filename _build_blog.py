#!/usr/bin/env python3
"""
Build:
- /blog/index.html (blog listing)
- 3 general editorial blog posts
- 48 cost-by-city blog posts (6 services × 8 cities)
"""
import os
from _data import BUSINESS, CITIES, CITY_ORDER, SERVICES, SERVICE_ORDER, CHECKLIST, REVIEWS, WA_LINK, TEL_LINK, GENERAL_BLOG_POSTS
from _gen import (
    page_head, header, footer, render_schemas, localbiz_schema, breadcrumb_schema,
    article_schema, faq_schema, faq_block, stat_badge, wa_banner, cta_banner,
    internal_links_box, SITE,
)

OUT = "/home/claude/sarasota-flooring"

# ============================================================================
# Pre-generate the cost-blog topic list
# ============================================================================
COST_BLOG_POSTS = []
for s_slug in SERVICE_ORDER:
    sv = SERVICES[s_slug]
    for c_slug in CITY_ORDER:
        city = CITIES[c_slug]
        COST_BLOG_POSTS.append({
            "slug": f"{s_slug}-cost-{c_slug}",
            "service_slug": s_slug,
            "city_slug": c_slug,
            "title": f"{sv['short']} Flooring Cost in {city['name']}, FL (2026 Guide)",
            "h1": f"How Much Does {sv['name']} Cost in {city['name']}, FL? (2026 Guide)",
            "summary": f"Real 2026 installed pricing for {sv['name'].lower()} in {city['name']} — by product tier, by neighborhood, by subfloor condition. From {BUSINESS['review_count']}+ verified installs.",
            "category": "Cost Guide",
            "read_time": "10 min read",
            "date": "2026-04-01",
        })

ALL_POSTS = GENERAL_BLOG_POSTS + COST_BLOG_POSTS

# ============================================================================
# /blog/index.html
# ============================================================================
blog_title = f"Flooring Blog | Sarasota &amp; Manatee Cost Guides | {BUSINESS['short_name']}"
blog_desc = "Sarasota flooring blog — cost guides, climate notes, buyer guides, and 2026 pricing across 8 cities. Honest writing from the owner who installs the floor."
blog_schemas = [
    localbiz_schema(page_path="blog"),
    breadcrumb_schema([("Home","/"),("Blog",None)]),
]

# Top 3 general posts
featured_cards = []
for p in GENERAL_BLOG_POSTS:
    featured_cards.append(f"""<a href="/blog/{p['slug']}/" class="blog-card">
  <div class="blog-card-body">
    <div class="blog-category">{p['category']}</div>
    <h3>{p['title']}</h3>
    <p>{p['summary']}</p>
    <div class="blog-card-meta"><span>{p['read_time']}</span><span>{p['date']}</span></div>
  </div>
</a>""")

# Cost posts grouped by service
cost_sections = []
for s_slug in SERVICE_ORDER:
    sv = SERVICES[s_slug]
    items = [p for p in COST_BLOG_POSTS if p['service_slug']==s_slug]
    cards = []
    for p in items:
        cards.append(f"""<a href="/blog/{p['slug']}/" class="blog-card">
  <div class="blog-card-body">
    <div class="blog-category">{p['category']}</div>
    <h3>{p['title']}</h3>
    <p>{p['summary']}</p>
    <div class="blog-card-meta"><span>{p['read_time']}</span><span>{p['date']}</span></div>
  </div>
</a>""")
    cost_sections.append(f"""<div style="margin-top:2.6rem">
  <h2 style="margin-bottom:.4rem">{sv['name']} — cost by city</h2>
  <p style="color:var(--gray);margin-bottom:1.3rem">2026 installed pricing for {sv['name'].lower()} across all 8 cities in our service area.</p>
  <div class="blog-grid">{"".join(cards)}</div>
</div>""")

blog_index_html = f"""{page_head(blog_title, blog_desc, "blog/")}
<body>
{render_schemas(blog_schemas)}
{header()}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow on-dark">Sarasota Flooring Blog</span>
    <h1>Cost guides, climate notes, <span class="accent">honest answers.</span></h1>
    <p class="lead">Written by the owner who installs the floor — not a marketing department. Updated for 2026.</p>
  </div>
</section>
<nav class="breadcrumbs"><div class="container"><ol><li><a href="/">Home</a></li><li>Blog</li></ol></div></nav>

<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Featured</span>
      <h2>Buyer guides &amp; market context</h2>
    </div>
    <div class="blog-grid">{"".join(featured_cards)}</div>
    {"".join(cost_sections)}
  </div>
</section>

{cta_banner()}
{footer()}
</body></html>"""
with open(f"{OUT}/blog/index.html","w",encoding="utf-8") as f: f.write(blog_index_html)
print("✓ Built /blog/")


# ============================================================================
# 3 GENERAL BLOG POSTS
# ============================================================================

# POST 1: Best Flooring for Sarasota's Humidity
post1_slug = "best-flooring-sarasota-humidity"
post1 = next(p for p in GENERAL_BLOG_POSTS if p["slug"]==post1_slug)
post1_faqs = [
    ("What's the worst flooring choice for Sarasota humidity?",
     "Solid hardwood installed directly on a slab-on-grade Florida home is the choice we get hired to remediate most often. The slab moisture, combined with seasonal humidity swings, will cup, gap, or crown the floor inside the first eighteen months — and there's no cosmetic fix once it happens. Engineered hardwood with a multi-ply substrate is the right call for slab homes."),
    ("Does LVP handle Sarasota humidity better than hardwood?",
     "Yes, fundamentally. LVP and SPC are dimensionally inert in humidity — they don't expand and contract the way real wood does. That's why we recommend LVP for slab-on-grade rentals, beach houses with intermittent HVAC, and any space where humidity gradients are hard to control. The tradeoff is that LVP doesn't have the resale-defensible appeal that real hardwood carries in primary residences."),
    ("Is tile the safest choice for a Sarasota home?",
     "From a moisture-tolerance standpoint, yes — porcelain and ceramic are immune to humidity and slab moisture. The risk with tile is the installation quality: a tile floor over an unprepared subfloor cracks within five years, and the only fix is to remove and reinstall. Tile is the safest material when installed right; it's the most expensive to fix when installed wrong."),
    ("How does humidity differ between Lakewood Ranch and Siesta Key?",
     "Substantially. Lakewood Ranch sits inland with tightly-controlled HVAC in newer planned-community homes — interior humidity typically holds at 45–55%. Siesta Key sits on a barrier island with salt-air exposure, more frequent open-window conditions, and humidity gradients that swing wider. We extend hardwood acclimation from 72 to 96 hours on Siesta and Longboat for that reason."),
]
post1_body = f"""<p style="font-size:1.15rem;color:var(--ink);font-weight:500;margin-bottom:1.4rem">If you've moved to Sarasota from a drier climate, the flooring decision you faced up north isn't the flooring decision you face here. Gulf-Coast humidity, salt-air corrosion on the barrier islands, and the unique HVAC behavior of slab-on-grade Florida homes change everything about what to install and where.</p>

<p>This guide breaks it down by room, by climate zone, and by material — based on what we've learned across hundreds of installs across Sarasota County and Manatee County. We're an owner-installed flooring company, so you're reading writing from the same person who sets the planks. No upsell, no commission-driven steering — just honest material-by-material analysis.</p>

<h2>The humidity reality in Sarasota and Manatee.</h2>

<p>From May through October, dew points in our service area sit between 65 and 75 degrees Fahrenheit. The interior humidity of a properly-conditioned home runs between 45 and 55 percent. <strong>That ten-to-thirty-point gradient between outdoor and indoor humidity is where most flooring failures originate.</strong> Material shipped from a humid warehouse, installed in a cold-conditioned house without acclimation, will expand or contract — and the failure shows up six to eighteen months later.</p>

<p>The microclimates within our service area also vary. Sarasota's bayfront humidity runs five to eight percent higher than Lakewood Ranch's inland air. Siesta Key and Longboat Key, both barrier islands, add saltwater air to the mix — which corrodes fasteners, attacks adhesives, and shortens the service life of poorly-specified installs. Parrish sits twenty minutes inland and runs the driest of any city we work in.</p>

<h2>The five flooring materials, ranked for Sarasota.</h2>

<h3>1. Engineered hardwood — the best balance.</h3>
<p>For ninety percent of Florida slab-on-grade homes, engineered hardwood is the right call. The multi-ply substrate resists the dimensional movement that destroys solid hardwood on slab installs, while the real-wood top veneer carries the resale-defensible appeal of "real wood." We install engineered widths from 5 inches up through 10 inches, with the 7-inch wide-plank European White Oak being our single most-installed product across Lakewood Ranch, Country Club East, and the Lake Club.</p>
<p>Cost: $9–$15 per square foot installed for mid-range engineered; $14–$19 for premium European white oak. Two-year written warranty.</p>

<h3>2. Luxury vinyl plank (LVP) and SPC — the smart-money play.</h3>
<p>If you'd asked us in 2018, we would have said LVP was a compromise material. In 2026, that's no longer true. Premium SPC (Stone-Plastic Composite) at 8 mm thickness with a 22-mil wear layer reads remarkably close to real engineered hardwood from anywhere outside ten feet, costs less than half the price, and is completely waterproof. For kitchens, family rooms, pet households, and any rental property, it's the smart-money choice.</p>
<p>Cost: $2.75–$5.50 per square foot installed for mid-range SPC; $5.50–$9.50 for premium wide-plank LVP. Same two-year written warranty.</p>

<h3>3. Porcelain tile — the safest long-term choice.</h3>
<p>If your priority is "I want a floor I never have to think about again," porcelain tile is it. It's immune to humidity, immune to water damage, doesn't fade, doesn't dent, and lasts effectively forever. The catches: it's harder underfoot than wood or vinyl, it's cold (which matters less in Florida), and it requires expert installation — a poorly-installed tile floor fails within five years.</p>
<p>Cost: $6–$15 per square foot installed for standard porcelain; $9–$15 for large-format; $12–$22 for natural stone.</p>

<h3>4. Laminate — the right answer in specific situations.</h3>
<p>Modern 12 mm AC4 and AC5 laminate has surprised us in the last five years. The visual quality is much closer to hardwood than older laminates, the scratch resistance beats LVP, and the cost is competitive. The tradeoff: laminate is not waterproof. For dry-space high-traffic situations (home offices, hallways, bedrooms, kid playrooms), it's often the smartest dollar-per-square-foot installation in the market.</p>
<p>Cost: $3.25–$5 per square foot installed for AC4; $4.50–$6.75 for AC5 commercial-grade.</p>

<h3>5. Solid hardwood — the right call for specific situations only.</h3>
<p>Solid hardwood remains the right choice for second-story plywood-subfloor installs, historic restoration work in the older Sarasota and Venice neighborhoods, and homes where the owner specifically wants the refinish-ability that engineered hardwood doesn't fully match. <strong>It is not the right choice for slab-on-grade homes</strong> regardless of what a salesperson tells you. The failure rate on slab-installed solid hardwood in our climate is unacceptably high.</p>
<p>Cost: $10–$14 per square foot installed for 3-to-5-inch widths; $14–$19 for wide-plank European white oak.</p>

<h2>Room-by-room recommendations.</h2>

<h3>Kitchen.</h3>
<p>LVP or porcelain tile. Real hardwood (solid or engineered) is workable but requires diligent maintenance around the sink, the dishwasher, and the refrigerator. For most clients we install LVP — waterproof, dent-resistant, easier on dropped glassware than tile.</p>

<h3>Primary bathroom.</h3>
<p>Porcelain tile, always. LVP is technically rated for bathroom use but the long-term exposure to humidity, hot showers, and standing water at the vanity makes tile the smarter call. Heated-floor systems under tile are increasingly popular in our Sarasota installs — even in Florida, a heated floor on a January morning is a real comfort upgrade.</p>

<h3>Living and family room.</h3>
<p>Owner preference territory. For resale-conscious clients we install engineered hardwood. For practical-comfort clients we install premium SPC. Both are excellent calls.</p>

<h3>Bedrooms.</h3>
<p>Carpet has fallen out of favor in our market — most clients want hard-surface throughout the house. For bedrooms specifically, laminate (AC4 or AC5) is often the smartest call: warmer underfoot than tile, more scratch-resistant than LVP, and less expensive than hardwood.</p>

<h3>Barrier-island (Siesta Key, Longboat Key) waterfront homes.</h3>
<p>Salt air changes everything. We use marine-grade stainless fasteners, salt-tolerant adhesive systems, and extended acclimation windows. For waterfront primary homes our top recommendation is engineered hardwood with the salt-air spec; for STR (short-term-rental) waterfront we recommend premium SPC for durability under the turnover cycle.</p>

<h2>The acclimation question.</h2>
<p>Whatever material you install, demand on-site acclimation. We log seventy-two hours minimum across our service area, and ninety-six hours on Siesta Key, Longboat Key, and Anna Maria where humidity gradients run wider. Boxes opened on-site, planks cross-stacked for air circulation around every face, and a digital hygrometer logging through the full window. The acclimation log is part of every job folder we hand over at walk-through.</p>

<h2>What questions to ask any flooring contractor.</h2>
<p>Before you sign:</p>
<ul>
  <li>What's the workmanship warranty period and is it in writing?</li>
  <li>Will the owner be on-site, or will subcontractors handle the install?</li>
  <li>What's the on-site acclimation protocol — how many hours, how documented?</li>
  <li>For slab installs: what moisture-testing protocol will be used and when?</li>
  <li>What happens if the floor cups or gaps inside the warranty period?</li>
  <li>Can you provide a written, itemized estimate before any deposit?</li>
</ul>
<p>If you get vague answers to any of those, you've identified a flooring contractor you don't want to hire. The right answers are specific, written, and accompanied by documentation samples.</p>

<h2>Free in-home estimate in 24 hours.</h2>
<p>If you're navigating this decision for a Sarasota, Bradenton, Lakewood Ranch, Venice, Parrish, Palmetto, Siesta Key, or Longboat Key home — call or text. Sample bring-outs and quotes are free, no obligation, no sales pressure.</p>

<p><a href="{TEL_LINK}" class="btn btn-primary">📞 Call {BUSINESS['phone_display']}</a> <a href="/contact/" class="btn btn-secondary" style="margin-left:.6rem">Contact Form</a></p>"""

# POST 2: STR Flooring
post2_slug = "flooring-short-term-rental-sarasota"
post2 = next(p for p in GENERAL_BLOG_POSTS if p["slug"]==post2_slug)
post2_faqs = [
    ("What's the best flooring for a Siesta Key beach rental?",
     "Premium SPC luxury vinyl plank — 8 mm thickness with a 22-mil wear layer, glued down rather than floated. The combination is fully waterproof (matters when wet beach towels and sandy feet are part of every turnover), scratch-resistant under high foot traffic, and salt-air tolerant. We've installed it in dozens of Siesta, Longboat, and Anna Maria rentals; performance has been consistent."),
    ("Should I install hardwood in a vacation rental?",
     "We generally advise against it. The combination of high turnover traffic, inconsistent HVAC management between guests, salt-air exposure on barrier islands, and aggressive cleaning chemicals shortens the service life of real hardwood dramatically. Most STR owners who install hardwood end up replacing it inside five years. Premium SPC delivers similar visual quality at a fraction of the lifecycle cost."),
    ("Should I install tile throughout an STR?",
     "Tile works well in wet areas and entryways but it's hard underfoot for guests — and the cold, hard surface affects listing photos and reviews. Most successful STR floor plans use tile in the wet areas (bathrooms, laundry, kitchen) and LVP in the living and bedroom spaces. The visual continuity between the two materials matters; we flush-mount transitions so the floor reads as one continuous surface in listing photos."),
    ("Can I install flooring between bookings without losing a weekend?",
     "Often yes. Floating LVP can be installed in 2 days for a typical 1,200-1,500 sq ft rental. With careful scheduling we can demolish old floors on a check-out day, install on the off-day, and have it cleaned and ready before the next check-in. We've done dozens of these tight-turn installs on Siesta and Longboat."),
]
post2_body = f"""<p style="font-size:1.15rem;color:var(--ink);font-weight:500;margin-bottom:1.4rem">Short-term-rental floors take five times the wear of a primary residence, get cleaned with chemicals most homeowners would never touch, and need to look brand-new in listing photos for the next decade. After dozens of STR reflooring installs across Siesta Key, Longboat Key, Anna Maria Island, and the Wellen Park rental cluster, this is our spec.</p>

<h2>What an STR floor has to survive.</h2>
<p>Imagine a residential floor that gets the foot traffic of a small restaurant, the cleaning regimen of a hotel, the humidity exposure of an open-window Florida home, the moisture exposure of a beach house with wet swimsuits and sandy feet on every turnover, and the maintenance attention of a property that no one lives in full-time. That's the STR floor reality. Standard residential-grade flooring fails on STR duty inside three years.</p>

<h2>The material we install in 90% of Sarasota STRs.</h2>
<p>Premium SPC (Stone-Plastic Composite) luxury vinyl plank — 8 mm thickness, 22-mil wear layer, glued down rather than floated. We standardize on three brands that have held up consistently in our barrier-island installs: COREtec Pro Plus, Karndean LooseLay Longboard, and Shaw Floorté Pro 1000.</p>

<p>Why glued-down rather than floating: in an STR with constant temperature swings (HVAC off between bookings, on for two days, off for three), floating floors expand and contract enough at the seams that you eventually get visible separation. Glue-down eliminates the seam issue entirely. The install costs $1.50–$2.50/sq ft more than floating; over the ten-year service life of the floor it's the cheaper choice.</p>

<h2>Layout strategy for STRs.</h2>
<h3>Wet areas: large-format porcelain tile.</h3>
<p>Bathrooms, laundry, the entryway from the front door to the kitchen. 24x24 or 24x48 porcelain in a neutral tone — cleans easy, never absorbs moisture, lasts 30+ years. Cost: $9–$15 per square foot installed for large-format.</p>

<h3>Living areas, bedrooms: premium SPC.</h3>
<p>Wide-plank (7"+) SPC, glued down. The wider plank reads better in listing photos than narrow plank. Neutral light-oak or driftwood tones photograph best and have the longest aesthetic shelf life. Cost: $5.50–$9.50 per square foot installed.</p>

<h3>Transitions: flush-mount.</h3>
<p>The visual continuity between tile and SPC in listing photos matters. We flush-mount every transition — the tile and the SPC sit at the same finished-floor height — so the floor reads as one continuous surface in wide-angle shots. Builder-grade T-mold transitions destroy the look; we don't install them on STR work.</p>

<h2>Staircase strategy.</h2>
<p>Most barrier-island STRs have stairs. The standard builder solution is carpeted stairs — and carpeted stairs in an STR are a maintenance nightmare. We replace them with matched LVP treads with custom nosings, fabricated to match the field floor downstairs. The visual upgrade lifts listing photos noticeably; the cleaning savings over the life of the property pays for the install many times over. Cost: $65–$105 per tread installed including matching nosing.</p>

<h2>What we won't install in an STR.</h2>
<ul>
  <li><strong>Real hardwood</strong> — fails fast under STR conditions, despite what some flooring salespeople tell investors</li>
  <li><strong>Floating LVP</strong> — seam separation issues over the duty cycle (we glue down on every STR)</li>
  <li><strong>Light or white-tone flooring</strong> — sand, salt, and sunscreen residue show too aggressively; medium-tone neutrals are the right call</li>
  <li><strong>High-gloss finishes</strong> — every scratch is visible; matte and low-sheen finishes age better in listing photos</li>
  <li><strong>Carpet anywhere</strong> — the maintenance reality on STR carpet is brutal; we steer every client to hard-surface throughout</li>
</ul>

<h2>Timing the install around bookings.</h2>
<p>Most of our STR work happens during the September-to-November off-season window when nightly rates dip and owners can absorb a one-to-two-week property closure without major revenue loss. For owners who can't close the property: we've completed dozens of tight-turn installs — out by Saturday checkout, in by Sunday afternoon, ready for Monday check-in. The trick is full pre-staging of materials and a single-purpose crew (which, in our case, is the owner plus one experienced installer working a focused two-day window).</p>

<h2>What the floor costs to flooring an STR.</h2>
<p>A typical 1,400 sq ft Siesta Key or Longboat Key STR with the spec above:</p>
<ul>
  <li>1,100 sq ft of premium SPC at $7/sq ft installed = $7,700</li>
  <li>300 sq ft of large-format porcelain at $12/sq ft installed = $3,600</li>
  <li>18 stair treads at $85 each installed = $1,530</li>
  <li>Demo and haul of existing material: $2,200</li>
  <li><strong>Total: approximately $15,030</strong></li>
</ul>
<p>For a property generating $80,000–$200,000 in annual revenue, that's a one-time install that pays back in improved booking conversion, reduced maintenance issues, and a meaningful boost to comparable-listing photo quality.</p>

<h2>Free in-home estimate for STR investors.</h2>
<p>If you're managing or evaluating a short-term rental in Sarasota, Bradenton, Lakewood Ranch, Venice, Parrish, Palmetto, Siesta Key, or Longboat Key — we'll meet you at the property, walk the install scope, and have a written quote in your inbox inside 24 hours.</p>

<p><a href="{TEL_LINK}" class="btn btn-primary">📞 Call {BUSINESS['phone_display']}</a> <a href="/contact/" class="btn btn-secondary" style="margin-left:.6rem">Contact Form</a></p>"""

# POST 3: Lakewood Ranch Replacement Window
post3_slug = "lakewood-ranch-flooring-replacement-window"
post3 = next(p for p in GENERAL_BLOG_POSTS if p["slug"]==post3_slug)
post3_faqs = [
    ("My Lakewood Ranch home has builder-grade engineered hardwood from 2008. Can I sand and refinish it?",
     "Sometimes, but rarely. Builder-grade engineered hardwood from the 2005-2015 era typically has a 2-3 mm wear-layer veneer; that's barely enough material for a single light sand-and-refinish, and if there's any unevenness in the original installation a sander will burn through to the substrate. We test the veneer thickness with a destructive sample plank before recommending refinish vs. replacement."),
    ("Should I replace with the same product type or change material?",
     "Most Lakewood Ranch replacements move from builder-grade engineered hardwood to either premium engineered hardwood (wider plank, thicker veneer, better finish) or premium SPC luxury vinyl plank. The premium engineered route preserves the resale-defensible 'real wood' positioning; the premium SPC route prioritizes durability and pet-friendliness. We've installed both extensively in Country Club East, The Lake Club, and the family villages — both perform well."),
    ("How long does a whole-house Lakewood Ranch reflooring take?",
     "A typical 2,800-3,500 sq ft Lakewood Ranch home runs 5-8 working days from demo to walkthrough for engineered hardwood, 3-5 days for SPC luxury vinyl, and 7-10 days for tile-heavy installs. We schedule around your life — including pet boarding windows, work travel, and key social events. Most clients move out for the duration of demo and reinstall, return for the walkthrough."),
    ("What's the typical 2026 budget for a Lakewood Ranch whole-house refloor?",
     "Budgets cluster around four common tiers: $18,000-$28,000 for SPC luxury vinyl throughout (excluding wet areas); $32,000-$45,000 for premium engineered hardwood plus tile in wet areas; $48,000-$70,000 for wide-plank European white oak with custom tile; $75,000+ for whole-house premium tile with custom inlay work. All numbers are turnkey including demo, haul, materials, install, and transitions."),
]
post3_body = f"""<p style="font-size:1.15rem;color:var(--ink);font-weight:500;margin-bottom:1.4rem">The vast majority of Lakewood Ranch homes were built between 2005 and 2015. Both the engineered hardwood and the builder-grade porcelain tile installed in that fifteen-year window are now reaching their replacement threshold. If you bought a Lakewood Ranch home in the last few years and the floors are showing wear, this guide breaks down the scope, the budget, and the smart upgrade paths.</p>

<h2>The Lakewood Ranch flooring timeline.</h2>
<p>Lakewood Ranch began aggressive expansion in 2005. Through 2015, the dominant builder spec for the residential market was 5-inch engineered hardwood with a 2-3 mm wear-layer veneer (acceptable but not premium), 18-inch porcelain field tile in the wet areas (durable but bland), and builder-grade carpet in the bedrooms.</p>
<p>That fifteen-year cohort is now hitting its expected replacement window. Engineered hardwood with a 2-3 mm veneer carries about a 15-to-20-year service life under normal residential conditions, and the builder-grade installations from the 2005-2010 period are showing the wear: edge separation, surface dullness that doesn't recoat well, and frequently noticeable wear paths in high-traffic zones. The 18-inch porcelain tile from the same era still functions but reads as visually dated against current 24-inch and 24x48 large-format trends.</p>

<h2>The four common upgrade paths.</h2>

<h3>Path 1: Premium wide-plank engineered hardwood ($32,000–$45,000 whole-house).</h3>
<p>Move from 5-inch builder engineered to 7-inch or 9-inch wide-plank premium engineered with a 4-6 mm veneer. The visual upgrade is dramatic — wide-plank reads as architecturally premium against the narrow-plank builder spec — and the thicker veneer extends service life to 25-30 years with one sand-and-refinish available. Most popular product: European White Oak in character grade. This is the most-requested upgrade in The Lake Club and Country Club East.</p>

<h3>Path 2: Premium SPC luxury vinyl plank ($18,000–$28,000 whole-house).</h3>
<p>Move from engineered hardwood to premium SPC at 8 mm with a 22+ mil wear layer. The cost is dramatically lower than premium engineered hardwood, the durability is significantly higher, and the visual quality of premium SPC at 9"+ plank widths is genuinely close to real wood from anywhere outside ten feet. Most common in the family villages — Mallory Park, Lorraine Lakes, Park East — where the homeowner is choosing practical durability over resale-positioning.</p>

<h3>Path 3: Large-format porcelain throughout ($48,000–$70,000 whole-house).</h3>
<p>Replace both the wood and the existing tile with large-format porcelain (24x48 is the dominant 2026 spec). Permanent solution — porcelain doesn't dent, doesn't fade, lasts forty-plus years. Higher upfront cost, dramatically lower lifecycle cost. Most common in Country Club East and The Lake Club estates where the homeowner is planning a 20-year hold.</p>

<h3>Path 4: Custom mixed install ($45,000–$95,000 whole-house).</h3>
<p>Premium engineered hardwood in main living areas, large-format porcelain in wet areas and entryway, custom tile in primary bath (often with inlay or accent work), upgraded SPC in bonus rooms or pool decks. This is the most-requested in Country Club East estates and the most rewarding from a craft perspective — every install gets a custom design pass and the finished floor has the kind of architectural distinction that supports a top-of-market resale price.</p>

<h2>What to look for when assessing your existing floor.</h2>
<p>Before you call us, look at four things:</p>
<ol>
  <li><strong>Wear paths.</strong> Visible dulling or scratching in high-traffic lanes (kitchen-to-island, sofa-to-TV, doorway-to-bedroom) indicates the wear layer is approaching end-of-life.</li>
  <li><strong>Edge gaps and squeaks.</strong> Small gaps between planks that didn't exist five years ago indicate the floor is starting to fail. Squeaks often indicate subfloor issues that the new floor should address.</li>
  <li><strong>Cupping or crowning.</strong> Visible bow in planks — convex (crown) or concave (cup) — indicates moisture imbalance. A new floor needs to address the source.</li>
  <li><strong>Sun-fade.</strong> Engineered hardwood near south-facing windows often fades meaningfully over 15-20 years. Worth assessing before committing to refinish or replace.</li>
</ol>

<h2>The HOA and architectural-review process.</h2>
<p>Most Lakewood Ranch villages have architectural-review committees that approve exterior changes but generally do not require approval for interior flooring work. The exceptions: HOA-managed condominium buildings (where interior changes affect downstairs neighbors) and a small number of communities where deeded restrictions touch on flooring choices in shared-wall units. We handle the HOA paperwork on every install where it's required — packet preparation, neighbor notification windows, freight elevator scheduling, and post-install certification.</p>

<h2>Timeline expectations for a 2026 Lakewood Ranch install.</h2>
<p>From first call to walkthrough:</p>
<ul>
  <li>Day 1: Initial call, schedule in-home estimate</li>
  <li>Day 2-3: In-home estimate with sample bring-out</li>
  <li>Day 4: Written quote in inbox</li>
  <li>Day 5-12: Decision, contract, deposit, material order</li>
  <li>Day 18-25: Material arrives and acclimates on-site</li>
  <li>Day 26-32: Demolition and install</li>
  <li>Day 33: Walkthrough and final payment</li>
</ul>
<p>The whole process is typically 4-5 weeks from initial call to walking on the new floor. Larger projects (custom mixed installs, premium tile work) add 1-3 weeks.</p>

<h2>Free in-home estimate.</h2>
<p>If you're in Country Club East, The Lake Club, Esplanade, Polo Run, Mallory Park, Lorraine Lakes, Park East, Solera, or any other Lakewood Ranch village — call or text the owner direct. We bring samples sized for your home's lighting, your cabinets, and your existing furniture. The estimate is free, no obligation, no sales pressure.</p>

<p><a href="{TEL_LINK}" class="btn btn-primary">📞 Call {BUSINESS['phone_display']}</a> <a href="/contact/" class="btn btn-secondary" style="margin-left:.6rem">Contact Form</a></p>"""

GENERAL_POSTS_DATA = [
    (post1, post1_body, post1_faqs),
    (post2, post2_body, post2_faqs),
    (post3, post3_body, post3_faqs),
]

for (post, body, faqs) in GENERAL_POSTS_DATA:
    title = post["title"]
    desc = post["summary"][:158]
    schemas = [
        article_schema(post["title"], post["summary"], post["slug"], post["date"]),
        faq_schema(faqs),
        breadcrumb_schema([("Home","/"),("Blog","/blog/"),(post["title"][:50],None)]),
    ]
    html = f"""{page_head(title, desc, f"blog/{post['slug']}/")}
<body>
{render_schemas(schemas)}
{header()}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow on-dark">{post['category']} · {post['read_time']}</span>
    <h1>{post['h1']}</h1>
    <p class="lead">{post['summary']}</p>
  </div>
</section>
<nav class="breadcrumbs"><div class="container"><ol><li><a href="/">Home</a></li><li><a href="/blog/">Blog</a></li><li>{post['title'][:50]}</li></ol></div></nav>
<article class="article">
  <div class="container">
    <div class="article-meta">
      <span>Published {post['date']}</span>
      <span>By the Owner — {BUSINESS['name']}</span>
      <span>{post['read_time']}</span>
    </div>
    <div class="article-content">{body}</div>
  </div>
</article>
{faq_block(faqs, heading="Frequently Asked Questions", eyebrow="FAQ")}
{cta_banner()}
{footer()}
</body></html>"""
    path = f"{OUT}/blog/{post['slug']}/index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w",encoding="utf-8") as f: f.write(html)
    print(f"✓ Built /blog/{post['slug']}/")


# ============================================================================
# 48 COST-BY-CITY BLOG POSTS
# Each one is a real ~1500-2000 word piece using the SERVICE and CITY data
# to create a unique combination.
# ============================================================================

for post in COST_BLOG_POSTS:
    sv = SERVICES[post["service_slug"]]
    city = CITIES[post["city_slug"]]
    title = post["title"][:65]
    desc = post["summary"][:158]

    # Generate the FAQs specific to this combo
    faqs = [
        (f"What does {sv['name'].lower()} typically cost in {city['name']}, FL in 2026?",
         f"{sv['name']} installed pricing in {city['name']} ranges from {sv['pricing_rows'][0][1]} on the entry-tier products up to {sv['pricing_rows'][3][1] if len(sv['pricing_rows'])>3 else sv['pricing_rows'][-1][1]} on the premium tier. {city['humidity_note']} Most {city['name']} clients land in the mid-tier — call or text for a free, itemized estimate inside 24 hours."),
        (f"What's included in the {sv['name'].lower()} install price?",
         f"Our quoted prices in {city['name']} are turnkey: material, labor, subfloor moisture testing, self-leveling where required, demo and haul of the existing floor, transition strip carpentry, quarter-round, and a final detailed cleanup. The only add-ons that would change the quote post-signing are scope changes you approve — never surprise fees."),
        (f"How long does a {sv['short'].lower()} install take in {city['name']}?",
         f"A typical {city['name']} install runs {sv['faqs'][3][1].split('.')[0].lower()} — varies by square footage, subfloor condition, and selected product. We share an exact day-by-day schedule once we've walked the home and confirmed the scope."),
        (f"Do you guarantee the work?",
         f"Yes — every install in {city['name']} carries our two-year written workmanship warranty, the longest in the Sarasota–Manatee flooring market. {BUSINESS['guarantee']} Direct line to the owner for the full warranty period and beyond."),
    ]

    schemas = [
        article_schema(post["title"], post["summary"], post["slug"], post["date"]),
        faq_schema(faqs),
        localbiz_schema(page_path=f"blog/{post['slug']}", city_slug=post["city_slug"], city_name=city["name"]),
        breadcrumb_schema([("Home","/"),("Blog","/blog/"),(post["title"][:50],None)]),
    ]

    # Pricing rows as readable list
    pricing_rows_html = "".join(
        f"<li><strong>{label}</strong> — {price}. <em style='color:var(--gray)'>{note}</em></li>"
        for (label,price,note) in sv["pricing_rows"]
    )

    # Neighborhoods sentence
    neighborhoods_sentence = ", ".join(city["neighborhoods"][:6]) + f", and the rest of {city['name']}"

    body = f"""<p style="font-size:1.13rem;color:var(--ink);font-weight:500;margin-bottom:1.4rem">If you're researching {sv['name'].lower()} pricing for a home in {city['name']}, this guide gives you real 2026 numbers — by product tier, by scope, by typical {city['name']} install conditions. It's written by the owner of an owner-installed flooring company, not by a marketing team or an aggregator site.</p>

<h2>{sv['name']} cost in {city['name']} — the 2026 pricing landscape.</h2>
<p>{sv['intro_long_p1']}</p>
<p><strong>Here in {city['name']} specifically</strong>: {city['context_short']} That market profile shapes what's typically installed: {city['primary_market']}.</p>

<h2>{sv['name']} prices in {city['name']}, FL (full table).</h2>
<p>Real installed pricing for the {city['name']} market. Includes material, labor, subfloor moisture testing where applicable, demo and haul of existing flooring, transitions, and a final detailed cleanup. Custom quotes vary by subfloor condition and selected product.</p>
<ul>{pricing_rows_html}</ul>

<h2>What changes the {sv['name'].lower()} price in {city['name']}.</h2>
<p>Four factors move pricing up or down on any {city['name']} install:</p>
<ul>
  <li><strong>Subfloor condition.</strong> A flat, dry, sound subfloor adds nothing to the price. A slab with a quarter-inch dip in ten feet requires self-leveling ($250–$700 per room). A subfloor with squeaks or soft spots requires repair before installation can begin.</li>
  <li><strong>Material selection.</strong> Builder-grade products at the bottom of the price range; premium products at the top. The price-to-quality jump is biggest between the entry tier and the mid-tier — beyond mid-tier, returns diminish.</li>
  <li><strong>Demo scope.</strong> Carpet pulls cheap. Glued-down tile pulls expensive. Honest demo pricing in advance prevents surprise costs.</li>
  <li><strong>Layout complexity.</strong> Straight-line installs run faster than herringbone or chevron patterns. Custom inlays or accent work add labor cost but lift visual impact.</li>
</ul>

<h2>{sv['name']} climate considerations in {city['name']}.</h2>
<p>{city['humidity_note']}</p>
<p>{sv['intro_long_p2']}</p>

<h2>Neighborhoods we install across {city['name']}.</h2>
<p>{sv['short']} work in {city['name']} spans {neighborhoods_sentence}. ZIP codes served: {", ".join(city['zips'])}.</p>

<h2>What's typically included in a {sv['short'].lower()} install in {city['name']}.</h2>
<ul>{"".join(f"<li>{i}</li>" for i in sv['scope_items'][:10])}</ul>

<h2>The {CHECKLIST['points']}-point standard — applied to every {city['name']} install.</h2>
<p>Every job we run in {city['name']} follows the {CHECKLIST['name']}: pre-install site inspection, subfloor and moisture diagnostics, material acclimation, demolition and site protection, installation craft, and the quality-control walk-through. {CHECKLIST['points']} documented checkpoints, every one initialed at completion. You receive the full job folder — moisture logs, batch numbers, photo documentation, and the signed two-year warranty — at the walkthrough.</p>

<h2>The {city['name']} install timeline.</h2>
<p>A typical {sv['short'].lower()} install in {city['name']}: in-home estimate within 24 hours of the first call; written quote in your inbox before end of business that day; material order on contract signing; on-site acclimation begins 7-10 days after the material arrives; installation 2-5 working days depending on square footage; walkthrough on the final install day. Total from initial call to finished floor: 3-5 weeks for most projects.</p>

<h2>Why we're not the cheapest quote you'll receive.</h2>
<p>We won't be the lowest bid you get in {city['name']}, and we don't try to be. Owner-on-site installation costs more than a subcontracted crew. {CHECKLIST['points']}-point documented quality control costs more than checklist-free installs. Two-year written workmanship warranty costs more to underwrite than the 30-to-90-day verbal warranties most of our competitors offer. We charge for the difference. What we deliver in exchange is a floor that won't fail in eighteen months and a single person to call if it does.</p>

<h2>Get a real, written {city['name']} estimate in 24 hours.</h2>
<p>Call or text the owner direct. We'll meet you at your home in {city['name']} — usually same day — with material samples sized for your lighting, your cabinets, and your existing finishes. Sample bring-outs are free, in-home consultations are free, and the written itemized quote lands in your inbox before end of business.</p>

<p><a href="{TEL_LINK}" class="btn btn-primary">📞 Call {BUSINESS['phone_display']}</a> <a href="/contact/" class="btn btn-secondary" style="margin-left:.6rem">Contact Form</a></p>

<p style="margin-top:1.6rem;font-size:.92rem;color:var(--gray)"><strong>Related reading:</strong> <a href="/{post['service_slug']}/{post['city_slug']}/">{sv['name']} in {city['name']}, FL</a> · <a href="/{post['city_slug']}/">All flooring services in {city['name']}</a> · <a href="/{post['service_slug']}/">{sv['name']} across our service area</a></p>"""

    html = f"""{page_head(title, desc, f"blog/{post['slug']}/")}
<body>
{render_schemas(schemas)}
{header()}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow on-dark">{post['category']} · {post['read_time']}</span>
    <h1>{post['h1']}</h1>
    <p class="lead">{post['summary']}</p>
  </div>
</section>
<nav class="breadcrumbs"><div class="container"><ol>
<li><a href="/">Home</a></li>
<li><a href="/blog/">Blog</a></li>
<li>{post['title'][:50]}</li>
</ol></div></nav>
<article class="article">
  <div class="container">
    <div class="article-meta">
      <span>Published {post['date']}</span>
      <span>By the Owner — {BUSINESS['name']}</span>
      <span>{post['read_time']}</span>
    </div>
    <div class="article-content">{body}</div>
  </div>
</article>
{faq_block(faqs, heading="Frequently Asked Questions", eyebrow="FAQ")}
{cta_banner()}
{footer()}
</body></html>"""
    path = f"{OUT}/blog/{post['slug']}/index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w",encoding="utf-8") as f: f.write(html)

print(f"\nAll {len(GENERAL_BLOG_POSTS)+len(COST_BLOG_POSTS)} blog posts built.")
