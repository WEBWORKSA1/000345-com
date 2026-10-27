# 000345.com — the square-corner toolkit

Free construction layout and estimating calculators built around the 3-4-5 rule, with a homeowner → contractor quote funnel, sponsorships, contests and reader support. Static site, hosted free on GitHub Pages.

- **Live (GitHub Pages):** https://webworksa1.github.io/000345-com/
- **Research & concept:** [docs/RESEARCH.md](docs/RESEARCH.md)
- **Phase-wise build prompts:** [docs/BUILD-PROMPTS.md](docs/BUILD-PROMPTS.md)

## What's inside
- 18 calculators (`/calculators/`): 3-4-5 squaring, right triangle, diagonal check, concrete slab, footings, roof pitch, rafters, stairs, deck boards, fence, tile, flooring, paint, drywall, gravel, square footage, board feet and brick
- 7 long-form guides (`/guides/`), plus a video library, contest, careers, pro sign-up, quotes, support and advertise pages
- About, contact, methodology, privacy, terms, disclaimer, trademark & copyright disclosure, and 404 pages
- `sitemap.xml`, `robots.txt`, `ads.txt` and a web manifest
- Google AdSense (`ca-pub-6620975821265271`) on every page, and an ownership notice linking to web.works/contact at the top of every page

## How it is served
GitHub Pages builds the site with Jekyll straight from the `main` branch:

| Path | Role |
|---|---|
| `_layouts/default.html` | Shared head, notice bar, header, footer, cookie notice and scripts |
| `_includes/lead.html` | The "get free quotes" lead block |
| `*.html`, `calculators/`, `guides/` | Page bodies, with front matter (title, description, canonical, schema) |
| `assets/` | CSS, JS (`calc.js` holds the calculator math, `main.js` the site behaviour) and the favicon |

`tools/` holds the original Python generator (`python3 tools/build.py`) that produced the page content. It is excluded from the Jekyll build.

## One-time owner setup
1. **Turn on Pages:** go to **Settings → Pages → Build and deployment → Source: Deploy from a branch → `main` / `(root)` → Save**. The site goes live at the URL above in 1–2 minutes.
2. **Forms:** forms are relayed by FormSubmit. The first submission sends an activation email to the site inbox. Click the confirmation link once, and all forms will deliver from then on.
3. **Custom domain:**
   - At your registrar, add A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153` and `185.199.111.153`, plus `CNAME www → webworksa1.github.io`.
   - In **Settings → Pages**, set the custom domain to `000345.com`, then enable **Enforce HTTPS**.
   - Google only reads `ads.txt` at the domain root, so this step is required before AdSense review.
4. **AdSense:** add the site and keep Auto ads on. Turn on Google's certified CMP for EEA/UK/Switzerland.
5. **Donations (optional):** add a hosted payment link (Stripe Payment Link, PayPal, Buy Me a Coffee) to the support page.
6. **Contest prizes:** set each month's prize values on `contests.html` before announcing a round.
7. **Social image (optional):** add a 1200×630 `assets/img/og-image.png`, and an `og:image` meta tag in `_layouts/default.html`.

The contact address is never written in plain text anywhere in this repository. It is stored as encoded character codes and assembled in the browser.

## Legal
000345.com is independent and not affiliated with any company, security, product or registration that uses the number 000345. See `legal.html`. © 000345.com.
