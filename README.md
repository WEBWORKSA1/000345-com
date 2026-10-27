# 000345.com — the square-corner toolkit

Free construction layout and estimating calculators built around the 3-4-5 rule, with a homeowner → contractor quote funnel, sponsorships, contests and reader support. Static site, hosted free on GitHub Pages.

- **Live (GitHub Pages):** https://webworksa1.github.io/000345-com/
- **Research & concept:** [docs/RESEARCH.md](docs/RESEARCH.md)
- **Phase-wise build prompts:** [docs/BUILD-PROMPTS.md](docs/BUILD-PROMPTS.md)

## What's inside
- 18 calculators (`/calculators/`) — 3-4-5 squaring, right triangle, diagonal check, concrete slab, footings, roof pitch, rafters, stairs, deck boards, fence, tile, flooring, paint, drywall, gravel, square footage, board feet, brick
- 7 long-form guides (`/guides/`), video library, contest, careers, pro sign-up, quotes, support, advertise
- About, contact, methodology, privacy, terms, disclaimer, trademark & copyright disclosure, 404
- `sitemap.xml`, `robots.txt`, `ads.txt`, web manifest, Open Graph image
- Google AdSense (`ca-pub-6620975821265271`) on every page; ownership notice linking to web.works/contact at the top of every page

## How the site is built
HTML pages are generated from Python sources in `tools/`. On every push to `main`, the GitHub Actions workflow (`.github/workflows/build-deploy.yml`) generates the images, builds all pages, commits the output back to `main`, and deploys to GitHub Pages.

To build locally:

```
pip install pillow
python3 tools/images.py
python3 tools/build.py
```

| File | Controls |
|---|---|
| `tools/layout.py` | Head, header, footer, cookie notice, `SITE` config (donation link, ad slot IDs) |
| `tools/calcs.py` | Calculator inputs and page content |
| `tools/guides.py` | Guide articles |
| `tools/pages.py` | Home, quotes, pros, support, contests, careers, advertise, policies, video list |
| `assets/js/calc.js` | Calculator math |
| `tools/src/main.js` | Site behaviour (built into `assets/js/main.js`) |
| `assets/css/style.css` | Design system |

## One-time owner setup
1. **GitHub Pages:** Settings → Pages → Source: **GitHub Actions**. Then re-run the latest "Build and deploy" workflow (Actions tab) if its deploy step ran before Pages was enabled.
2. **Forms:** forms are relayed by FormSubmit. The first submission sends an activation email to the site inbox — click the confirmation link once, then all forms deliver.
3. **Custom domain:** at your registrar add A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` and `CNAME www → webworksa1.github.io`. Then in **Settings → Pages** set the custom domain to `000345.com` and enable **Enforce HTTPS**. `ads.txt` is only read by Google at the domain root, so this step is required before AdSense review.
4. **AdSense:** add the site, keep Auto ads on, and turn on Google's certified CMP for EEA/UK/Switzerland. After approval, paste display/in-article slot IDs into `SITE` in `tools/layout.py`.
5. **Donations:** optional — paste a hosted payment link (Stripe Payment Link, PayPal, Buy Me a Coffee) into `SITE["donate_url"]` to show a direct "Give now" button.
6. **Contest prizes:** set each month's prize values on the contest page (`tools/pages.py`) before announcing a round.

The contact address is never written in plain text anywhere in this repository; it is stored as encoded character codes and assembled in the browser.

## Legal
000345.com is independent and not affiliated with any company, security, product or registration that uses the number 000345. See `legal.html`. © 000345.com.
