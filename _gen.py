#!/usr/bin/env python3
"""
Sarasota Flooring Company — Shared Page Generator
Design system: deep emerald + caramel wood + cream + ink charcoal.
Imported by every _build_*.py script.
"""
import json
from _data import (
    BUSINESS, CITIES, CITY_ORDER, SERVICES, SERVICE_ORDER,
    CHECKLIST, REVIEWS, WA_LINK, TEL_LINK, SMS_LINK,
    WHY_US_POINTS, PROCESS_STEPS, HERO_TRUST_BADGES,
    GENERAL_BLOG_POSTS,
)

DOMAIN = BUSINESS["domain"]
SITE = f"https://{DOMAIN}"

# ============================================================================
# CSS — Deep emerald + caramel wood + cream design system
# ============================================================================
CSS = r"""
:root{
  /* Brand palette — emerald, caramel wood, cream, ink */
  --emerald:#1F5F3F;
  --emerald-dark:#163E29;
  --emerald-soft:#E8F2EC;
  --caramel:#C8893D;
  --caramel-dark:#A36C25;
  --caramel-soft:#FAF1E2;
  --cream:#FBF8F2;
  --cream-deep:#F4EFE3;
  --ink:#1B1B1B;
  --ink-soft:#2F2F2F;
  --gray:#5E6362;
  --gray-light:#8A8F8D;
  --gray-border:#E1DED5;
  --white:#FFFFFF;
  --whatsapp:#25D366;
  --warning:#C2410C;
  --shadow-sm:0 1px 3px rgba(22,62,41,.08);
  --shadow:0 4px 14px rgba(22,62,41,.12);
  --shadow-lg:0 14px 38px rgba(22,62,41,.16);
  --radius:10px;
  --radius-lg:18px;
  --font-head:'Outfit','Inter',-apple-system,BlinkMacSystemFont,sans-serif;
  --font-body:'Lato','Helvetica Neue',Arial,sans-serif;
  --font-serif:'Georgia',serif;
  --container:1200px;
  --container-wide:1380px;
  --transition:.22s cubic-bezier(.4,0,.2,1);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;scroll-padding-top:88px}
body{font-family:var(--font-body);font-size:16px;line-height:1.65;color:var(--ink);background:var(--cream);overflow-x:hidden;-webkit-font-smoothing:antialiased}
img{max-width:100%;height:auto;display:block}
a{color:var(--emerald);text-decoration:none;transition:color var(--transition)}
a:hover{color:var(--caramel-dark)}
h1,h2,h3,h4,h5{font-family:var(--font-head);font-weight:700;line-height:1.18;letter-spacing:-.02em;color:var(--ink)}
h1{font-size:clamp(2.1rem,5vw,3.4rem)}
h2{font-size:clamp(1.65rem,3.5vw,2.45rem)}
h3{font-size:clamp(1.18rem,2vw,1.45rem)}
h4{font-size:1.1rem;font-weight:600}
p{margin:0 0 1rem}
ul,ol{margin:0 0 1rem 1.25rem}
li{margin-bottom:.4rem}
strong{font-weight:700;color:var(--ink)}
em{font-style:italic}
.container{max-width:var(--container);margin:0 auto;padding:0 22px}
.container-wide{max-width:var(--container-wide);margin:0 auto;padding:0 22px}
.eyebrow{display:inline-block;font-family:var(--font-head);font-size:.78rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--emerald);background:var(--emerald-soft);padding:6px 14px;border-radius:50px;margin-bottom:.85rem}
.eyebrow.on-dark{background:rgba(255,255,255,.16);color:#fff}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:14px 26px;font-family:var(--font-head);font-weight:600;font-size:.98rem;border-radius:50px;text-decoration:none;cursor:pointer;border:none;transition:all var(--transition);white-space:nowrap}
.btn-primary{background:var(--caramel);color:#fff;box-shadow:0 4px 14px rgba(200,137,61,.32)}
.btn-primary:hover{background:var(--caramel-dark);color:#fff;transform:translateY(-2px);box-shadow:0 8px 22px rgba(200,137,61,.4)}
.btn-secondary{background:#fff;color:var(--emerald);border:2px solid var(--emerald)}
.btn-secondary:hover{background:var(--emerald);color:#fff}
.btn-emerald{background:var(--emerald);color:#fff;box-shadow:0 4px 14px rgba(22,62,41,.28)}
.btn-emerald:hover{background:var(--emerald-dark);color:#fff;transform:translateY(-2px)}
.btn-ghost{background:transparent;color:#fff;border:2px solid rgba(255,255,255,.55)}
.btn-ghost:hover{background:#fff;color:var(--emerald);border-color:#fff}
.btn-wa{background:var(--whatsapp);color:#fff;box-shadow:0 4px 14px rgba(37,211,102,.32)}
.btn-wa:hover{background:#1eb858;color:#fff;transform:translateY(-2px)}

/* HEADER — emerald nav bar */
.site-header{position:sticky;top:0;z-index:100;background:var(--emerald-dark);box-shadow:0 2px 16px rgba(22,62,41,.28)}
.nav-bar{display:flex;align-items:center;justify-content:space-between;padding:0 22px;max-width:var(--container);margin:0 auto;gap:1rem;height:68px}
.brand{display:flex;align-items:center;gap:11px;text-decoration:none;flex-shrink:0;min-width:240px}
.brand img{height:40px;width:auto}
.brand-text{display:flex;flex-direction:column;line-height:1}
.brand-name{font-family:var(--font-head);font-weight:800;font-size:1.1rem;color:#fff;letter-spacing:-.02em;white-space:nowrap}
.brand-tag{font-size:.65rem;letter-spacing:.18em;color:#F8DDA8;text-transform:uppercase;margin-top:3px;white-space:nowrap;font-weight:600;opacity:.85}
.nav-menu{display:flex;align-items:center;gap:.2rem;list-style:none;flex-wrap:nowrap;margin:0;padding:0}
.nav-menu li{position:relative;margin:0}
.nav-menu>li>a{font-family:var(--font-head);font-weight:500;color:rgba(255,255,255,.9);font-size:.91rem;padding:8px 12px;white-space:nowrap;border-radius:6px}
.nav-menu>li>a:hover{color:#fff;background:rgba(255,255,255,.12)}
.dropdown{position:absolute;top:calc(100% + 4px);left:0;background:#fff;min-width:240px;border-radius:var(--radius);box-shadow:0 16px 40px rgba(22,62,41,.22);padding:.5rem 0;opacity:0;visibility:hidden;transition:all var(--transition);z-index:99;border:1px solid var(--gray-border);list-style:none;margin:0}
.nav-menu li:hover .dropdown{opacity:1;visibility:visible}
.dropdown li{margin:0}
.dropdown a{display:block;padding:10px 20px;font-size:.92rem;font-weight:400;color:var(--ink);white-space:nowrap}
.dropdown a:hover{background:var(--emerald-soft);color:var(--emerald)}
.nav-cta{display:flex;align-items:center;gap:.75rem;flex-shrink:0}
.nav-phone{display:flex;align-items:center;gap:6px;color:#F8DDA8;font-family:var(--font-head);font-weight:700;font-size:.95rem;white-space:nowrap}
.nav-phone svg{width:16px;height:16px;flex-shrink:0}
.nav-phone:hover{color:#fff}
.menu-toggle{display:none;background:none;border:none;cursor:pointer;padding:8px;color:#fff}
.menu-toggle svg{width:26px;height:26px}

/* HERO */
.hero{position:relative;min-height:88vh;min-height:680px;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff;overflow:hidden;padding:100px 22px 90px}
.hero-bg{position:absolute;inset:0;z-index:0}
.hero-bg-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center}
.hero-overlay{position:absolute;inset:0;z-index:1;background:linear-gradient(135deg,rgba(22,62,41,.86) 0%,rgba(31,95,63,.80) 50%,rgba(22,62,41,.74) 100%)}
.hero-overlay::after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 50% 65%,transparent 0%,rgba(22,62,41,.35) 100%)}
.hero-content{position:relative;z-index:2;max-width:920px;margin:0 auto;animation:fadeUp .8s ease-out}
.hero h1{color:#fff;margin-bottom:1.1rem}
.hero h1 .accent{background:linear-gradient(90deg,#F8DDA8,var(--caramel));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero p.lead{font-size:clamp(1.05rem,2vw,1.22rem);color:rgba(255,255,255,.94);max-width:760px;margin:0 auto 1.85rem;line-height:1.55}
.hero-ctas{display:flex;flex-wrap:wrap;gap:.85rem;justify-content:center;margin-bottom:2rem}
.hero-trust{display:flex;justify-content:center;flex-wrap:wrap;gap:.7rem 1.7rem;margin-top:1.5rem;font-size:.9rem;color:rgba(255,255,255,.95)}
.hero-trust span{display:inline-flex;align-items:center;gap:7px;font-weight:600;font-family:var(--font-head)}
.hero-trust span::before{content:"✓";color:#F8DDA8;font-weight:700;font-size:1.05rem}

/* PAGE HEAD (for non-hero pages — service, city, blog, about) */
.page-hero{padding:3.5rem 0 2.6rem;background:linear-gradient(135deg,var(--emerald-dark) 0%,var(--emerald) 70%,#2D7A55 100%);color:#fff;text-align:center}
.page-hero h1{color:#fff;margin-bottom:.85rem}
.page-hero h1 .accent{background:linear-gradient(90deg,#F8DDA8,var(--caramel));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.page-hero p.lead{font-size:1.08rem;color:rgba(255,255,255,.92);max-width:760px;margin:0 auto 1.5rem}
.page-hero-trust{display:flex;justify-content:center;flex-wrap:wrap;gap:.7rem 1.6rem;margin-top:1.4rem;font-size:.88rem;color:rgba(255,255,255,.95)}
.page-hero-trust span{display:inline-flex;align-items:center;gap:6px;font-weight:600;font-family:var(--font-head)}
.page-hero-trust span::before{content:"✓";color:#F8DDA8;font-weight:700}

/* BREADCRUMBS */
.breadcrumbs{background:#fff;padding:14px 0;font-size:.85rem;border-bottom:1px solid var(--gray-border)}
.breadcrumbs ol{list-style:none;display:flex;flex-wrap:wrap;align-items:center;gap:8px;color:var(--gray);margin:0;padding:0}
.breadcrumbs li{display:flex;align-items:center;gap:8px;margin:0}
.breadcrumbs li::after{content:"›";color:var(--gray-light);margin-left:8px}
.breadcrumbs li:last-child::after{display:none}
.breadcrumbs a{color:var(--emerald);font-weight:500}
.breadcrumbs li:last-child{color:var(--ink);font-weight:600}

/* SECTIONS */
section{padding:4.2rem 0}
.section-head{text-align:center;max-width:760px;margin:0 auto 2.8rem}
.section-head p{color:var(--gray);font-size:1.05rem;margin-top:.6rem}

/* SOCIAL PROOF STRIP */
.proof-strip{background:var(--ink);color:#fff;padding:1.8rem 0}
.proof-grid{max-width:var(--container);margin:0 auto;padding:0 22px;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1.2rem 2rem;text-align:center}
.proof-item{display:flex;flex-direction:column;align-items:center;gap:4px}
.proof-num{font-family:var(--font-head);font-size:1.65rem;font-weight:800;color:#F8DDA8;letter-spacing:-.02em;line-height:1}
.proof-label{font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.75);font-weight:600}

/* INTRO */
.intro{padding:3.5rem 0;background:var(--cream)}
.intro-content{max-width:790px;margin:0 auto;font-size:1.05rem;line-height:1.75;color:var(--ink-soft)}
.intro-content p{margin-bottom:1.25rem}

/* SERVICES GRID */
.services-section{background:var(--cream-deep)}
.services-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem;margin-top:2rem}
.service-card{background:#fff;border:1px solid var(--gray-border);border-radius:var(--radius-lg);padding:1.6rem;transition:all var(--transition);text-decoration:none;color:var(--ink);display:flex;flex-direction:column;gap:.85rem;box-shadow:var(--shadow-sm)}
.service-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg);border-color:var(--emerald);color:var(--ink)}
.service-card-num{font-family:var(--font-head);font-size:.85rem;font-weight:800;color:var(--caramel);letter-spacing:.08em}
.service-card h3{margin:0;color:var(--ink);font-size:1.3rem}
.service-card p{color:var(--gray);font-size:.95rem;flex-grow:1;margin:0}
.service-card-arrow{color:var(--emerald);font-weight:700;font-family:var(--font-head);font-size:.92rem;letter-spacing:.02em}

/* WHY US */
.why-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:1.4rem;margin-top:2rem}
.why-card{background:#fff;border:1px solid var(--gray-border);border-radius:var(--radius-lg);padding:1.7rem;display:flex;flex-direction:column;gap:.65rem;box-shadow:var(--shadow-sm)}
.why-icon{font-size:2rem;line-height:1}
.why-card h3{font-size:1.15rem;color:var(--emerald-dark);margin:0}
.why-card p{color:var(--gray);font-size:.95rem;margin:0;line-height:1.6}

/* PROCESS */
.process-section{background:var(--emerald);color:#fff;padding:4.5rem 0}
.process-section h2{color:#fff;text-align:center}
.process-section .eyebrow{background:rgba(255,255,255,.16);color:#fff}
.process-section .section-head p{color:rgba(255,255,255,.9)}
.process-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.6rem;margin-top:2.2rem}
.process-step{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);border-radius:var(--radius-lg);padding:1.7rem;backdrop-filter:blur(8px)}
.process-num{font-family:var(--font-head);font-size:.85rem;font-weight:800;color:#F8DDA8;letter-spacing:.08em;margin-bottom:.5rem}
.process-step h3{color:#fff;font-size:1.18rem;margin-bottom:.55rem}
.process-step p{color:rgba(255,255,255,.85);font-size:.92rem;line-height:1.55;margin:0}

/* REVIEWS */
.reviews-section{background:var(--cream)}
.reviews-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:1.4rem;margin-top:2rem}
.review-card{background:#fff;border:1px solid var(--gray-border);border-radius:var(--radius-lg);padding:1.65rem;box-shadow:var(--shadow-sm);display:flex;flex-direction:column;gap:.85rem}
.review-stars{color:var(--caramel);font-size:1.1rem;letter-spacing:.05em}
.review-text{color:var(--ink-soft);font-size:.95rem;line-height:1.6;font-style:italic;flex-grow:1}
.review-meta{border-top:1px solid var(--gray-border);padding-top:.85rem;font-size:.82rem;color:var(--gray)}
.review-name{font-weight:700;color:var(--ink);font-family:var(--font-head)}

/* SERVICE-AREAS */
.areas-section{background:#fff;padding:4rem 0}
.areas-pills{display:flex;flex-wrap:wrap;gap:.7rem;justify-content:center;margin-top:2rem}
.area-pill{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;background:var(--emerald-soft);color:var(--emerald-dark);border-radius:50px;font-family:var(--font-head);font-weight:600;font-size:.92rem;text-decoration:none;transition:all var(--transition);border:1px solid transparent}
.area-pill:hover{background:var(--emerald);color:#fff;transform:translateY(-2px)}

/* CTA BANNER */
.cta-banner{background:linear-gradient(135deg,var(--emerald-dark),var(--emerald) 50%,var(--caramel-dark) 100%);color:#fff;text-align:center;padding:4.5rem 0}
.cta-banner h2{color:#fff;margin-bottom:.85rem}
.cta-banner p{color:rgba(255,255,255,.92);font-size:1.05rem;max-width:660px;margin:0 auto 1.6rem}
.cta-phone-large{display:inline-block;font-family:var(--font-head);font-size:2rem;font-weight:800;color:#F8DDA8;text-decoration:none;letter-spacing:-.02em;margin:.85rem 0 1.2rem}
.cta-phone-large:hover{color:#fff}
.cta-buttons{display:flex;flex-wrap:wrap;gap:.85rem;justify-content:center}

/* CHECKLIST */
.checklist-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:1.2rem;margin-top:2rem}
.checklist-card{background:#fff;border:1px solid var(--gray-border);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm)}
.checklist-head{background:var(--emerald);color:#fff;padding:.95rem 1.2rem;display:flex;align-items:center;gap:.85rem}
.checklist-icon{font-size:1.55rem;line-height:1}
.checklist-head-text p{margin:0;color:#fff}
.checklist-head-text p:first-child{font-family:var(--font-head);font-weight:700;font-size:.98rem}
.checklist-head-text p:last-child{font-size:.78rem;color:rgba(255,255,255,.78);font-family:var(--font-head)}
.checklist-list{margin:0;padding:.9rem 1.1rem .9rem 2rem;list-style:decimal}
.checklist-list li{font-size:.88rem;color:var(--ink-soft);line-height:1.5;margin-bottom:.4rem}

/* PRICING */
.pricing-block{background:#fff;border:1.5px solid var(--gray-border);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm);margin:1.6rem 0}
.pricing-table{width:100%;border-collapse:collapse;font-size:.94rem}
.pricing-table thead{background:var(--emerald)}
.pricing-table th{padding:14px 18px;text-align:left;color:#fff;font-family:var(--font-head);font-weight:600;font-size:.86rem;letter-spacing:.02em}
.pricing-table td{padding:12px 18px;border-bottom:1px solid var(--gray-border);vertical-align:top}
.pricing-table td:first-child{font-weight:600;color:var(--ink)}
.pricing-table td:nth-child(2){font-weight:700;color:var(--caramel-dark);white-space:nowrap}
.pricing-table td:last-child{color:var(--gray);font-size:.88rem}
.pricing-table tr:nth-child(even){background:var(--cream)}
.pricing-table tr:last-child td{border-bottom:none}

/* STAT BADGE */
.stat-badge{background:linear-gradient(135deg,var(--caramel-soft),#FDF6E5);border:1.5px solid var(--caramel);border-radius:var(--radius);padding:1rem 1.25rem;margin:1.5rem 0;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.stat-badge .stat-icon{font-size:2rem}
.stat-badge p{margin:0;font-size:14px;font-weight:600;color:var(--caramel-dark)}
.stat-badge p+p{margin-top:2px;font-size:12px;color:var(--gray);font-weight:500}

/* FAQ */
.faq-section{background:var(--cream-deep);padding:4rem 0}
.faq-list{max-width:820px;margin:0 auto}
.faq-item{background:#fff;border:1px solid var(--gray-border);border-radius:var(--radius);margin-bottom:.85rem;overflow:hidden;box-shadow:var(--shadow-sm)}
.faq-item summary{padding:1.15rem 1.35rem;font-family:var(--font-head);font-weight:600;color:var(--ink);font-size:1rem;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:1rem}
.faq-item summary::after{content:"+";color:var(--emerald);font-size:1.5rem;font-weight:400;transition:transform var(--transition);line-height:1;flex-shrink:0}
.faq-item[open] summary::after{transform:rotate(45deg)}
.faq-item summary::-webkit-details-marker{display:none}
.faq-item-body{padding:0 1.35rem 1.25rem;color:var(--ink-soft);font-size:.95rem;line-height:1.65}

/* SCOPE / NEIGHBORHOODS LISTS */
.scope-list{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:.45rem .85rem;margin:1.4rem 0;padding:0;list-style:none}
.scope-list li{position:relative;padding-left:1.6rem;color:var(--ink-soft);font-size:.94rem;line-height:1.5}
.scope-list li::before{content:"✓";position:absolute;left:0;top:0;color:var(--caramel);font-weight:700}
.neighborhood-grid{display:flex;flex-wrap:wrap;gap:.55rem;margin:1.4rem 0}
.neighborhood-pill{display:inline-block;padding:7px 14px;background:#fff;border:1px solid var(--gray-border);border-radius:50px;font-size:.85rem;color:var(--ink-soft);font-weight:500}

/* WHATSAPP FLOAT */
.wa-float{position:fixed;bottom:22px;right:22px;z-index:9999;display:flex;align-items:center;gap:8px;background:var(--whatsapp);color:#fff;padding:13px 20px;border-radius:50px;text-decoration:none;font-family:var(--font-head);font-size:14px;font-weight:600;box-shadow:0 6px 18px rgba(37,211,102,.42);transition:all var(--transition)}
.wa-float:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(37,211,102,.5);color:#fff}
.wa-float svg{width:18px;height:18px}

/* WA INLINE BANNER */
.wa-banner{background:linear-gradient(135deg,var(--whatsapp),#128C7E);border-radius:var(--radius-lg);padding:1.4rem 1.6rem;margin:2rem 0;display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;color:#fff}
.wa-banner p{margin:0;color:#fff}
.wa-banner .wa-banner-head{font-family:var(--font-head);font-size:1.05rem;font-weight:700}
.wa-banner .wa-banner-sub{font-size:.85rem;color:rgba(255,255,255,.9);margin-top:2px}
.wa-banner a.btn{background:#fff;color:#128C7E;padding:11px 22px}
.wa-banner a.btn:hover{background:#FBF8F2;color:#0e6b5f}

/* INTERNAL LINK BOX */
.internal-links{background:#fff;border:1px solid var(--gray-border);border-radius:var(--radius-lg);padding:1.5rem;margin:2rem 0}
.internal-links h3{color:var(--emerald-dark);font-size:1.1rem;margin-bottom:.85rem}
.internal-links ul{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.5rem}
.internal-links li{margin:0}
.internal-links a{display:inline-flex;align-items:center;gap:6px;color:var(--emerald);font-weight:500;font-size:.93rem}
.internal-links a::before{content:"→";color:var(--caramel)}

/* FOOTER */
.site-footer{background:var(--ink);color:rgba(255,255,255,.85);padding:4rem 0 1.5rem}
.footer-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:2.4rem;max-width:var(--container);margin:0 auto;padding:0 22px}
.footer-col h4{color:#fff;font-family:var(--font-head);font-size:1.05rem;font-weight:700;margin-bottom:1rem}
.footer-col p{font-size:.92rem;line-height:1.65;color:rgba(255,255,255,.7);margin-bottom:.65rem}
.footer-col ul{list-style:none;margin:0;padding:0}
.footer-col li{margin-bottom:.5rem}
.footer-col a{color:rgba(255,255,255,.78);font-size:.92rem}
.footer-col a:hover{color:#F8DDA8}
.footer-brand-block{font-family:var(--font-head)}
.footer-brand-name{font-size:1.2rem;font-weight:800;color:#fff}
.footer-brand-tag{font-size:.75rem;color:var(--caramel);text-transform:uppercase;letter-spacing:.14em;margin:.3rem 0 1rem;font-weight:600}
.footer-contact-line{display:flex;align-items:flex-start;gap:8px;margin-bottom:.55rem;font-size:.92rem;color:rgba(255,255,255,.78)}
.footer-contact-line svg{flex-shrink:0;margin-top:3px}
.footer-bottom{max-width:var(--container);margin:2.5rem auto 0;padding:1.5rem 22px 0;border-top:1px solid rgba(255,255,255,.12);display:flex;flex-wrap:wrap;justify-content:space-between;gap:1rem;font-size:.82rem;color:rgba(255,255,255,.6)}
.footer-bottom a{color:rgba(255,255,255,.7)}

/* BLOG */
.blog-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:1.6rem;margin-top:2rem}
.blog-card{background:#fff;border:1px solid var(--gray-border);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-sm);transition:all var(--transition);text-decoration:none;color:var(--ink);display:flex;flex-direction:column}
.blog-card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg);border-color:var(--emerald);color:var(--ink)}
.blog-card-body{padding:1.4rem 1.5rem 1.55rem;display:flex;flex-direction:column;gap:.7rem;flex-grow:1}
.blog-category{font-family:var(--font-head);font-size:.74rem;font-weight:700;color:var(--caramel-dark);letter-spacing:.1em;text-transform:uppercase}
.blog-card h3{color:var(--ink);font-size:1.15rem;line-height:1.32;margin:0}
.blog-card p{color:var(--gray);font-size:.92rem;line-height:1.55;margin:0;flex-grow:1}
.blog-card-meta{font-size:.8rem;color:var(--gray-light);font-weight:500;margin-top:auto;display:flex;justify-content:space-between}

/* BLOG-ARTICLE */
.article{max-width:780px;margin:0 auto;padding:3rem 0}
.article-meta{display:flex;flex-wrap:wrap;gap:.7rem 1.5rem;color:var(--gray);font-size:.88rem;margin-bottom:1.5rem;align-items:center}
.article-content{font-size:1.04rem;line-height:1.78;color:var(--ink-soft)}
.article-content p{margin-bottom:1.25rem}
.article-content h2{margin:2.5rem 0 1rem;color:var(--emerald-dark)}
.article-content h3{margin:1.8rem 0 .85rem;color:var(--ink)}
.article-content ul,.article-content ol{margin:0 0 1.25rem 1.4rem}
.article-content li{margin-bottom:.55rem}
.article-content blockquote{border-left:3px solid var(--caramel);padding:.4rem 0 .4rem 1.25rem;margin:1.6rem 0;font-style:italic;color:var(--ink)}

/* RESPONSIVE */
@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
@media(max-width:880px){
  .nav-menu{display:none;position:absolute;top:100%;left:0;right:0;background:var(--emerald-dark);flex-direction:column;align-items:stretch;padding:.5rem 0;box-shadow:0 8px 24px rgba(22,62,41,.3)}
  .nav-menu.open{display:flex}
  .nav-menu li{margin:0;width:100%}
  .nav-menu>li>a{padding:.85rem 1.5rem;display:block;border-bottom:1px solid rgba(255,255,255,.1);color:rgba(255,255,255,.9);border-radius:0}
  .dropdown{position:static;transform:none;opacity:1;visibility:visible;box-shadow:none;border:none;background:rgba(255,255,255,.06);min-width:0;border-radius:0;padding:.4rem 0;display:none}
  .nav-menu li.menu-open .dropdown{display:block}
  .dropdown a{padding-left:2.5rem;color:rgba(255,255,255,.85)}
  .dropdown a:hover{background:rgba(255,255,255,.1);color:#fff}
  .menu-toggle{display:block}
  .nav-phone span{display:none}
  .nav-phone svg{width:22px;height:22px}
  .hero{min-height:auto;padding:3rem 22px 2.5rem}
  .hero-split{flex-direction:column;min-height:auto}
  .hero-left,.hero-right{width:100%;padding:0}
  .hero-left{padding-bottom:0}
  .hero-right .form-card{margin-top:2rem;border-radius:var(--radius-lg)}
  .page-hero{padding:2.6rem 0 2rem}
  section{padding:3.2rem 0}
  .proof-grid{grid-template-columns:repeat(2,1fr);gap:1rem}
  .proof-num{font-size:1.4rem}
  .wa-float{padding:11px 16px;font-size:13px}
  .cta-phone-large{font-size:1.55rem}
}
@media(max-width:520px){
  .brand img{height:38px}
  .brand-name{font-size:1.02rem}
  .brand-tag{font-size:.62rem}
  .nav-phone{padding:6px 10px;background:var(--emerald);color:#fff;border-radius:50px}
  .proof-grid{grid-template-columns:1fr 1fr}
}
"""

