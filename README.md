# Sarasota Flooring Company — Static Site

Production-ready static HTML site for **sarasotaflooringcompany.com**. 

Built to rank: Google · Bing · Apple Maps · ChatGPT · Claude · Gemini · Perplexity citations.

## Architecture

- **Static HTML** — every page pre-generated, zero JavaScript framework
- **Python build system** — single source of truth (`_data.py`) → all 120+ pages
- **Cloudflare Pages** deploy via GitHub auto-build
- **Inline CSS + minimal vanilla JS** — sub-second First Contentful Paint
- **Full schema markup** — Organization, LocalBusiness, FAQPage, BreadcrumbList, Article

## File structure

```
sarasota-flooring/
├── _data.py              # SINGLE SOURCE OF TRUTH — business, cities, services, reviews
├── _gen.py               # Shared design system, components, schema generators
├── _build_home.py        # → /index.html
├── _build_pages.py       # → /about/, /contact/, /faq/, /financing/, /warranty/, /thanks/, /privacy/, /terms/, /404.html
├── _build_services.py    # → /[service]/index.html (6 pages)
├── _build_cities.py      # → /[city]/index.html (8) + /[service]/[city]/index.html (48)
├── _build_blog.py        # → /blog/index.html + 51 posts (3 editorial + 48 cost-by-city)
├── _build_sitemap.py     # → /sitemap.xml, /robots.txt
├── _headers              # Cloudflare security & cache headers
├── _redirects            # Cloudflare 301 redirects
├── favicon.svg
├── index.html            # generated
├── 404.html              # generated
├── robots.txt            # generated
├── sitemap.xml           # generated
├── about/ contact/ faq/ financing/ warranty/ thanks/ privacy/ terms/
├── hardwood-flooring/ vinyl-plank-flooring/ tile-installation/ laminate-flooring/ stair-treads/ floor-repair/
├── sarasota/ bradenton/ lakewood-ranch/ venice/ parrish/ palmetto/ siesta-key/ longboat-key/
├── blog/
└── images/               # logo.png, hero-og.jpg, favicon.png, etc.
```

## How to rebuild

After any edit to `_data.py` (price change, new review, new city), regenerate:

```bash
python3 _build_home.py
python3 _build_pages.py
python3 _build_services.py
python3 _build_cities.py
python3 _build_blog.py
python3 _build_sitemap.py
```

Or all at once:

```bash
for f in _build_*.py; do python3 "$f"; done
```

## What to update in `_data.py` after launch

1. **Real reviews** as you collect them: replace the placeholder entries in the `REVIEWS` list at line ~600.
2. **Review count and rating** in `BUSINESS` dict: `"rating"` and `"review_count"`.
3. **Google Business Profile URL**: `"google_profile"` once GMB is live.
4. **Social profile URLs** (Yelp, Thumbtack, Angi, BBB, Houzz, Facebook, Instagram) as you register on each.
5. **License number**: `"license"` once Manatee County LBTR is issued.

## Deploy to Cloudflare Pages

1. Push this repo to GitHub.
2. Cloudflare Pages → Create project → Connect to GitHub → Select repo.
3. Build settings:
   - **Build command**: leave empty (pre-generated HTML; nothing to compile)
   - **Build output directory**: `/`
   - **Root directory**: `/`
4. Connect custom domain: `sarasotaflooringcompany.com` and `www.sarasotaflooringcompany.com`.

## SEO submission checklist

- [ ] Google Search Console — verify domain, submit `sitemap.xml`
- [ ] Bing Webmaster Tools — verify, submit sitemap, set up IndexNow
- [ ] Apple Business Connect — for Siri/Safari citation
- [ ] Google Business Profile — verify, add 8+ products, weekly posts
- [ ] Yelp Business — claim, add all services + service areas
- [ ] Thumbtack — claim, set service areas to all 8 cities
- [ ] Angi — claim, complete profile
- [ ] BBB — register, verify
- [ ] Houzz — pro account, upload all install photos
- [ ] HomeAdvisor — register
- [ ] Manta, Yellow Pages, MerchantCircle — bulk citation submission

## Key SEO assets baked in

- **EMD** (Exact Match Domain): `sarasotaflooringcompany.com`
- **Aggregate Rating schema** on homepage, all service pages, all city pages
- **LocalBusiness schema** on every page with `areaServed` arrays
- **FAQ schema** on services, blog posts, FAQ page (50+ Q&A combined)
- **Article schema** on every blog post
- **BreadcrumbList schema** on every page
- **Cross-link network** to partner sites (Braza Cleaning, Ocoee Concrete, The Villages Remodeling) — boosts authority signals
- **Unique 63-point checklist** with named identifier on every install page
- **Unique stat** (`100% owner-supervised`) repeated across the site for AI citation
- **Real neighborhood data** for every city (20+ per city)
- **Transparent pricing** on every service and service×city page

## Total pages generated

| Type | Count |
|------|-------|
| Homepage | 1 |
| Core pages (about, contact, FAQ, financing, warranty, thanks, privacy, terms, 404) | 9 |
| Service index | 6 |
| City index | 8 |
| Service × City | 48 |
| Blog index | 1 |
| Editorial blog posts | 3 |
| Cost-by-city blog posts | 48 |
| **Total HTML pages** | **124** |

Plus `sitemap.xml`, `robots.txt`, `_headers`, `_redirects`, `favicon.svg`.

## Contact

Built for **Luciano** — Sarasota Flooring Company LLC.  
Phone: **(941) 241-3724** · ZIP **34212** (Lakewood Ranch, Manatee County, FL).
