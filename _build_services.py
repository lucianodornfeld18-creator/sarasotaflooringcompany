#!/usr/bin/env python3
"""
Build the 6 service-index pages: /[service]/index.html
Each one shows the service overview + pricing + checklist + per-city links + FAQ.
"""
import os
from _data import BUSINESS, CITIES, CITY_ORDER, SERVICES, SERVICE_ORDER, CHECKLIST, REVIEWS, WA_LINK, TEL_LINK
from _gen import (
    page_head, header, footer, render_schemas, localbiz_schema, breadcrumb_schema,
    faq_schema, stat_badge, wa_banner, cta_banner, reviews_block, faq_block,
    checklist_block, pricing_block, scope_list_html, internal_links_box, SITE,
)

OUT = "/home/claude/sarasota-flooring"

for slug in SERVICE_ORDER:
    sv = SERVICES[slug]
    title = f"{sv['h1_phrase']} Sarasota FL | {BUSINESS['short_name']}"[:65]
    desc = (
        f"{sv['name']} installation across Sarasota, Bradenton, Lakewood Ranch &amp; the barrier islands. "
        f"Owner-installed, {CHECKLIST['points']}-point standard, 2-year written warranty. Free estimate in 24 hours."
    )[:158]
    if len(desc) > 158: desc = desc[:155] + "..."

    schemas = [
        localbiz_schema(
            page_path=slug,
            service_slug=slug,
            service_name=sv["name"],
            description=sv["intro_lead"],
        ),
        faq_schema(sv["faqs"]),
        breadcrumb_schema([("Home","/"),(sv["name"],None)]),
    ]

    # Other services as related links
    other_services = [(SERVICES[s]["name"], f"/{s}/") for s in SERVICE_ORDER if s != slug]
    # All cities for this service
    city_links = [(f"{sv['name']} in {CITIES[c]['name']}, FL", f"/{slug}/{c}/") for c in CITY_ORDER]

    html = f"""{page_head(title, desc, slug+"/")}
<body>
{render_schemas(schemas)}
{header()}

<section class="page-hero">
  <div class="container">
    <span class="eyebrow on-dark">{sv['name']} · Sarasota &amp; Manatee Counties</span>
    <h1>{sv['h1_phrase']} in <span class="accent">Sarasota, FL</span></h1>
    <p class="lead">{sv['intro_lead']}</p>
    <div class="page-hero-trust">
      <span>Owner on every job</span>
      <span>{CHECKLIST['points']}-point standard</span>
      <span>2-year written warranty</span>
      <span>Free estimate in 24 hours</span>
    </div>
  </div>
</section>

<nav class="breadcrumbs"><div class="container"><ol><li><a href="/">Home</a></li><li>{sv['name']}</li></ol></div></nav>

<section class="intro">
  <div class="container">
    <div class="intro-content">
      <p>{sv['intro_long_p1']}</p>
      <p>{sv['intro_long_p2']}</p>
      {stat_badge()}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:880px;margin:0 auto">
      <span class="eyebrow">What's Included</span>
      <h2 style="margin-bottom:1rem">Every {sv['short'].lower()} install includes:</h2>
      {scope_list_html(sv['scope_items'])}
    </div>
  </div>
</section>

<section class="services-section">
  <div class="container">
    <div style="max-width:880px;margin:0 auto">
      <span class="eyebrow">Pricing</span>
      <h2 style="margin-bottom:.45rem">{sv['name']} prices in Sarasota &amp; Manatee (2026)</h2>
      <p style="color:var(--gray);margin-bottom:1.2rem">Transparent installed pricing. Final pricing varies by subfloor condition and project scope — every quote is custom and itemized. <a href="{TEL_LINK}" style="color:var(--emerald);font-weight:600">Free in-home estimate →</a></p>
      {pricing_block(sv)}
    </div>
  </div>
</section>

{checklist_block()}

<section class="areas-section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">By City</span>
      <h2>{sv['h1_phrase']} across all 8 service areas.</h2>
      <p>Same install standard, same owner-on-site supervision, same 2-year warranty — across every city we serve.</p>
    </div>
    <div class="areas-pills">{"".join(f'<a href="/{slug}/{c}/" class="area-pill">{sv["short"]} in {CITIES[c]["name"]}</a>' for c in CITY_ORDER)}</div>
  </div>
</section>

{reviews_block(limit=4)}

{wa_banner()}

<section>
  <div class="container">
    {internal_links_box(f"Related — Other Services We Install",other_services)}
  </div>
</section>

{faq_block(sv['faqs'], heading=f"{sv['name']} FAQ")}

{cta_banner(
    headline=f"Ready for {sv['short'].lower()}? Free in-home estimate.",
    sub=f"Owner brings samples sized for your home, your lighting, and your existing finishes. {BUSINESS['response_time']}"
)}

{footer()}
</body></html>"""

    path = f"{OUT}/{slug}/index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w",encoding="utf-8") as f: f.write(html)
    print(f"✓ Built /{slug}/")

print(f"\nAll {len(SERVICE_ORDER)} service-index pages built.")