# ============================================================================
# JS — minimal, vanilla, mobile menu only
# ============================================================================
JS = r"""
document.addEventListener('DOMContentLoaded',function(){
  var t=document.querySelector('.menu-toggle');var m=document.querySelector('.nav-menu');
  if(t&&m){t.addEventListener('click',function(){m.classList.toggle('open')});
  m.querySelectorAll('li').forEach(function(li){
    var sub=li.querySelector('.dropdown');
    if(sub){var a=li.querySelector('a');a.addEventListener('click',function(e){
      if(window.innerWidth<=880&&a.getAttribute('href').indexOf('#')!==0){e.preventDefault();li.classList.toggle('menu-open')}
    })}
  })}
});
"""

# ============================================================================
# LOGO SVG (inline, used everywhere)
# ============================================================================
LOGO_SVG = """<svg viewBox="0 0 300 50" xmlns="http://www.w3.org/2000/svg" aria-label="Sarasota Flooring Company" style="height:44px;width:auto;flex-shrink:0">
  <!-- Plank-icon: subtle reference to floor planks -->
  <rect x="0" y="6" width="42" height="38" rx="5" fill="#1F5F3F"/>
  <rect x="6"  y="14" width="30" height="3" rx="1.5" fill="#F0B96A"/>
  <rect x="6"  y="22" width="20" height="3" rx="1.5" fill="#C8893D"/>
  <rect x="20" y="22" width="16" height="3" rx="1.5" fill="#F0B96A" opacity=".7"/>
  <rect x="6"  y="30" width="30" height="3" rx="1.5" fill="#C8893D"/>
  <rect x="14" y="38" width="22" height="3" rx="1.5" fill="#F0B96A" opacity=".8"/>
  <!-- Wordmark -->
  <text x="54" y="22" font-family="'Outfit','Inter',-apple-system,sans-serif" font-weight="800" font-size="18" fill="#FFFFFF" letter-spacing="-0.2">SARASOTA</text>
  <text x="55" y="40" font-family="'Outfit','Inter',-apple-system,sans-serif" font-weight="500" font-size="10.5" fill="#F8DDA8" letter-spacing="3.2">FLOORING COMPANY</text>
</svg>"""

