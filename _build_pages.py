#!/usr/bin/env python3
"""
Build static support pages: /about/, /contact/, /faq/, /financing/, /warranty/,
/thanks/, /privacy/, /terms/, /404.html
"""
import os, json
from _data import BUSINESS, CITIES, CITY_ORDER, SERVICES, SERVICE_ORDER, CHECKLIST, REVIEWS, WA_LINK, TEL_LINK, SMS_LINK
from _gen import (
    page_head, header, footer, render_schemas, org_schema, localbiz_schema,
    breadcrumb_schema, faq_schema, stat_badge, cta_banner, reviews_block,
    write, SITE,
)

OUT = "/home/claude/sarasota-flooring"

def write_html(path,html):
    full = f"{OUT}/{path}"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full,"w",encoding="utf-8") as f: f.write(html)
    print(f"✓ Built /{path}")

# ============================================================================
# /about/index.html
# ============================================================================
about_title = f"About {BUSINESS['short_name']} | Owner-Installed Flooring in Sarasota"
about_desc = (
    "Meet the owner of Sarasota Flooring Company. Owner-installed, owner-supervised — "
    "every single flooring job in Sarasota, Bradenton, Lakewood Ranch &amp; the barrier islands. "
    "2-year written warranty. Free estimate in 24 hours."
)
about_schemas = [
    org_schema(),
    {
        "@context":"https://schema.org",
        "@type":"AboutPage",
        "name":f"About {BUSINESS['name']}",
        "url":f"{SITE}/about/",
        "description":about_desc,
    },
    breadcrumb_schema([("Home","/"),("About",None)]),
]
about_html = f"""{page_head(about_title,about_desc,"about/")}
<body>
{render_schemas(about_schemas)}
{header()}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow on-dark">About Us</span>
    <h1>The <span class="accent">owner-installed</span> flooring company<br>built for Sarasota homes.</h1>
    <p class="lead">{BUSINESS['tagline_long']}</p>
    <div class="page-hero-trust">
      <span>Founded {BUSINESS['year_founded']}</span>
      <span>{BUSINESS['rating']}★ Google Rated</span>
      <span>{BUSINESS['review_count']} verified reviews</span>
      <span>2-year written warranty</span>
    </div>
  </div>
</section>

{breadcrumb_schema([("Home","/"),("About",None)]) and ''}
<nav class="breadcrumbs"><div class="container"><ol><li><a href="/">Home</a></li><li>About</li></ol></div></nav>

<section>
  <div class="container">
    <div style="max-width:780px;margin:0 auto;font-size:1.05rem;line-height:1.75;color:var(--ink-soft)">
      <h2 style="margin-bottom:1.2rem">Why we built a flooring company differently.</h2>
      <p>Sarasota and Manatee Counties have more than eight hundred flooring contractors. Most of them operate the same way: a salesperson with a clipboard quotes the job, a subcontracted crew you've never met installs it, and the company you signed with disappears once the check clears. We've spent the last decade watching that model fail homeowners — and the floors fail with it — and we built Sarasota Flooring Company as the opposite.</p>

      <p>Every install is hand-supervised by the owner. The same person who walks your home to scope the job is on-site for the demo, for the moisture testing, for the acclimation logs, for the first plank set and the last quarter-round mitered into place. There are no subcontracted crews. There are no faceless install teams. The number on this website rings the owner's phone, every day, through the entire two-year warranty period and beyond.</p>

      <h2 style="margin:2.4rem 0 1.1rem">What that changes about your floor.</h2>
      <p>It changes the failure rate. Most flooring failures in Sarasota and Manatee don't happen because the wrong material was selected — they happen because the install was rushed. Acclimation gets skipped because the schedule is tight. Moisture testing gets skipped because the meter battery is dead. The subfloor doesn't get leveled because the crew was paid by the square foot, not the job. When the owner is the installer, none of those shortcuts make economic sense. The shortcut would be the owner's own warranty problem in eighteen months.</p>

      <p>It changes the documentation. Every job we finish hands you a folder at walk-through: moisture readings, acclimation log, batch and lot numbers, manufacturer warranty paperwork, photo documentation, and our written two-year workmanship warranty. If something moves wrong in year one or year two, we know exactly what was installed, where, and how to source matching material to fix it. That's not standard practice in flooring. It should be.</p>

      <p>It changes the communication. There's one person to call if something goes sideways during the install — and that person is the one who installed it. No CSR escalation queue. No subcontractor finger-pointing. The phone gets answered, the problem gets fixed, and the floor gets handed over the way it was supposed to be.</p>

      <h2 style="margin:2.4rem 0 1.1rem">Where we install — and why we focus.</h2>
      <p>We install across eight cities in Sarasota County and Manatee County: Sarasota, Bradenton, Lakewood Ranch, Venice, Parrish, Palmetto, Siesta Key, and Longboat Key. We don't service Tampa, St. Petersburg, or Cape Coral — those drives stretch an installation day past the point where craft quality holds up. Staying tight to the Sarasota–Bradenton metro lets us be at any job within thirty minutes, lets us do free in-home sample bring-outs without scheduling around the calendar, and lets us return for warranty work without it becoming an expedition.</p>

      <p>Our home base is in the 34212 ZIP — east Bradenton, inside Lakewood Ranch — which puts us at the geographic center of the service area. From here we're twenty minutes to downtown Sarasota, fifteen minutes to Heritage Harbour, twenty-five minutes to Wellen Park in Venice, and thirty minutes to Siesta Key. The barrier islands take a little longer, but we do enough work on Siesta, Longboat, and Anna Maria that we treat the salt-air install specs as routine.</p>

      <h2 style="margin:2.4rem 0 1.1rem">The {CHECKLIST['points']}-point standard.</h2>
      <p>Every install — whether it's a 200 sq ft tile bathroom in West Bradenton or a 4,000 sq ft whole-house wide-plank European white oak job in The Lake Club — gets the same {CHECKLIST['points']}-point checklist. Pre-install site inspection. Subfloor and moisture diagnostics. Material acclimation. Demolition and site protection. Installation craft. Quality control and walk-through. Six phases, sixty-three documented checkpoints, every one of them initialed when complete. The checklist isn't a marketing prop — it's the working document we run the job from.</p>

      <p><strong>You can review the full {CHECKLIST['points']}-point standard on any service page</strong>, or call the owner direct at <a href="{TEL_LINK}">{BUSINESS['phone_display']}</a> with any specific question. We're transparent about how we work because the kind of homeowner who hires us is the kind who reads the fine print first.</p>

      {stat_badge()}

      <h2 style="margin:2.4rem 0 1.1rem">Free in-home estimate in 24 hours.</h2>
      <p>Call or text — we typically have a sample case and a tape measure at your door inside twenty-four hours, often same-day. The estimate is free, the in-home consultation is free, and the written quote (itemized, line by line, no allowance line-items hiding upcharges) lands in your inbox before the end of the same business day.</p>

      <p style="margin-top:1.6rem">
        <a href="{TEL_LINK}" class="btn btn-primary">📞 Call {BUSINESS['phone_display']}</a>
        <a href="/contact/" class="btn btn-secondary" style="margin-left:.6rem">Online Form</a>
      </p>
    </div>
  </div>
</section>

{cta_banner()}
{footer()}
</body></html>"""
write_html("about/index.html", about_html)

