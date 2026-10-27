"""Bodies for the non-calculator pages."""
from layout import SITE, lead_block, video_card, faq_html

VIDEOS = [
 ("b-Wp9hkxW54", "3,4,5 rule - square up a building easily", "tecmath", "Squaring"),
 ("asjvSJBqFUw", "How To Use The 3-4-5 Rule To Make A Square", "Bunnings Warehouse", "Squaring"),
 ("A2ahtESv6kg", "How To Make Something Square (3 4 5 Triangle Method)", "Davids Diy Reviews", "Squaring"),
 ("8m-G9qrDpng", "How To Layout like a PRO with String and Batter Boards", "RR Buildings", "Foundations"),
 ("eOj-Fv0tSgI", "Using Batterboards for Laying out Building Foundations", "Creative Education", "Foundations"),
 ("jC7FDqhoKXM", "Square up a deck or wall using the 3 4 5 Rule", "Contractor John", "Decks"),
 ("C8mDz-5dI-A", "How To Build A Deck: How To Square Your Deck", "Colorado Custom Covers & Decks", "Decks"),
 ("yb8mIvNGbgQ", "How to Calculate Roof Pitch", "Digital Roofing Innovations", "Roofing"),
 ("oTvPF4YesjY", "How to Determine the Pitch of a Roof", "seejanedrill", "Roofing"),
 ("tkxWaj57TEA", "Framing Square Setup for Stair Stringer Layout", "stairbuilding", "Stairs"),
 ("GYfRFOBgZsU", "How to Cut Stair Stringers Step by Step", "Whitehead Woodworks", "Stairs"),
 ("QDKLkD4uDFE", "Learn how to pour a concrete slab - DIY with MARSHALLTOWN", "MARSHALLTOWN", "Concrete"),
 ("k1XFWNT7pAM", "How to Pour a Concrete Slab for Beginners DIY", "Odell Complete Concrete", "Concrete"),
 ("pbf4lcJhIfI", "Pythagorean Theorem - Basic Introduction", "The Organic Chemistry Tutor", "Math"),
]

def hp(name="_honey"):
    return f'<div class="hp" aria-hidden="true"><label>Leave empty<input type="text" name="{name}" tabindex="-1" autocomplete="off"></label></div>'

def msg():
    return '<div class="form-msg" role="status" aria-live="polite"></div>'

CONSENT = ('<label class="check"><input type="checkbox" name="consent" value="yes" required> '
           'I agree that 000345 may share these details with up to three matched contractors, who may contact me by phone, text or email about this project. Consent is not a condition of any purchase. I can withdraw at any time.</label>')

def home(calcs, guides):
    feat = ["3-4-5-squaring-calculator", "concrete-slab-calculator", "stair-calculator", "roof-pitch-calculator", "deck-board-calculator", "rectangle-diagonal-check"]
    by = {c["slug"]: c for c in calcs}
    items = "".join(f'<a href="calculators/{s}.html"><span class="tag">{by[s]["cat"]}</span><h3>{by[s]["title"]}</h3><p>{by[s]["short"]}</p></a>' for s in feat)
    gl = "".join(f'<li><a href="guides/{g["slug"]}.html">{g["title"]}</a><p>{g["summary"]}</p></li>' for g in guides[:4])
    vids = "".join(video_card(v, t, c) for v, t, c, _ in VIDEOS[:3])
    return f"""
<section class="hero">
 <div class="wrap hero-grid">
  <div>
   <h1><span class="num">000 · 345</span>Start at zero. Square it with three, four, five.</h1>
   <p class="lede">Free layout and estimating calculators for builders and DIYers — built around the oldest rule on the job site. Get the corner right, then get the numbers right, then get it built.</p>
   <div class="cta-row"><a class="btn btn-tape" href="calculators/index.html">Open the calculators</a><a class="btn btn-ghost" href="quotes.html">Get 3 free quotes</a></div>
   <div class="trust"><div><strong>{len(calcs)}</strong>free calculators</div><div><strong>ft + m</strong>imperial and metric</div><div><strong>$0</strong>no sign-up, no paywall</div></div>
  </div>
  <div class="squarer" id="squarer" aria-label="Interactive 3-4-5 corner checker">
   <svg viewBox="0 0 420 300" role="img" aria-label="Diagram of the corner being checked"></svg>
   <div class="fields">
    <div><label for="sq-a">Side A</label><input id="sq-a" type="number" inputmode="decimal" step="any" min="0" value="3"></div>
    <div><label for="sq-b">Side B</label><input id="sq-b" type="number" inputmode="decimal" step="any" min="0" value="4"></div>
    <div><label for="sq-m">Your diagonal</label><input id="sq-m" type="number" inputmode="decimal" step="any" min="0" value="5.05"></div>
   </div>
   <p class="verdict" aria-live="polite"></p>
  </div>
 </div>
</section>

<section class="band">
 <div class="wrap">
  <div class="section-head"><h2>Most-used calculators</h2><p>Every tool works in feet or metres, shows its formula, and explains the result in plain language.</p></div>
  <div class="calc-list">{items}</div>
  <p style="margin-top:18px"><a href="calculators/index.html">See all {len(calcs)} calculators</a></p>
 </div>
</section>

<section class="band alt">
 <div class="wrap two-col">
  <div class="prose">
   <h2>Why 000345?</h2>
   <p>Every build starts from a zero point — a corner stake, a ledger end, the first tile line. From there, three units one way and four the other, and a diagonal of exactly five, gives you a right angle you can trust. That sequence, 0-0-0-3-4-5, is the whole idea of this site.</p>
   <p>We turn that idea into tools: calculators that square corners, size slabs and footings, lay out stairs and rafters, and count boards, tiles, bricks and paint. Each one explains its method so you can check the math yourself.</p>
   <p><a href="about.html">About the project</a> · <a href="methodology.html">How we calculate</a></p>
  </div>
  <div>
   <h2>Guides</h2>
   <ul class="guide-list">{gl}</ul>
   <p style="margin-top:12px"><a href="guides/index.html">All guides</a></p>
  </div>
 </div>
</section>

<section class="band"><div class="wrap">{lead_block(0)}</div></section>

<section class="band alt">
 <div class="wrap">
  <div class="section-head"><h2>Watch it done</h2><p>Hand-picked how-to videos from builders and educators. Videos load only when you press play.</p></div>
  <div class="video-grid">{vids}</div>
  <p style="margin-top:18px"><a href="videos.html">Open the video library</a></p>
 </div>
</section>

<section class="band">
 <div class="wrap">
  <div class="tiers">
   <div class="tier"><h3>Square Corner Challenge</h3><p>Share a project you squared with 3-4-5. Monthly prizes for the best builds, chosen by a judging panel and the community.</p><a class="btn btn-ink btn-sm" href="contests.html">Enter the challenge</a></div>
   <div class="tier"><h3>Contractors: get local leads</h3><p>Homeowners arrive with measurements already worked out. Pick your trades and service area, and set your own monthly cap.</p><a class="btn btn-ink btn-sm" href="pros.html">Join as a pro</a></div>
   <div class="tier"><h3>Keep the tools free</h3><p>No paywalls, no accounts. Support from readers and sponsors pays for hosting, new calculators and contest prizes.</p><a class="btn btn-tape btn-sm" href="support.html">Support 000345</a></div>
  </div>
 </div>
</section>
"""