# ============================================================================
# HEADER (used everywhere)
# ============================================================================
def header():
    services_dd = "".join(
        f'<li><a href="/{s}/">{SERVICES[s]["name"]}</a></li>'
        for s in SERVICE_ORDER
    )
    areas_dd = "".join(
        f'<li><a href="/{c}/">{CITIES[c]["name"]}, FL</a></li>'
        for c in CITY_ORDER
    )
    return f"""<header class="site-header">
  <nav class="nav-bar" aria-label="Primary navigation">
    <a href="/" class="brand" aria-label="{BUSINESS['name']} — home">
      {LOGO_SVG}
    </a>
    <ul class="nav-menu" role="menubar">
      <li role="none"><a href="/" role="menuitem">Home</a></li>
      <li role="none"><a href="#services" role="menuitem">Services ▾</a>
        <ul class="dropdown">{services_dd}</ul>
      </li>
      <li role="none"><a href="#areas" role="menuitem">Service Areas ▾</a>
        <ul class="dropdown">{areas_dd}</ul>
      </li>
      <li role="none"><a href="/about/" role="menuitem">About</a></li>
      <li role="none"><a href="/blog/" role="menuitem">Blog</a></li>
      <li role="none"><a href="/contact/" role="menuitem">Contact</a></li>
    </ul>
    <div class="nav-cta">
      <a href="{TEL_LINK}" class="nav-phone" aria-label="Call us">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.05-.24c1.12.37 2.33.57 3.57.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.24 1.05l-2.2 2.17z"/></svg>
        <span>{BUSINESS['phone_display']}</span>
      </a>
      <a href="/contact/" class="btn btn-primary" style="background:var(--caramel);color:#fff;padding:10px 20px;font-size:.9rem">Free Estimate</a>
    </div>
    <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    </button>
  </nav>
</header>"""