# ============================================================================
# /contact/index.html
# ============================================================================
contact_title = f"Contact {BUSINESS['short_name']} | Free Flooring Estimate in 24 Hours"
contact_desc = (
    f"Get a free in-home flooring estimate across Sarasota, Bradenton &amp; Lakewood Ranch. "
    f"Call or text {BUSINESS['phone_display']} or fill out the form — Sarasota Flooring Company responds in 24 hours."
)
contact_schemas = [
    localbiz_schema(page_path="contact"),
    {
        "@context":"https://schema.org",
        "@type":"ContactPage",
        "name":f"Contact {BUSINESS['name']}",
        "url":f"{SITE}/contact/",
    },
    breadcrumb_schema([("Home","/"),("Contact",None)]),
]
hours_html = "".join(f"<tr><td>{d}</td><td>{o}–{c}</td></tr>" for (d,o,c) in BUSINESS["hours"])
contact_html = f"""{page_head(contact_title,contact_desc,"contact/")}
<body>
{render_schemas(contact_schemas)}
{header()}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow on-dark">Contact</span>
    <h1>Get a <span class="accent">free estimate</span><br>in 24 hours.</h1>
    <p class="lead">Call or text Sarasota Flooring Company directly. We'll be at your home with samples — often same day.</p>
  </div>
</section>
<nav class="breadcrumbs"><div class="container"><ol><li><a href="/">Home</a></li><li>Contact</li></ol></div></nav>

<section>
  <div class="container">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:2.5rem;max-width:1080px;margin:0 auto">
      <div>
        <h2 style="margin-bottom:1rem">Direct line to the owner.</h2>
        <p style="color:var(--ink-soft);font-size:1.02rem;line-height:1.65">No call-center routing, no front-desk filtering — the phone on this page rings the owner's mobile. Sample bring-outs are free, in-home estimates are free, and we don't sell on the spot. You get the written quote in your inbox and decide on your timeline.</p>

        <div style="background:var(--emerald-soft);border-radius:var(--radius-lg);padding:1.6rem;margin-top:1.6rem">
          <p style="font-family:var(--font-head);font-weight:700;font-size:.85rem;letter-spacing:.1em;text-transform:uppercase;color:var(--emerald-dark);margin-bottom:.4rem">Phone &amp; Text</p>
          <a href="{TEL_LINK}" style="display:block;font-family:var(--font-head);font-size:1.85rem;font-weight:800;color:var(--emerald-dark);text-decoration:none;letter-spacing:-.02em">{BUSINESS['phone_display']}</a>
          <p style="margin:.4rem 0 1rem;font-size:.92rem;color:var(--gray)">Mon–Fri 7am–7pm · Sat 8am–5pm · Sun 9am–4pm</p>
          <div style="display:flex;flex-wrap:wrap;gap:.6rem">
            <a href="{TEL_LINK}" class="btn btn-emerald">📞 Call Now</a>
            <a href="{SMS_LINK}" class="btn btn-secondary">💬 Text</a>
            
          </div>
        </div>

        <div style="background:var(--caramel-soft);border-radius:var(--radius-lg);padding:1.6rem;margin-top:1rem">
          <p style="font-family:var(--font-head);font-weight:700;font-size:.85rem;letter-spacing:.1em;text-transform:uppercase;color:var(--caramel-dark);margin-bottom:.4rem">Email</p>
          <a href="mailto:{BUSINESS['email']}" style="font-family:var(--font-head);font-size:1.18rem;font-weight:600;color:var(--ink);text-decoration:none">{BUSINESS['email']}</a>
          <p style="margin:.5rem 0 0;font-size:.88rem;color:var(--gray)">Most email replies within 4 hours during business days.</p>
        </div>

        <div style="background:var(--cream-deep);border:1px solid var(--gray-border);border-radius:var(--radius-lg);padding:1.6rem;margin-top:1rem">
          <p style="font-family:var(--font-head);font-weight:700;font-size:.85rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink);margin-bottom:.4rem">Service Area Headquarters</p>
          <p style="margin:0;font-size:1rem;font-weight:600;color:var(--ink)">{BUSINESS['street']}</p>
          <p style="margin:.15rem 0 .6rem;font-size:1rem;font-weight:600;color:var(--ink)">{BUSINESS['city']}, {BUSINESS['state']} {BUSINESS['zip']}</p>
          <p style="margin:0;font-size:.88rem;color:var(--gray)">Serving Sarasota and Manatee Counties — by appointment only. All quotes happen in your home with samples and a tape measure.</p>
        </div>
      </div>

      <div>
        <h2 style="margin-bottom:1rem">Request your estimate.</h2>
        <p style="color:var(--ink-soft);font-size:1rem;line-height:1.65;margin-bottom:1.2rem">Tell us a little about your project. The owner responds within 24 hours with next steps.</p>

        <form action="/thanks/" method="POST" style="display:flex;flex-direction:column;gap:1rem">
          <div>
            <label style="font-family:var(--font-head);font-size:.85rem;font-weight:600;color:var(--ink);margin-bottom:.4rem;display:block">Your Name *</label>
            <input type="text" name="name" required style="width:100%;padding:.85rem 1rem;border:1.5px solid var(--gray-border);border-radius:8px;font-family:var(--font-body);font-size:1rem;background:#fff">
          </div>
          <div>
            <label style="font-family:var(--font-head);font-size:.85rem;font-weight:600;color:var(--ink);margin-bottom:.4rem;display:block">Phone *</label>
            <input type="tel" name="phone" required style="width:100%;padding:.85rem 1rem;border:1.5px solid var(--gray-border);border-radius:8px;font-family:var(--font-body);font-size:1rem;background:#fff">
          </div>
          <div>
            <label style="font-family:var(--font-head);font-size:.85rem;font-weight:600;color:var(--ink);margin-bottom:.4rem;display:block">Email</label>
            <input type="email" name="email" style="width:100%;padding:.85rem 1rem;border:1.5px solid var(--gray-border);border-radius:8px;font-family:var(--font-body);font-size:1rem;background:#fff">
          </div>
          <div>
            <label style="font-family:var(--font-head);font-size:.85rem;font-weight:600;color:var(--ink);margin-bottom:.4rem;display:block">City</label>
            <select name="city" style="width:100%;padding:.85rem 1rem;border:1.5px solid var(--gray-border);border-radius:8px;font-family:var(--font-body);font-size:1rem;background:#fff">
              <option>Sarasota</option><option>Bradenton</option><option>Lakewood Ranch</option>
              <option>Venice</option><option>Parrish</option><option>Palmetto</option>
              <option>Siesta Key</option><option>Longboat Key</option><option>Other</option>
            </select>
          </div>
          <div>
            <label style="font-family:var(--font-head);font-size:.85rem;font-weight:600;color:var(--ink);margin-bottom:.4rem;display:block">Project Type</label>
            <select name="service" style="width:100%;padding:.85rem 1rem;border:1.5px solid var(--gray-border);border-radius:8px;font-family:var(--font-body);font-size:1rem;background:#fff">
              <option>Hardwood Flooring</option><option>Vinyl Plank Flooring</option><option>Tile Installation</option>
              <option>Laminate Flooring</option><option>Stair Treads</option><option>Floor Repair</option>
              <option>Not sure yet — need a recommendation</option>
            </select>
          </div>
          <div>
            <label style="font-family:var(--font-head);font-size:.85rem;font-weight:600;color:var(--ink);margin-bottom:.4rem;display:block">Tell us about the project</label>
            <textarea name="message" rows="4" placeholder="Square footage, timing, any specific products in mind..." style="width:100%;padding:.85rem 1rem;border:1.5px solid var(--gray-border);border-radius:8px;font-family:var(--font-body);font-size:1rem;background:#fff;resize:vertical"></textarea>
          </div>
          <button type="submit" class="btn btn-primary" style="margin-top:.5rem">Get My Free Estimate</button>
          <p style="font-size:.82rem;color:var(--gray);margin:0">No spam, no sales pressure. The owner responds in 24 hours with a written quote.</p>
        </form>
      </div>
    </div>
  </div>
</section>

{cta_banner()}
{footer()}
</body></html>"""
write_html("contact/index.html", contact_html)

