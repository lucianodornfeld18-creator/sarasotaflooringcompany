#!/usr/bin/env python3
"""
Build the homepage: /index.html
Hero: SPLIT LAYOUT — left headline/trust + right conversion FORM (stcloudflconcrete style)
Completely different from Triangle's centered dark hero.
"""
import os
from _data import (
    BUSINESS, CITIES, CITY_ORDER, SERVICES, SERVICE_ORDER,
    CHECKLIST, REVIEWS, WA_LINK, TEL_LINK, SMS_LINK,
    HERO_TRUST_BADGES, WHY_US_POINTS, PROCESS_STEPS, GENERAL_BLOG_POSTS,
)
from _gen import (
    page_head, header, footer, render_schemas, org_schema, localbiz_schema,
    breadcrumb_schema, stat_badge, wa_banner, cta_banner, reviews_block,
    faq_block, write, SITE,
)

TITLE = f"Flooring Company in Sarasota FL | Hardwood, Vinyl, Tile | {BUSINESS['short_name']}"
DESC = (
    "Sarasota's owner-installed flooring company. Hardwood, LVP, tile, laminate & stair treads "
    "across Sarasota, Bradenton, Lakewood Ranch & Siesta Key. 5★ · 2-year warranty · free estimate."
)

service_cards = []
for s in SERVICE_ORDER:
    sv = SERVICES[s]
    service_cards.append(f"""<a href="/{s}/" class="service-card">
  <div class="service-card-num">SERVICE {sv['icon']}</div>
  <h3>{sv['name']}</h3>
  <p>{sv['intro_lead'][:145]}{'…' if len(sv['intro_lead'])>145 else ''}</p>
  <span class="service-card-arrow">Explore {sv['short'].lower()} →</span>
</a>""")

why_cards = []
for w in WHY_US_POINTS:
    why_cards.append(f"""<div class="why-card">
  <span class="why-icon">{w['icon']}</span>
  <h3>{w['title']}</h3>
  <p>{w['body']}</p>
</div>""")

process_html = []
for (num, title, body) in PROCESS_STEPS:
    process_html.append(f"""<div class="process-step">
  <div class="process-num">STEP {num}</div>
  <h3>{title}</h3>
  <p>{body}</p>
</div>""")

area_pills = "".join(
    f'<a href="/{c}/" class="area-pill">{CITIES[c]["name"]}, FL</a>'
    for c in CITY_ORDER
)

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

schemas = [
    org_schema(),
    localbiz_schema(page_path=""),
    breadcrumb_schema([("Home", None)]),
]

