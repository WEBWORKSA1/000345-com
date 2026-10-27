# 000345.com — Phase-wise Build Prompts

Copy each prompt into an AI coding assistant in order. Each phase ends with a checkable result. This repository is the output of running Phases 1–6; Phases 7–8 are the growth roadmap.

Global constraints to paste at the top of every session:

```
Project: 000345.com — "the square-corner toolkit": free construction layout & estimating calculators built around the 3-4-5 rule, monetized by Google AdSense (ca-pub-6620975821265271), contractor lead generation, sponsorships and reader support.
Hosting: GitHub Pages free plan (repo WEBWORKSA1/000345-com). Static HTML/CSS/vanilla JS only. Every internal link must be RELATIVE so the site works both at the github.io project path and at the custom domain root.
Every page: AdSense script in <head> exactly as:
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>
Every page, very top: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership" linking to https://web.works/contact.
The site's single contact email must NEVER appear in markup, source files, README or docs. Store it only as obfuscated character codes; assemble it in JavaScript at click/submit time for mailto links and the form relay endpoint.
No trademark use of "000345" as anyone else's mark; include a trademark/copyright disclosure page.
Accessibility: semantic HTML, labels on every input, visible focus, prefers-reduced-motion, dark mode, 16px gutters on mobile.
```

---

## Phase 1 — Research & positioning
```
Research what the number "000345" means in commerce, business, AI, the economy and culture. Identify every real-world use (stock codes, product codes, math/construction). Pick the single meaning with the largest evergreen search demand and commercial intent. Then audit at least 25 leading sites in that niche (calculators, home-improvement lead marketplaces, DIY publishers, donation and contest platforms). For each, record: features, lead-capture pattern, content types, design notes, monetization. Output: a ranked list of 25 features to adopt, the best-converting lead form pattern, design conventions, AdSense approval content requirements, and 8–12 verified YouTube video IDs for the niche. Write it to docs/RESEARCH.md with a revenue model and sources.
```
**Done when:** docs/RESEARCH.md exists with the concept decision ("start at zero, square it with 3-4-5") and the feature list.

## Phase 2 — Design system & page chrome
```
Create assets/css/style.css with a distinctive construction-site identity: concrete grey background (#EDEFF0), graphite ink (#1D2329), tape-measure yellow (#F5B800) for primary actions, chalk-line blue (#2357C6) for links/diagonals, marker red (#C8322B) for errors, green (#1E7A46) for "square". Type: Barlow Condensed (display) + Source Sans 3 (body). A tape-measure tick strip under the top notice is the signature device. Build a Python generator (tools/layout.py) that renders shared <head> (SEO meta, Open Graph, canonical, JSON-LD, AdSense script, google-adsense-account meta), the ownership notice strip, sticky header with mobile menu and theme toggle, footer with full link map and a short legal line, and a cookie notice offering "Accept all" or "Non-personalised ads only" (sets requestNonPersonalizedAds). Include an optional ad_unit() helper that renders manual AdSense units only when slot IDs are configured.
```
**Done when:** a blank page renders correctly at 390px and 1280px in light and dark mode.

## Phase 3 — Calculator engine + 18 calculators
```
Write assets/js/calc.js: a dependency-free engine where each .calc-box[data-calc] maps to a pure function(values, system) returning result rows and notes. Support imperial/metric toggle (persisted in localStorage) that swaps unit labels and defaults. Format lengths as decimal feet and feet-inches to the nearest 1/16". Build these calculators: 3-4-5 squaring (with measured-diagonal checker giving real angle, open/closed verdict and offset), right triangle, rectangle diagonal check, concrete slab, post-hole/footing concrete, roof pitch, rafter length, stairs (with code and comfort checks), deck boards, fence, tile, flooring, paint, drywall, gravel/mulch/soil, square footage, board feet, brick. Also an interactive SVG hero on the home page that draws the triangle live and shows the verdict.
For each calculator write original content (tools/calcs.py): intro, how to use, formula, worked example (verified against the engine), tips/tables, 3–4 FAQs, related tools, matching YouTube video, and a project tag used to prefill the quote form. Render each as /calculators/<slug>.html with WebApplication + FAQPage + BreadcrumbList schema, byline and last-reviewed date, sticky sidebar (related tools, quote CTA, support CTA) and a lead block.
```
**Done when:** every calculator produces results on load in both unit systems with no console errors, and worked examples match the engine output.

