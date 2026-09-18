# Sarasota Flooring Company — sarasotaflooringcompany.com

Static site for a flooring installation contractor covering every community within 40 miles of Sarasota, FL.
Cloudflare Pages serves **`dist/`** (build output directory = `dist`, no build command — the generated site is committed). A push to `main` deploys.

## Layout

```
src/
  build.py            one command builds the whole site into dist/
  theme.py            design system (logo palette), header/footer, components, JSON-LD
  tools.py            cost calculator, Florida flooring finder, condo approval checklist
  data_core.py        business identity, services, price tables, Web3Forms key
  content/            everything that is prose, one JSON file per page
    home.json  areas.json  city_list.json (21 cities: distance, tier, core flag)
    pages/  services_extra/  landings/  cost_guides/  cities/  city_service/  posts/
    merged_slugs.json  legacy_redirects.json
  qa_content.py       content QA: limits, banned phrases, forbidden claims, duplicate sentences
  kw_report.py        keyword coverage of the built site -> docs/keyword-coverage.md
  audit_site.py       technical + duplication audit (also against sibling sites)
static/               copied verbatim into dist/ (images, _headers, _redirects, favicon, IndexNow key)
dist/                 the published site (generated — do not edit by hand)
docs/                 audit, owner inputs, research, reports
```

## Build

```bash
python src/qa_content.py     # must print "issues 0"
python src/build.py          # writes dist/, validates every internal link (docs/link-report.json)
python src/kw_report.py      # optional: keyword coverage
```
Requires Python 3.10+ and Pillow. Works on Windows, macOS and Linux (no hard-coded paths).

## Editing

- Prices: `SERVICES[...]["pricing_rows"]` in `src/data_core.py` (the calculator in `src/tools.py` mirrors them; worked examples inside cost guides are prose and must be updated by hand).
- A new question post: drop `src/content/posts/<slug>.json` (schema in `docs/` research notes) and rebuild — blog index, FAQ hub, feed, sitemap and llms files update themselves.
- A new city: add it to `src/content/city_list.json` and write `src/content/cities/<slug>.json`.
- Real reviews / Google Business Profile / social profiles: see `docs/OWNER-INPUTS.md`.

Leads: every form posts to Web3Forms and redirects to `/thanks/`. `hello@` and catch-all mail forward through Cloudflare Email Routing.

Read `docs/AUDITORIA-SEO-GEO-AEO.md` for what was audited and changed on 2026-09-18, and `docs/OWNER-INPUTS.md` for what still depends on the owner.
