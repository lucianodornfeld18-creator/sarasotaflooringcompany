#!/usr/bin/env python3
"""
Sarasota Flooring Company — theme v2 ("Gulf plank").
Design system derived from the logo: three planks — wood tan, ocean teal, sand —
with a cream sun. Deep teal #044452 · ocean #045A6A · wood #D4AC72 · cream #FAF3E6.
Everything visual lives here: CSS, header, footer, components, JSON-LD.
"""
import json, html as _html
from data_core import BUSINESS, SERVICES, SERVICE_ORDER, TEL_LINK, SMS_LINK, WEB3FORMS_ENDPOINT, WEB3FORMS_KEY

DOMAIN = BUSINESS["domain"]
SITE = f"https://{DOMAIN}"
NAME = BUSINESS["name"]
PHONE = BUSINESS["phone_display"]
ASSET_V = "3"          # cache-bust for /images/*

def esc(s):
    """Escape once: source data already contains a few HTML entities (&amp;, &nbsp;)."""
    return _html.escape(_html.unescape(str(s)), quote=True)

# ============================================================================
# CSS
# ============================================================================
CSS = r"""
:root{--deep:#044452;--ocean:#045A6A;--ocean-2:#0B7285;--wood:#D4AC72;--wood-dark:#A97C3C;--wood-soft:#F4E6CE;--cream:#FAF3E6;--sand:#F3E9D6;--foam:#E6F1F2;--ink:#12272C;--ink-soft:#33494E;--gray:#5B6E72;--line:#E4D9C3;--white:#fff;--ok:#1B7A4B;
--shadow-sm:0 1px 3px rgba(4,68,82,.10);--shadow:0 6px 18px rgba(4,68,82,.12);--shadow-lg:0 18px 44px rgba(4,68,82,.18);--r:10px;--r-lg:18px;
--head:'Montserrat','Segoe UI',system-ui,-apple-system,sans-serif;--body:'Source Sans 3','Segoe UI',system-ui,-apple-system,sans-serif;--wrap:1180px;--t:.2s cubic-bezier(.4,0,.2,1)}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;font-family:var(--body);font-size:1.0625rem;line-height:1.68;color:var(--ink-soft);background:var(--cream);overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{color:var(--ocean);text-decoration-thickness:1px;text-underline-offset:3px}
a:hover{color:var(--wood-dark)}
h1,h2,h3,h4{font-family:var(--head);color:var(--deep);line-height:1.16;margin:0 0 .6em;letter-spacing:-.015em}
h1{font-size:clamp(2rem,4.6vw,3.15rem);font-weight:800}
h2{font-size:clamp(1.5rem,3vw,2.1rem);font-weight:800}
h3{font-size:1.2rem;font-weight:700}
h4{font-size:1rem;font-weight:700}
p{margin:0 0 1.05em}
ul,ol{margin:0 0 1.1em;padding-left:1.25em}
li{margin-bottom:.4em}
table{border-collapse:collapse;width:100%}
:focus-visible{outline:3px solid var(--wood);outline-offset:2px;border-radius:4px}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 22px}
.narrow{max-width:820px}
section{padding:4.2rem 0}
.bg-sand{background:var(--sand)}.bg-white{background:#fff}.bg-foam{background:var(--foam)}
.bg-deep{background:var(--deep);color:#DCEBED}.bg-deep h2,.bg-deep h3{color:#fff}.bg-deep a{color:var(--wood)}
.skip{position:absolute;left:-999px;top:0;background:#fff;padding:.6rem 1rem;z-index:200}.skip:focus{left:8px;top:8px}
.eyebrow{display:inline-flex;align-items:center;gap:.5rem;font-family:var(--head);font-size:.74rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--ocean);margin-bottom:.8rem}
.eyebrow::before{content:"";width:26px;height:9px;border-top:3px solid var(--wood);border-bottom:3px solid var(--ocean)}
.on-dark .eyebrow,.eyebrow.on-dark{color:var(--wood)}
.lede{font-size:1.16rem;color:var(--ink-soft)}
.sec-head{max-width:780px;margin:0 0 2.4rem}.sec-head.center{margin:0 auto 2.6rem;text-align:center}.sec-head.center .eyebrow{justify-content:center}

/* planks divider — the logo's three boards */
.planks{display:block;height:14px;background:linear-gradient(var(--wood) 0 4px,transparent 4px 5px,var(--ocean) 5px 9px,transparent 9px 10px,var(--wood-soft) 10px 14px)}

/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;padding:.86rem 1.55rem;font-family:var(--head);font-weight:700;font-size:.95rem;border-radius:999px;text-decoration:none;border:2px solid transparent;cursor:pointer;transition:all var(--t);line-height:1.2;text-align:center}
.btn-wood{background:var(--wood);color:var(--deep);box-shadow:0 5px 16px rgba(169,124,60,.35)}.btn-wood:hover{background:#E2BD85;color:var(--deep);transform:translateY(-2px)}
.btn-deep{background:var(--deep);color:#fff}.btn-deep:hover{background:var(--ocean);color:#fff;transform:translateY(-2px)}
.btn-line{background:transparent;color:var(--deep);border-color:var(--deep)}.btn-line:hover{background:var(--deep);color:#fff}
.btn-ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.6)}.btn-ghost:hover{background:#fff;color:var(--deep)}
.btn-row{display:flex;flex-wrap:wrap;gap:.8rem}

/* header */
.topbar{background:var(--deep);color:#CFE3E6;font-size:.84rem}
.topbar .wrap{display:flex;justify-content:space-between;gap:1rem;padding-top:.42rem;padding-bottom:.42rem;flex-wrap:wrap}
.topbar a{color:#fff;text-decoration:none;font-weight:600}
.site-header{position:sticky;top:0;z-index:100;background:rgba(255,253,248,.97);backdrop-filter:saturate(1.4) blur(8px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;justify-content:space-between;gap:1rem;max-width:1280px;margin:0 auto;padding:.55rem 22px}
.brand{display:flex;align-items:center;gap:.7rem;text-decoration:none;min-width:0}
.brand img{height:50px;width:auto;flex:none}
.brand-txt{display:flex;flex-direction:column;line-height:1;min-width:0}
.brand-name{font-family:var(--head);font-weight:800;font-size:1.32rem;letter-spacing:.06em;color:var(--deep)}
.brand-tag{font-family:var(--head);font-weight:700;font-size:.62rem;letter-spacing:.3em;color:var(--wood-dark);margin-top:.28rem;white-space:nowrap}
.menu{display:flex;align-items:center;gap:.2rem;list-style:none;margin:0;padding:0}
.menu>li{position:relative;margin:0}
.menu>li>a,.menu>li>button{display:block;white-space:nowrap;padding:.6rem .7rem;font-family:var(--head);font-weight:600;font-size:.9rem;color:var(--deep);text-decoration:none;background:none;border:0;cursor:pointer;border-radius:8px}
.menu>li>a:hover,.menu>li>button:hover{background:var(--foam)}
.drop{position:absolute;top:100%;left:0;min-width:260px;background:#fff;border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow-lg);padding:.5rem;list-style:none;margin:0;opacity:0;visibility:hidden;transform:translateY(6px);transition:all var(--t)}
.drop.cols{min-width:430px;columns:2}
.menu>li:hover>.drop,.menu>li:focus-within>.drop{opacity:1;visibility:visible;transform:none}
.drop li{margin:0;break-inside:avoid}.drop a{display:block;padding:.48rem .7rem;border-radius:8px;font-size:.92rem;color:var(--ink-soft);text-decoration:none}.drop a:hover{background:var(--foam);color:var(--deep)}
.nav-cta{display:flex;align-items:center;gap:.6rem;flex:none}
.nav-phone{display:inline-flex;align-items:center;gap:.4rem;font-family:var(--head);font-weight:800;color:var(--deep);text-decoration:none;font-size:1rem;white-space:nowrap}
.nav-phone svg{width:18px;height:18px;color:var(--wood-dark)}
.nav-cta .btn{padding:.62rem 1.1rem;font-size:.86rem}
.burger{display:none;background:none;border:0;padding:.4rem;color:var(--deep);cursor:pointer}.burger svg{width:28px;height:28px;display:block}

/* hero */
.hero{position:relative;background:linear-gradient(160deg,#033640 0%,var(--deep) 45%,var(--ocean) 100%);color:#E4F0F1;padding:4.2rem 0 5.6rem;overflow:hidden}
.hero::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:64px;background:var(--cream);-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 64' preserveAspectRatio='none'%3E%3Cpath d='M0 40C200 8 380 66 600 38S1010 4 1200 34V64H0Z'/%3E%3C/svg%3E") center/100% 100% no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 64' preserveAspectRatio='none'%3E%3Cpath d='M0 40C200 8 380 66 600 38S1010 4 1200 34V64H0Z'/%3E%3C/svg%3E") center/100% 100% no-repeat}
.hero .sun{position:absolute;right:-90px;top:-90px;width:340px;height:340px;border-radius:50%;background:radial-gradient(circle,rgba(250,243,230,.22),rgba(250,243,230,0) 68%)}
.hero h1{color:#fff;margin-bottom:.55em}.hero h1 em{font-style:normal;color:var(--wood)}
.hero .lede{color:#D3E6E8;max-width:640px}
.hero-grid{position:relative;display:grid;grid-template-columns:1.15fr .85fr;gap:3rem;align-items:center}
.hero-points{list-style:none;padding:0;margin:1.4rem 0 1.8rem;display:grid;gap:.5rem}
.hero-points li{position:relative;padding-left:1.7rem;margin:0;color:#E4F0F1}.hero-points li::before{content:"";position:absolute;left:0;top:.45em;width:14px;height:8px;border-left:3px solid var(--wood);border-bottom:3px solid var(--wood);transform:rotate(-45deg)}
.page-hero{background:linear-gradient(160deg,#033640,var(--deep) 55%,var(--ocean));color:#DCEBED;padding:3rem 0 3.4rem;position:relative}
.page-hero h1{color:#fff;max-width:900px}.page-hero .lede{color:#D3E6E8;max-width:780px;margin-bottom:0}
.crumbs{font-size:.86rem;margin-bottom:1.1rem;color:#A9CBD0}.crumbs a{color:#DCEBED;text-decoration:none}.crumbs a:hover{color:var(--wood)}.crumbs span{margin:0 .4rem;opacity:.6}
.updated{font-size:.84rem;color:#A9CBD0;margin-top:1rem}

/* answer capsule */
.capsule{background:#fff;border:1px solid var(--line);border-left:6px solid var(--wood);border-radius:var(--r);padding:1.25rem 1.4rem;margin:0 0 1.8rem;box-shadow:var(--shadow-sm)}
.capsule .k{font-family:var(--head);font-size:.72rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--wood-dark);margin-bottom:.35rem}
.capsule p{margin:0;color:var(--ink);font-size:1.09rem}

/* cards & grids */
.grid{display:grid;gap:1.3rem}.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:1.5rem;box-shadow:var(--shadow-sm);transition:all var(--t);position:relative;overflow:hidden}
.card::before{content:"";position:absolute;left:0;right:0;top:0;height:5px;background:linear-gradient(90deg,var(--wood) 0 34%,var(--ocean) 34% 67%,var(--wood-soft) 67%)}
a.card{text-decoration:none;color:inherit;display:block}a.card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg);border-color:var(--wood)}
.card h3{margin-bottom:.4rem}.card p{margin:0;font-size:.98rem;color:var(--gray)}
.card .more{display:inline-block;margin-top:.8rem;font-family:var(--head);font-weight:700;font-size:.86rem;color:var(--ocean)}
.card .num{font-family:var(--head);font-weight:800;font-size:.8rem;letter-spacing:.14em;color:var(--wood-dark);margin-bottom:.5rem}
.photo{border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow);background:var(--sand)}
.photo img{width:100%;aspect-ratio:4/3;object-fit:cover}
figure{margin:0}figcaption{font-size:.84rem;color:var(--gray);padding:.55rem .2rem 0}
.split{display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center}.split>*,.lf>*,.hero-grid>*{min-width:0}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;text-align:center}
.stat b{display:block;font-family:var(--head);font-size:1.7rem;font-weight:800;color:var(--wood)}.stat span{font-size:.86rem;color:#CFE3E6}
.pills{display:flex;flex-wrap:wrap;gap:.5rem;list-style:none;padding:0;margin:0}
.pills li{margin:0}.pills a,.pills span{display:inline-block;padding:.42rem .95rem;border-radius:999px;background:#fff;border:1px solid var(--line);font-size:.92rem;color:var(--deep);text-decoration:none;font-weight:600}
.pills a:hover{background:var(--deep);color:#fff;border-color:var(--deep)}
.tier{font-family:var(--head);font-size:.68rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--wood-dark)}

/* tables */
.tbl-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:var(--r);background:#fff;margin:0 0 1.6rem;-webkit-overflow-scrolling:touch}
.tbl th,.tbl td{padding:.72rem .95rem;text-align:left;border-bottom:1px solid var(--line);font-size:.97rem;vertical-align:top}
.tbl thead th{background:var(--deep);color:#fff;font-family:var(--head);font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;white-space:nowrap}
.tbl tbody tr:last-child td{border-bottom:0}.tbl tbody tr:nth-child(even){background:#FDFAF3}
.tbl caption{caption-side:bottom;font-size:.82rem;color:var(--gray);padding:.6rem .95rem;text-align:left}

/* prose */
.prose h2{margin-top:2.2rem}.prose h3{margin-top:1.6rem}.prose>:first-child{margin-top:0}
.prose ul li::marker{color:var(--wood-dark)}
.sources{font-size:.9rem;color:var(--gray);border-top:1px solid var(--line);margin-top:2.2rem;padding-top:1.1rem}.sources ol{margin:0;padding-left:1.2em}.sources li{margin-bottom:.3em;word-break:break-word}
.byline{display:flex;flex-wrap:wrap;gap:.4rem 1.2rem;font-size:.9rem;color:var(--gray);margin:0 0 1.6rem;padding-bottom:1rem;border-bottom:1px solid var(--line)}
.callout{background:var(--foam);border-radius:var(--r);padding:1.1rem 1.3rem;margin:0 0 1.6rem;border:1px solid #CFE3E6}
.callout strong{color:var(--deep)}
.toc{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:1rem 1.3rem;margin:0 0 1.8rem}.toc p{font-family:var(--head);font-weight:800;color:var(--deep);margin:0 0 .4rem;font-size:.9rem;letter-spacing:.06em;text-transform:uppercase}.toc ol{margin:0;columns:2;column-gap:2rem}.toc li{font-size:.95rem;break-inside:avoid}
.layout{display:grid;grid-template-columns:minmax(0,1fr) 330px;gap:3rem;align-items:start}.layout>*{min-width:0}
.aside{position:sticky;top:96px;display:grid;gap:1.2rem}
.aside .card ul{list-style:none;padding:0;margin:.4rem 0 0}.aside .card li{margin:0;border-top:1px solid var(--line)}.aside .card li:first-child{border:0}.aside .card li a{display:block;padding:.5rem 0;text-decoration:none;font-size:.95rem}

/* FAQ — open by default so the answers are plain HTML for crawlers and AI */
.faq{display:grid;gap:.8rem}
.faq details{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:0 1.2rem}
.faq summary{cursor:pointer;list-style:none;padding:1rem 1.6rem 1rem 0;font-family:var(--head);font-weight:700;color:var(--deep);position:relative;font-size:1.02rem}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:0;top:.8rem;font-size:1.4rem;color:var(--wood-dark)}.faq details[open] summary::after{content:"–"}
.faq .a{padding:0 0 1.1rem;color:var(--ink-soft)}.faq .a p:last-child{margin:0}

/* lead form */
.leadform{background:var(--sand);scroll-margin-top:90px}
.lf{display:grid;grid-template-columns:1fr 1.05fr;gap:3rem;align-items:center}
.lf ul{list-style:none;padding:0;margin:1.2rem 0}.lf li{position:relative;padding-left:1.7rem}.lf li::before{content:"";position:absolute;left:0;top:.5em;width:13px;height:7px;border-left:3px solid var(--ocean);border-bottom:3px solid var(--ocean);transform:rotate(-45deg)}
.formcard{background:#fff;border-radius:16px;box-shadow:var(--shadow-lg);padding:1.8rem;border-top:6px solid var(--wood)}
.formcard .t{font-family:var(--head);font-weight:800;font-size:1.22rem;color:var(--deep);margin:0 0 .2rem}.formcard .s{font-size:.9rem;color:var(--gray);margin:0 0 1.1rem}
.fg{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}
.fg label{display:block;font-family:var(--head);font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--deep)}
.fg .full{grid-column:1/-1}
.fg input,.fg select,.fg textarea{display:block;width:100%;margin-top:.3rem;padding:.74rem .85rem;border:1.5px solid var(--line);border-radius:9px;font:400 1rem var(--body);color:var(--ink);background:#fff;letter-spacing:0;text-transform:none}
.fg textarea{min-height:88px;resize:vertical}
.fg input:focus,.fg select:focus,.fg textarea:focus{outline:none;border-color:var(--ocean);box-shadow:0 0 0 3px var(--foam)}
.fg .btn{grid-column:1/-1;width:100%}
.fnote{grid-column:1/-1;font-size:.78rem;color:var(--gray);margin:0;text-align:center}

/* CTA band */
.cta{background:linear-gradient(135deg,#033640,var(--deep) 50%,var(--ocean));color:#DCEBED;text-align:center;padding:4rem 0}
.cta h2{color:#fff}.cta p{max-width:660px;margin:0 auto 1.4rem}
.cta .tel{display:inline-block;font-family:var(--head);font-weight:800;font-size:2rem;color:var(--wood);text-decoration:none;margin-bottom:1.2rem}
.cta .btn-row{justify-content:center}

/* footer */
.site-footer{background:#032E37;color:#B7D0D4;font-size:.95rem;padding:3.6rem 0 0}
.fgrid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr 1.2fr;gap:2.2rem}
.site-footer h4{color:#fff;font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;margin-bottom:.9rem}
.site-footer ul{list-style:none;padding:0;margin:0}.site-footer li{margin-bottom:.42rem}
.site-footer a{color:#B7D0D4;text-decoration:none}.site-footer a:hover{color:var(--wood)}
.flogo{background:var(--cream);border-radius:14px;padding:1rem;display:inline-block;margin-bottom:1rem}.flogo img{width:190px}
.fbottom{border-top:1px solid rgba(255,255,255,.12);margin-top:2.6rem;padding:1.2rem 0;font-size:.84rem;display:flex;flex-wrap:wrap;gap:.6rem 1.5rem;justify-content:space-between}
.sticky-call{display:none}

/* tools */
.tool{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:1.6rem;box-shadow:var(--shadow)}
.tool .out{background:var(--foam);border-radius:var(--r);padding:1.1rem 1.3rem;margin-top:1.2rem}
.tool .out b{font-family:var(--head);color:var(--deep);font-size:1.5rem}
.opt{display:flex;flex-wrap:wrap;gap:.5rem;margin:.4rem 0 1.1rem}
.opt label{cursor:pointer}.opt input{position:absolute;opacity:0}
.opt span{display:inline-block;padding:.5rem 1rem;border:1.5px solid var(--line);border-radius:999px;font-weight:600;font-size:.93rem;color:var(--deep);background:#fff}
.opt input:checked+span{background:var(--deep);color:#fff;border-color:var(--deep)}.opt input:focus-visible+span{outline:3px solid var(--wood)}

@media(max-width:1080px){.menu{display:none;position:absolute;left:0;right:0;top:100%;background:#fff;flex-direction:column;align-items:stretch;padding:.6rem 22px 1.2rem;border-bottom:1px solid var(--line);box-shadow:var(--shadow-lg);max-height:calc(100vh - 70px);overflow:auto}
 .menu.open{display:flex}.menu>li>a,.menu>li>button{width:100%;text-align:left;padding:.8rem .2rem;font-size:1rem;border-bottom:1px solid var(--line);border-radius:0}
 .drop,.drop.cols{position:static;opacity:1;visibility:visible;transform:none;box-shadow:none;border:0;min-width:0;columns:1;padding:.2rem 0 .6rem .8rem;display:none}.menu>li.open>.drop{display:block}
 .burger{display:block}.nav-cta .btn{display:none}
 .fgrid{grid-template-columns:1fr 1fr 1fr}.layout{grid-template-columns:minmax(0,1fr)}.aside{position:static}.g4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:820px){section{padding:3rem 0}.hero{padding:2.6rem 0 4.4rem}.hero-grid,.split,.lf{grid-template-columns:1fr;gap:2rem}.g3{grid-template-columns:1fr 1fr}.stats{grid-template-columns:1fr 1fr}.toc ol{columns:1}.topbar .hide-sm{display:none}
 .sticky-call{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:90;background:var(--deep);box-shadow:0 -6px 20px rgba(0,0,0,.25)}
 .sticky-call a{flex:1;text-align:center;padding:.85rem .4rem;font-family:var(--head);font-weight:800;font-size:.92rem;text-decoration:none;color:#fff}.sticky-call a+a{background:var(--wood);color:var(--deep)}
 body{padding-bottom:52px}}
@media(max-width:560px){.g2,.g3,.g4,.fg,.fgrid{grid-template-columns:1fr}.brand img{height:42px}.brand-name{font-size:1.08rem}.brand-tag{font-size:.52rem;letter-spacing:.22em}.nav-phone span{display:none}.nav-phone{padding:.5rem;border-radius:50%;background:var(--foam)}.nav{padding:.5rem 16px}.wrap{padding:0 18px}.formcard{padding:1.3rem}.cta .tel{font-size:1.6rem}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""

JS = r"""
document.addEventListener('DOMContentLoaded',function(){
  var b=document.querySelector('.burger'),m=document.querySelector('.menu');
  if(b&&m){b.addEventListener('click',function(){var o=m.classList.toggle('open');b.setAttribute('aria-expanded',o)});
    m.querySelectorAll('li>button').forEach(function(x){x.addEventListener('click',function(){x.parentNode.classList.toggle('open')})})}
  document.querySelectorAll('input[name="page"]').forEach(function(i){i.value=location.pathname});
});
"""

PHONE_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.05-.24c1.12.37 2.33.57 3.57.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1.02l-2.2 2.2z"/></svg>'


# ============================================================================
# HEAD
# ============================================================================
def page_head(title, description, path, og_image=None, schemas=None, robots=None, og_type="website", extra=""):
    canonical = f"{SITE}{path}"
    og = og_image or f"/images/og-default.jpg?v={ASSET_V}"
    robots = robots or "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    ld = "".join(f'\n<script type="application/ld+json">{json.dumps(s, ensure_ascii=False, separators=(",", ":"))}</script>'
                 for s in (schemas or []))
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="geo.region" content="US-FL">
<meta name="geo.placename" content="Sarasota, Florida">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#044452">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png">
<link rel="apple-touch-icon" href="/images/favicon-180.png">
<link rel="alternate" type="application/rss+xml" title="{NAME} — flooring answers" href="/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
{extra}<style>{CSS}</style>{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>"""