def calc_index(calcs):
    cats = []
    for c in calcs:
        if c["cat"] not in cats:
            cats.append(c["cat"])
    out = ""
    for cat in cats:
        items = "".join(f'<a href="{c["slug"]}.html"><h3>{c["title"]}</h3><p>{c["short"]}</p></a>' for c in calcs if c["cat"] == cat)
        out += f'<h2 style="margin-top:34px">{cat}</h2><div class="calc-list">{items}</div>'
    return f"""<div class="page-head"><div class="wrap"><h1>Construction calculators</h1><p>{len(calcs)} free tools for layout, concrete, framing, roofing, decks, fences and finishes. Imperial and metric, with formulas and worked examples on every page.</p></div></div>
<div class="wrap">{out}<div style="margin-top:44px">{lead_block(1)}</div></div>"""

def guide_index(guides):
    gl = "".join(f'<li><a href="{g["slug"]}.html">{g["title"]}</a><p>{g["summary"]}</p></li>' for g in guides)
    return f"""<div class="page-head"><div class="wrap"><h1>Guides</h1><p>Practical, field-tested explanations of layout, measuring and estimating — written to be used with a tape in your hand.</p></div></div>
<div class="wrap" style="padding-top:28px"><ul class="guide-list prose" style="max-width:none">{gl}</ul><div style="margin-top:40px">{lead_block(1)}</div></div>"""

def videos():
    groups = []
    for v in VIDEOS:
        if v[3] not in groups:
            groups.append(v[3])
    out = ""
    for g in groups:
        out += f'<h2 style="margin-top:34px">{g}</h2><div class="video-grid">' + "".join(video_card(v, t, c) for v, t, c, gg in VIDEOS if gg == g) + "</div>"
    return f"""<div class="page-head"><div class="wrap"><h1>Video library</h1><p>Short, practical videos on squaring, layout, roofs, stairs and concrete, from creators we think explain it well. Videos are embedded from YouTube in privacy-enhanced mode and load only when you press play.</p></div></div>
<div class="wrap">{out}
<div class="callout" style="margin-top:34px">Made a great how-to video? <a href="careers.html#creators">Join our creator program</a> or <a href="#" data-mail="Video suggestion — 000345.com">suggest a video</a>. All videos remain the property of their creators.</div></div>"""