# ============================================================================
# FOOTER (used everywhere)
# ============================================================================
def footer():
    same_as = [
        BUSINESS["google_profile"],
    ]
    for label,url,desc in BUSINESS["partner_sites"]:
        same_as.append(url)
    services_links = "".join(
        f'<li><a href="/{s}/">{SERVICES[s]["name"]}</a></li>' for s in SERVICE_ORDER
    )
    areas_links = "".join(
        f'<li><a href="/{c}/">{CITIES[c]["name"]}, FL</a></li>' for c in CITY_ORDER
    )
    partner_links = "".join(
        f'<li><a href="{url}" target="_blank" rel="noopener" title="{desc}">{label}</a></li>'
        for (label,url,desc) in BUSINESS["partner_sites"]
    )
    return f"""<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-col">
      <div class="footer-brand-block">
        <div class="footer-brand-name">{BUSINESS['name']}</div>
        <div class="footer-brand-tag">{BUSINESS['tagline']}</div>
      </div>
      <p>{BUSINESS['tagline_long']}</p>
      <p style="margin-top:.85rem;font-size:.82rem;color:#F8DDA8;font-weight:600">{BUSINESS['unique_stat_full']}.</p>
    </div>
    <div class="footer-col">
      <h4>Services</h4>
      <ul>{services_links}</ul>
    </div>
    <div class="footer-col">
      <h4>Service Areas</h4>
      <ul>{areas_links}</ul>
    </div>
    <div class="footer-col">
      <h4>Contact</h4>
      <div class="footer-contact-line">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="#F8DDA8"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.05-.24c1.12.37 2.33.57 3.57.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.24 1.05l-2.2 2.17z"/></svg>
        <a href="{TEL_LINK}">{BUSINESS['phone_display']}</a>
      </div>
      <div class="footer-contact-line">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="#F8DDA8"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        <a href="mailto:{BUSINESS['email']}">{BUSINESS['email']}</a>
      </div>
      <div class="footer-contact-line">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="#F8DDA8"><path d="M12 2C8 2 5 5 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-4-3-7-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"/></svg>
        <span>{BUSINESS['street']}<br>{BUSINESS['city']}, {BUSINESS['state']} {BUSINESS['zip']}</span>
      </div>
      <div class="footer-contact-line">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="#F8DDA8"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm.5 5h-1v6l5.25 3.15.5-.86-4.75-2.82V7z"/></svg>
        <span>Mon–Fri 7am–7pm · Sat 8am–5pm · Sun 9am–4pm</span>
      </div>
    </div>
    <div class="footer-col">
      <h4>Find Us Online</h4>
      <ul>
        <li><a href="{BUSINESS['google_profile']}" target="_blank" rel="noopener">Google Business Profile</a></li>
        <li><a href="/blog/">Flooring Blog</a></li>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/financing/">Financing Options</a></li>
        <li><a href="/warranty/">2-Year Warranty</a></li>
      </ul>
      <h4 style="margin-top:1.4rem">Trusted Partners</h4>
      <ul>{partner_links}</ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© 2026 {BUSINESS['legal_name']}. All rights reserved. {BUSINESS['license']}.</span>
    <span><a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="/sitemap.xml">Sitemap</a></span>
  </div>
</footer>
<a href="{SMS_LINK}" class="wa-float" style="background:var(--emerald)" aria-label="Text us">
  <svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/></svg>
  Text Us
</a>
<script>{JS}</script>"""