html = page_head(TITLE, DESC, "", og_image="/images/hero-og.jpg") + """
<body>
""" + render_schemas(schemas) + """
""" + header() + """

<!-- HERO — SPLIT LAYOUT (text left / form right) -->
<section style="background:var(--emerald-dark);position:relative;overflow:hidden">
  <div style="position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(200,137,61,.04) 0px,rgba(200,137,61,.04) 1px,transparent 1px,transparent 60px),repeating-linear-gradient(0deg,rgba(200,137,61,.02) 0px,rgba(200,137,61,.02) 1px,transparent 1px,transparent 80px);pointer-events:none"></div>
  <div class="container" style="position:relative;z-index:2;display:flex;align-items:center;gap:3.5rem;padding-top:4rem;padding-bottom:4rem;flex-wrap:wrap">

    <!-- LEFT: headline + trust -->
    <div style="flex:1 1 400px;min-width:0;color:#fff">
      <span style="display:inline-block;font-family:var(--font-head);font-size:.78rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#F8DDA8;margin-bottom:1.1rem">Sarasota &amp; Manatee Counties, FL</span>
      <h1 style="color:#fff;font-size:clamp(2.2rem,4.5vw,3.3rem);margin-bottom:1.1rem;line-height:1.12">
        Flooring installed by<br><span style="background:linear-gradient(90deg,#F8DDA8,#C8893D);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">the owner himself.</span>
      </h1>
      <p style="color:rgba(255,255,255,.9);font-size:1.08rem;line-height:1.6;margin-bottom:2rem;max-width:480px">No subcontracted crews, no middlemen. Hardwood, vinyl plank, tile, laminate and stair treads — hand-installed and warranted in writing for 2 years. Free estimate in 24 hours.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.6rem 1.4rem;margin-bottom:2rem">
        <span style="display:inline-flex;align-items:center;gap:7px;color:rgba(255,255,255,.95);font-family:var(--font-head);font-weight:600;font-size:.9rem"><span style="color:#F8DDA8;font-size:1.1rem">✓</span>Owner on every job</span>
        <span style="display:inline-flex;align-items:center;gap:7px;color:rgba(255,255,255,.95);font-family:var(--font-head);font-weight:600;font-size:.9rem"><span style="color:#F8DDA8;font-size:1.1rem">✓</span>63-point standard</span>
        <span style="display:inline-flex;align-items:center;gap:7px;color:rgba(255,255,255,.95);font-family:var(--font-head);font-weight:600;font-size:.9rem"><span style="color:#F8DDA8;font-size:1.1rem">✓</span>2-year written warranty</span>
        <span style="display:inline-flex;align-items:center;gap:7px;color:rgba(255,255,255,.95);font-family:var(--font-head);font-weight:600;font-size:.9rem"><span style="color:#F8DDA8;font-size:1.1rem">✓</span>Estimate in 24 hours</span>
      </div>
      <div style="display:flex;align-items:center;gap:1.4rem;flex-wrap:wrap">
        <div style="display:flex;align-items:center;gap:8px">
          <span style="font-size:1.4rem">⭐⭐⭐⭐⭐</span>
          <div>
            <div style="font-family:var(--font-head);font-weight:800;font-size:1.1rem;color:#F8DDA8">""" + BUSINESS['rating'] + """ Google Rating</div>
            <div style="font-size:.78rem;color:rgba(255,255,255,.7)">""" + str(BUSINESS['review_count']) + """ verified reviews</div>
          </div>
        </div>
        <div style="width:1px;height:36px;background:rgba(255,255,255,.2)"></div>
        <a href=""" + f'"{TEL_LINK}"' + """ style="color:#F8DDA8;font-family:var(--font-head);font-weight:700;font-size:1.18rem;text-decoration:none">📞 """ + BUSINESS['phone_display'] + """</a>
      </div>
    </div>

    <!-- RIGHT: form card -->
    <div style="flex:0 0 380px;max-width:100%">
      <div style="background:#fff;border-radius:16px;box-shadow:0 24px 60px rgba(0,0,0,.28);padding:2rem 2rem 1.75rem;position:relative">
        <div style="position:absolute;top:0;left:2rem;right:2rem;height:3px;background:linear-gradient(90deg,var(--caramel),#F8DDA8,var(--caramel));border-radius:0 0 4px 4px"></div>
        <p style="font-family:var(--font-head);font-weight:800;font-size:1.25rem;color:var(--emerald-dark);margin-bottom:.25rem">Get a Free Flooring Estimate</p>
        <p style="font-size:.88rem;color:var(--gray);margin-bottom:1.4rem">Owner responds within 24 hours · No obligation</p>
        <form action="/thanks/" method="POST" style="display:flex;flex-direction:column;gap:.85rem">
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:.75rem">
            <div>
              <label style="font-family:var(--font-head);font-size:.75rem;font-weight:700;color:var(--ink);display:block;margin-bottom:.3rem;letter-spacing:.05em;text-transform:uppercase">Name *</label>
              <input type="text" name="name" required placeholder="Your name" style="width:100%;padding:.72rem .9rem;border:1.5px solid var(--gray-border);border-radius:8px;font-size:.94rem;font-family:var(--font-body);color:var(--ink)">
            </div>
            <div>
              <label style="font-family:var(--font-head);font-size:.75rem;font-weight:700;color:var(--ink);display:block;margin-bottom:.3rem;letter-spacing:.05em;text-transform:uppercase">Phone *</label>
              <input type="tel" name="phone" required placeholder="(941) 000-0000" style="width:100%;padding:.72rem .9rem;border:1.5px solid var(--gray-border);border-radius:8px;font-size:.94rem;font-family:var(--font-body);color:var(--ink)">
            </div>
          </div>
          <div>
            <label style="font-family:var(--font-head);font-size:.75rem;font-weight:700;color:var(--ink);display:block;margin-bottom:.3rem;letter-spacing:.05em;text-transform:uppercase">Email</label>
            <input type="email" name="email" placeholder="your@email.com" style="width:100%;padding:.72rem .9rem;border:1.5px solid var(--gray-border);border-radius:8px;font-size:.94rem;font-family:var(--font-body);color:var(--ink)">
          </div>
          <div>
            <label style="font-family:var(--font-head);font-size:.75rem;font-weight:700;color:var(--ink);display:block;margin-bottom:.3rem;letter-spacing:.05em;text-transform:uppercase">Property Address</label>
            <input type="text" name="address" placeholder="City or full address" style="width:100%;padding:.72rem .9rem;border:1.5px solid var(--gray-border);border-radius:8px;font-size:.94rem;font-family:var(--font-body);color:var(--ink)">
          </div>
          <div>
            <label style="font-family:var(--font-head);font-size:.75rem;font-weight:700;color:var(--ink);display:block;margin-bottom:.3rem;letter-spacing:.05em;text-transform:uppercase">Tell Us About Your Project</label>
            <textarea name="message" rows="3" placeholder="Service type, approx. sq ft, timing…" style="width:100%;padding:.72rem .9rem;border:1.5px solid var(--gray-border);border-radius:8px;font-size:.94rem;font-family:var(--font-body);color:var(--ink);resize:vertical"></textarea>
          </div>
          <button type="submit" style="width:100%;padding:.95rem;background:var(--caramel);color:#fff;font-family:var(--font-head);font-weight:700;font-size:1.05rem;border:none;border-radius:50px;cursor:pointer;box-shadow:0 4px 16px rgba(200,137,61,.38)">
            Get My Free Estimate →
          </button>
        </form>
        <p style="text-align:center;margin-top:1rem;font-size:.82rem;color:var(--gray)">
          Or call/text: <a href=""" + f'"{TEL_LINK}"' + """ style="color:var(--emerald);font-weight:700">""" + BUSINESS['phone_display'] + """</a>
          &nbsp;·&nbsp;
          <a href=""" + f'"{WA_LINK}"' + """ target="_blank" rel="noopener" style="color:#25D366;font-weight:700">WhatsApp</a>
        </p>
      </div>
    </div>
  </div>
</section>

<!-- PROOF STRIP -->
<div style="background:var(--ink);padding:1.5rem 0">
  <div class="proof-grid container">
    <div class="proof-item"><span class="proof-num">""" + BUSINESS['rating'] + """★</span><span class="proof-label">Google Rated</span></div>
    <div class="proof-item"><span class="proof-num">100%</span><span class="proof-label">Owner-Supervised</span></div>
    <div class="proof-item"><span class="proof-num">63</span><span class="proof-label">Point Standard</span></div>
    <div class="proof-item"><span class="proof-num">2-Year</span><span class="proof-label">Written Warranty</span></div>
    <div class="proof-item"><span class="proof-num">8</span><span class="proof-label">Cities Served</span></div>
  </div>
</div>

<!-- INTRO -->
<section class="intro">
  <div class="container">
    <div class="intro-content">
      <p style="font-size:1.18rem;color:var(--ink);font-weight:500">If you've shopped flooring contractors in Sarasota or Manatee County recently, you've probably noticed the same pattern: a polished salesperson, a quick walkthrough, and an install handled by a subcontracted crew you never met. We do this differently.</p>
      <p>Sarasota Flooring Company is owner-installed. The number on this site rings the owner's phone. The same person who quotes the job is on-site every day of the install, working the floor and supervising every detail of our """ + str(CHECKLIST['points']) + """-point installation standard — built around Gulf-Coast climate realities: humidity gradients, slab moisture, salt-air corrosion on the barrier islands.</p>
      <p>Every install comes with a <strong>two-year written workmanship warranty</strong> — the longest in the Sarasota market. Service area covers Sarasota County and Manatee County: Sarasota, Bradenton, Lakewood Ranch, Venice, Parrish, Palmetto, Siesta Key, and Longboat Key.</p>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="services-section" id="services">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">What We Install</span>
      <h2>Six core services. Every install owner-supervised.</h2>
    </div>
    <div class="services-grid">""" + "".join(service_cards) + """</div>
  </div>
</section>

<!-- WHY US -->
<section style="background:#fff">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Why Choose Us</span>
      <h2>What you get when the owner installs the floor.</h2>
    </div>
    <div class="why-grid">""" + "".join(why_cards) + """</div>
  </div>
</section>

<!-- PROCESS -->
<section class="process-section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow on-dark">How It Works</span>
      <h2 style="color:#fff">From first call to 2-year warranty.</h2>
    </div>
    <div class="process-grid">""" + "".join(process_html) + """</div>
  </div>
</section>

<!-- AREAS -->
<section class="areas-section" id="areas">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Service Areas</span>
      <h2>Serving 8 cities across Sarasota &amp; Manatee.</h2>
    </div>
    <div class="areas-pills">""" + area_pills + """</div>
  </div>
</section>

""" + reviews_block(limit=4) + """

<!-- BLOG -->
<section style="background:var(--cream-deep)">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">From the Blog</span>
      <h2>Insider guides for Sarasota homeowners.</h2>
      <p>Honest writing from the owner who installs the floor. <a href="/blog/" style="color:var(--emerald);font-weight:600">See all posts →</a></p>
    </div>
    <div class="blog-grid">""" + "".join(blog_cards) + """</div>
  </div>
</section>

""" + cta_banner("Ready to start? Free in-home estimate within 24 hours.", "Call or text the owner. We bring samples sized for your lighting, cabinets, and existing floor. Free, no obligation, no pressure.") + """

""" + footer() + """
</body>
</html>"""

with open("/home/claude/sarasota-flooring/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("✓ Built /index.html — split-hero with conversion form")