def quotes():
    trades = [("foundation", "Foundation / layout"), ("concrete", "Concrete / slab"), ("deck", "Deck"), ("fence", "Fence"), ("roofing", "Roofing"),
              ("stairs", "Stairs"), ("framing", "Framing / addition"), ("flooring", "Flooring / tile"), ("painting", "Painting"), ("drywall", "Drywall"),
              ("masonry", "Brick / masonry"), ("landscaping", "Landscaping"), ("general", "Something else")]
    tiles = "".join(f'<label><input type="radio" name="project_type" value="{v}" required> {t}</label>' for v, t in trades)
    return f"""<div class="page-head"><div class="wrap"><h1>Get up to 3 free quotes from local pros</h1><p>Answer a few quick questions. We match your project with up to three contractors who serve your area. Free for homeowners, with no obligation to hire.</p></div></div>
<div class="wrap" style="padding-top:28px">
<div class="calc-layout">
 <div>
 <form class="calc-box" data-form="Quote request" data-steps data-success="Request received. Matched pros usually reach out within one business day. Check your email and phone." novalidate>
  <div class="steps-bar" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
  <div class="step"><h2 class="mt0">What are you building?</h2><div class="choice-grid">{tiles}</div>
   <div class="field"><label for="q-zip">ZIP / postal code</label><input id="q-zip" name="zip" required autocomplete="postal-code" pattern="[A-Za-z0-9 \\-]{{3,10}}"></div>
   <div class="step-nav"><span></span><button type="button" class="btn btn-tape" data-next>Continue</button></div></div>
  <div class="step"><h2 class="mt0">Size and scope</h2>
   <div class="field"><label for="q-size">Size or measurements</label><input id="q-size" name="size" placeholder="e.g. 12 × 16 ft deck, 192 ft²" required></div>
   <div class="field"><label for="q-desc">Describe the job (optional)</label><textarea id="q-desc" name="description" placeholder="Materials, access, existing structure to remove, anything the pro should know"></textarea></div>
   <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>Back</button><button type="button" class="btn btn-tape" data-next>Continue</button></div></div>
  <div class="step"><h2 class="mt0">Timing and budget</h2>
   <div class="row2"><div class="field"><label for="q-time">When do you want to start?</label><select id="q-time" name="timeline" required><option value="">Choose one</option><option>As soon as possible</option><option>Within 1–3 months</option><option>In 3+ months</option><option>Just researching costs</option></select></div>
   <div class="field"><label for="q-budget">Budget range</label><select id="q-budget" name="budget" required><option value="">Choose one</option><option>Under $2,500</option><option>$2,500–$10,000</option><option>$10,000–$25,000</option><option>$25,000–$75,000</option><option>Over $75,000</option><option>Not sure yet</option></select></div></div>
   <div class="field"><label for="q-own">Do you own the property?</label><select id="q-own" name="ownership" required><option value="">Choose one</option><option>Yes, I own it</option><option>I'm buying it</option><option>No, I rent (landlord approval needed)</option><option>I'm a property manager</option></select></div>
   <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>Back</button><button type="button" class="btn btn-tape" data-next>Continue</button></div></div>
  <div class="step"><h2 class="mt0">Where should pros send quotes?</h2>
   <div class="row2"><div class="field"><label for="q-name">First name</label><input id="q-name" name="name" required autocomplete="given-name"></div>
   <div class="field"><label for="q-email">Email</label><input id="q-email" name="email" type="email" required autocomplete="email"></div></div>
   <div class="row2"><div class="field"><label for="q-phone">Phone</label><input id="q-phone" name="phone" type="tel" required autocomplete="tel" pattern="[0-9+()\\-. ]{{7,20}}"></div>
   <div class="field"><label for="q-contact">Best way to reach you</label><select id="q-contact" name="contact_pref"><option>Phone call</option><option>Text message</option><option>Email</option></select></div></div>
   <div class="field">{CONSENT}</div>{hp()}
   <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>Back</button><button type="submit" class="btn btn-tape">Get my free quotes</button></div></div>
  {msg()}
 </form>
 </div>
 <aside><div class="sticky-aside">
  <div class="aside-box"><h3>How it works</h3><ol style="padding-left:18px;margin:0"><li>Tell us about the job (about 60 seconds).</li><li>We match it with up to three local pros.</li><li>Compare quotes and hire only if you want to.</li></ol></div>
  <div class="aside-box"><h3>Your information</h3><p style="margin:0">We share your request only with the contractors matched to it. We never sell your details to list brokers. <a href="privacy.html">Privacy policy</a>.</p></div>
  <div class="aside-box"><h3>Before you hire</h3><p style="margin:0">Read our <a href="guides/how-to-hire-a-contractor.html">contractor hiring checklist</a> — licences, insurance, contracts and payment schedules.</p></div>
 </div></aside>
</div></div>"""

def pros():
    return f"""<div class="page-head"><div class="wrap"><h1>Join as a pro: leads from homeowners who already measured</h1><p>People who use our calculators have worked out their square footage, cubic yards and stair counts before they ask for a quote. That makes for faster estimates and better-qualified jobs.</p></div></div>
<div class="wrap" style="padding-top:28px">
<div class="two-col">
 <div class="prose">
  <h2>What you get</h2>
  <ul><li><strong>Your trades, your area.</strong> Choose services and postal codes; we only send matching jobs.</li>
  <li><strong>Shared with no more than three pros.</strong> Each request goes to a maximum of three contractors.</li>
  <li><strong>Budget control.</strong> Set a monthly cap and pause any time.</li>
  <li><strong>Project details up front.</strong> Size, timeline, budget range and ownership are on every lead.</li>
  <li><strong>Featured listings and sponsorships</strong> on the calculator pages your customers use.</li></ul>
  <h2>Who we work with</h2>
  <p>Licensed or registered contractors (where your jurisdiction requires it) with current liability insurance. We ask for proof before sending leads and recheck it each year.</p>
  <h2>Founding-partner terms</h2>
  <p>Contractors who join during launch get founding-partner pricing locked for 12 months. Tell us your trade and area and we will send the rate card for your market.</p>
 </div>
 <form class="calc-box" data-form="Contractor sign-up" data-success="Thanks — we'll send your market's rate card and onboarding steps within one business day.">
  <h2 class="mt0">Apply to receive leads</h2>
  <div class="field"><label for="p-biz">Business name</label><input id="p-biz" name="business" required></div>
  <div class="row2"><div class="field"><label for="p-name">Your name</label><input id="p-name" name="name" required></div>
  <div class="field"><label for="p-phone">Phone</label><input id="p-phone" name="phone" type="tel" required></div></div>
  <div class="field"><label for="p-email">Email</label><input id="p-email" name="email" type="email" required></div>
  <div class="field"><label for="p-trade">Main trade</label><select id="p-trade" name="trade" required><option value="">Choose one</option><option>General contractor</option><option>Concrete / foundations</option><option>Decks & fences</option><option>Roofing</option><option>Framing / carpentry</option><option>Flooring & tile</option><option>Painting & drywall</option><option>Masonry</option><option>Landscaping</option><option>Other</option></select></div>
  <div class="field"><label for="p-area">Service area (cities or postal codes)</label><input id="p-area" name="service_area" required></div>
  <div class="row2"><div class="field"><label for="p-lic">Licence / registration no. (if applicable)</label><input id="p-lic" name="licence"></div>
  <div class="field"><label for="p-vol">Leads you can handle per month</label><select id="p-vol" name="volume"><option>1–5</option><option>6–15</option><option>16–40</option><option>40+</option></select></div></div>
  <div class="field"><label class="check"><input type="checkbox" name="insured" value="yes" required> I carry current general liability insurance and can provide a certificate.</label></div>
  {hp()}<button class="btn btn-tape" type="submit">Apply as a pro</button>{msg()}
 </form>
</div></div>"""