# ============================================================================
# SCHEMA GENERATORS — Organization, LocalBusiness, BreadcrumbList, FAQ, Article
# ============================================================================
def org_schema():
    """Used on homepage only — full Organization w/ aggregateRating."""
    return {
        "@context":"https://schema.org",
        "@type":"Organization",
        "@id":f"{SITE}/#organization",
        "name":BUSINESS["name"],
        "legalName":BUSINESS["legal_name"],
        "url":SITE,
        "logo":{"@type":"ImageObject","url":f"{SITE}/images/logo.png","width":512,"height":512},
        "image":f"{SITE}/images/hero-og.jpg",
        "telephone":BUSINESS["phone"],
        "email":BUSINESS["email"],
        "foundingDate":str(BUSINESS["year_founded"]),
        "slogan":BUSINESS["tagline"],
        "description":BUSINESS["tagline_long"],
        "priceRange":"$$$",
        "address":{
            "@type":"PostalAddress",
            "streetAddress":BUSINESS["street"],
            "addressLocality":BUSINESS["city"],
            "addressRegion":BUSINESS["state"],
            "postalCode":BUSINESS["zip"],
            "addressCountry":BUSINESS["country"],
        },
        "geo":{"@type":"GeoCoordinates","latitude":BUSINESS["lat"],"longitude":BUSINESS["lng"]},
        "areaServed":[
            {"@type":"City","name":CITIES[c]["name"],"containedInPlace":{"@type":"AdministrativeArea","name":CITIES[c]["county"]}}
            for c in CITY_ORDER
        ],
        "sameAs":[BUSINESS["google_profile"]] + [u for (_,u,_) in BUSINESS["partner_sites"]],
        "aggregateRating":{
            "@type":"AggregateRating",
            "ratingValue":BUSINESS["rating"],
            "reviewCount":str(BUSINESS["review_count"]),
            "bestRating":"5",
            "worstRating":"5",
        },
        "openingHoursSpecification":[
            {"@type":"OpeningHoursSpecification","dayOfWeek":d,"opens":o,"closes":c}
            for (d,o,c) in BUSINESS["hours"]
        ],
    }

