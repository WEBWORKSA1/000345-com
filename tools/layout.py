"""Shared page chrome for the 000345 static site generator."""
import json, html

SITE = {
    "name": "000345",
    "tagline": "Start at zero. Square it with 3-4-5.",
    "domain": "https://000345.com",
    "adsense": "ca-pub-6620975821265271",
    "notice_url": "https://web.works/contact",
    "updated": "October 2026",
    # Optional: paste a hosted payment link (PayPal, Stripe Payment Link, Buy Me a Coffee) to show a direct "Give now" button.
    "donate_url": "",
    # Optional: AdSense display ad slot IDs. Empty = Auto ads only (recommended until approval).
    "ad_slot_in_article": "",
    "ad_slot_display": "",
}

NAV = [
    ("calculators/index.html", "Calculators"),
    ("guides/index.html", "Guides"),
    ("videos.html", "Videos"),
    ("contests.html", "Contests"),
    ("pros.html", "For Pros"),
    ("support.html", "Support"),
]

LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="6" fill="#F5B800"/>'
        '<path d="M9 31V9M9 31H31M9 31L31 9" stroke="#1D2329" stroke-width="3.2" stroke-linecap="round" fill="none"/>'
        '<path d="M9 25h6v6" stroke="#2357C6" stroke-width="2.4" fill="none"/></svg>')

def esc(s):
    return html.escape(s, quote=True)

def ad_unit(kind="display"):
    slot = SITE["ad_slot_in_article"] if kind == "in-article" else SITE["ad_slot_display"]
    if not slot:
        return ""
    fmt = 'data-ad-layout="in-article" data-ad-format="fluid"' if kind == "in-article" else 'data-ad-format="auto" data-full-width-responsive="true"'
    return (f'<div class="ad-wrap"><span class="ad-label">Advertisement</span>'
            f'<ins class="adsbygoogle" style="display:block" data-ad-client="{SITE["adsense"]}" data-ad-slot="{slot}" {fmt}></ins>'
            f'<script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script></div>')

def page(path, title, description, body, depth=0, schema=None, current=None, extra_head="", scripts=("main",), og_type="website"):
    p = "../" * depth
    canonical = SITE["domain"] + "/" + ("" if path == "index.html" else path.replace("index.html", ""))
    nav = "".join(
        f'<a href="{p}{href}"{" aria-current=\"page\"" if current == href else ""}>{label}</a>' for href, label in NAV
    )
    ld = [{
        "@context": "https://schema.org", "@type": "WebSite", "name": SITE["name"], "url": SITE["domain"] + "/",
        "description": "Free construction layout and estimating calculators built around the 3-4-5 rule.",
    }]
    if schema:
        ld += schema if isinstance(schema, list) else [schema]
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    js = "".join(f'<script src="{p}assets/js/{s}.js" defer></script>' for s in scripts)
    full_title = title if title.endswith("000345") else f"{title} | 000345"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="google-adsense-account" content="{SITE['adsense']}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="000345">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE['domain']}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F5B800">