def support():
    direct = (f'<p><a class="btn btn-tape" href="{SITE["donate_url"]}" rel="noopener" target="_blank">Give now</a></p>' if SITE["donate_url"] else "")
    return f"""<div class="page-head"><div class="wrap"><h1>Support 000345</h1><p>Every calculator here is free, with no account and no paywall. Reader support and sponsors pay for hosting, new tools, video production, contest prizes and the people who build and check them.</p></div></div>
<div class="wrap" style="padding-top:28px">
<h2>Where your support goes</h2>
<div class="tiers" style="margin-bottom:34px">
 <div class="tier"><h3>Operations</h3><p>Hosting, domains, security and the time it takes to keep every formula checked and current.</p></div>
 <div class="tier"><h3>New tools & content</h3><p>Hiring tradespeople and writers to build new calculators and review existing ones.</p></div>
 <div class="tier"><h3>Contests & prizes</h3><p>Funding the monthly Square Corner Challenge and its prizes.</p></div>
 <div class="tier"><h3>Promotion</h3><p>Reaching more builders and DIYers through outreach, video and partnerships.</p></div>
</div>
<div class="two-col">
 <div>
  <h2>Choose an amount</h2>
  <p>Pick a one-time or monthly amount and leave your details. We'll reply with a secure payment link. You can also give anonymously.</p>
  {direct}
  <div class="unit-switch" style="flex-wrap:wrap;margin-bottom:14px">
   <button type="button" data-amount="5" aria-pressed="false">$5 · a coffee</button><button type="button" data-amount="15" aria-pressed="true">$15 · a box of screws</button>
   <button type="button" data-amount="50" aria-pressed="false">$50 · a new calculator page</button><button type="button" data-amount="150" aria-pressed="false">$150 · a month of prizes</button>
  </div>
  <form class="calc-box" data-form="Donation pledge" data-success="Thank you. We'll email a secure payment link shortly.">
   <div class="row2"><div class="field"><label for="pledge-amount">Amount (USD)</label><input id="pledge-amount" name="amount" type="number" min="1" step="1" value="15" required></div>
   <div class="field"><label for="d-freq">Frequency</label><select id="d-freq" name="frequency"><option>One time</option><option>Monthly</option><option>Yearly</option></select></div></div>
   <div class="field"><label for="d-purpose">Put it toward</label><select id="d-purpose" name="purpose"><option>Where it's needed most</option><option>Operations</option><option>New tools & content</option><option>Contest prizes</option><option>Promotion & marketing</option><option>Hiring talent</option></select></div>
   <div class="row2"><div class="field"><label for="d-name">Name</label><input id="d-name" name="name" autocomplete="name"></div>
   <div class="field"><label for="d-email">Email</label><input id="d-email" name="email" type="email" required autocomplete="email"></div></div>
   <div class="field"><label for="d-msg">Message (optional, may appear on the supporter wall)</label><textarea id="d-msg" name="message"></textarea></div>
   <div class="field"><label class="check"><input type="checkbox" name="anonymous" value="yes"> Keep my name off the supporter wall</label></div>
   {hp()}<button class="btn btn-tape" type="submit">Pledge support</button>{msg()}
   <p class="muted" style="font-size:.88rem;margin:.8em 0 0">000345 is not a registered charity; contributions are not tax-deductible.</p>
  </form>
 </div>
 <div>
  <h2>Sponsor the project</h2>
  <p>Brands, suppliers and contractors can sponsor a calculator, a contest month or the video library. Sponsors are clearly labelled and never change our calculations.</p>
  <div class="tiers">
   <div class="tier"><h3>Bronze</h3><p class="price">Calculator</p><ul><li>Logo and link on one calculator page</li><li>Listed on supporter wall</li></ul></div>
   <div class="tier feature"><h3>Silver</h3><p class="price">Category</p><ul><li>Logo on every calculator in a category</li><li>Mention in the monthly newsletter</li></ul></div>
   <div class="tier"><h3>Gold</h3><p class="price">Contest</p><ul><li>Presenting sponsor of a Square Corner Challenge month</li><li>Prize placement and winner feature</li></ul></div>
  </div>
  <p style="margin-top:16px"><a class="btn btn-ink" href="advertise.html">Request the sponsor kit</a></p>
  <h2 style="margin-top:30px">Supporter wall</h2>
  <p class="muted">Our first supporters will be listed here. Be one of them.</p>
 </div>
</div></div>"""