def localbiz_schema(page_path,city_slug=None,city_name=None,service_slug=None,service_name=None,description=None):
    """LocalBusiness schema for service pages and city pages."""
    city_obj = CITIES[city_slug] if city_slug else None
    locality = city_obj["name"] if city_obj else BUSINESS["city"]
    region = "FL"
    lat = city_obj["lat"] if city_obj else BUSINESS["lat"]
    lng = city_obj["lng"] if city_obj else BUSINESS["lng"]
    page_url = f"{SITE}/{page_path}/" if page_path else f"{SITE}/"
    return {
        "@context":"https://schema.org",
        "@type":["LocalBusiness","HomeAndConstructionBusiness"],
        "@id":f"{page_url}#business",
        "name":BUSINESS["name"],
        "description":description or BUSINESS["tagline_long"],
        "url":page_url,
        "telephone":BUSINESS["phone"],
        "email":BUSINESS["email"],
        "image":f"{SITE}/images/hero-og.jpg",
        "priceRange":"$$$",
        "address":{
            "@type":"PostalAddress",
            "streetAddress":BUSINESS["street"],
            "addressLocality":BUSINESS["city"],
            "addressRegion":region,
            "postalCode":BUSINESS["zip"],
            "addressCountry":"US",
        },
        "geo":{"@type":"GeoCoordinates","latitude":lat,"longitude":lng},
        "areaServed":({"@type":"City","name":city_name or locality}) if city_name else None,
        "sameAs":[BUSINESS["google_profile"]] + [u for (_,u,_) in BUSINESS["partner_sites"]],
        "aggregateRating":{
            "@type":"AggregateRating",
            "ratingValue":BUSINESS["rating"],
            "reviewCount":str(BUSINESS["review_count"]),
            "bestRating":"5",
        },
    }