## Phase 4 — Lead generation & money pages
```
Build quotes.html: a 4-step form (project type tiles + ZIP → size/description → timeline/budget/ownership → name/email/phone/contact preference + explicit consent checkbox for sharing with up to 3 matched pros). Progress bar, Back/Continue, per-step validation, prefill from ?project= and ?zip=. Add a ZIP-first lead block that appears on the home page, every calculator and every guide.
Build pros.html (contractor application: business, trade, service area, licence, monthly volume, insurance attestation), support.html (donation presets $5/$15/$50/$150, frequency, purpose = operations/new tools/contest prizes/promotion/hiring, optional direct payment link from config, sponsor tiers, supporter wall), contests.html (monthly Square Corner Challenge: entry form, prizes table, 100-point judging rubric, official-rules summary with no-purchase-necessary and skill-testing question), careers.html (6 roles + application form), advertise.html (sponsorship, exclusive leads, contest sponsor, content partnership, licensing, domain acquisition + media-kit form).
All forms POST as JSON to the FormSubmit AJAX relay; the endpoint address is built in JS from obfuscated char codes. Include honeypot, custom subject per form, success and error messages, and a GA4-ready generate_lead event hook.
```
**Done when:** each form validates, shows success/error states, and no email address exists anywhere in the repository.

## Phase 5 — Content depth for AdSense approval
```
Write 7 long-form original guides (tools/guides.py): the complete 3-4-5 rule guide, foundation layout with batter boards, how to square a deck, layout tolerances (with an error-growth table), Pythagorean triples for builders, how much concrete to order, how to hire a contractor. Add Article + FAQPage schema. Build a video library page (click-to-load youtube-nocookie embeds, grouped by topic, creator credited). Add About, Contact, How We Calculate (methodology), Privacy (AdSense cookie disclosure with Google opt-out links, form handling, rights, retention), Terms, Disclaimer (structural/code limits, ad disclosure), Trademark & Copyright disclosure (non-affiliation with any security/product using 000345; third-party marks; embedded video ownership; complaint process), and a 404 page that works at both base paths.
```
**Done when:** 40+ indexable pages, every page has a unique title/description, and the policy pages are linked from every footer.

## Phase 6 — SEO, platform files, QA, deploy
```
Generate sitemap.xml, robots.txt (allow Mediapartners-Google), ads.txt ("google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0"), site.webmanifest, favicon.svg, apple-touch-icon.png, 1200×630 og.png and .nojekyll. Run automated QA: every page contains the AdSense script and ownership notice; zero broken relative links; zero occurrences of the email; every calculator returns results; headless screenshots at 390px and 1280px. Push to WEBWORKSA1/000345-com (main) with a GitHub Actions workflow that builds the site and deploys it to GitHub Pages on every push.
```
**Done when:** the site is live at https://webworksa1.github.io/000345-com/ and passes the QA script.

## Phase 7 — Custom domain & AdSense application (owner actions)
```
Point 000345.com to GitHub Pages: A records 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 and a CNAME for www → webworksa1.github.io. Set the custom domain in Settings → Pages and enable Enforce HTTPS. Confirm ads.txt resolves at https://000345.com/ads.txt. Add the site in AdSense, keep Auto ads on, and enable Google's certified CMP for EEA/UK/CH visitors. Submit sitemap.xml in Google Search Console. After approval, create in-article and display units and paste their slot IDs into SITE in tools/layout.py.
```

## Phase 8 — Growth roadmap
```
1. Contractor network: sign 3–5 pros per launch metro before buying traffic; document lead pricing and routing.
2. Programmatic city pages ("concrete slab cost in <city>") using real supplier price data only.
3. Printable full-scale stair-stringer and rafter templates (PDF export) — strongest backlink magnet in the niche.
4. Embeddable calculator widget with attribution link.
5. Newsletter with a free "Layout checklist" PDF lead magnet.
6. Phone verification on quote requests once volume justifies an SMS provider.
7. Spanish and French versions of the top 6 calculators.
8. Monthly contest gallery and supporter wall populated from real entries.
```