def contests():
    return f"""<div class="page-head"><div class="wrap"><h1>The Square Corner Challenge</h1><p>A monthly contest for builders and DIYers. Show us a project you laid out square — a deck, slab, shed, patio, tile floor or garden bed — and tell us how you did it.</p></div></div>
<div class="wrap" style="padding-top:28px">
<div class="two-col">
 <div class="prose">
  <h2>How to enter</h2>
  <ol><li>Build something that needed a square corner.</li><li>Take a photo or short video, ideally showing your layout (strings, tape on the diagonal, the finished corner).</li>
  <li>Share it publicly (Instagram, YouTube, Google Drive or Dropbox link) and submit the link with the form.</li><li>Tell us in a few sentences how you squared it.</li></ol>
  <h2>Prizes each month</h2>
  <div class="table-scroll"><table><thead><tr><th>Place</th><th>Prize</th></tr></thead><tbody>
  <tr><td>First</td><td>Tool gift card, winner feature on the homepage and newsletter</td></tr>
  <tr><td>Second</td><td>Tool gift card and feature in the gallery</td></tr>
  <tr><td>Third</td><td>Tool gift card</td></tr>
  <tr><td>Community choice</td><td>Feature and a 000345 tape-measure prize pack</td></tr></tbody></table></div>
  <p>Prize values are announced at the start of each round and are funded by sponsors and supporters. <a href="support.html">Help fund the prize pool</a> or <a href="advertise.html">sponsor a month</a>.</p>
  <h2>Judging</h2>
  <p>Entries are scored out of 100: accuracy and craftsmanship (40), how clearly the layout method is explained (30), creativity and difficulty (20) and presentation (10). Community choice is decided by public vote on our social channels.</p>
  <h2>Official rules (summary)</h2>
  <ul><li>No purchase or payment is necessary to enter or win. A purchase does not improve the chance of winning.</li>
  <li>Open to individuals who are of the age of majority where they live. Void where prohibited. Residents of jurisdictions that require registration or bonding for contests may be excluded.</li>
  <li>One entry per person per round. Entries must be your own original work and must not infringe anyone's rights.</li>
  <li>Each round opens on the 1st of the month and closes at 11:59 p.m. Eastern on the last day of the month. Winners are announced within 15 days and contacted by email.</li>
  <li>Where required by law (for example in Canada), prize winners must correctly answer a time-limited skill-testing question.</li>
  <li>By entering, you allow 000345 to show your entry, first name and city on this site and its social channels, with credit.</li>
  <li>Prizes are non-transferable and may be substituted with a prize of equal or greater value. Winners are responsible for any taxes.</li>
  <li>The sponsor of each round is named on this page when the round opens. Full rules are available on request.</li></ul>
 </div>
 <div>
 <form class="calc-box sticky-aside" data-form="Contest entry" data-success="Entry received. Good luck — winners are announced within 15 days of the round closing.">
  <h2 class="mt0">Submit your entry</h2>
  <div class="row2"><div class="field"><label for="c-name">Full name</label><input id="c-name" name="name" required></div>
  <div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" required></div></div>
  <div class="row2"><div class="field"><label for="c-city">City and region</label><input id="c-city" name="city" required></div>
  <div class="field"><label for="c-type">Project type</label><select id="c-type" name="project"><option>Deck</option><option>Slab / patio</option><option>Shed / building</option><option>Tile / flooring</option><option>Fence</option><option>Garden / landscape</option><option>Other</option></select></div></div>
  <div class="field"><label for="c-link">Link to photos or video</label><input id="c-link" name="link" type="url" placeholder="https://" required></div>
  <div class="field"><label for="c-how">How did you square it?</label><textarea id="c-how" name="method" required></textarea></div>
  <div class="field"><label class="check"><input type="checkbox" name="rules" value="accepted" required> I have read the official rules, I am of the age of majority where I live, and this is my own work.</label></div>
  {hp()}<button class="btn btn-tape" type="submit">Submit my entry</button>{msg()}
 </form>
 </div>
</div></div>"""

def careers():
    roles = [
     ("Trade content writer", "Remote · freelance", "Write and update calculator guides and how-tos. You have hands-on experience in construction, carpentry, concrete or a related trade and can explain it clearly."),
     ("Technical reviewer (licensed contractor or engineer)", "Remote · per review", "Check formulas, worked examples and safety notes before publication. Your name appears as reviewer on pages you approve."),
     ("Video creator", "Remote · per video", "Produce short, practical layout and estimating videos for our library and YouTube channel.", "creators"),
     ("Front-end developer", "Remote · contract", "Build new calculators in plain HTML, CSS and JavaScript with a focus on accuracy, accessibility and speed."),
     ("Growth & partnerships", "Remote · commission-based", "Bring on contractors, suppliers and sponsors, and grow our audience through outreach and partnerships."),
     ("Local pro ambassador", "Your city · part-time", "Represent 000345 to contractors in your area and help us match homeowners with good local pros."),
    ]
    rl = "".join(f'<article class="aside-box" id="{r[3] if len(r)>3 else ""}"><h3>{r[0]}</h3><p class="pill">{r[1]}</p><p style="margin:.6em 0 0">{r[2]}</p></article>' for r in roles)
    opts = "".join(f"<option>{r[0]}</option>" for r in roles)
    return f"""<div class="page-head"><div class="wrap"><h1>Careers at 000345</h1><p>We're a small, remote team building the most useful layout and estimating toolkit on the web. We hire people who know the trades and people who know the web.</p></div></div>
<div class="wrap" style="padding-top:28px"><div class="two-col">
 <div><h2>Open roles</h2>{rl}</div>
 <form class="calc-box" data-form="Job application" data-success="Application received. If there's a fit, we'll be in touch within two weeks.">
  <h2 class="mt0">Apply</h2>
  <div class="field"><label for="j-role">Role</label><select id="j-role" name="role" required>{opts}<option>Something else</option></select></div>
  <div class="row2"><div class="field"><label for="j-name">Full name</label><input id="j-name" name="name" required></div>
  <div class="field"><label for="j-email">Email</label><input id="j-email" name="email" type="email" required></div></div>
  <div class="row2"><div class="field"><label for="j-loc">Location / time zone</label><input id="j-loc" name="location"></div>
  <div class="field"><label for="j-link">Portfolio, LinkedIn or résumé link</label><input id="j-link" name="portfolio" type="url" placeholder="https://" required></div></div>
  <div class="field"><label for="j-why">Relevant experience</label><textarea id="j-why" name="experience" required></textarea></div>
  {hp()}<button class="btn btn-tape" type="submit">Send application</button>{msg()}
 </form>
</div></div>"""

