"""Build the 000345 static site into the repository root.  Run:  python3 tools/build.py"""
import os, json, datetime
from layout import SITE, page, crumbs, faq_schema, faq_html, lead_block, video_card, ad_unit, esc
from calcs import CALCS
from guides import GUIDES
import pages as P

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()
written = []

def out(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    written.append(path)

def inputs_html(c):
    html = ""
    for spec in c["inputs"]:
        if spec[0] == "select":
            _, name, label, opts, help_ = spec
            o = "".join(f'<option value="{v}">{t}</option>' for v, t in opts)
            html += f'<div class="field"><label for="{c["fn"]}-{name}">{label}</label><select id="{c["fn"]}-{name}" name="{name}">{o}</select></div>'
        else:
            name, label, ui, um, di, dm, help_ = spec
            hid = f'{c["fn"]}-{name}-help'
            hattr = f' aria-describedby="{hid}"' if help_ else ""
            htxt = f'<small id="{hid}" class="muted" style="display:block;font-size:.82rem;margin-top:3px">{help_}</small>' if help_ else ""
            html += (f'<div class="field"><label for="{c["fn"]}-{name}">{label}<span class="u"> ({ui})</span></label>'
                     f'<input id="{c["fn"]}-{name}" name="{name}" type="number" inputmode="decimal" step="any" min="0" value="{di}" '
                     f'data-imp="{di}" data-met="{dm}" data-u-imp="{ui}" data-u-met="{um}"{hattr}>{htxt}</div>')
    return html

by_slug = {c["slug"]: c for c in CALCS}

# ---------- calculator pages ----------
for c in CALCS:
    path = f'calculators/{c["slug"]}.html'
    cr, cs = crumbs([("calculators/", "Calculators"), (path, c["title"])], 1)
    rel = "".join(f'<li><a href="{s}.html">{by_slug[s]["title"]}</a></li>' for s in c["related"])
    vid = ""
    if c.get("video"):
        v = next((x for x in P.VIDEOS if x[0] == c["video"]), None)
        if v:
            vid = f'<h2>Watch: how it is done</h2><div class="video-grid" style="grid-template-columns:1fr">{video_card(v[0], v[1], v[2])}</div><p class="muted" style="font-size:.9rem">Video by {esc(v[2])} on YouTube. More in our <a href="../videos.html">video library</a>.</p>'
    app = {"@context": "https://schema.org", "@type": "WebApplication", "name": c["title"], "applicationCategory": "UtilitiesApplication",
           "operatingSystem": "Any (web browser)", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
           "url": SITE["domain"] + "/" + path, "description": c["desc"]}
    body = f"""{cr}
<div class="page-head" style="border-bottom:0;background:transparent;padding-bottom:6px"><div class="wrap"><h1>{c["title"]}</h1><p>{c["short"]}</p></div></div>
<div class="wrap"><div class="calc-layout">
 <article>
  <div class="calc-box" data-calc="{c["fn"]}">
   <div class="unit-switch" role="group" aria-label="Units"><button type="button" data-sys="imp" aria-pressed="true">Imperial (ft, in)</button><button type="button" data-sys="met" aria-pressed="false">Metric (m, cm)</button></div>
   <div class="inputs">{inputs_html(c)}</div>
   <div class="results" aria-live="polite"></div>
   <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:14px"><button type="button" class="btn btn-ghost btn-sm" data-reset>Reset</button><button type="button" class="btn btn-ghost btn-sm" data-print>Print</button><button type="button" class="btn btn-ghost btn-sm" data-share>Share</button><a class="btn btn-tape btn-sm" href="../quotes.html?project={c["project"]}">Get quotes for this job</a></div>
  </div>
  <p class="byline">By the 000345 editorial team · Last reviewed {SITE["updated"]} · <a href="../methodology.html">How we calculate</a></p>
  {ad_unit("in-article")}
  <div class="prose">{c["body"]}
  {vid}
  <h2>Frequently asked questions</h2>{faq_html(c["faqs"])}
  <p class="muted" style="margin-top:20px;font-size:.92rem">Results are planning estimates. For structural work, confirm requirements with your local building authority and a qualified professional. See our <a href="../disclaimer.html">disclaimer</a>.</p>
  </div>
 </article>
 <aside><div class="sticky-aside">
  <div class="aside-box"><h3>Related calculators</h3><ul>{rel}</ul></div>
  <div class="aside-box" style="border-top:6px solid var(--tape)"><h3>Need a pro for this?</h3><p>Get up to three free quotes from local contractors. Bring the numbers from this calculator.</p><a class="btn btn-tape btn-sm" href="../quotes.html?project={c["project"]}">Get free quotes</a></div>
  <div class="aside-box"><h3>Keep these tools free</h3><p style="margin-bottom:10px">Reader support pays for new calculators and contest prizes.</p><a href="../support.html">Support 000345</a></div>
 </div></aside>
</div>
<div style="margin-top:30px">{lead_block(1, c["project"])}</div>
{ad_unit()}
</div>"""
    out(path, page(path, c["title"] + " (Free, ft & m)", c["desc"], body, depth=1, schema=[app, faq_schema(c["faqs"]), cs],
                   current="calculators/index.html", scripts=("main", "calc")))

# ---------- guides ----------
for g in GUIDES:
    path = f'guides/{g["slug"]}.html'
    cr, cs = crumbs([("guides/", "Guides"), (path, g["title"])], 1)
    art = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
           "author": {"@type": "Organization", "name": "000345 editorial team"}, "publisher": {"@type": "Organization", "name": "000345"},
           "dateModified": TODAY, "mainEntityOfPage": SITE["domain"] + "/" + path}
    vid = ""
    if g.get("video"):
        v = g["video"]
        vid = f'<h2>Watch</h2><div class="video-grid" style="grid-template-columns:1fr">{video_card(*v)}</div>'
    others = "".join(f'<li><a href="{x["slug"]}.html">{x["title"]}</a></li>' for x in GUIDES if x is not g)
    body = f"""{cr}
<div class="wrap"><div class="calc-layout" style="margin-top:14px">
 <article class="prose">
  <h1>{g["title"]}</h1>
  <p class="byline">By the 000345 editorial team · Updated {SITE["updated"]}</p>
  {g["body"]}
  {ad_unit("in-article")}
  {vid}
  <h2>Questions</h2>{faq_html(g["faqs"])}
 </article>
 <aside><div class="sticky-aside">
  <div class="aside-box" style="border-top:6px solid var(--tape)"><h3>Try the calculator</h3><p>Get the exact diagonal for any corner, or check one you've already set.</p><a class="btn btn-tape btn-sm" href="../calculators/3-4-5-squaring-calculator.html">3-4-5 calculator</a></div>
  <div class="aside-box"><h3>More guides</h3><ul>{others}</ul></div>
 </div></aside>
</div>
<div style="margin-top:34px">{lead_block(1)}</div></div>"""
    out(path, page(path, g["title"], g["desc"], body, depth=1, schema=[art, faq_schema(g["faqs"]), cs], current="guides/index.html", og_type="article"))