# ============================================================================
# /faq/index.html
# ============================================================================
# Aggregate FAQs across all services + add general business FAQs
GENERAL_FAQS = [
    ("How fast can I get a flooring estimate in Sarasota?",
     f"Most of the time, within 24 hours. We schedule the in-home estimate around your availability — often same-day for calls received before noon. The estimate is free, the in-home consultation is free, and we bring physical material samples sized for your lighting, your cabinets, and your existing floor. Call {BUSINESS['phone_display']} or fill out the contact form."),
    ("What's the cheapest flooring option in Sarasota right now?",
     "Standard builder-grade laminate ($2.25–$3.75 / sq ft installed) and standard click-lock LVP ($1.75–$3.25 / sq ft installed) are the most affordable installed flooring categories in our service area. For rental properties and tight-budget renovations they make economic sense. For long-term primary residences we usually recommend stepping up to mid-range SPC luxury vinyl (~$3.50/sq ft installed) — the durability and visual quality jump is far bigger than the price jump."),
    ("Do you install on weekends?",
     "Yes — Saturday and Sunday installs are routine, especially for short-term-rental work on Siesta Key and Longboat Key where turnover windows are tight. Our standard hours are Mon–Fri 7am–7pm, Saturday 8am–5pm, Sunday 9am–4pm. Emergency repair work (failed dishwashers, hurricane recovery, water damage) is handled outside normal hours where the situation calls for it."),
    ("Does the warranty stay valid if I sell the house?",
     "The 2-year written workmanship warranty is tied to the property, not the homeowner — so it transfers to the next owner if you sell within the warranty window. We just ask that you forward the warranty packet (which we hand over at walk-through) along with the property records."),
    ("Are you licensed and insured?",
     f"Yes. Sarasota Flooring Company holds a Manatee County Local Business Tax Receipt for flooring installation work and carries general liability and workers' compensation insurance. Florida does not require a state contractor license for flooring installation (unlike for plumbing or electrical work) — but all of our installers carry insurance, and we can provide certificates of insurance to your HOA or property manager on request before a job starts."),
    ("Do you take credit cards or only cash and check?",
     "We accept all major credit cards (Visa, MasterCard, AmEx, Discover), ACH bank transfer, Zelle, and check. We offer 0% financing through GreenSky and Synchrony for qualifying projects over $2,500 — see the <a href='/financing/'>financing page</a> for details."),
    ("What if I don't like the floor after it's installed?",
     "We invest in the front-end consultation to make sure that doesn't happen. We bring full-size samples to your home before quoting so you see the product in your lighting; we let samples sit for 48 hours so you see them at all hours of the day; and we walk through every product question before any material gets ordered. For the 1-in-a-200 cases where there's still a remorse issue post-install, we work it out — usually with a partial-replacement plan against the next material purchase."),
    ("How long until you can start the install?",
     "Typically 2–4 weeks from contract signing for residential jobs in Sarasota and Manatee, depending on material lead times and our project queue. Emergency repair work and short-term-rental reflooring (where the property has a hard booking date) gets prioritized — we'll often slot in an STR turnover ahead of a non-urgent residential install with the residential client's consent."),
    ("Do you do commercial flooring?",
     "Yes — restaurants, retail, offices, and short-term-rental properties are routine. Larger commercial projects (5,000+ sq ft) usually require glue-down LVP or large-format tile and full-detail flatness work; we're happy to walk through commercial scope on a site visit."),
    ("Why is your warranty longer than other flooring companies?",
     "Two years instead of the industry-standard 30-to-90-days because we install the floor ourselves and we're confident in our installs. Most flooring contractors limit workmanship warranty because the install was done by a subcontracted crew the company doesn't fully control. We're in the install, we documented it, and we'll stand behind it for two years in writing."),
]