def advertise():
    return f"""<div class="page-head"><div class="wrap"><h1>Advertise and partner with 000345</h1><p>Reach homeowners, DIYers and contractors at the exact moment they are measuring a project — before they buy materials or hire.</p></div></div>
<div class="wrap" style="padding-top:28px">
<div class="tiers">
 <div class="tier"><h3>Calculator sponsorship</h3><p>Own a calculator page: logo, short message and link beside the tool. Example: a concrete supplier on the slab calculator.</p></div>
 <div class="tier"><h3>Exclusive local leads</h3><p>Be the only contractor in your trade receiving requests from your postal codes.</p></div>
 <div class="tier"><h3>Contest presenting sponsor</h3><p>Fund a month's prizes and get named presenting-sponsor placement on the contest, winner features and newsletter.</p></div>
 <div class="tier"><h3>Video & content partnership</h3><p>Co-produce a how-to video or guide. All sponsored content is clearly labelled.</p></div>
 <div class="tier"><h3>Tool & data licensing</h3><p>Embed our calculators on your site or app under a white-label licence.</p></div>
 <div class="tier"><h3>Domain & site acquisition</h3><p>Interested in acquiring or partnering on 000345.com itself? <a href="{SITE['notice_url']}" target="_blank" rel="noopener">Contact the owner</a>.</p></div>
</div>
<div class="two-col" style="margin-top:34px">
 <div class="prose"><h2>Our standards</h2><ul><li>Sponsors never change calculator results or editorial conclusions.</li><li>Every paid placement is labelled "Sponsored".</li><li>We don't accept ads for products that conflict with building safety.</li><li>Display ads are served by Google AdSense under Google's policies.</li></ul></div>
 <form class="calc-box" data-form="Advertising / partnership inquiry" data-success="Thanks. We'll send the media kit and availability within one business day.">
  <h2 class="mt0">Request the media kit</h2>
  <div class="row2"><div class="field"><label for="a-name">Name</label><input id="a-name" name="name" required></div>
  <div class="field"><label for="a-co">Company</label><input id="a-co" name="company" required></div></div>
  <div class="row2"><div class="field"><label for="a-email">Work email</label><input id="a-email" name="email" type="email" required></div>
  <div class="field"><label for="a-site">Website</label><input id="a-site" name="website" type="url" placeholder="https://"></div></div>
  <div class="field"><label for="a-int">Interested in</label><select id="a-int" name="interest"><option>Calculator sponsorship</option><option>Exclusive local leads</option><option>Contest sponsorship</option><option>Video / content partnership</option><option>Tool licensing</option><option>Domain / site acquisition</option><option>Other partnership</option></select></div>
  <div class="field"><label for="a-budget">Monthly budget</label><select id="a-budget" name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div>
  <div class="field"><label for="a-msg">Goals</label><textarea id="a-msg" name="message"></textarea></div>
  {hp()}<button class="btn btn-tape" type="submit">Request media kit</button>{msg()}
 </form>
</div></div>"""

def about():
    return f"""<div class="page-head"><div class="wrap"><h1>About 000345</h1><p>An independent toolkit for squaring, measuring and estimating construction work.</p></div></div>
<div class="wrap prose" style="padding-top:28px">
<h2>What we do</h2>
<p>000345 publishes free calculators and guides for layout and estimating: squaring corners with the 3-4-5 rule, sizing concrete, laying out stairs and rafters, and counting the materials for decks, fences, floors and walls. Every tool works in imperial and metric units and shows the formula it uses.</p>
<h2>Why the name</h2>
<p>Every build starts from a zero point. From that corner you measure three units one way, four the other, and check for five on the diagonal. 0-0-0-3-4-5 is that sequence, and it describes what we want every visitor to leave with: a corner, and a project, that starts square.</p>
<h2>How we work</h2>
<ul><li><strong>Show the math.</strong> Every calculator page explains the formula and includes a worked example you can check by hand.</li>
<li><strong>Plain language.</strong> We write for someone holding a tape measure, not a textbook.</li>
<li><strong>Safety first.</strong> Structural work depends on local codes, soils and loads that a calculator cannot see. We say so on every relevant page.</li>
<li><strong>Clear money.</strong> The site is funded by advertising, sponsorships, reader support and contractor referrals. Sponsors never change our numbers. See <a href="methodology.html">How we calculate</a>.</li></ul>
<h2>Contact</h2>
<p>Questions, corrections and partnership ideas are welcome. Use the <a href="contact.html">contact page</a>. Last reviewed {SITE['updated']}.</p>
</div>"""