# ============================================================================
# HEADER / FOOTER
# ============================================================================
def header(nav_cities, landings=None):
    """nav_cities = [(slug, name)] shown in the Areas dropdown."""
    sv = "".join(f'<li><a href="/{s}/">{esc(SERVICES[s]["name"])}</a></li>' for s in SERVICE_ORDER)
    sv += "".join(f'<li><a href="/{sl}/">{esc(lb)}</a></li>' for sl, lb in (landings or []))
    ar = "".join(f'<li><a href="/{s}/">{esc(n)}, FL</a></li>' for s, n in nav_cities)
    return f"""<div class="topbar"><div class="wrap"><span>Flooring installation across Sarasota, Manatee &amp; Charlotte counties <span class="hide-sm">· 40-mile service radius</span></span><span class="hide-sm">Free in-home estimate · <a href="{TEL_LINK}">{PHONE}</a></span></div></div>
<header class="site-header">
  <nav class="nav" aria-label="Primary">
    <a class="brand" href="/" aria-label="{NAME} — home">
      <img src="/images/logo-icon.png?v={ASSET_V}" alt="{NAME} logo — sunset over the Gulf on three flooring planks" width="107" height="50">
      <span class="brand-txt"><span class="brand-name">SARASOTA</span><span class="brand-tag">FLOORING COMPANY</span></span>
    </a>
    <ul class="menu" id="menu">
      <li><button type="button" aria-haspopup="true">Services ▾</button><ul class="drop cols">{sv}<li><a href="/cost/">Flooring cost guides</a></li></ul></li>
      <li><button type="button" aria-haspopup="true">Areas ▾</button><ul class="drop cols">{ar}<li><a href="/areas/"><strong>All areas · 40-mile map</strong></a></li></ul></li>
      <li><a href="/blog/">Answers</a></li>
      <li><a href="/tools/">Tools</a></li>
      <li><a href="/faq/">FAQ</a></li>
      <li><a href="/about/">About</a></li>
      <li><a href="/contact/">Contact</a></li>
    </ul>
    <div class="nav-cta">
      <a class="nav-phone" href="{TEL_LINK}" aria-label="Call {PHONE}">{PHONE_SVG}<span>{PHONE}</span></a>
      <a class="btn btn-wood" href="#estimate">Free Estimate</a>
      <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    </div>
  </nav>
</header>"""


