#!/usr/bin/env python3
"""
Build the homepage: /index.html
"""
import os, json
from _data import BUSINESS, CITIES, CITY_ORDER, SERVICES, SERVICE_ORDER, CHECKLIST, REVIEWS, WA_LINK, TEL_LINK, HERO_TRUST_BADGES, WHY_US_POINTS, PROCESS_STEPS, GENERAL_BLOG_POSTS
from _gen import (
    page_head, header, footer, render_schemas, org_schema, localbiz_schema, breadcrumb_schema,
    stat_badge, wa_banner, cta_banner, reviews_block, faq_block, write, SITE,
)

TITLE = f"Flooring Company in Sarasota FL | Hardwood, Vinyl, Tile | {BUSINESS['short_name']}"
DESC = (
    f"Sarasota's owner-installed flooring company. Hardwood, LVP, tile, laminate &amp; stair "
    f"treads across Sarasota, Bradenton, Lakewood Ranch &amp; Siesta Key. {BUSINESS['rating']}★ "
    f"· 2-year warranty · free estimate in 24 hours."
)

# Trust badges in hero
trust_html = "".join(f"<span>{b}</span>" for b in HERO_TRUST_BADGES)

# Service cards
service_cards = []
for s in SERVICE_ORDER:
    sv = SERVICES[s]
    service_cards.append(f"""<a href="/{s}/" class="service-card">
  <div class="service-card-num">SERVICE / {sv['icon']}</div>
  <h3>{sv['name']}</h3>
  <p>{sv['intro_lead']}</p>
  <span class="service-card-arrow">Explore {sv['short'].lower()} →</span>
</a>""")

# Why us cards
why_cards = []
for w in WHY_US_POINTS:
    why_cards.append(f"""<div class="why-card">
  <span class="why-icon">{w['icon']}</span>
  <h3>{w['title']}</h3>
  <p>{w['body']}</p>
</div>""")

# Process steps
process_html = []
for (num,title,body) in PROCESS_STEPS:
    process_html.append(f"""<div class="process-step">
  <div class="process-num">STEP {num}</div>
  <h3>{title}</h3>
  <p>{body}</p>
</div>""")

# Service area pills
area_pills = "".join(f'<a href="/{c}/" class="area-pill">{CITIES[c]["name"]}, FL</a>' for c in CITY_ORDER)

# Blog teaser
blog_cards = []
for p in GENERAL_BLOG_POSTS[:3]:
    blog_cards.append(f"""<a href="/blog/{p['slug']}/" class="blog-card">
  <div class="blog-card-body">
    <div class="blog-category">{p['category']}</div>
    <h3>{p['title']}</h3>
    <p>{p['summary']}</p>
    <div class="blog-card-meta"><span>{p['read_time']}</span><span>{p['date']}</span></div>
  </div>
</a>""")

# Schemas
schemas = [
    org_schema(),
    localbiz_schema(page_path=""),
    breadcrumb_schema([("Home",None)]),
]