def contact():
    return f"""<div class="page-head"><div class="wrap"><h1>Contact us</h1><p>Questions about a calculator, a correction, press, partnerships or anything else. We reply within one business day.</p></div></div>
<div class="wrap" style="padding-top:28px"><div class="two-col">
 <form class="calc-box" data-form="Contact form" data-success="Message sent. We'll reply within one business day.">
  <div class="row2"><div class="field"><label for="ct-name">Name</label><input id="ct-name" name="name" required autocomplete="name"></div>
  <div class="field"><label for="ct-email">Email</label><input id="ct-email" name="email" type="email" required autocomplete="email"></div></div>
  <div class="field"><label for="ct-topic">Topic</label><select id="ct-topic" name="topic"><option>General question</option><option>Report a calculation error</option><option>Suggest a calculator</option><option>Advertising / sponsorship</option><option>Partnership</option><option>Domain / website acquisition</option><option>Press</option><option>Privacy request</option></select></div>
  <div class="field"><label for="ct-msg">Message</label><textarea id="ct-msg" name="message" required></textarea></div>
  {hp()}<button class="btn btn-tape" type="submit">Send message</button>{msg()}
 </form>
 <div class="prose">
  <h2>Other ways to reach us</h2>
  <p><a href="#" data-mail="Inquiry from 000345.com" class="btn btn-ghost">Email the team</a></p>
  <p>Interested in this website, the domain name, sponsorship, advertising or a partnership? You can also reach the owner at <a href="{SITE['notice_url']}" target="_blank" rel="noopener">web.works/contact</a>.</p>
  <h3>Found an error?</h3>
  <p>Tell us the calculator, the inputs you used and the result you expected. We check every report and credit people who catch real errors.</p>
 </div>
</div></div>"""

def methodology():
    return f"""<div class="page-head"><div class="wrap"><h1>How we calculate</h1><p>The methods, assumptions and sources behind every 000345 calculator.</p></div></div>
<div class="wrap prose" style="padding-top:28px">
<h2>Principles</h2>
<ul><li>Geometry is exact: right triangles use the Pythagorean theorem, angles use standard trigonometry, and areas and volumes use standard formulas.</li>
<li>Material yields (bags of concrete, coverage of paint, densities of gravel) are typical published figures. They vary by product, so we name the assumption on each page and tell you to check the label.</li>
<li>Code checks (stair risers and treads, for example) use widely adopted residential figures. Local codes differ and always take priority.</li>
<li>All calculations run in your browser. We don't store the numbers you enter.</li></ul>
<h2>Rounding</h2>
<p>Lengths in imperial units are shown in decimal feet and in feet-inches to the nearest 1/16". Counts of things you buy (bags, boards, sheets, tiles) are always rounded up.</p>
<h2>Review</h2>
<p>Each calculator is tested against hand-worked examples, which appear on the page so you can check them yourself. Pages show the date they were last reviewed. Corrections are welcome through the <a href="contact.html">contact page</a>.</p>
<h2>Independence</h2>
<p>Advertising and sponsorships pay for the site. Sponsors do not see or change formulas, results or editorial conclusions, and paid placements are labelled.</p>
<h2>Limits</h2>
<p>Calculators help with planning and estimating. They don't replace engineered drawings, permits or inspections. For structural work — foundations, beams, decks, stairs, roofs — confirm with your local building authority and a qualified professional.</p>
</div>"""

def legal():
    return f"""<div class="page-head"><div class="wrap"><h1>Trademark & copyright disclosure</h1><p>Plain-language notice of what 000345 is, and is not, connected to.</p></div></div>
<div class="wrap prose" style="padding-top:28px">
<h2>The name "000345"</h2>
<p>"000345" is the domain name of this website and is used here only to identify this independent toolkit. The digits 0-0-0-3-4-5 refer to the construction practice of starting at a zero point and squaring a corner with a 3-4-5 triangle.</p>
<p>The same digits, or parts of them, are used elsewhere as stock and security codes on various exchanges, as product, part, model, catalogue and registration numbers, as postal or phone codes and in other identifiers. <strong>000345.com is not affiliated with, endorsed by, sponsored by or connected to any company, listed security, issuer, product, brand or organisation that uses "000345", "00345", "345" or any similar number.</strong> Nothing on this site is investment advice or information about any security.</p>
<h2>Third-party trademarks</h2>
<p>Product names, company names, brands and logos mentioned on this site (including names of YouTube channels and building-material manufacturers) are the property of their respective owners and are used only for identification and description. Their mention does not imply endorsement.</p>
<h2>Copyright</h2>
<p>Unless stated otherwise, the text, calculators, code, diagrams and design of this site are © 000345.com. You may link to any page and quote short excerpts with attribution. Reproducing whole pages or calculators without permission is not allowed.</p>
<p>The 3-4-5 rule, the Pythagorean theorem and standard engineering formulas are public knowledge and not claimed by anyone; our explanations and implementations of them are original work.</p>
<h2>Embedded videos</h2>
<p>Videos are embedded from YouTube using YouTube's standard embed player and remain the property of their creators. We don't host, copy or modify them. Creators who would like a video removed can contact us and we will remove it promptly.</p>
<h2>Copyright complaints</h2>
<p>If you believe content on this site infringes your copyright, send a notice through our <a href="contact.html">contact page</a> identifying the work, the page on our site, your contact details and a statement of good-faith belief. We respond to valid notices promptly.</p>
<h2>Fonts and software</h2>
<p>Typefaces are served by Google Fonts under the SIL Open Font License. Site code uses no third-party libraries.</p>
</div>"""