def footer(footer_cities, year=2026):
    sv = "".join(f'<li><a href="/{s}/">{esc(SERVICES[s]["name"])}</a></li>' for s in SERVICE_ORDER)
    half = (len(footer_cities) + 1) // 2
    c1 = "".join(f'<li><a href="/{s}/">Flooring in {esc(n)}</a></li>' for s, n in footer_cities[:half])
    c2 = "".join(f'<li><a href="/{s}/">Flooring in {esc(n)}</a></li>' for s, n in footer_cities[half:])
    return f"""<span class="planks" aria-hidden="true"></span>
<footer class="site-footer">
  <div class="wrap">
    <div class="fgrid">
      <div>
        <span class="flogo"><img src="/images/logo-full.png?v={ASSET_V}" alt="{NAME}" width="190" height="113" loading="lazy"></span>
        <p>Flooring company serving Sarasota, Bradenton, Lakewood Ranch, Venice, North Port and every Gulf Coast community within 40 miles. Hardwood, luxury vinyl plank, tile, laminate, stair treads and floor repair.</p>
        <p><a href="{TEL_LINK}"><strong style="color:#fff;font-size:1.15rem">{PHONE}</strong></a><br><a href="mailto:{BUSINESS['email']}">{BUSINESS['email']}</a><br>{esc(BUSINESS['city'])}, {BUSINESS['state']} {BUSINESS['zip']} · by appointment</p>
      </div>
      <div><h4>Flooring services</h4><ul>{sv}<li><a href="/cost/">Cost guides</a></li></ul></div>
      <div><h4>Service areas</h4><ul>{c1}</ul></div>
      <div><h4>&nbsp;</h4><ul>{c2}<li><a href="/areas/">All service areas</a></li></ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="/about/">About us</a></li><li><a href="/blog/">Flooring answers</a></li><li><a href="/tools/">Calculators &amp; tools</a></li>
        <li><a href="/faq/">FAQ</a></li><li><a href="/warranty/">Workmanship warranty</a></li><li><a href="/financing/">Financing</a></li>
        <li><a href="/editorial-standards/">How we research &amp; price</a></li><li><a href="/contact/">Contact</a></li></ul></div>
    </div>
    <div class="fbottom"><span>© {year} {esc(BUSINESS['legal_name'])}. All rights reserved.</span><span><a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="/sitemap.xml">Sitemap</a></span></div>
  </div>
</footer>
<div class="sticky-call"><a href="{TEL_LINK}">Call {PHONE}</a><a href="#estimate">Free Estimate</a></div>
<script>{JS}</script>"""