# ---------- index pages ----------
org = {"@context": "https://schema.org", "@type": "Organization", "name": "000345", "url": SITE["domain"] + "/",
       "logo": SITE["domain"] + "/assets/img/apple-touch-icon.png"}
out("index.html", page("index.html", "000345 — Free 3-4-5 Squaring & Construction Calculators",
    "Square any corner with the 3-4-5 rule and estimate concrete, stairs, roofs, decks, tile and more. Free construction calculators in feet and metres, plus free quotes from local pros.",
    P.home(CALCS, GUIDES), schema=[org], scripts=("main", "calc")))
out("calculators/index.html", page("calculators/index.html", "Construction Calculators", f"{len(CALCS)} free construction calculators: 3-4-5 squaring, concrete, stairs, roof pitch, rafters, decks, fences, tile, paint, drywall and more.",
    P.calc_index(CALCS), depth=1, current="calculators/index.html"))
out("guides/index.html", page("guides/index.html", "Layout & Estimating Guides", "Practical guides to the 3-4-5 rule, foundation layout, squaring decks, tolerances, Pythagorean triples, ordering concrete and hiring contractors.",
    P.guide_index(GUIDES), depth=1, current="guides/index.html"))

simple = [
 ("videos.html", "Construction How-To Video Library", "Hand-picked how-to videos on the 3-4-5 rule, batter boards, deck squaring, roof pitch, stair stringers and pouring concrete.", P.videos(), "videos.html"),
 ("quotes.html", "Get Free Contractor Quotes", "Request up to three free quotes from local contractors for decks, concrete, foundations, roofing, stairs, fences, flooring and more.", P.quotes(), None),
 ("pros.html", "Contractor Leads — Join as a Pro", "Receive qualified local leads from homeowners who have already measured their projects. Choose your trades, area and monthly cap.", P.pros(), "pros.html"),
 ("support.html", "Support 000345", "Help keep free construction calculators free. Support operations, new tools, contest prizes and promotion, or become a sponsor.", P.support(), "support.html"),
 ("contests.html", "The Square Corner Challenge — Monthly Build Contest", "Enter the monthly Square Corner Challenge: share a project you laid out square and compete for tool prizes. Official rules inside.", P.contests(), "contests.html"),
 ("careers.html", "Careers", "Join 000345: trade writers, technical reviewers, video creators, developers and partnership roles.", P.careers(), None),
 ("advertise.html", "Advertise, Sponsor & Partner", "Sponsor calculators, contests and videos, buy exclusive local leads, or license our tools. Request the 000345 media kit.", P.advertise(), None),
 ("about.html", "About", "About 000345, the independent toolkit for squaring, measuring and estimating construction work.", P.about(), None),
 ("contact.html", "Contact", "Contact the 000345 team about calculators, corrections, partnerships, advertising or the domain.", P.contact(), None),
 ("methodology.html", "How We Calculate", "The formulas, assumptions, rounding and review process behind 000345 calculators.", P.methodology(), None),
 ("privacy.html", "Privacy Policy", "How 000345 handles form submissions, cookies, Google AdSense advertising and your privacy rights.", P.privacy(), None),
 ("terms.html", "Terms of Use", "Terms of use for 000345.com calculators, guides and contractor matching.", P.terms(), None),
 ("disclaimer.html", "Disclaimer", "Important limits of 000345 calculators and guides, plus advertising disclosure.", P.disclaimer(), None),
 ("legal.html", "Trademark & Copyright Disclosure", "000345.com is independent and not affiliated with any company, security or product using the number 000345. Trademark and copyright notice.", P.legal(), None),
]
for path, title, desc, body, cur in simple:
    out(path, page(path, title, desc, body, current=cur))

