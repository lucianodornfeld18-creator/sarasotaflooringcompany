#!/usr/bin/env python3
"""
Homepage with real project photos + keyword-dense copy (stcloudflconcrete strategy).
"""
import os
from _data import (
    BUSINESS, CITIES, CITY_ORDER, SERVICES, SERVICE_ORDER,
    CHECKLIST, REVIEWS, TEL_LINK, SMS_LINK,
    WHY_US_POINTS, PROCESS_STEPS, GENERAL_BLOG_POSTS,
)
from _gen import (
    page_head, header, footer, render_schemas, org_schema, localbiz_schema,
    breadcrumb_schema, stat_badge, wa_banner, cta_banner, reviews_block, SITE,
)

TITLE = "Flooring Company in Sarasota FL | Hardwood, Vinyl Plank, Tile Installation | Sarasota Flooring Company"
DESC = (
    "Sarasota Flooring Company — flooring installation in Sarasota, Bradenton, Lakewood Ranch & Siesta Key. "
    "Hardwood, LVP, tile, laminate, stair treads. 5★ rated · 2-year warranty · free estimate."
)

service_cards = []
for s in SERVICE_ORDER:
    sv = SERVICES[s]
    service_cards.append(f"""<a href="/{s}/" class="service-card">
  <div class="service-card-num">SERVICE {sv['icon']}</div>
  <h3>{sv['name']}</h3>
  <p>{sv['intro_lead'][:145]}{"…" if len(sv["intro_lead"])>145 else ""}</p>
  <span class="service-card-arrow">View {sv['short']} services →</span>
</a>""")

why_cards = "".join(f"""<div class="why-card">
  <span class="why-icon">{w['icon']}</span>
  <h3>{w['title']}</h3>
  <p>{w['body']}</p>
</div>""" for w in WHY_US_POINTS)

process_html = "".join(f"""<div class="process-step">
  <div class="process-num">STEP {num}</div>
  <h3>{title}</h3>
  <p>{body}</p>
</div>""" for (num, title, body) in PROCESS_STEPS)

area_pills = "".join(f'<a href="/{c}/" class="area-pill">{CITIES[c]["name"]}, FL</a>' for c in CITY_ORDER)

blog_cards = "".join(f"""<a href="/blog/{p['slug']}/" class="blog-card">
  <div class="blog-card-body">
    <div class="blog-category">{p['category']}</div>
    <h3>{p['title']}</h3>
    <p>{p['summary']}</p>
    <div class="blog-card-meta"><span>{p['read_time']}</span><span>{p['date']}</span></div>
  </div>
</a>""" for p in GENERAL_BLOG_POSTS[:3])

schemas = [
    org_schema(),
    localbiz_schema(page_path=""),
    breadcrumb_schema([("Home", None)]),
]

# Photo gallery of real work
gallery_photos = [
    ("hero-hardwood.jpg", "Wide-plank engineered hardwood flooring in Sarasota waterfront home", "Hardwood · Sarasota"),
    ("hardwood-flooring-sarasota.jpg", "Hardwood flooring installation in Sarasota FL", "Hardwood · Bradenton"),
    ("tile-bathroom-sarasota.jpg", "Large-format porcelain tile bathroom installation Sarasota FL", "Tile · Sarasota"),
    ("tile-installation-sarasota.jpg", "Outdoor porcelain tile installation Sarasota FL", "Tile · Lakewood Ranch"),
    ("lvp-hallway-sarasota.jpg", "Luxury vinyl plank flooring installation Sarasota FL", "LVP · Venice"),
    ("stair-installation-sarasota.jpg", "Hardwood stair tread installation Sarasota FL", "Stair Treads · Sarasota"),
]

gallery_html = "".join(f"""<div style="position:relative;overflow:hidden;border-radius:10px;aspect-ratio:1/1;background:#163E29">
  <img src="/images/{photo}" alt="{alt}" loading="lazy" width="400" height="300"
    style="width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s"
    onmouseover="this.style.transform='scale(1.04)'" onmouseout="this.style.transform='scale(1)'">
  <div style="position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(22,62,41,.85));padding:.6rem .9rem">
    <p style="margin:0;font-family:var(--font-head);font-size:.78rem;font-weight:600;color:#F8DDA8">{label}</p>
  </div>
</div>""" for (photo, alt, label) in gallery_photos)