def privacy():
    return f"""<div class="page-head"><div class="wrap"><h1>Privacy policy</h1><p>Last updated {SITE['updated']}.</p></div></div>
<div class="wrap prose" style="padding-top:28px">
<h2>Summary</h2>
<p>Calculators run in your browser and we don't store what you type into them. We collect personal information only when you send it to us through a form. We use Google AdSense to show ads, which uses cookies.</p>
<h2>Information you give us</h2>
<p>When you request quotes, apply as a contractor, enter a contest, apply for a job, pledge support or contact us, we receive what you enter in the form (such as your name, email, phone, postal code and project details). Forms are delivered to us by email through the FormSubmit relay service.</p>
<h2>How we use it</h2>
<ul><li><strong>Quote requests:</strong> to match your project with up to three contractors, who receive your details so they can contact you. We do not sell your information to list brokers.</li>
<li><strong>Other forms:</strong> only to respond to you and run the related program (contest, application, sponsorship, donation).</li></ul>
<h2>Advertising and cookies</h2>
<p>This site uses Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on visits to this site and/or other sites on the Internet. You can opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" rel="noopener" target="_blank">Google Ads Settings</a>, or opt out of some third-party vendors' cookies at <a href="https://www.aboutads.info/choices/" rel="noopener" target="_blank">aboutads.info</a>. Learn more in <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">how Google uses information from sites that use its services</a>.</p>
<p>Our cookie notice lets you choose non-personalised ads. In regions where a consent management platform is required, consent is collected through Google's certified consent tools.</p>
<h2>Local storage</h2>
<p>We store your theme, unit system and cookie choice in your browser so the site remembers them. This never leaves your device.</p>
<h2>Embedded videos</h2>
<p>Videos use YouTube's privacy-enhanced mode and only load after you press play. Once loaded, YouTube's own privacy policy applies.</p>
<h2>Retention and your rights</h2>
<p>We keep form submissions only as long as needed for the purpose you sent them for, and no longer than 24 months. You can ask to access, correct or delete your information, or withdraw consent, through the <a href="contact.html">contact page</a>. Depending on where you live (for example under the GDPR, CCPA/CPRA or PIPEDA), you may have additional rights, which we honour.</p>
<h2>Children</h2>
<p>This site is intended for adults and does not knowingly collect information from children under 13 (or the age required by local law).</p>
<h2>Changes</h2>
<p>We'll post any changes on this page with a new date.</p>
</div>"""

def terms():
    return f"""<div class="page-head"><div class="wrap"><h1>Terms of use</h1><p>Last updated {SITE['updated']}.</p></div></div>
<div class="wrap prose" style="padding-top:28px">
<p>By using 000345.com you agree to these terms.</p>
<h2>Use of the tools</h2><p>The calculators and guides are provided free for personal and professional planning. Results are estimates based on the inputs you provide and the assumptions stated on each page. You are responsible for verifying measurements, quantities and code requirements before buying materials or building.</p>
<h2>No professional advice</h2><p>Nothing on this site is engineering, architectural, legal or financial advice. See our <a href="disclaimer.html">disclaimer</a>.</p>
<h2>Contractor matching</h2><p>000345 is not a contractor and does not perform, supervise or guarantee any work. Contractors are independent businesses. Any agreement for work is between you and the contractor. Check licences, insurance and references before hiring.</p>
<h2>User submissions</h2><p>When you submit content (contest entries, messages), you confirm you have the right to share it and grant us a non-exclusive licence to display it as described on the relevant page.</p>
<h2>Acceptable use</h2><p>Don't misuse the site: no scraping that burdens the service, no automated form submissions, no attempts to interfere with ads or security.</p>
<h2>Intellectual property</h2><p>See the <a href="legal.html">trademark & copyright disclosure</a>.</p>
<h2>Liability</h2><p>To the extent permitted by law, the site is provided "as is" and we are not liable for losses arising from its use, including errors in calculations or third-party contractor work.</p>
<h2>Changes</h2><p>We may update these terms; the date above shows the latest version.</p>
</div>"""

def disclaimer():
    return f"""<div class="page-head"><div class="wrap"><h1>Disclaimer</h1><p>Read this before relying on any result.</p></div></div>
<div class="wrap prose" style="padding-top:28px">
<p>The calculators, guides and videos on 000345.com are for general information, planning and estimating. They are not a substitute for professional engineering or architectural design, permits, inspections or the advice of a qualified contractor.</p>
<ul><li>Structural elements — footings, foundations, beams, joists, rafters, stairs and decks — must meet the building code in force where you build. Codes vary by country, province, state and municipality.</li>
<li>Material yields, coverage and densities vary by manufacturer and conditions. Always check product labels and supplier figures.</li>
<li>Always contact your local utility-locate service before digging.</li>
<li>Use appropriate safety equipment and follow manufacturers' instructions.</li></ul>
<h2>Advertising and affiliate disclosure</h2>
<p>This site shows ads through Google AdSense and may receive compensation from sponsors and from contractors who receive referrals. Sponsored content is labelled. Compensation never affects calculator results.</p>
<h2>External links and videos</h2>
<p>We link to and embed third-party content that we think is useful. We don't control it and aren't responsible for its accuracy or availability.</p>
</div>"""

def notfound():
    return """<div class="page-head"><div class="wrap"><h1>That page isn't on the plan</h1><p>The link may be old or mistyped. Start from the calculators, or go back to the home page.</p></div></div>
<div class="wrap" style="padding:28px 20px"><p><a class="btn btn-tape" href="calculators/index.html">Open the calculators</a> <a class="btn btn-ghost" href="index.html">Home</a></p></div>"""