# ============================================================================
# BUILD THE PAGE
# ============================================================================
html = f"""{page_head(TITLE,DESC,"",og_image="/images/hero-og.jpg")}
<body>
{render_schemas(schemas)}
{header()}

<!-- HERO -->
<section class="hero" role="banner">
  <div class="hero-bg">
    <div class="hero-overlay"></div>
  </div>
  <div class="hero-content">
    <span class="eyebrow on-dark">{BUSINESS['city']}, FL · Sarasota &amp; Manatee Counties</span>
    <h1>Sarasota's <span class="accent">owner-installed</span><br>flooring company.</h1>
    <p class="lead">Hardwood, luxury vinyl plank, tile, laminate, and stair treads — installed by hand, supervised by the owner on every single job, and warranted in writing for two years. Free in-home estimate within 24 hours across all of Sarasota and Manatee.</p>
    <div class="hero-ctas">
      <a href="{TEL_LINK}" class="btn btn-primary">📞 Call {BUSINESS['phone_display']}</a>
      <a href="/contact/" class="btn btn-ghost">Get Free Estimate</a>
    </div>
    <div class="hero-trust">{trust_html}</div>
  </div>
</section>

<!-- PROOF STRIP -->
<section class="proof-strip" style="padding:1.8rem 0">
  <div class="proof-grid">
    <div class="proof-item">
      <span class="proof-num">{BUSINESS['rating']}★</span>
      <span class="proof-label">Google Rated</span>
    </div>
    <div class="proof-item">
      <span class="proof-num">100%</span>
      <span class="proof-label">Owner-Supervised</span>
    </div>
    <div class="proof-item">
      <span class="proof-num">{CHECKLIST['points']}</span>
      <span class="proof-label">Point Standard</span>
    </div>
    <div class="proof-item">
      <span class="proof-num">2-Year</span>
      <span class="proof-label">Written Warranty</span>
    </div>
    <div class="proof-item">
      <span class="proof-num">24 hr</span>
      <span class="proof-label">Estimate Response</span>
    </div>
  </div>
</section>

<!-- INTRO -->
<section class="intro">
  <div class="container">
    <div class="intro-content">
      <p style="font-size:1.18rem;color:var(--ink);font-weight:500">If you've shopped flooring contractors in Sarasota or Manatee County recently, you've probably noticed the same pattern: a polished salesperson, a quick walkthrough, and an install handled by a subcontracted crew you never met until they showed up at your door. We do this differently.</p>
      <p>Sarasota Flooring Company is owner-installed. The number on this site rings the owner's phone. The same person who quotes the job is on-site every day of the install, working the floor and supervising every detail of the {CHECKLIST['points']}-point installation standard we built around Gulf-Coast climate realities — humidity gradients, slab moisture, salt-air corrosion on the barrier islands, and the HVAC quirks of newly-built planned communities.</p>
      <p>We install hardwood (solid and engineered), luxury vinyl plank (click-lock and glue-down), tile (porcelain, ceramic, natural stone, large-format), laminate (AC4 and AC5 commercial-grade), and full-staircase tread replacements. Service area covers Sarasota County and Manatee County: Sarasota, Bradenton, Lakewood Ranch, Venice, Parrish, Palmetto, Siesta Key, and Longboat Key.</p>
      <p>Every install comes with a <strong>two-year written workmanship warranty</strong> — the longest in the Sarasota market. Free in-home estimates within 24 hours, sample bring-outs free of charge, and a direct line to the owner for the entire warranty period. No call-center hand-offs, ever.</p>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="services-section" id="services">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">What We Install</span>
      <h2>Six core services. Every install owner-supervised.</h2>
      <p>From wide-plank European white oak to short-term-rental SPC vinyl, large-format porcelain to laminate stair treads — we install it all, by hand, with the same documented {CHECKLIST['points']}-point standard on every job.</p>
    </div>
    <div class="services-grid">{"".join(service_cards)}</div>
  </div>
</section>

<!-- WHY US -->
<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Why Choose Us</span>
      <h2>What you get when the owner does the install.</h2>
      <p>Six reasons our clients in Country Club East, Sanderling Club, Wellen Park, Heritage Harbour, and across the barrier islands hire us — and refer their neighbors.</p>
    </div>
    <div class="why-grid">{"".join(why_cards)}</div>
  </div>
</section>

<!-- PROCESS -->
<section class="process-section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow on-dark">How It Works</span>
      <h2>From first call to two-year warranty.</h2>
    </div>
    <div class="process-grid">{"".join(process_html)}</div>
  </div>
</section>

<!-- SERVICE AREAS -->
<section class="areas-section" id="areas">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Service Areas</span>
      <h2>Serving 8 cities across Sarasota &amp; Manatee.</h2>
      <p>From historic Laurel Park to the barrier islands to Lakewood Ranch's master-planned villages — we install across the full Sarasota–Bradenton metro.</p>
    </div>
    <div class="areas-pills">{area_pills}</div>
  </div>
</section>

<!-- REVIEWS -->
{reviews_block(limit=4)}

<!-- BLOG TEASER -->
<section style="background:var(--cream-deep)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">From the Blog</span>
      <h2>Insider guides for Sarasota homeowners.</h2>
      <p>Honest writing on what to install, what to skip, and what nobody tells you about Gulf-Coast flooring. <a href="/blog/" style="color:var(--emerald);font-weight:600">See all posts →</a></p>
    </div>
    <div class="blog-grid">{"".join(blog_cards)}</div>
  </div>
</section>

<!-- FINAL CTA -->
{cta_banner("Ready to start? Free in-home estimate within 24 hours.", "Call or text the owner directly. We bring samples sized for your lighting, your cabinets, and your existing floor. Free, no obligation, no pressure.")}

{footer()}
</body>
</html>"""

# Write
import os
os.makedirs("/home/claude/sarasota-flooring", exist_ok=True)
with open("/home/claude/sarasota-flooring/index.html","w",encoding="utf-8") as f:
    f.write(html)
print("✓ Built /index.html")