faq_title = f"FAQ — Flooring Questions Answered | {BUSINESS['short_name']}"
faq_desc = "Flooring FAQ: pricing, warranty, install timelines, weekend availability, financing & more. Honest answers from Sarasota's owner-installed flooring company."
all_faqs = GENERAL_FAQS + [(q,a) for s in SERVICE_ORDER for (q,a) in SERVICES[s]["faqs"]]

faq_schemas = [
    localbiz_schema(page_path="faq"),
    faq_schema(all_faqs[:20]),
    breadcrumb_schema([("Home","/"),("FAQ",None)]),
]

items = "".join(f'<details class="faq-item"><summary>{q}</summary><div class="faq-item-body">{a}</div></details>' for (q,a) in all_faqs)
faq_html = f"""{page_head(faq_title,faq_desc,"faq/")}
<body>
{render_schemas(faq_schemas)}
{header()}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow on-dark">FAQ</span>
    <h1>Flooring questions, <span class="accent">honestly answered.</span></h1>
    <p class="lead">Pricing, warranty, install timelines, product comparisons — answers from {BUSINESS['review_count']}+ verified installs across Sarasota and Manatee.</p>
  </div>
</section>
<nav class="breadcrumbs"><div class="container"><ol><li><a href="/">Home</a></li><li>FAQ</li></ol></div></nav>

<section class="faq-section">
  <div class="container">
    <div class="faq-list">{items}</div>
  </div>
</section>
{cta_banner()}
{footer()}
</body></html>"""
write_html("faq/index.html", faq_html)