base_js = ('<script>(function(){var p=location.pathname.indexOf("/000345-com/")===0?"/000345-com/":"/";'
           'document.write(\'<base href="\'+p+\'">\');})();</script>')
html404 = page("404.html", "Page not found", "This page could not be found.", P.notfound(), extra_head="")
html404 = html404.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + base_js, 1).replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
out("404.html", html404)

# ---------- main.js with obfuscated contact address ----------
# Contact address stored only as shifted, reversed char codes (decoded in the browser at click/submit time).
codes = [116, 118, 106, 53, 115, 112, 104, 116, 110, 71, 56, 104, 122, 114, 121, 118, 126, 105, 108, 126]
with open(os.path.join(ROOT, "tools/src/main.js"), encoding="utf-8") as f:
    js = f.read().replace("__EM__", json.dumps(codes))
out("assets/js/main.js", js)

# ---------- SEO + platform files ----------
urls = [p for p in written if p.endswith(".html") and p != "404.html"]
prio = lambda p: "1.0" if p == "index.html" else ("0.9" if p.startswith("calculators/") else "0.7")
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f'  <url><loc>{SITE["domain"]}/{"" if p=="index.html" else p.replace("index.html","")}</loc><lastmod>{TODAY}</lastmod><priority>{prio(p)}</priority></url>\n' for p in urls) + "</urlset>\n"
out("sitemap.xml", sm)
out("robots.txt", f"User-agent: *\nAllow: /\n\nUser-agent: Mediapartners-Google\nAllow: /\n\nSitemap: {SITE['domain']}/sitemap.xml\n")
out("ads.txt", "google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n")
out(".nojekyll", "")
out("site.webmanifest", json.dumps({"name": "000345 — Square-corner toolkit", "short_name": "000345", "start_url": "./index.html", "display": "standalone",
    "background_color": "#EDEFF0", "theme_color": "#F5B800", "icons": [{"src": "assets/img/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"},
    {"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=1))
out("assets/img/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="6" fill="#F5B800"/><path d="M9 31V9M9 31H31M9 31L31 9" stroke="#1D2329" stroke-width="3.2" stroke-linecap="round" fill="none"/><path d="M9 25h6v6" stroke="#2357C6" stroke-width="2.4" fill="none"/></svg>')

print(f"Built {len(written)} files; {len(urls)} indexable pages.")