def breadcrumb_schema(items):
    """items = [(name, url|None), ...]"""
    return {
        "@context":"https://schema.org",
        "@type":"BreadcrumbList",
        "itemListElement":[
            {
                "@type":"ListItem",
                "position":i+1,
                "name":name,
                **({"item":url} if url else {}),
            }
            for i,(name,url) in enumerate(items)
        ],
    }

def faq_schema(qa_list):
    """qa_list = [(question, answer), ...]"""
    return {
        "@context":"https://schema.org",
        "@type":"FAQPage",
        "mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}}
            for q,a in qa_list
        ],
    }

def article_schema(title,description,slug,date_pub,author=None):
    return {
        "@context":"https://schema.org",
        "@type":"Article",
        "headline":title,
        "description":description,
        "image":f"{SITE}/images/blog-{slug}.jpg",
        "datePublished":date_pub,
        "dateModified":date_pub,
        "author":{"@type":"Person","name":author or "Sarasota Flooring Company Owner"},
        "publisher":{
            "@type":"Organization",
            "name":BUSINESS["name"],
            "logo":{"@type":"ImageObject","url":f"{SITE}/images/logo.png"},
        },
        "mainEntityOfPage":{"@type":"WebPage","@id":f"{SITE}/blog/{slug}/"},
    }

def render_schemas(schemas):
    """Render a list of schema dicts as <script> tags. None entries skipped."""
    out = []
    for s in schemas:
        if not s: continue
        # Drop None values from dicts
        def clean(o):
            if isinstance(o,dict): return {k:clean(v) for k,v in o.items() if v is not None}
            if isinstance(o,list): return [clean(x) for x in o]
            return o
        out.append(f'<script type="application/ld+json">{json.dumps(clean(s),ensure_ascii=False)}</script>')
    return "\n".join(out)

# ============================================================================
# COMPONENT BUILDERS — shared widgets
# ============================================================================
def page_head(title,description,canonical_path,og_image=None,extra_meta=""):
    """Standard <head> block — call from every page builder."""
    og_img = og_image or "/images/hero-og.jpg"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE}/{canonical_path}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="author" content="{BUSINESS['name']}">
<meta name="geo.region" content="US-FL">
<meta name="geo.placename" content="{BUSINESS['city']}, Florida">
<meta name="geo.position" content="{BUSINESS['lat']};{BUSINESS['lng']}">
<meta name="ICBM" content="{BUSINESS['lat']}, {BUSINESS['lng']}">
{extra_meta}
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{SITE}/{canonical_path}">
<meta property="og:image" content="{SITE}{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="{BUSINESS['name']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE}{og_img}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/images/favicon.png">
<link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>"""

def stat_badge():
    return f"""<div class="stat-badge">
  <span class="stat-icon">⭐</span>
  <div>
    <p>{BUSINESS['unique_stat_full']}.</p>
    <p>{BUSINESS['review_count']} verified reviews · {BUSINESS['rating']} ★ Google Rating · {BUSINESS['guarantee']}</p>
  </div>
</div>"""

def wa_banner(message=None):
    msg = message or "Get a free flooring estimate in Sarasota — 24 hours"
    return f"""<div class="wa-banner">
  <div>
    <p class="wa-banner-head">{msg}</p>
    <p class="wa-banner-sub">Call or text {BUSINESS['phone_display']} — 7 days a week, Sarasota &amp; Manatee Counties</p>
  </div>
  <a href="{TEL_LINK}" class="btn">Call Now</a>
