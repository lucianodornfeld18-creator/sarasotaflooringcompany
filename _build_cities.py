#!/usr/bin/env python3
"""
Build:
- 8 city index pages: /[city]/index.html
- 48 service x city pages: /[service]/[city]/index.html
"""
import os
from _data import BUSINESS, CITIES, CITY_ORDER, SERVICES, SERVICE_ORDER, CHECKLIST, REVIEWS, WA_LINK, TEL_LINK
from _gen import (
    page_head, header, footer, render_schemas, localbiz_schema, breadcrumb_schema,
    faq_schema, stat_badge, wa_banner, cta_banner, reviews_block, faq_block,
    checklist_block, pricing_block, scope_list_html, internal_links_box,
    neighborhoods_pills, SITE,
)

OUT = "/home/claude/sarasota-flooring"

# ============================================================================
# 8 CITY INDEX PAGES — /[city]/index.html
# ============================================================================
for city_slug in CITY_ORDER:
    city = CITIES[city_slug]
    title = f"Flooring Installation {city['name']} FL | {BUSINESS['short_name']}"[:65]
    desc = (
        f"Owner-installed flooring in {city['name']}, FL — hardwood, LVP, tile, laminate, stair treads. "
        f"{CHECKLIST['points']}-point standard, 2-year warranty. Free estimate in 24 hours."
    )[:158]

    schemas = [
        localbiz_schema(
            page_path=city_slug,
            city_slug=city_slug,
            city_name=city["name"],
            description=f"Flooring installation services in {city['name']}, {city['county']}, FL. " + BUSINESS["tagline_long"],
        ),
        breadcrumb_schema([("Home","/"),(city["name"]+", FL",None)]),
    ]

    # Service cards for this city
    service_cards = []
    for s in SERVICE_ORDER:
        sv = SERVICES[s]
        service_cards.append(f"""<a href="/{s}/{city_slug}/" class="service-card">
  <div class="service-card-num">SERVICE / {sv['icon']}</div>
  <h3>{sv['name']} in {city['name']}</h3>
  <p>{sv['intro_lead'][:165]}{'…' if len(sv['intro_lead'])>165 else ''}</p>
  <span class="service-card-arrow">{sv['short']} in {city['name']} →</span>
</a>""")

    # Related blog posts for this city
    blog_links = []
    for s in SERVICE_ORDER:
        sv = SERVICES[s]
        slug = f"{s.replace('-flooring','').replace('-installation','-installation') if s != 'tile-installation' else 'tile-installation'}-cost-{city_slug}"
        # actually use a cleaner slug
        slug = f"{s}-cost-{city_slug}"
        blog_links.append((f"{sv['short']} cost in {city['name']}, FL (2026)", f"/blog/{slug}/"))

    html = f"""{page_head(title, desc, city_slug+"/")}
<body>
{render_schemas(schemas)}
{header()}

<section class="page-hero">
  <div class="container">
    <span class="eyebrow on-dark">{city['county']} · {city['state']}</span>
    <h1>Flooring Installation in <span class="accent">{city['name']}, FL</span></h1>
    <p class="lead">Owner-installed flooring across {city['name']} — hardwood, luxury vinyl plank, tile, laminate, and stair treads. {CHECKLIST['name']}, two-year written warranty, free in-home estimate within 24 hours.</p>
    <div class="page-hero-trust">
      <span>Owner on every job</span>
      <span>{CHECKLIST['points']}-point standard</span>
      <span>2-year written warranty</span>
      <span>Free estimate in 24 hours</span>
    </div>
  </div>
</section>

<nav class="breadcrumbs"><div class="container"><ol><li><a href="/">Home</a></li><li>{city['name']}, FL</li></ol></div></nav>

<section class="intro">
  <div class="container">
    <div class="intro-content">
      <span class="eyebrow">{city['name']} Market Context</span>
      <h2 style="margin:.4rem 0 1rem">Flooring in {city['name']}, {city['state']} — what we know about this market.</h2>
      <p>{city['context']}</p>
      <p><strong>{city['name']} climate note:</strong> {city['humidity_note']}</p>
      {stat_badge()}
    </div>
  </div>
</section>

<section class="services-section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">All Services</span>
      <h2>Six core services we install in {city['name']}.</h2>
      <p>Same owner-on-site supervision and {CHECKLIST['points']}-point standard across every flooring type.</p>
    </div>
    <div class="services-grid">{"".join(service_cards)}</div>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:880px;margin:0 auto">
      <span class="eyebrow">Neighborhoods We Serve</span>
      <h2 style="margin-bottom:.4rem">{city['name']} communities and neighborhoods.</h2>
      <p style="color:var(--gray);margin-bottom:1.2rem">From {city['neighborhoods'][0]} to {city['neighborhoods'][-1]} — we work across every neighborhood and ZIP code in {city['name']}.</p>
      {neighborhoods_pills(city_slug)}
      <p style="margin-top:1rem;font-size:.92rem;color:var(--gray)"><strong>ZIPs served:</strong> {", ".join(city['zips'])}</p>
      <p style="font-size:.92rem;color:var(--gray)"><strong>Local landmarks:</strong> {city['landmarks']}.</p>
    </div>
  </div>
</section>

{checklist_block()}

{reviews_block(limit=4, city_filter=city['name'])}

{wa_banner(f"Free in-home estimate in {city['name']} within 24 hours")}

<section>
  <div class="container">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:1.6rem;max-width:1080px;margin:0 auto">
      {internal_links_box(f"{city['name']} Cost Guides on the Blog",blog_links)}
      {internal_links_box(f"Services in {city['name']}", [(f"{SERVICES[s]['name']}",f"/{s}/{city_slug}/") for s in SERVICE_ORDER])}
    </div>
  </div>
</section>

{cta_banner(
    headline=f"Ready to install in {city['name']}? Free estimate, 24 hours.",
    sub=f"Owner brings samples to your home in {city['name']} — often same day. Sample bring-outs and quotes are free, no obligation."
)}

{footer()}
</body></html>"""

    path = f"{OUT}/{city_slug}/index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w",encoding="utf-8") as f: f.write(html)
    print(f"✓ Built /{city_slug}/")