<link rel="icon" href="{p}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{p}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/style.css">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>
{ld_html}
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="notice" role="region" aria-label="Site ownership notice"><div class="wrap"><span>Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership:</span> <a href="{SITE['notice_url']}" rel="noopener" target="_blank">web.works/contact</a></div></div>
<div class="tape" aria-hidden="true"></div>
<header class="site-head">
 <div class="wrap">
  <a class="brand" href="{p}index.html" aria-label="000345 home">{LOGO}<span><b>000345</b><small>Square-corner toolkit</small></span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn btn-tape btn-sm" href="{p}quotes.html">Get free quotes</a><button class="theme-btn" aria-label="Switch light or dark theme" title="Theme">◐</button></nav>
 </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-foot">
 <div class="wrap">
  <div class="foot-grid">
   <div><a class="brand" href="{p}index.html" style="color:#fff">{LOGO}<span><b>000345</b></span></a>
    <p style="margin-top:12px">Free layout and estimating calculators for builders and DIYers. Start at zero, square it with 3-4-5, and build it right.</p>
    <p><a href="#" data-mail="General inquiry — 000345.com">Email the team</a></p></div>
   <div><h4>Tools</h4><ul>
    <li><a href="{p}calculators/3-4-5-squaring-calculator.html">3-4-5 squaring</a></li>
    <li><a href="{p}calculators/concrete-slab-calculator.html">Concrete slab</a></li>
    <li><a href="{p}calculators/stair-calculator.html">Stairs</a></li>
    <li><a href="{p}calculators/roof-pitch-calculator.html">Roof pitch</a></li>
    <li><a href="{p}calculators/index.html">All calculators</a></li></ul></div>
   <div><h4>Learn</h4><ul>
    <li><a href="{p}guides/index.html">Guides</a></li>
    <li><a href="{p}videos.html">Video library</a></li>
    <li><a href="{p}methodology.html">How we calculate</a></li>
    <li><a href="{p}contests.html">Square Corner Challenge</a></li></ul></div>
   <div><h4>Work with us</h4><ul>
    <li><a href="{p}quotes.html">Get free quotes</a></li>
    <li><a href="{p}pros.html">Join as a pro</a></li>
    <li><a href="{p}advertise.html">Advertise &amp; sponsor</a></li>
    <li><a href="{p}careers.html">Careers</a></li>
    <li><a href="{p}support.html">Support the project</a></li></ul></div>
   <div><h4>Company</h4><ul>
    <li><a href="{p}about.html">About</a></li>
    <li><a href="{p}contact.html">Contact</a></li>
    <li><a href="{p}privacy.html">Privacy</a></li>
    <li><a href="{p}terms.html">Terms</a></li>
    <li><a href="{p}disclaimer.html">Disclaimer</a></li>
    <li><a href="{p}legal.html">Trademark &amp; copyright</a></li></ul></div>
  </div>
  <div class="foot-legal">© <span data-year>2026</span> 000345.com. All rights reserved. Calculations are estimates for planning; confirm structural work with local code and a qualified professional. 000345 is an independent site and is not affiliated with any company, security, product or registration that shares this number. <a href="{p}legal.html">Full disclosure</a>.</div>
 </div>
</footer>
<div class="cookie" role="dialog" aria-live="polite" aria-label="Cookie choices">
 <strong>Cookies on 000345</strong>
 <p class="muted" style="margin:.3em 0 0">We use cookies to keep your settings and to show ads through Google AdSense, which may personalise ads. <a href="{p}privacy.html">Privacy policy</a>.</p>
 <div class="row"><button class="btn btn-tape btn-sm" data-cookie="all">Accept all</button><button class="btn btn-ghost btn-sm" data-cookie="essential">Non-personalised ads only</button></div>
</div>
{js}
</body>
</html>
"""

def crumbs(items, depth):
    p = "../" * depth
    parts = [f'<a href="{p}index.html">Home</a>']
    for href, label in items[:-1]:
        parts.append(f'<a href="{p}{href}">{label}</a>')
    parts.append(f'<span aria-current="page">{items[-1][1]}</span>')
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": lab, "item": SITE["domain"] + "/" + href}
        for i, (href, lab) in enumerate([("", "Home")] + items)]}
    return '<nav class="crumbs wrap" aria-label="Breadcrumb">' + " / ".join(parts) + "</nav>", schema

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a.replace("<", " <")).strip()}}
        for q, a in faqs]}

def faq_html(faqs):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

def lead_block(depth, project="", heading="Ready to build? Get up to 3 free quotes from local pros."):
    p = "../" * depth
    q = f"?project={project}" if project else ""
    return f"""<div class="lead">
 <div><h2>{heading}</h2>
  <p>Tell us about the project in about a minute. We pass it to up to three vetted local contractors who cover your area.</p>
  <ul><li>Free for homeowners, no obligation to hire</li><li>Your details go only to the pros matched to your job</li><li>Bring your calculator numbers — pros quote faster with real measurements</li></ul></div>
 <div class="formcard"><h3>Start with your postal code</h3>
  <form action="{p}quotes.html" method="get">
   <input type="hidden" name="project" value="{project}">
   <div class="field"><label for="zip-{project or 'g'}">ZIP / postal code</label><input id="zip-{project or 'g'}" name="zip" required pattern="[A-Za-z0-9 \\-]{{3,10}}" autocomplete="postal-code" placeholder="e.g. 90210 or H2X 1Y4"></div>
   <button class="btn btn-tape" type="submit" style="width:100%">Get free quotes</button>
   <p style="font-size:.85rem;margin:.8em 0 0">Takes about 60 seconds. No spam.</p>
  </form></div>
</div>"""

def video_card(vid, title, channel):
    return (f'<article class="video"><div class="frame"><button data-yt="{vid}" aria-label="Play: {esc(title)}"><span>▶ Play video</span></button></div>'
            f'<div class="meta"><h3>{esc(title)}</h3><p class="muted" style="margin:0">{esc(channel)} · YouTube</p></div></article>')