# ============================================================================
# /financing/index.html
# ============================================================================
financing_title = f"Flooring Financing in Sarasota | 0% Options Available | {BUSINESS['short_name']}"
financing_desc = "0% financing options through GreenSky &amp; Synchrony for qualifying flooring projects in Sarasota, Bradenton &amp; Lakewood Ranch. Apply online, decisions in minutes."
financing_schemas = [
    localbiz_schema(page_path="financing"),
    breadcrumb_schema([("Home","/"),("Financing",None)]),
]
financing_html = f"""{page_head(financing_title,financing_desc,"financing/")}
<body>
{render_schemas(financing_schemas)}
{header()}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow on-dark">Financing</span>
    <h1>0% financing for <span class="accent">qualifying installs.</span></h1>
    <p class="lead">Spread the cost of a quality flooring install over 12 to 60 months — same install, same warranty, no interest if paid in full inside the promo window.</p>
  </div>
</section>
<nav class="breadcrumbs"><div class="container"><ol><li><a href="/">Home</a></li><li>Financing</li></ol></div></nav>
<section>
  <div class="container">
    <div style="max-width:780px;margin:0 auto;font-size:1.04rem;line-height:1.75;color:var(--ink-soft)">
      <h2 style="margin-bottom:1.1rem">How financing works.</h2>
      <p>We offer two financing programs for qualifying flooring projects across Sarasota and Manatee:</p>

      <div style="background:var(--emerald-soft);border-radius:var(--radius-lg);padding:1.6rem;margin:1.6rem 0">
        <h3 style="color:var(--emerald-dark);margin-bottom:.6rem">GreenSky Financing — 0% APR Promotional Periods</h3>
        <p style="margin:0;font-size:.96rem">Same-day decisions on online application. 0% APR for 12 or 18 months on qualifying balances; conventional 6-month, 24-month, and 60-month plans for larger projects. Soft credit check for pre-qualification, no hit to your credit score. Minimum project size: $2,500.</p>
      </div>

      <div style="background:var(--caramel-soft);border-radius:var(--radius-lg);padding:1.6rem;margin:1.6rem 0">
        <h3 style="color:var(--caramel-dark);margin-bottom:.6rem">Synchrony Home Financing</h3>
        <p style="margin:0;font-size:.96rem">Revolving line of credit specifically for home-improvement spending. 6 or 12-month 0% APR promotional periods; reduced-APR plans up to 84 months for larger remodels. Pre-qualification soft check. Useful when you're financing flooring as part of a larger renovation budget.</p>
      </div>

      <h2 style="margin:2.2rem 0 1rem">When financing makes sense.</h2>
      <p>Financing makes the most sense in one of three situations:</p>
      <ol style="margin:1rem 0 1.4rem 1.5rem">
        <li><strong>You're upgrading flooring as part of a property-resale strategy</strong> — the cost of the install gets baked into the higher sale price, and financing keeps your liquid capital free during the sale.</li>
        <li><strong>You're combining flooring with other renovations</strong> — kitchen, bath, paint, cabinetry — and want one financing instrument across the whole project rather than draining savings on the flooring slice alone.</li>
        <li><strong>The 0% promotional period lines up with bonus or commission income you know is coming</strong> — and paying off the balance inside the promo window costs nothing.</li>
      </ol>

      <h2 style="margin:2.2rem 0 1rem">How to apply.</h2>
      <p>The cleanest path is to request a written estimate first, then we send you the application link sized to your project total. Soft-check decisions land in your inbox in minutes; if approved, the install proceeds on your timeline and you pay the lender, not us.</p>

      <p style="margin-top:1.6rem">
        <a href="{TEL_LINK}" class="btn btn-primary">Call to Discuss Financing</a>
        <a href="/contact/" class="btn btn-secondary" style="margin-left:.6rem">Request Estimate First</a>
      </p>

      <p style="font-size:.82rem;color:var(--gray);margin-top:1.5rem">Financing is provided by third-party lenders (GreenSky, Synchrony). Approval and rates depend on credit and lender criteria. Sarasota Flooring Company is not the lender. Promotional 0% APR rates require full balance repayment inside the stated promotional period; otherwise interest accrues retroactively to the financing date.</p>
    </div>
  </div>
</section>
{cta_banner()}
{footer()}
</body></html>"""
write_html("financing/index.html", financing_html)