# ============================================================================
# 48 SERVICE × CITY PAGES — /[service]/[city]/index.html
# ============================================================================
for s_slug in SERVICE_ORDER:
    sv = SERVICES[s_slug]
    for c_slug in CITY_ORDER:
        city = CITIES[c_slug]
        title = f"{sv['h1_phrase']} {city['name']} FL | {BUSINESS['short_name']}"[:65]
        desc = (
            f"{sv['name']} in {city['name']}, FL — owner-installed, {CHECKLIST['points']}-point standard, "
            f"2-year warranty. Servicing {', '.join(city['neighborhoods'][:3])}. Free estimate in 24 hours."
        )[:158]

        schemas = [
            localbiz_schema(
                page_path=f"{s_slug}/{c_slug}",
                city_slug=c_slug,
                city_name=city["name"],
                service_slug=s_slug,
                service_name=sv["name"],
                description=f"{sv['name']} installation in {city['name']}, {city['county']}, FL. {sv['intro_lead']}",
            ),
            faq_schema(sv["faqs"]),
            breadcrumb_schema([
                ("Home","/"),
                (sv["name"],f"/{s_slug}/"),
                (city["name"]+", FL",None),
            ]),
        ]

        # Other cities for this service
        other_city_links = [(f"{sv['short']} in {CITIES[c]['name']}", f"/{s_slug}/{c}/") for c in CITY_ORDER if c != c_slug]
        # Other services in this city
        other_service_links = [(f"{SERVICES[s]['name']} in {city['name']}", f"/{s}/{c_slug}/") for s in SERVICE_ORDER if s != s_slug]
        # Cost blog post for this combo
        cost_blog_link = (f"{sv['short']} cost in {city['name']}, FL — 2026 guide", f"/blog/{s_slug}-cost-{c_slug}/")

        html = f"""{page_head(title, desc, f"{s_slug}/{c_slug}/")}
<body>
{render_schemas(schemas)}
{header()}

<section class="page-hero">
  <div class="container">
    <span class="eyebrow on-dark">{sv['name']} · {city['name']}, {city['state']}</span>
    <h1>{sv['h1_phrase']} in <span class="accent">{city['name']}, FL</span></h1>
    <p class="lead">{sv['intro_lead']} Servicing {', '.join(city['neighborhoods'][:4])}, and every neighborhood across {city['name']}.</p>
    <div class="page-hero-trust">
      <span>Owner on every job</span>
      <span>{CHECKLIST['points']}-point standard</span>
      <span>2-year written warranty</span>
      <span>Free estimate in 24 hours</span>
    </div>
  </div>
</section>

<nav class="breadcrumbs"><div class="container"><ol>
<li><a href="/">Home</a></li>
<li><a href="/{s_slug}/">{sv['name']}</a></li>
<li>{city['name']}, FL</li>
</ol></div></nav>

<section class="intro">
  <div class="container">
    <div class="intro-content">
      <p>{sv['intro_long_p1']}</p>
      <p>Here in <strong>{city['name']}</strong>: {city['context_short']} {city['humidity_note']}</p>
      <p>{sv['intro_long_p2']}</p>
      {stat_badge()}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:880px;margin:0 auto">
      <span class="eyebrow">Pricing</span>
      <h2 style="margin-bottom:.45rem">{sv['name']} prices in {city['name']} (2026)</h2>
      <p style="color:var(--gray);margin-bottom:1.2rem">Real installed pricing for the {city['name']} market. Every quote custom and itemized. <a href="{TEL_LINK}" style="color:var(--emerald);font-weight:600">Free in-home estimate →</a></p>
      {pricing_block(sv)}
    </div>
  </div>
</section>

<section class="services-section">
  <div class="container">
    <div style="max-width:880px;margin:0 auto">
      <span class="eyebrow">What's Included</span>
      <h2 style="margin-bottom:1rem">Every {sv['short'].lower()} install in {city['name']} includes:</h2>
      {scope_list_html(sv['scope_items'])}
    </div>
  </div>
</section>

{checklist_block()}

<section>
  <div class="container">
    <div style="max-width:880px;margin:0 auto">
      <span class="eyebrow">{city['name']} Neighborhoods</span>
      <h2 style="margin-bottom:.4rem">Where we install in {city['name']}.</h2>
      <p style="color:var(--gray);margin-bottom:1.2rem">{city['primary_market']}. We've installed across {city['name']}'s full neighborhood map — from {city['neighborhoods'][0]} and {city['neighborhoods'][1]} to {city['neighborhoods'][-2]} and {city['neighborhoods'][-1]}.</p>
      {neighborhoods_pills(c_slug)}
      <p style="margin-top:1rem;font-size:.92rem;color:var(--gray)"><strong>ZIPs served in {city['name']}:</strong> {", ".join(city['zips'])}</p>
      <p style="font-size:.92rem;color:var(--gray)"><strong>Landmarks near our {city['name']} install sites:</strong> {city['landmarks']}.</p>
    </div>
  </div>
</section>

{reviews_block(limit=3, city_filter=city['name'])}

{wa_banner(f"Free {sv['short'].lower()} estimate in {city['name']} — 24 hours")}

<section>
  <div class="container">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:1.6rem;max-width:1080px;margin:0 auto">
      {internal_links_box(f"{sv['short']} in Other Cities",other_city_links)}
      {internal_links_box(f"Other Services in {city['name']}",other_service_links)}
    </div>
    <div style="max-width:1080px;margin:1.6rem auto 0">
      {internal_links_box(f"Cost Guide on the Blog",[cost_blog_link])}
    </div>
  </div>
</section>

{faq_block(sv['faqs'], heading=f"{sv['name']} in {city['name']} — FAQ")}

{cta_banner(
    headline=f"Ready for {sv['short'].lower()} in {city['name']}? Free estimate, 24 hours.",
    sub=f"Owner brings samples to your home in {city['name']} — often same day. {BUSINESS['response_time']}"
)}

{footer()}
</body></html>"""

        path = f"{OUT}/{s_slug}/{c_slug}/index.html"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path,"w",encoding="utf-8") as f: f.write(html)
        print(f"✓ Built /{s_slug}/{c_slug}/")

print(f"\nAll {len(CITY_ORDER)} city pages and {len(SERVICE_ORDER)*len(CITY_ORDER)} service×city pages built.")
