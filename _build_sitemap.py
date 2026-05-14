#!/usr/bin/env python3
"""
Build /sitemap.xml and /robots.txt
"""
import os
from datetime import date
from _data import BUSINESS, CITIES, CITY_ORDER, SERVICES, SERVICE_ORDER, GENERAL_BLOG_POSTS
from _gen import SITE

OUT = "/home/claude/sarasota-flooring"
TODAY = date.today().isoformat()

urls = []

def add(path, priority="0.7", freq="weekly"):
    url = f"{SITE}/{path}" if path else f"{SITE}/"
    urls.append((url, priority, freq))

# Homepage
add("", "1.0", "weekly")

# Core pages
add("about/", "0.8", "monthly")
add("contact/", "0.85", "monthly")
add("faq/", "0.7", "monthly")
add("financing/", "0.6", "monthly")
add("warranty/", "0.6", "monthly")
add("privacy/", "0.3", "yearly")
add("terms/", "0.3", "yearly")

# Service index pages
for s in SERVICE_ORDER:
    add(f"{s}/", "0.9", "weekly")

# City index pages
for c in CITY_ORDER:
    add(f"{c}/", "0.85", "weekly")

# Service × city pages
for s in SERVICE_ORDER:
    for c in CITY_ORDER:
        add(f"{s}/{c}/", "0.8", "monthly")

# Blog index
add("blog/", "0.8", "weekly")

# Blog posts
for p in GENERAL_BLOG_POSTS:
    add(f"blog/{p['slug']}/", "0.7", "monthly")
for s in SERVICE_ORDER:
    for c in CITY_ORDER:
        add(f"blog/{s}-cost-{c}/", "0.65", "monthly")

# Write sitemap.xml
url_entries = "\n".join(
    f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{f}</changefreq>\n    <priority>{p}</priority>\n  </url>"
    for (u,p,f) in urls
)
sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{url_entries}
</urlset>
"""
with open(f"{OUT}/sitemap.xml","w",encoding="utf-8") as f: f.write(sitemap)
print(f"✓ Built /sitemap.xml ({len(urls)} URLs)")

# Write robots.txt
robots = f"""User-agent: *
Allow: /
Disallow: /thanks/

# Sitemap
Sitemap: {SITE}/sitemap.xml

# AI Crawlers — explicitly allowed (for AI citation)
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: CCBot
Allow: /

# Bing IndexNow auto-discovery
# Key: see /indexnow-key.txt
"""
with open(f"{OUT}/robots.txt","w",encoding="utf-8") as f: f.write(robots)
print("✓ Built /robots.txt")