# ============================================================================
# /warranty/index.html
# ============================================================================
warranty_title = f"2-Year Workmanship Warranty | {BUSINESS['short_name']}"
warranty_desc = "Sarasota's longest written flooring workmanship warranty — 2 years in writing, signed and dated at walk-through. Covers gapping, cupping, lippage, seam separation."
warranty_schemas = [
    localbiz_schema(page_path="warranty"),
    breadcrumb_schema([("Home","/"),("Warranty",None)]),
]
warranty_html = f"""{page_head(warranty_title,warranty_desc,"warranty/")}
<body>
{render_schemas(warranty_schemas)}
{header()}
<section class="page-hero">
  <div class="container">
    <span class="eyebrow on-dark">Warranty</span>
    <h1>Two years. <span class="accent">In writing.</span></h1>
    <p class="lead">The longest written workmanship warranty in the Sarasota–Manatee flooring market. Signed and dated at walk-through, before the final invoice.</p>
  </div>
</section>
<nav class="breadcrumbs"><div class="container"><ol><li><a href="/">Home</a></li><li>Warranty</li></ol></div></nav>
<section>
  <div class="container">
    <div style="max-width:780px;margin:0 auto;font-size:1.04rem;line-height:1.75;color:var(--ink-soft)">
      <h2 style="margin-bottom:1.1rem">What our 2-year workmanship warranty covers.</h2>
      <p>The warranty covers <strong>anything that goes wrong with our installation work</strong> within 24 months of the walk-through date. Specifically:</p>
      <ul style="margin:1rem 0 1.5rem 1.5rem">
        <li><strong>Hardwood gapping or cupping</strong> related to install (acclimation, moisture testing, or expansion-gap issues)</li>
        <li><strong>Tile lippage</strong> exceeding manufacturer-spec tolerances</li>
        <li><strong>Cracked tile</strong> from substrate-prep failures (skipped crack-isolation membrane, slab dip uncorrected)</li>
        <li><strong>Grout failure</strong> within 24 months on our installs</li>
        <li><strong>LVP and laminate seam separation</strong> on our floating installs</li>
        <li><strong>Squeaks</strong> developing from subfloor-prep issues</li>
        <li><strong>Stair-tread loosening</strong> within 24 months of install</li>
        <li><strong>Transition strip failures</strong> on our work</li>
      </ul>

      <h2 style="margin:2.2rem 0 1rem">What the warranty doesn't cover.</h2>
      <p>The workmanship warranty doesn't cover material defects (those are covered by the manufacturer's warranty, which we organize and hand over at walk-through), abuse damage, water damage from non-flooring sources (failed plumbing, hurricane intrusion, roof leaks), pet damage, or impact damage from dropped items.</p>

      <h2 style="margin:2.2rem 0 1rem">How to file a warranty claim.</h2>
      <p>Call or text the owner directly at <a href="{TEL_LINK}">{BUSINESS['phone_display']}</a>. We'll schedule a diagnostic visit within 7 days — usually within 48 hours for anything affecting daily livability. Diagnostic visits inside the warranty period are free. If the issue is covered, we repair at no charge; if the issue is a material defect, we coordinate the manufacturer claim on your behalf.</p>

      <h2 style="margin:2.2rem 0 1rem">What happens after 2 years.</h2>
      <p>After year 2 the workmanship warranty ends, but we don't disappear. We still handle warranty diagnostics, source matching material from our records (batch and lot numbers stay in your job folder for life), and quote repair work at a reduced "former customer" rate. The relationship doesn't end when the warranty does.</p>

      <p style="margin-top:1.6rem">
        <a href="{TEL_LINK}" class="btn btn-primary">📞 Call Owner Direct</a>
        <a href="/contact/" class="btn btn-secondary" style="margin-left:.6rem">Contact Form</a>
      </p>
    </div>
  </div>
</section>
{cta_banner()}
{footer()}
</body></html>"""
write_html("warranty/index.html", warranty_html)