</div>"""

def cta_banner(headline=None,sub=None):
    headline = headline or "Ready to start? Free estimate within 24 hours."
    sub = sub or "Call or text Sarasota Flooring Company directly. Free sample bring-outs and in-home consultations across all 8 service areas."
    return f"""<section class="cta-banner">
  <div class="container">
    <h2>{headline}</h2>
    <p>{sub}</p>
    <a href="{TEL_LINK}" class="cta-phone-large">📞 {BUSINESS['phone_display']}</a>
    <div class="cta-buttons">
      <a href="{TEL_LINK}" class="btn btn-primary">Call Now</a>
      <a href="{SMS_LINK}" class="btn btn-secondary" style="background:#fff;color:var(--emerald)">💬 Text Us</a>
      <a href="/contact/" class="btn btn-ghost" style="border-color:rgba(255,255,255,.5);color:#fff">Online Form</a>
    </div>
  </div>
</section>"""

def breadcrumbs_html(items):
    """items = [(name, url|None)]"""
    lis = []
    for name,url in items:
        if url:
            lis.append(f'<li><a href="{url}">{name}</a></li>')
        else:
            lis.append(f'<li>{name}</li>')
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><div class="container"><ol>{"".join(lis)}</ol></div></nav>'

def faq_block(faqs,heading="Frequently Asked Questions",eyebrow="FAQ"):
    items = []
    for q,a in faqs:
        items.append(f'<details class="faq-item"><summary>{q}</summary><div class="faq-item-body">{a}</div></details>')
    return f"""<section class="faq-section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{heading}</h2>
    </div>
    <div class="faq-list">{"".join(items)}</div>
  </div>
</section>"""

def checklist_block():
    """Render the 63-point installation standard as a grid of cards."""
    cards = []
    for cat in CHECKLIST["categories"]:
        lis = "".join(f"<li>{p}</li>" for p in cat["points"])
        cards.append(f"""<div class="checklist-card">
  <div class="checklist-head">
    <span class="checklist-icon">{cat['icon']}</span>
    <div class="checklist-head-text">
      <p>{cat['category']}</p>
      <p>{len(cat['points'])} points</p>
    </div>
  </div>
  <ol class="checklist-list">{lis}</ol>
</div>""")
    return f"""<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Our 63-Point Standard</span>
      <h2>{CHECKLIST['name']}</h2>
      <p>Sixty-three documented checkpoints across six install phases. Every job folder hands you the moisture log, batch numbers, and photo documentation at walk-through — so you know exactly what was installed, how, and where to source matching material later.</p>
    </div>
    <div class="checklist-grid">{"".join(cards)}</div>
  </div>
</section>"""

def neighborhoods_pills(city_slug):
    """Render the neighborhood list for a city as pills."""
    nb = CITIES[city_slug]["neighborhoods"]
    pills = "".join(f'<span class="neighborhood-pill">{n}</span>' for n in nb)
    return f'<div class="neighborhood-grid">{pills}</div>'

def reviews_block(limit=4,city_filter=None,service_filter=None):
    """Render review cards. Optionally filter by city or service."""
    pool = REVIEWS
    if city_filter:
        pool = [r for r in pool if r[1]==city_filter]
    if service_filter:
        pool = [r for r in pool if service_filter.lower() in r[2].lower()]
    if not pool:
        pool = REVIEWS[:limit]
    cards = []
    for (name,city,service,rating,date,text) in pool[:limit]:
        stars = "★"*int(float(rating))
        cards.append(f"""<div class="review-card">
  <div class="review-stars">{stars}</div>
  <p class="review-text">"{text}"</p>
  <div class="review-meta">
    <span class="review-name">{name}</span> · {city}, FL · {service}<br>
    <span style="color:var(--gray-light);font-size:.78rem">Verified Google Review · {date}</span>
  </div>
</div>""")
    return f"""<section class="reviews-section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">5.0 ★ Google Rated</span>
      <h2>What Our Clients Say</h2>
      <p>Real reviews from real installs across Sarasota and Manatee Counties. <a href="{BUSINESS['google_profile']}" target="_blank" rel="noopener">See all on Google →</a></p>
    </div>
    <div class="reviews-grid">{"".join(cards)}</div>
  </div>
</section>"""

def pricing_block(service):
    """Render a pricing table for a service."""
    rows = []
    for (label,price,note) in service["pricing_rows"]:
        rows.append(f'<tr><td>{label}</td><td>{price}</td><td>{note}</td></tr>')
    return f"""<div class="pricing-block">
  <table class="pricing-table">
    <thead>
      <tr><th>Service</th><th>Installed Price</th><th>Notes</th></tr>
    </thead>
    <tbody>{"".join(rows)}</tbody>
  </table>
</div>
<p style="font-size:.85rem;color:var(--gray);margin:.85rem 0 0">Prices reflect typical Sarasota and Manatee County installations as of 2026. Final pricing varies by subfloor condition, material selection, and project scope — every quote is custom and itemized. <a href="/contact/">Get a free written estimate within 24 hours →</a></p>"""

def scope_list_html(items):
    return f'<ul class="scope-list">{"".join(f"<li>{i}</li>" for i in items)}</ul>'

def internal_links_box(heading,links):
    """links = [(label,url),...]"""
    lis = "".join(f'<li><a href="{u}">{l}</a></li>' for (l,u) in links)
    return f'<div class="internal-links"><h3>{heading}</h3><ul>{lis}</ul></div>'

def write(path,html):
    """Write file to /home/claude/sarasota-flooring/<path>."""
    import os
    full = f"/home/claude/sarasota-flooring/{path}"
    os.makedirs(os.path.dirname(full) if os.path.dirname(full) else full, exist_ok=True)
    if path.endswith(".html") or "." in path.split("/")[-1]:
        with open(full,"w",encoding="utf-8") as f: f.write(html)
    else:
        with open(full,"w",encoding="utf-8") as f: f.write(html)
    return full