html = page_head(TITLE, DESC, "", og_image="/images/hero-hardwood.jpg",
    extra_meta='<link rel="preload" as="image" href="/images/hero-hardwood.jpg" fetchpriority="high">') + """
<body>
""" + render_schemas(schemas) + """
""" + header() + f"""

<!-- ====================================================
     HERO — real project photo + form (stcloudflconcrete style)
     ==================================================== -->
<section style="position:relative;overflow:hidden;min-height:auto;display:flex;align-items:flex-start">
  <!-- Real hardwood photo background -->
  <div style="position:absolute;inset:0;z-index:0">
    <img src="/images/hero-hardwood.jpg" alt="Flooring company in Sarasota FL — hardwood installation by Sarasota Flooring Company"
      width="1600" height="900" fetchpriority="high"
      style="width:100%;height:100%;object-fit:cover;object-position:center">
    <div style="position:absolute;inset:0;background:linear-gradient(105deg,rgba(22,62,41,.92) 0%,rgba(22,62,41,.82) 45%,rgba(22,62,41,.5) 100%)"></div>
  </div>

  <div class="container" style="position:relative;z-index:2;display:flex;align-items:center;gap:3.5rem;padding-top:1rem;padding-bottom:1.8rem;flex-wrap:wrap;align-items:flex-start">

    <!-- LEFT: headline + keyword-rich trust copy -->
    <div style="flex:1 1 400px;min-width:0;color:#fff">
      <span style="display:inline-block;font-family:var(--font-head);font-size:.75rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#F8DDA8;margin-bottom:1.1rem">
        Flooring Company · Sarasota, FL · Manatee County
      </span>
      <h1 style="color:#fff;font-size:clamp(2rem,4.5vw,3.2rem);margin-bottom:1rem;line-height:1.12">
        Flooring Installation in<br><span style="background:linear-gradient(90deg,#F8DDA8,#C8893D);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">Sarasota &amp; Manatee, FL</span>
      </h1>
      <p style="color:rgba(255,255,255,.92);font-size:1.06rem;line-height:1.62;margin-bottom:1.4rem;max-width:490px">
        <strong style="color:#F8DDA8">Sarasota Flooring Company</strong> is a full-service flooring contractor serving Sarasota, Bradenton, Lakewood Ranch, Venice, Parrish, Palmetto, Siesta Key, and Longboat Key. We specialize in hardwood flooring, luxury vinyl plank, tile installation, laminate, and stair treads — with a 2-year written warranty on every install.
      </p>
      <div style="display:flex;flex-wrap:wrap;gap:.55rem 1.3rem;margin-bottom:2rem">
        <span style="display:inline-flex;align-items:center;gap:7px;color:rgba(255,255,255,.95);font-family:var(--font-head);font-weight:600;font-size:.88rem"><span style="color:#F8DDA8">✓</span>Licensed &amp; Insured</span>
        <span style="display:inline-flex;align-items:center;gap:7px;color:rgba(255,255,255,.95);font-family:var(--font-head);font-weight:600;font-size:.88rem"><span style="color:#F8DDA8">✓</span>63-Point Installation Standard</span>
        <span style="display:inline-flex;align-items:center;gap:7px;color:rgba(255,255,255,.95);font-family:var(--font-head);font-weight:600;font-size:.88rem"><span style="color:#F8DDA8">✓</span>2-Year Written Warranty</span>
        <span style="display:inline-flex;align-items:center;gap:7px;color:rgba(255,255,255,.95);font-family:var(--font-head);font-weight:600;font-size:.88rem"><span style="color:#F8DDA8">✓</span>Free Estimate · 24 Hours</span>
      </div>
      <div style="display:flex;align-items:center;gap:1.4rem;flex-wrap:wrap">
        <div style="display:flex;align-items:center;gap:8px">
          <span style="font-size:1.35rem">⭐⭐⭐⭐⭐</span>
          <div>
            <div style="font-family:var(--font-head);font-weight:800;font-size:1.05rem;color:#F8DDA8">{BUSINESS['rating']} Google Rating</div>
            <div style="font-size:.76rem;color:rgba(255,255,255,.7)">{BUSINESS['review_count']} verified reviews</div>
          </div>
        </div>
        <div style="width:1px;height:34px;background:rgba(255,255,255,.25)"></div>
        <a href="{TEL_LINK}" style="color:#F8DDA8;font-family:var(--font-head);font-weight:700;font-size:1.15rem;text-decoration:none;white-space:nowrap">📞 {BUSINESS['phone_display']}</a>
      </div>
    </div>

    <!-- RIGHT: conversion form -->
    <div style="flex:0 0 370px;max-width:100%">
      <div style="background:#fff;border-radius:14px;box-shadow:0 24px 60px rgba(0,0,0,.32);padding:1.85rem 1.85rem 1.6rem;position:relative">
        <div style="position:absolute;top:0;left:1.85rem;right:1.85rem;height:3px;background:linear-gradient(90deg,var(--caramel),#F8DDA8,var(--caramel));border-radius:0 0 4px 4px"></div>
        <p style="font-family:var(--font-head);font-weight:800;font-size:1.2rem;color:var(--emerald-dark);margin-bottom:.2rem">Get a Free Flooring Estimate</p>
        <p style="font-size:.85rem;color:var(--gray);margin-bottom:1.3rem">Sarasota Flooring Company — free estimate, no obligation</p>
        <form action="/thanks/" method="POST" style="display:flex;flex-direction:column;gap:.8rem">
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:.7rem">
            <div>
              <label style="font-family:var(--font-head);font-size:.72rem;font-weight:700;color:var(--ink);display:block;margin-bottom:.28rem;letter-spacing:.06em;text-transform:uppercase">Name *</label>
              <input type="text" name="name" required placeholder="Your name" style="width:100%;padding:.68rem .85rem;border:1.5px solid var(--gray-border);border-radius:7px;font-size:.93rem;font-family:var(--font-body);color:var(--ink)">
            </div>
            <div>
              <label style="font-family:var(--font-head);font-size:.72rem;font-weight:700;color:var(--ink);display:block;margin-bottom:.28rem;letter-spacing:.06em;text-transform:uppercase">Phone *</label>
              <input type="tel" name="phone" required placeholder="(941) 000-0000" style="width:100%;padding:.68rem .85rem;border:1.5px solid var(--gray-border);border-radius:7px;font-size:.93rem;font-family:var(--font-body);color:var(--ink)">
            </div>
          </div>
          <div>
            <label style="font-family:var(--font-head);font-size:.72rem;font-weight:700;color:var(--ink);display:block;margin-bottom:.28rem;letter-spacing:.06em;text-transform:uppercase">Email</label>
            <input type="email" name="email" placeholder="your@email.com" style="width:100%;padding:.68rem .85rem;border:1.5px solid var(--gray-border);border-radius:7px;font-size:.93rem;font-family:var(--font-body);color:var(--ink)">
          </div>
          <div>
            <label style="font-family:var(--font-head);font-size:.72rem;font-weight:700;color:var(--ink);display:block;margin-bottom:.28rem;letter-spacing:.06em;text-transform:uppercase">Property Address</label>
            <input type="text" name="address" placeholder="City or full address" style="width:100%;padding:.68rem .85rem;border:1.5px solid var(--gray-border);border-radius:7px;font-size:.93rem;font-family:var(--font-body);color:var(--ink)">
          </div>
          <div>
            <label style="font-family:var(--font-head);font-size:.72rem;font-weight:700;color:var(--ink);display:block;margin-bottom:.28rem;letter-spacing:.06em;text-transform:uppercase">Tell Us About Your Project</label>
            <textarea name="message" rows="2" placeholder="Service type, sq ft, timing…" style="width:100%;padding:.68rem .85rem;border:1.5px solid var(--gray-border);border-radius:7px;font-size:.93rem;font-family:var(--font-body);color:var(--ink);resize:vertical"></textarea>
          </div>
          <button type="submit" style="width:100%;padding:.9rem;background:var(--caramel);color:#fff;font-family:var(--font-head);font-weight:700;font-size:1rem;border:none;border-radius:50px;cursor:pointer;box-shadow:0 4px 16px rgba(200,137,61,.38)">
            Get My Free Estimate! →
          </button>
        </form>
        <p style="text-align:center;margin-top:.9rem;font-size:.8rem;color:var(--gray)">
          Or call now: <a href="{TEL_LINK}" style="color:var(--emerald);font-weight:700">{BUSINESS['phone_display']}</a>
        </p>
      </div>
    </div>
  </div>
</section>

<!-- PROOF STRIP -->
<div style="background:var(--ink);padding:1.4rem 0">
  <div class="proof-grid container">
    <div class="proof-item"><span class="proof-num">{BUSINESS['rating']}★</span><span class="proof-label">Google Rated</span></div>
    <div class="proof-item"><span class="proof-num">100%</span><span class="proof-label">Owner-Supervised</span></div>
    <div class="proof-item"><span class="proof-num">63</span><span class="proof-label">Point Standard</span></div>
    <div class="proof-item"><span class="proof-num">2-Year</span><span class="proof-label">Written Warranty</span></div>
    <div class="proof-item"><span class="proof-num">8</span><span class="proof-label">Cities Served</span></div>
  </div>
</div>

<!-- ABOUT / KEYWORD-RICH INTRO (stcloudflconcrete strategy) -->
<section style="background:#fff">
  <div class="container">
    <div style="max-width:880px;margin:0 auto">
      <span class="eyebrow">Flooring Company in Sarasota, FL</span>
      <h2 style="margin:.4rem 0 1.2rem">Sarasota Flooring Company — Hardwood, LVP, Tile &amp; More</h2>
      <p style="font-size:1.06rem;line-height:1.75;color:var(--ink-soft)">If you're looking for a reliable flooring company in Sarasota, FL, <strong>Sarasota Flooring Company</strong> is your answer. We are a full-service flooring contractor serving Sarasota County and Manatee County, specializing in hardwood flooring installation, luxury vinyl plank (LVP), tile installation, laminate flooring, stair tread replacement, and floor repair. Whether you need new flooring for a Lakewood Ranch home, a Siesta Key beach rental, a Bradenton renovation, or a Longboat Key condo — <strong>Sarasota Flooring Company</strong> has the experience and expertise to get the job done right.</p>

      <p style="font-size:1.06rem;line-height:1.75;color:var(--ink-soft);margin-top:1rem">Our flooring services in Sarasota, FL cover everything from a single room to a whole-house install. We work with homeowners, investors, property managers, and short-term rental operators across Sarasota, Bradenton, Lakewood Ranch, Venice, Parrish, Palmetto, Siesta Key, and Longboat Key. Every flooring installation by <strong>Sarasota Flooring Company</strong> follows our {CHECKLIST['points']}-point installation standard and is backed by a 2-year written workmanship warranty — the longest in the Sarasota–Manatee flooring market. <a href="/contact/" style="color:var(--emerald);font-weight:600">Contact Sarasota Flooring Company</a> today for a free estimate.</p>

      <div style="display:flex;flex-wrap:wrap;gap:1rem;margin-top:1.6rem">
        <a href="{TEL_LINK}" class="btn btn-primary">📞 Call {BUSINESS['phone_display']}</a>
        <a href="/contact/" class="btn btn-secondary">Get a Free Estimate</a>
      </div>
    </div>
  </div>
</section>

<!-- REAL PROJECT PHOTOS GALLERY -->
<section style="background:var(--cream-deep)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Our Work in Sarasota &amp; Manatee</span>
      <h2>Real flooring projects by Sarasota Flooring Company.</h2>
      <p>Hardwood, vinyl plank, tile, and stair treads — installed across Sarasota, Bradenton, Lakewood Ranch &amp; the barrier islands.</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.1rem;margin-top:1.8rem">
      {gallery_html}
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="services-section" id="services">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Flooring Services in Sarasota, FL</span>
      <h2>Six flooring services. Sarasota, Bradenton &amp; all of Manatee.</h2>
      <p>Sarasota Flooring Company installs hardwood, luxury vinyl plank, tile, laminate, stair treads, and handles floor repair across all 8 cities in our service area.</p>
    </div>
    <div class="services-grid">{"".join(service_cards)}</div>
  </div>
</section>

<!-- WHY US + KEYWORD PARAGRAPH -->
<section style="background:#fff">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Why Choose Sarasota Flooring Company</span>
      <h2>Why homeowners in Sarasota and Manatee choose us.</h2>
    </div>
    <div class="why-grid">{why_cards}</div>

    <!-- Extra keyword paragraph below the cards -->
    <div style="max-width:880px;margin:2.5rem auto 0;font-size:1.02rem;line-height:1.75;color:var(--ink-soft);text-align:center">
      <p>When it comes to flooring installation in Sarasota, FL, <strong>Sarasota Flooring Company</strong> stands apart. We are committed to quality craftsmanship, transparent pricing, and exceptional customer service. From hardwood flooring in Lakewood Ranch to tile installation in Siesta Key, from LVP in Bradenton to stair treads in Venice — <strong>Sarasota Flooring Company</strong> delivers professional flooring services across all of Sarasota County and Manatee County. <a href="/about/" style="color:var(--emerald);font-weight:600">Learn more about Sarasota Flooring Company →</a></p>
    </div>
  </div>
</section>

<!-- PROCESS -->
<section class="process-section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow on-dark">How We Work</span>
      <h2 style="color:#fff">How to get flooring installed by Sarasota Flooring Company.</h2>
    </div>
    <div class="process-grid">{process_html}</div>
  </div>
</section>

<!-- SERVICE AREAS + KEYWORD PARAGRAPH -->
<section class="areas-section" id="areas">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Service Areas</span>
      <h2>Flooring installation across Sarasota &amp; Manatee Counties.</h2>
      <p><strong>Sarasota Flooring Company</strong> serves homeowners and businesses across 8 cities in the Sarasota–Bradenton metro area.</p>
    </div>
    <div class="areas-pills">{area_pills}</div>
    <p style="text-align:center;margin-top:1.6rem;font-size:.95rem;color:var(--gray);max-width:660px;margin-left:auto;margin-right:auto">Our flooring service area covers Sarasota, Bradenton, Lakewood Ranch, Venice, Parrish, Palmetto, Siesta Key, and Longboat Key. If you're not sure whether we service your neighborhood, <a href="/contact/" style="color:var(--emerald);font-weight:600">contact Sarasota Flooring Company</a> and we'll confirm.</p>
  </div>
</section>

""" + reviews_block(limit=4) + f"""

<!-- BLOG -->
<section style="background:var(--cream-deep)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Sarasota Flooring Blog</span>
      <h2>Flooring cost guides for Sarasota &amp; Manatee homeowners.</h2>
      <p>Pricing guides, buyer tips, and local market insights from Sarasota Flooring Company. <a href="/blog/" style="color:var(--emerald);font-weight:600">See all guides →</a></p>
    </div>
    <div class="blog-grid">{blog_cards}</div>
  </div>
</section>

""" + cta_banner(
    "Ready for new flooring in Sarasota? Call Sarasota Flooring Company.",
    f"Sarasota Flooring Company offers free in-home estimates across Sarasota, Bradenton, Lakewood Ranch, Venice, Parrish, Palmetto, Siesta Key &amp; Longboat Key. Call {BUSINESS['phone_display']} or fill out the form — we respond within 24 hours."
) + """

""" + footer() + """
</body>
</html>"""

# Fill in the service_cards_html placeholder
html = html.replace("{"".join(service_cards)}", "".join(service_cards))

with open("/home/claude/sarasota-flooring/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("✓ Built /index.html — photos + keywords + SFC logo + no WhatsApp")