# ============================================================================
# /thanks/index.html
# ============================================================================
thanks_html = f"""{page_head("Thank You | "+BUSINESS["name"],"Your request has been received. Owner will respond within 24 hours.","thanks/")}
<body>
{render_schemas([localbiz_schema(page_path="thanks"), breadcrumb_schema([("Home","/"),("Thank You",None)])])}
{header()}
<section class="page-hero">
  <div class="container">
    <h1>Thanks — we got it. ✓</h1>
    <p class="lead">Your request is in. The owner will personally respond within 24 hours — typically same business day.</p>
  </div>
</section>
<section>
  <div class="container">
    <div style="max-width:680px;margin:0 auto;text-align:center">
      <h2>While you wait, here's what happens next:</h2>
      <div style="text-align:left;margin:2rem auto;max-width:520px">
        <p style="margin-bottom:1rem"><strong>1.</strong> Owner reviews your project details and pulls relevant material samples for your city and home style.</p>
        <p style="margin-bottom:1rem"><strong>2.</strong> Phone call to schedule the in-home estimate — usually same-day.</p>
        <p style="margin-bottom:1rem"><strong>3.</strong> In-home estimate at your scheduled time, with samples and tape measure.</p>
        <p style="margin-bottom:1rem"><strong>4.</strong> Written, itemized quote in your inbox within 24 hours of the visit.</p>
      </div>
      <p style="margin-top:2rem">Need anything urgent in the meantime?</p>
      <p><a href="{TEL_LINK}" class="btn btn-primary">📞 {BUSINESS['phone_display']}</a></p>
      <p style="margin-top:2rem"><a href="/" style="color:var(--emerald);font-weight:600">← Back to home</a></p>
    </div>
  </div>
</section>
{footer()}
</body></html>"""
write_html("thanks/index.html", thanks_html)

# ============================================================================
# /privacy/index.html and /terms/index.html
# ============================================================================
privacy_html = f"""{page_head("Privacy Policy | "+BUSINESS["name"],"Privacy policy for "+BUSINESS["domain"]+". How we collect, use, and protect your information.","privacy/")}
<body>
{render_schemas([breadcrumb_schema([("Home","/"),("Privacy",None)])])}
{header()}
<section class="page-hero">
  <div class="container">
    <h1>Privacy Policy</h1>
    <p class="lead">Last updated: April 2026</p>
  </div>
</section>
<nav class="breadcrumbs"><div class="container"><ol><li><a href="/">Home</a></li><li>Privacy</li></ol></div></nav>
<section>
  <div class="container">
    <div style="max-width:780px;margin:0 auto;font-size:1rem;line-height:1.75;color:var(--ink-soft)">
      <h2>What we collect.</h2>
      <p>We collect information you voluntarily provide when you fill out a contact form, request an estimate, or contact us by phone or email — typically your name, phone number, email address, project address, and project details. We don't sell, rent, or trade this information.</p>
      <h2>How we use it.</h2>
      <p>We use your information solely to respond to your inquiry, schedule estimates, complete installations, manage warranties, and contact you with relevant project updates. We do not subscribe you to marketing newsletters unless you explicitly opt in.</p>
      <h2>Third-party processors.</h2>
      <p>We use standard third-party services for normal business operations: email (Google Workspace), payment processing (Square, Stripe), financing applications (GreenSky, Synchrony), and analytics (Google Analytics, Cloudflare). Each service has its own privacy policy.</p>
      <h2>Your rights.</h2>
      <p>You can request deletion of your information at any time by emailing <a href="mailto:{BUSINESS['email']}">{BUSINESS['email']}</a>. We honor opt-out requests within 7 business days unless we're legally required to retain records (warranty period, tax records).</p>
      <h2>Cookies &amp; analytics.</h2>
      <p>This site uses minimal cookies for site functionality and Google Analytics for traffic measurement. We don't use targeted advertising cookies. You can block cookies through your browser settings.</p>
      <h2>Contact.</h2>
      <p>Questions about this policy? Email <a href="mailto:{BUSINESS['email']}">{BUSINESS['email']}</a> or call <a href="{TEL_LINK}">{BUSINESS['phone_display']}</a>.</p>
    </div>
  </div>
</section>
{footer()}
</body></html>"""
write_html("privacy/index.html", privacy_html)