# ============================================================================
# COMPONENTS
# ============================================================================
def crumbs(items):
    """items = [(name, url|None)] — Home is prepended."""
    parts = ['<a href="/">Home</a>']
    for n, u in items:
        parts.append(f'<a href="{u}">{esc(n)}</a>' if u else f'<span aria-current="page" style="margin:0;opacity:1">{esc(n)}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + "<span>›</span>".join(parts) + "</nav>"


def page_hero(h1, lede, trail, updated=None, eyebrow=None):
    eb = f'<span class="eyebrow on-dark">{esc(eyebrow)}</span>' if eyebrow else ""
    up = f'<p class="updated">Last reviewed {updated} · {NAME} editorial team</p>' if updated else ""
    return f"""<section class="page-hero on-dark"><div class="wrap">{crumbs(trail)}{eb}<h1>{h1}</h1><p class="lede">{lede}</p>{up}</div></section>"""


def capsule(text, label="Short answer"):
    return f'<div class="capsule"><div class="k">{esc(label)}</div><p>{text}</p></div>'


def faq_block(faqs):
    """faqs = [(q, a_html)] — first three open so answers are visible without JS."""
    out = []
    for i, (q, a) in enumerate(faqs):
        a_html = a if a.lstrip().startswith("<") else f"<p>{a}</p>"
        out.append(f'<details{" open" if i < 3 else ""}><summary>{esc(q)}</summary><div class="a">{a_html}</div></details>')
    return '<div class="faq">' + "".join(out) + "</div>"


def table(headers, rows, caption=None):
    th = "".join(f"<th scope=\"col\">{esc(h)}</th>" for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    cap = f"<caption>{caption}</caption>" if caption else ""
    return f'<div class="tbl-wrap"><table class="tbl">{cap}<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def picture(name, alt, w=960, h=720, lazy=True, cls="", sizes="(max-width:820px) 100vw, 560px"):
    """Responsive WebP written by build.py as /images/<name>-{480,960,1600}.webp (+ .jpg fallback)."""
    lz = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return (f'<picture><source type="image/webp" srcset="/images/{name}-480.webp 480w, /images/{name}-960.webp 960w, /images/{name}-1600.webp 1600w" sizes="{sizes}">'
            f'<img src="/images/{name}-960.jpg" alt="{esc(alt)}" width="{w}" height="{h}"{lz} class="{cls}"></picture>')


def web3_hidden(subject=None):
    subject = subject or f"New estimate request — {DOMAIN}"
    return (f'<input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">'
            f'<input type="hidden" name="subject" value="{esc(subject)}">'
            f'<input type="hidden" name="from_name" value="{NAME} website">'
            f'<input type="hidden" name="redirect" value="{SITE}/thanks/">'
            f'<input type="hidden" name="page" value="">'
            f'<input type="checkbox" name="botcheck" style="display:none" tabindex="-1" aria-hidden="true">')


def form_fields(city_names, preselect_city=None, preselect_service=None, idp="f"):
    co = "".join(f'<option{" selected" if n == preselect_city else ""}>{esc(n)}</option>' for n in city_names) + "<option>Other / not listed</option>"
    so = "".join(f'<option{" selected" if SERVICES[s]["name"] == preselect_service else ""}>{esc(SERVICES[s]["name"])}</option>' for s in SERVICE_ORDER) \
         + "<option>Not sure yet — need a recommendation</option>"
    return f"""<div class="fg">
<label for="{idp}-n">Name *<input id="{idp}-n" type="text" name="name" required autocomplete="name" placeholder="Your name"></label>
<label for="{idp}-p">Phone *<input id="{idp}-p" type="tel" name="phone" required autocomplete="tel" placeholder="(941) 000-0000"></label>
<label class="full" for="{idp}-e">Email<input id="{idp}-e" type="email" name="email" autocomplete="email" placeholder="your@email.com"></label>
<label for="{idp}-c">City<select id="{idp}-c" name="city">{co}</select></label>
<label for="{idp}-s">Project type<select id="{idp}-s" name="service">{so}</select></label>
<label class="full" for="{idp}-m">Tell us about the project<textarea id="{idp}-m" name="message" rows="3" placeholder="Square footage, rooms, timing, products you like…"></textarea></label>
<button type="submit" class="btn btn-wood">Get My Free Estimate →</button>
<p class="fnote">By sending this form you agree to be contacted about your project by phone, text or email. No spam, no list sharing.</p>
</div>"""


def lead_form(city_names, heading="Request your free flooring estimate", sub=None, preselect_city=None, preselect_service=None):
    sub = sub or "Tell us a little about the project. You get a reply within 24 hours, an in-home measure with samples, and a written, line-itemized quote."
    return f"""<section class="leadform" id="estimate"><div class="wrap"><div class="lf">
<div><span class="eyebrow">Free estimate · 24-hour reply</span><h2>{heading}</h2><p>{sub}</p>
<ul><li>Free in-home measure, samples brought to you</li><li>Moisture reading on the slab before any wood or vinyl quote</li><li>Written quote with material, labor, removal and trim on separate lines</li><li>Two-year written workmanship warranty</li></ul>
<p>Prefer to talk? <a href="{TEL_LINK}"><strong>{PHONE}</strong></a> · <a href="{SMS_LINK}">text us photos</a></p></div>
<div class="formcard"><p class="t">Get a free flooring estimate</p><p class="s">{NAME} · Sarasota, Manatee &amp; Charlotte counties</p>
<form method="POST" action="{WEB3FORMS_ENDPOINT}">{web3_hidden()}{form_fields(city_names, preselect_city, preselect_service, "lf")}</form></div>
</div></div></section>"""


def cta_band(headline=None, sub=None):
    headline = headline or "Ready for new floors? Free estimate within 24 hours."
    sub = sub or "Call or text and talk to the person who will measure your home. Free sample bring-outs across Sarasota, Bradenton, Lakewood Ranch, Venice and North Port."
    return f"""<section class="cta"><div class="wrap"><h2>{headline}</h2><p>{sub}</p><a class="tel" href="{TEL_LINK}">{PHONE}</a>
<div class="btn-row"><a class="btn btn-wood" href="{TEL_LINK}">Call now</a><a class="btn btn-ghost" href="{SMS_LINK}">Text us</a><a class="btn btn-ghost" href="#estimate">Online form</a></div></div></section>"""


def sources_block(sources):
    if not sources: return ""
    li = "".join(f'<li><a href="{esc(u)}" rel="noopener nofollow" target="_blank">{esc(t)}</a></li>' for t, u in sources)
    return f'<div class="sources"><strong>Sources</strong><ol>{li}</ol></div>'


# ============================================================================
# JSON-LD
# ============================================================================
ORG_ID = f"{SITE}/#business"

def _address():
    return {"@type": "PostalAddress", "addressLocality": BUSINESS["city"], "addressRegion": BUSINESS["state"],
            "postalCode": BUSINESS["zip"], "addressCountry": "US"}

def business_schema(area_names):
    """No AggregateRating / Review: the site carries no verified third-party reviews yet."""
    same = [u for u in (BUSINESS.get(k, "") for k in ("facebook", "instagram", "yelp", "houzz", "bbb", "angi", "thumbtack", "gbp")) if u]
    d = {"@context": "https://schema.org", "@type": ["HomeAndConstructionBusiness", "LocalBusiness"], "@id": ORG_ID,
         "name": NAME, "legalName": BUSINESS["legal_name"], "url": SITE + "/", "telephone": BUSINESS["phone"], "email": BUSINESS["email"],
         "image": f"{SITE}/images/og-default.jpg", "logo": f"{SITE}/images/favicon-512.png", "priceRange": "$$",
         "description": "Flooring installation company serving Sarasota, Manatee and Charlotte counties: hardwood, luxury vinyl plank, tile, laminate, stair treads and floor repair.",
         "address": _address(),
         "geo": {"@type": "GeoCoordinates", "latitude": float(BUSINESS["lat"]), "longitude": float(BUSINESS["lng"])},
         "areaServed": [{"@type": "City", "name": f"{n}, FL"} for n in area_names],
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": d_, "opens": o, "closes": c} for d_, o, c in BUSINESS["hours"]],
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Flooring services", "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@type": "Service", "name": SERVICES[s]["name"], "url": f"{SITE}/{s}/"}} for s in SERVICE_ORDER]}}
    if same: d["sameAs"] = same
    return d

def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": f"{SITE}/#website", "url": SITE + "/", "name": NAME,
            "inLanguage": "en-US", "publisher": {"@id": ORG_ID}}

def breadcrumb_schema(items):
    el = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (n, u) in enumerate(items, 2):
        e = {"@type": "ListItem", "position": i, "name": n}
        if u: e["item"] = SITE + u
        el.append(e)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": el}

def _strip(h):
    import re
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": _strip(a)}} for q, a in faqs]}

def service_schema(name, path, description, area_names):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "serviceType": name, "url": SITE + path,
            "description": description, "provider": {"@id": ORG_ID},
            "areaServed": [{"@type": "City", "name": f"{n}, FL"} for n in area_names]}

def article_schema(title, description, path, published, modified, image=None):
    return {"@context": "https://schema.org", "@type": "Article", "headline": title[:110], "description": description,
            "mainEntityOfPage": SITE + path, "datePublished": published, "dateModified": modified, "inLanguage": "en-US",
            "image": SITE + (image or "/images/og-default.jpg"),
            "author": {"@type": "Organization", "name": f"{NAME} editorial team", "url": f"{SITE}/editorial-standards/"},
            "publisher": {"@id": ORG_ID}}