terms_html = f"""{page_head("Terms of Service | "+BUSINESS["name"],"Terms of service for "+BUSINESS["domain"]+". Project terms, warranty conditions, payment terms.","terms/")}
<body>
{render_schemas([breadcrumb_schema([("Home","/"),("Terms",None)])])}
{header()}
<section class="page-hero">
  <div class="container">
    <h1>Terms of Service</h1>
    <p class="lead">Last updated: April 2026</p>
  </div>
</section>
<nav class="breadcrumbs"><div class="container"><ol><li><a href="/">Home</a></li><li>Terms</li></ol></div></nav>
<section>
  <div class="container">
    <div style="max-width:780px;margin:0 auto;font-size:1rem;line-height:1.75;color:var(--ink-soft)">
      <h2>Estimates.</h2>
      <p>Written estimates issued by Sarasota Flooring Company are valid for 30 days from the date issued. Material pricing can fluctuate due to manufacturer cost changes; we'll communicate any material-cost change before applying it to the project.</p>
      <h2>Payment terms.</h2>
      <p>Projects under $2,500: payment due in full at walk-through. Projects $2,500–$15,000: 30% deposit at material order, balance due at walk-through. Projects over $15,000: 30% deposit, 40% at midpoint, 30% at walk-through. Accepted payment methods: credit card (Visa/MC/AmEx/Discover), ACH transfer, Zelle, check.</p>
      <h2>Workmanship warranty.</h2>
      <p>Two-year written workmanship warranty applies to every installation. Full terms outlined on the <a href="/warranty/">warranty page</a>.</p>
      <h2>Material warranties.</h2>
      <p>Manufacturer warranties on materials are passed through to the customer and organized in the job folder at walk-through. Warranty claim filing for material defects is coordinated by us at no charge during the workmanship warranty period.</p>
      <h2>Cancellation.</h2>
      <p>Project cancellation prior to material order: refund of deposit minus a $250 administrative fee. After material order: deposit applied against material restocking fees (typically 25%); the remainder refunded. After install begins: pro-rated based on completed work.</p>
      <h2>Limitation of liability.</h2>
      <p>Sarasota Flooring Company's liability on any project is limited to the contract value of that project. We carry general liability insurance and workers' compensation; certificates of insurance are available on request.</p>
      <h2>Dispute resolution.</h2>
      <p>Disputes are first addressed through direct conversation between the customer and the owner. If unresolved, both parties agree to good-faith mediation through a mutually selected Sarasota-area mediator before any litigation.</p>
    </div>
  </div>
</section>
{footer()}
</body></html>"""
write_html("terms/index.html", terms_html)

# ============================================================================
# /404.html
# ============================================================================
notfound_html = f"""{page_head("Page Not Found | "+BUSINESS["name"],"This page doesn't exist. Find your way back to the flooring services you need.","404")}
<body>
{header()}
<section class="page-hero">
  <div class="container">
    <h1>This page doesn't exist.</h1>
    <p class="lead">Don't worry — we'll get you back on the right floor.</p>
  </div>
</section>
<section>
  <div class="container">
    <div style="max-width:680px;margin:0 auto;text-align:center">
      <h2 style="margin-bottom:1.3rem">Popular pages:</h2>
      <p><a href="/" class="btn btn-primary">🏠 Home</a> <a href="/contact/" class="btn btn-secondary" style="margin-left:.6rem">📞 Free Estimate</a></p>
      <h3 style="margin:2.4rem 0 1rem">Or explore by service:</h3>
      <p>{" · ".join(f'<a href="/{s}/" style="color:var(--emerald);font-weight:600">{SERVICES[s]["name"]}</a>' for s in SERVICE_ORDER)}</p>
      <h3 style="margin:2.4rem 0 1rem">By city:</h3>
      <p>{" · ".join(f'<a href="/{c}/" style="color:var(--emerald);font-weight:600">{CITIES[c]["name"]}</a>' for c in CITY_ORDER)}</p>
    </div>
  </div>
</section>
{footer()}
</body></html>"""
with open(f"{OUT}/404.html","w",encoding="utf-8") as f: f.write(notfound_html)
print("✓ Built /404.html")

print("\nAll support pages built.")
