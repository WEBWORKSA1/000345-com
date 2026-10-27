"""Calculator definitions: inputs + original explanatory content for each tool page."""

# Input: (name, label, imperial unit, metric unit, imperial default, metric default, help text)
# Select: ("select", name, label, [(value, text), ...], help)

CALCS = [
 {
  "slug": "3-4-5-squaring-calculator", "fn": "squaring", "cat": "Layout", "project": "foundation",
  "title": "3-4-5 Squaring Calculator", "short": "Find the exact diagonal for a square corner and check a measured one.",
  "desc": "Free 3-4-5 rule calculator. Enter two sides to get the diagonal for a perfect 90° corner, the largest 3-4-5 multiple that fits, and how far out of square a measured corner is.",
  "inputs": [
    ("a", "Side A", "ft", "m", 12, 3.6, "Distance measured from the corner along the first line."),
    ("b", "Side B", "ft", "m", 16, 4.8, "Distance measured from the corner along the second line."),
    ("m", "Measured diagonal (optional)", "ft", "m", 0, 0, "Tape reading between the two marks. Leave at 0 to just get the target."),
  ],
  "video": "b-Wp9hkxW54",
  "body": """
<p>The 3-4-5 rule is the fastest way to lay out a true right angle with nothing but a tape measure. Mark 3 units along one line, 4 units along the other, and adjust the corner until the diagonal between the marks reads exactly 5. Because 3² + 4² = 5², the only triangle that closes at those three lengths is a right triangle. This calculator does the same thing for any pair of sides, so you can use the longest legs your site allows and get a more accurate corner.</p>
<h2>How to use this calculator</h2>
<ol><li>Enter the length you can measure along each line from the corner. Longer is better: an error of 1/8" over 12 ft matters far less than the same error over 3 ft.</li>
<li>Read the <strong>diagonal for a true 90°</strong>. Hook the tape on one mark and swing it to the other; move the free line until the tape reads that number.</li>
<li>If you have already set the lines, type the diagonal you actually measured. The tool reports the real corner angle, whether the corner is open or closed, and how far the far end of side B needs to move.</li></ol>
<h2>The formula</h2>
<p>For legs <em>a</em> and <em>b</em>, the diagonal is <strong>c = √(a² + b²)</strong>. To check an existing corner, the law of cosines gives the real angle: <strong>θ = arccos((a² + b² − d²) ÷ 2ab)</strong>, where <em>d</em> is the measured diagonal. A diagonal longer than <em>c</em> means the angle is greater than 90° (open); shorter means it is under 90° (closed).</p>
<h2>Worked example</h2>
<p>You are setting out a 12 ft × 16 ft shed pad. Those sides are exactly 4 × (3, 4), so the diagonal should be 4 × 5 = 20 ft. You measure 20' 1/2". Plugging that into the checker gives an angle of about 90.25°: the corner is open, and the far end of the 16 ft line needs to swing in roughly 13/16" toward the 12 ft line.</p>
<table><thead><tr><th>Multiple</th><th>Side A</th><th>Side B</th><th>Diagonal</th><th>Good for</th></tr></thead><tbody>
<tr><td>×1</td><td>3</td><td>4</td><td>5</td><td>Cabinet bases, tile layout lines</td></tr>
<tr><td>×2</td><td>6</td><td>8</td><td>10</td><td>Wall plates, small decks</td></tr>
<tr><td>×3</td><td>9</td><td>12</td><td>15</td><td>Patios, garage slabs</td></tr>
<tr><td>×4</td><td>12</td><td>16</td><td>20</td><td>House footings, large decks</td></tr>
<tr><td>×5</td><td>15</td><td>20</td><td>25</td><td>Building corners, site layout</td></tr></tbody></table>
<h2>Field tips</h2>
<ul><li>Hook the tape on a nail or screw at the mark, not on a pencil line — a 1/16" slip at each end doubles the error.</li>
<li>Keep the tape level and taut. A tape that sags over a 20 ft diagonal reads long.</li>
<li>After squaring one corner, confirm the whole rectangle by comparing the two diagonals with the <a href="rectangle-diagonal-check.html">diagonal check calculator</a>.</li>
<li>Metric works the same way: 0.6 m / 0.8 m / 1.0 m or 3 m / 4 m / 5 m.</li></ul>""",
  "faqs": [
    ("Why does the 3-4-5 rule work?", "Because 3² + 4² = 9 + 16 = 25 = 5². By the converse of the Pythagorean theorem, any triangle whose sides satisfy a² + b² = c² has a right angle opposite the longest side."),
    ("Can I use other numbers than 3, 4 and 5?", "Yes. Any multiple works (6-8-10, 9-12-15), and so do other Pythagorean triples such as 5-12-13 or 8-15-17. You can also use any two lengths and compute the diagonal with this calculator."),
    ("How accurate is the 3-4-5 method?", "It is as accurate as your measurements. Using the longest practical multiple reduces error: a 1/8\" mistake on a 5 ft diagonal is about 0.2°, while on a 25 ft diagonal it is about 0.05°."),
    ("Does it work in metric?", "Yes. The ratio is unitless, so 3 m, 4 m and 5 m (or 300, 400 and 500 mm) give the same right angle."),
  ],
  "related": ["right-triangle-calculator", "rectangle-diagonal-check", "deck-board-calculator", "concrete-slab-calculator"],
 },
 {
  "slug": "right-triangle-calculator", "fn": "triangle", "cat": "Layout", "project": "framing",
  "title": "Right Triangle (Pythagorean) Calculator", "short": "Solve any right triangle from two sides: hypotenuse, angles, area.",
  "desc": "Pythagorean theorem calculator for builders. Enter any two sides of a right triangle to get the third side, both angles, the area and the perimeter.",
  "inputs": [
    ("a", "Side a (leg)", "ft", "m", 6, 1.8, "One of the two sides that meet at the right angle."),
    ("b", "Side b (leg)", "ft", "m", 8, 2.4, "The other side at the right angle."),
    ("c", "Hypotenuse c", "ft", "m", 0, 0, "The longest side. Leave at 0 if unknown."),
  ],
  "video": "pbf4lcJhIfI",
  "body": """
<p>Almost every layout problem on a job site — rafter lengths, stair stringers, diagonal braces, ramp lengths, squaring corners — is a right triangle in disguise. Enter any two sides and leave the unknown one at zero. The calculator returns the missing side, both acute angles, the area and the perimeter.</p>
<h2>The Pythagorean theorem</h2>
<p>In a right triangle, the square of the hypotenuse equals the sum of the squares of the two legs: <strong>a² + b² = c²</strong>. Rearranged, a missing leg is <strong>a = √(c² − b²)</strong>. The angles come from trigonometry: angle A = arctan(a ÷ b), and angle B = 90° − A.</p>
<h2>Worked example: a diagonal brace</h2>
<p>A gate frame is 4 ft wide and 6 ft tall. Its brace runs corner to corner, so c = √(4² + 6²) = √52 ≈ 7.211 ft, or about 7' 2-9/16". The brace meets the bottom rail at arctan(6 ÷ 4) ≈ 56.3°, which is the angle to set on your miter saw (as 33.7° from square on most saws).</p>
<h2>Where builders use it</h2>
<ul><li><strong>Rafters:</strong> run and rise are the legs; the rafter is the hypotenuse. See the <a href="rafter-length-calculator.html">rafter calculator</a>.</li>
<li><strong>Stairs:</strong> total rise and total run give the stringer length. See the <a href="stair-calculator.html">stair calculator</a>.</li>
<li><strong>Squaring:</strong> two wall lengths give the diagonal for a square corner. See the <a href="3-4-5-squaring-calculator.html">3-4-5 calculator</a>.</li>
<li><strong>Ramps:</strong> rise and horizontal length give the ramp surface length and slope angle.</li></ul>
<div class="callout">If you enter all three sides, the calculator tells you whether they actually form a right triangle — a quick way to check a frame you have already built.</div>""",
  "faqs": [
    ("Which side is the hypotenuse?", "The hypotenuse is always the longest side and is opposite the 90° angle. In a stair it is the stringer; in a roof it is the rafter."),
    ("Can I enter feet and inches?", "Enter decimal feet (for example 6.5 for 6' 6\"). Results show both decimal feet and feet-inches to the nearest 1/16\"."),
    ("What are common whole-number right triangles?", "3-4-5, 5-12-13, 8-15-17, 7-24-25 and 20-21-29 are the Pythagorean triples builders use most. Any multiple of these also works."),
  ],
  "related": ["3-4-5-squaring-calculator", "rafter-length-calculator", "stair-calculator", "roof-pitch-calculator"],
 },
 {
  "slug": "rectangle-diagonal-check", "fn": "rectangle", "cat": "Layout", "project": "foundation",
  "title": "Rectangle Diagonal Check Calculator", "short": "Compare two diagonals to prove a frame, slab or room is square.",
  "desc": "Check if a rectangle is square by comparing its diagonals. Get the ideal diagonal, the difference between measurements, and a tolerance verdict.",
  "inputs": [
    ("l", "Length", "ft", "m", 24, 7.2, "Long side of the frame or layout."),
    ("w", "Width", "ft", "m", 16, 4.8, "Short side."),
    ("d1", "Diagonal 1 measured", "ft", "m", 28.85, 8.65, "Corner to opposite corner."),
    ("d2", "Diagonal 2 measured", "ft", "m", 28.82, 8.66, "The other pair of corners."),
  ],
  "video": "8m-G9qrDpng",
  "body": """
<p>A rectangle is square only when both diagonals are equal. Squaring a single corner with 3-4-5 is not enough on its own, because the opposite sides might not be parallel or equal. Measuring both diagonals checks all four corners at once. This calculator gives the ideal diagonal, the difference between your two measurements, and whether that difference is inside a typical layout tolerance.</p>
<h2>How to check a layout</h2>
<ol><li>Confirm opposite sides are equal first. If the lengths differ, diagonals can be equal and the shape is still a trapezoid.</li>
<li>Measure corner to corner both ways, from the same reference point on each corner (outside of the form, centre of the string intersection, etc.).</li>
<li>If the diagonals differ, push the frame along the <strong>longer</strong> diagonal, or pull along the shorter one, by about half the difference. Re-measure.</li></ol>
<h2>Formula</h2>
<p>Ideal diagonal = √(length² + width²). For a 24 × 16 ft slab that is √832 ≈ 28.844 ft, or 28' 10-1/8".</p>
<h2>How square is square enough?</h2>
<p>Common layout practice for residential work is about 1/8" for runs under 10 ft and 1/4" from 10 ft to 100 ft. Cabinet and tile work want tighter numbers; rough site grading can live with more. Our <a href="../guides/layout-tolerances.html">tolerance guide</a> covers this in detail.</p>""",
  "faqs": [
    ("Why must opposite sides be equal before checking diagonals?", "A shape with unequal opposite sides can still have equal diagonals (an isosceles trapezoid). Equal sides plus equal diagonals guarantees a rectangle."),
    ("Which way do I push the frame?", "Push the corners that sit on the longer diagonal toward each other. That shortens the long diagonal and lengthens the short one until they match."),
    ("What tolerance should I use for a deck?", "Most deck builders aim for diagonals within 1/4\" on a typical 12–20 ft deck. Tighter is better for decking that runs parallel to the house."),
  ],
  "related": ["3-4-5-squaring-calculator", "right-triangle-calculator", "concrete-slab-calculator", "deck-board-calculator"],
 },
 {
  "slug": "concrete-slab-calculator", "fn": "concrete", "cat": "Concrete", "project": "concrete",
  "title": "Concrete Slab Calculator", "short": "Cubic yards, cubic metres and bag counts for slabs and pads.",
  "desc": "Concrete slab calculator: enter length, width and thickness to get cubic yards or cubic metres, 60 lb and 80 lb bag counts, and a ready-mix order with waste.",
  "inputs": [
    ("l", "Length", "ft", "m", 12, 3.6, "Inside of the forms."),
    ("w", "Width", "ft", "m", 10, 3, "Inside of the forms."),
    ("t", "Thickness", "in", "cm", 4, 10, "4\" (10 cm) for patios and walks, 5–6\" (13–15 cm) for driveways."),
    ("waste", "Waste allowance", "%", "%", 10, 10, "5–10% is typical."),
  ],
  "video": "QDKLkD4uDFE",
  "body": """
<p>Ordering too little concrete leaves a cold joint in the middle of your pour; ordering too much wastes money on material you cannot return. This calculator turns slab dimensions into an order: volume in cubic yards and cubic metres, the number of premix bags, and a ready-mix quantity rounded up to the quarter yard most plants deliver in.</p>
<h2>Formula</h2>
<p>Volume = length × width × thickness. In imperial units, convert thickness to feet (inches ÷ 12), multiply to get cubic feet, then divide by 27 for cubic yards. In metric, convert thickness to metres and the result is already in cubic metres.</p>
<h2>Worked example</h2>
<p>A 12 × 10 ft patio at 4" thick: 12 × 10 × (4 ÷ 12) = 40 ft³ ÷ 27 = 1.48 yd³. Add 10% and you need about 1.63 yd³ — order 1.75 yd³, or about 74 bags of 80 lb premix (each yields roughly 0.6 ft³).</p>
<h2>Bags or ready-mix?</h2>
<p>Under about 1 yd³, bagged concrete mixed on site is usually cheaper. Above 1.5–2 yd³, a ready-mix truck saves hours of mixing and gives a more consistent slab. Many plants have a short-load fee for small orders, so ask before you book.</p>
<h2>Thickness guide</h2>
<table><thead><tr><th>Use</th><th>Typical thickness</th></tr></thead><tbody>
<tr><td>Walkways, patios</td><td>4" / 100 mm</td></tr><tr><td>Shed or hot-tub pad</td><td>4–6" / 100–150 mm</td></tr>
<tr><td>Residential driveway</td><td>5–6" / 125–150 mm</td></tr><tr><td>Garage floor</td><td>4–6" / 100–150 mm</td></tr></tbody></table>
<p>Before forming, square the slab with the <a href="3-4-5-squaring-calculator.html">3-4-5 calculator</a> and confirm both diagonals match.</p>""",
  "faqs": [
    ("How many 80 lb bags make a cubic yard?", "About 45. Each 80 lb bag yields roughly 0.6 cubic feet, and a cubic yard is 27 cubic feet."),
    ("How much extra concrete should I order?", "5–10% covers spillage, an uneven base and forms that bow slightly. Use the higher end for hand-dug or uneven subgrade."),
    ("Is 4 inches thick enough for a driveway?", "For cars it can work on a well-compacted base, but 5–6 inches is the common recommendation for driveways, especially with heavier vehicles."),
  ],
  "related": ["footing-concrete-calculator", "3-4-5-squaring-calculator", "gravel-calculator", "rectangle-diagonal-check"],
 },
 {
  "slug": "footing-concrete-calculator", "fn": "footing", "cat": "Concrete", "project": "concrete",
  "title": "Post Hole & Footing Concrete Calculator", "short": "Concrete for round post holes and pier footings.",
  "desc": "Calculate concrete for round post holes, sonotubes and pier footings. Enter diameter, depth and number of holes to get volume and bag counts.",
  "inputs": [
    ("dia", "Hole diameter", "in", "cm", 12, 30, "Use the auger or form-tube diameter."),
    ("depth", "Hole depth", "in", "cm", 42, 110, "Usually below local frost depth."),
    ("n", "Number of holes", "", "", 9, 9, "Total posts or piers."),
    ("waste", "Waste allowance", "%", "%", 10, 10, "Holes are rarely perfect cylinders."),
  ],
  "video": "jC7FDqhoKXM",
  "body": """
<p>Deck piers, fence posts and pergola footings are all cylinders. This calculator finds the concrete in each one and the total for the job, so you buy the right number of bags in one trip.</p>
<h2>Formula</h2>
<p>Volume of a cylinder = π × r² × depth, where r is half the diameter. A 12" hole that is 42" deep holds π × 0.5² × 3.5 ≈ 2.75 ft³, or roughly 5 bags of 80 lb premix.</p>
<h2>Setting the footing depth</h2>
<p>Footings must reach below the local frost line so freeze-thaw cycles do not heave them. Frost depth ranges from a few inches in warm climates to more than 48" in cold ones; your local building department publishes the number. Bell-shaped bottoms and wider footing pads may also be required for deck loads.</p>
<h2>Layout first</h2>
<p>Pier locations must form a square grid or the beams will not sit straight. Set string lines on batter boards, square them with <a href="3-4-5-squaring-calculator.html">3-4-5</a>, and mark the hole centres where the strings cross. Our <a href="../guides/foundation-layout-batter-boards.html">batter board guide</a> walks through it.</p>""",
  "faqs": [
    ("How many bags of concrete per fence post?", "A typical 4x4 post in a 10\" × 36\" hole needs about 1.6 ft³ including the post, which is two to three 50 lb bags or two 80 lb bags."),
    ("Should the post sit in concrete or on gravel?", "Many builders put a few inches of gravel in the bottom for drainage, then concrete. Deck posts are often set on top of the pier with a metal base instead of being buried."),
    ("Does the calculator subtract the post volume?", "No. It returns the full hole volume; a 4x4 post displaces only about 0.11 ft³ per foot of depth, which is covered by the waste allowance."),
  ],
  "related": ["concrete-slab-calculator", "fence-calculator", "deck-board-calculator", "3-4-5-squaring-calculator"],
 },
 {
  "slug": "roof-pitch-calculator", "fn": "pitch", "cat": "Roofing", "project": "roofing",
  "title": "Roof Pitch Calculator", "short": "Pitch, angle, slope % and roof area from rise and run.",
  "desc": "Roof pitch calculator: enter rise and run to get pitch in x:12, angle in degrees, slope percentage, rafter multiplier and sloped roof area.",
  "inputs": [
    ("rise", "Rise", "in", "cm", 6, 15, "Vertical rise measured over the run."),
    ("run", "Run", "in", "cm", 12, 30, "Horizontal distance. 12\" is the convention in North America."),
    ("area", "Footprint area (optional)", "ft²", "m²", 1200, 110, "Plan area including overhangs, to estimate roof surface."),
  ],
  "video": "yb8mIvNGbgQ",
  "body": """
<p>Pitch tells you how steep a roof is, which decides the roofing material you can use, the length of every rafter, and how much surface you will be covering. Enter any rise and run — for example, hold a level 12" out from the roof and measure straight down to the surface — and the calculator converts it to every common format.</p>
<h2>Pitch, angle and slope</h2>
<ul><li><strong>Pitch</strong> is rise per 12 units of run: 6:12 means 6" of rise for every 12" horizontally.</li>
<li><strong>Angle</strong> is arctan(rise ÷ run). 6:12 is 26.57°.</li>
<li><strong>Slope</strong> as a percentage is rise ÷ run × 100. 6:12 is 50%.</li>
<li><strong>Rafter multiplier</strong> is √(1 + (rise ÷ run)²). Multiply plan area or horizontal run by it to get the sloped length or area.</li></ul>
<h2>Common pitches</h2>
<div class="table-scroll"><table><thead><tr><th>Pitch</th><th>Angle</th><th>Multiplier</th><th>Notes</th></tr></thead><tbody>
<tr><td>3:12</td><td>14.04°</td><td>1.031</td><td>Low slope, double underlayment</td></tr>
<tr><td>4:12</td><td>18.43°</td><td>1.054</td><td>Common ranch roofs</td></tr>
<tr><td>6:12</td><td>26.57°</td><td>1.118</td><td>Typical suburban gable</td></tr>
<tr><td>8:12</td><td>33.69°</td><td>1.202</td><td>Walkable with care</td></tr>
<tr><td>12:12</td><td>45.00°</td><td>1.414</td><td>Steep; staging required</td></tr></tbody></table></div>
<h2>Worked example</h2>
<p>A house footprint with overhangs measures 1,200 ft² and the pitch is 6:12. Roof area = 1,200 × 1.118 ≈ 1,342 ft², or 13.4 roofing squares (one square = 100 ft²). Add 10–15% for waste, hips and starter courses when ordering shingles.</p>""",
  "faqs": [
    ("What is the most common roof pitch?", "In North American houses, 4:12 to 9:12 covers most roofs, with 6:12 being very common."),
    ("What is the minimum pitch for asphalt shingles?", "Most manufacturers require at least 2:12, with special underlayment between 2:12 and 4:12. Below that, use a low-slope membrane."),
    ("How do I measure pitch from inside the attic?", "Hold a level horizontally against the underside of a rafter, mark 12\" along the level, and measure vertically from that mark up to the rafter. That number is the rise per 12."),
  ],
  "related": ["rafter-length-calculator", "right-triangle-calculator", "square-footage-calculator", "stair-calculator"],
 },
 {
  "slug": "rafter-length-calculator", "fn": "rafter", "cat": "Roofing", "project": "roofing",
  "title": "Rafter Length Calculator", "short": "Common rafter length, ridge height and plumb cut from span and pitch.",
  "desc": "Rafter length calculator for gable roofs. Enter building span, pitch and overhang to get rafter length, ridge rise, plumb-cut angle and stock length to buy.",
  "inputs": [
    ("span", "Building span (wall to wall)", "ft", "m", 24, 7.2, "Outside of wall to outside of wall."),
    ("pitch", "Pitch (rise per 12)", "", "", 6, 6, "6 means 6:12."),
    ("oh", "Overhang (horizontal)", "in", "cm", 12, 30, "Horizontal projection beyond the wall."),
  ],
  "video": "oTvPF4YesjY",
  "body": """
<p>A common rafter runs from the top of the wall to the ridge. Its length is the hypotenuse of a right triangle whose legs are the run (half the building span) and the rise (run × pitch ÷ 12). Add the overhang, also measured along the slope, and you have the board length to cut.</p>
<h2>Formula</h2>
<p>Run = span ÷ 2. Rafter multiplier = √(1 + (pitch ÷ 12)²). Rafter length = (run + overhang) × multiplier. Ridge rise = run × pitch ÷ 12.</p>
<h2>Worked example</h2>
<p>A 24 ft wide garage with a 6:12 roof and 12" overhangs: run = 12 ft, multiplier = 1.118, rafter = 13 × 1.118 ≈ 14.53 ft, about 14' 6-7/16". Buy 16 ft stock. The ridge sits 6 ft above the top plates (less the ridge-board deduction).</p>
<h2>Cuts to make</h2>
<ul><li><strong>Plumb cut</strong> at the ridge, at the roof angle (26.57° for 6:12) — set on a framing square using 6 and 12.</li>
<li><strong>Birdsmouth</strong> where the rafter sits on the wall plate: a seat cut no deeper than one-third of the rafter depth.</li>
<li><strong>Tail cut</strong> at the overhang, usually plumb for fascia.</li></ul>
<p>Lay out one pattern rafter, test-fit it on both sides of the building, then use it as a template for the rest.</p>""",
  "faqs": [
    ("What is the ridge-board deduction?", "Because rafters butt against a ridge board, shorten each one by half the ridge thickness measured perpendicular to the plumb cut — 3/4\" for a 1-1/2\" ridge board."),
    ("How deep can a birdsmouth be?", "A common rule is no deeper than one-third of the rafter depth, so the rafter keeps enough wood above the seat to carry the load."),
    ("Is this calculator suitable for hip rafters?", "No. Hip and valley rafters run at 45° in plan and use a different multiplier. This tool covers common rafters only."),
  ],
  "related": ["roof-pitch-calculator", "right-triangle-calculator", "board-feet-calculator", "stair-calculator"],
 },
 {
  "slug": "stair-calculator", "fn": "stairs", "cat": "Framing", "project": "stairs",
  "title": "Stair Calculator", "short": "Riser count, riser height, treads, total run and stringer length.",
  "desc": "Stair calculator: enter total rise to get the number of risers, exact riser height, tread count, total run, stringer length and code checks.",
  "inputs": [
    ("rise", "Total rise (floor to floor)", "in", "cm", 108, 274, "Finished floor to finished floor."),
    ("target", "Target riser height", "in", "cm", 7.25, 18, "7–7-3/4\" (178–196 mm) is typical."),
    ("tread", "Tread depth (run per step)", "in", "cm", 10.5, 27, "At least 10\" (254 mm) in most residential codes."),
  ],
  "video": "GYfRFOBgZsU",
  "body": """
<p>Stairs are where small math errors become trip hazards. Every riser must be the same height — codes typically allow only about 3/8" variation between the tallest and shortest riser. This calculator divides your total rise into equal risers, then works out treads, total run and stringer length.</p>
<h2>How the numbers work</h2>
<ol><li>Number of risers = total rise ÷ target riser, rounded up.</li>
<li>Actual riser height = total rise ÷ number of risers.</li>
<li>Number of treads = risers − 1 (the top floor is the last "tread").</li>
<li>Total run = treads × tread depth.</li>
<li>Stringer length = √(total rise² + total run²) — the Pythagorean theorem again.</li></ol>
<h2>Worked example</h2>
<p>Total rise is 108" with a 7-1/4" target: 108 ÷ 7.25 = 14.9, so 15 risers at exactly 7.2" (7-3/16"). That gives 14 treads; at 10-1/2" each, the total run is 147". The stringer is √(108² + 147²) ≈ 182.4", so cut from 2×12 stock at least 16 ft long.</p>
<h2>Comfort rule</h2>
<p>Two risers plus one tread should land between about 24" and 25" (610–635 mm). Steps in that range match a natural stride. The calculator shows this number so you can trade a little riser height for tread depth.</p>
<div class="callout">Code limits vary by country and municipality. The checks here use widely adopted residential figures (max riser 7-3/4", min tread 10"). Always confirm with your local building department.</div>""",
  "faqs": [
    ("How do I measure total rise?", "Measure from the finished surface of the lower floor to the finished surface of the upper floor. If flooring is not installed yet, add its thickness at both ends."),
    ("Why is there one fewer tread than risers?", "The upper floor acts as the final step, so a stair with 15 risers has 14 treads."),
    ("What size lumber do stringers need?", "Most residential stringers are cut from 2×12. After notching, at least 3-1/2\" to 5\" of solid wood should remain below the notches, depending on code and span."),
  ],
  "related": ["right-triangle-calculator", "board-feet-calculator", "deck-board-calculator", "rafter-length-calculator"],
 },
 {
  "slug": "deck-board-calculator", "fn": "deck", "cat": "Decks & fences", "project": "deck",
  "title": "Deck Board Calculator", "short": "Boards, linear feet, joists and screws for a rectangular deck.",
  "desc": "Deck board calculator: enter deck size, board width, gap and board length to get board count, linear footage, joists and screws.",
  "inputs": [
    ("l", "Deck length (board direction)", "ft", "m", 16, 4.8, "The direction the boards run."),
    ("w", "Deck width (across boards)", "ft", "m", 12, 3.6, "Measured across the boards."),
    ("bw", "Board width (actual)", "in", "mm", 5.5, 140, "A 5/4×6 or 2×6 is 5-1/2\" actual."),
    ("gap", "Gap between boards", "in", "mm", 0.1875, 5, "3/16\" (5 mm) is common."),
    ("bl", "Board length", "ft", "m", 16, 4.8, "Stock length you will buy."),
    ("waste", "Waste allowance", "%", "%", 10, 10, "10% straight, 15% for patterns."),
  ],
  "video": "C8mDz-5dI-A",
  "body": """
<p>Decking is sold by the piece, so the useful answer is not square footage — it is how many boards of a given length to put on the truck. This calculator counts rows of boards across the deck, pieces per row, and adds your waste factor. It also estimates joists at 16" (400 mm) on centre and the screws needed at every crossing.</p>
<h2>Method</h2>
<ul><li>Rows = deck width ÷ (board width + gap), rounded up.</li>
<li>Pieces per row = deck length ÷ board length, rounded up.</li>
<li>Boards = rows × pieces × (1 + waste).</li>
<li>Screws = rows × joists × 2.</li></ul>
<h2>Worked example</h2>
<p>A 16 × 12 ft deck with 5-1/2" boards and 3/16" gaps: each row takes 5.6875", so 12 ft (144") needs 26 rows. With 16 ft boards there is one piece per row, so 26 boards plus 10% = 29 boards. Joists at 16" o.c. over 16 ft = 13 joists, and 26 × 13 × 2 ≈ 710 screws.</p>
<h2>Square it before the first board</h2>
<p>An out-of-square deck shows up immediately in the last board, which ends up tapered. Square the ledger and rim joists with the <a href="3-4-5-squaring-calculator.html">3-4-5 calculator</a> and confirm diagonals with the <a href="rectangle-diagonal-check.html">diagonal check</a>. Our <a href="../guides/how-to-square-a-deck.html">deck squaring guide</a> shows the full sequence.</p>""",
  "faqs": [
    ("What gap should I leave between deck boards?", "Around 3/16\" (5 mm) is common for kiln-dried and composite boards. Wet pressure-treated boards are often butted tight because they shrink as they dry. Follow the board maker's instructions."),
    ("What joist spacing do I need?", "16\" on centre is standard for most wood and composite decking laid perpendicular. Diagonal decking and some composites need 12\"."),
    ("Should I buy longer boards to avoid joints?", "Yes, when possible. Full-length boards look better and need fewer butt joints, and each joint must land on a joist, often with blocking."),
  ],
  "related": ["3-4-5-squaring-calculator", "footing-concrete-calculator", "rectangle-diagonal-check", "board-feet-calculator"],
 },
 {
  "slug": "fence-calculator", "fn": "fence", "cat": "Decks & fences", "project": "fence",
  "title": "Fence Calculator", "short": "Posts, rails, pickets and concrete for a straight-run fence.",
  "desc": "Fence material calculator: enter fence length, post spacing, rails and picket size to get posts, rails, pickets and concrete bags.",
  "inputs": [
    ("len", "Fence length", "ft", "m", 100, 30, "Total run, excluding gates."),
    ("sp", "Post spacing", "ft", "m", 8, 2.4, "6–8 ft (1.8–2.4 m) is typical."),
    ("gates", "Number of gates", "", "", 1, 1, "Each gate usually adds a post."),
    ("rails", "Rails per section", "", "", 2, 2, "2 for fences under 5 ft, 3 for taller."),
    ("pw", "Picket width", "in", "mm", 5.5, 140, "Actual width."),
    ("pg", "Gap between pickets", "in", "mm", 0.5, 12, "0 for a privacy fence."),
  ],
  "video": "jC7FDqhoKXM",
  "body": """
<p>A fence is a row of repeated sections, so material counts come straight from the length and post spacing. This calculator gives posts (including gates), rails, pickets with a 5% allowance, and a two-bags-per-post concrete estimate.</p>
<h2>Method</h2>
<ul><li>Sections = length ÷ post spacing, rounded up.</li><li>Posts = sections + 1 + gates.</li>
<li>Rails = sections × rails per section.</li><li>Pickets = length ÷ (picket width + gap) + 5%.</li></ul>
<h2>Layout tips</h2>
<p>Set corner and end posts first and pull a mason's line between them at the top and bottom. Where the fence turns a corner, square it with 3-4-5 on the line before digging. Check your property line and call your local utility-locate service before digging — it is free and required in many places.</p>""",
  "faqs": [
    ("How far apart should fence posts be?", "8 ft is the maximum for most wood fences; 6 ft gives a sturdier fence in windy areas or with heavy boards."),
    ("How deep should fence posts go?", "A common rule is one-third to one-half of the above-ground height, and below the frost line in cold climates."),
    ("Does the picket count include gates?", "No. Gates are built separately; add their pickets based on gate width."),
  ],
  "related": ["footing-concrete-calculator", "3-4-5-squaring-calculator", "deck-board-calculator", "board-feet-calculator"],
 },
 {
  "slug": "tile-calculator", "fn": "tile", "cat": "Finishes", "project": "flooring",
  "title": "Tile Calculator", "short": "Tiles and boxes for floors, walls and backsplashes.",
  "desc": "Tile calculator: enter area and tile size with grout joint and waste to get the number of tiles and boxes to buy.",
  "inputs": [
    ("l", "Area length", "ft", "m", 10, 3, ""), ("w", "Area width", "ft", "m", 8, 2.4, ""),
    ("tl", "Tile length", "in", "cm", 12, 30, ""), ("tw", "Tile width", "in", "cm", 24, 60, ""),
    ("g", "Grout joint", "in", "mm", 0.125, 3, "1/16–1/4\" (2–6 mm)."),
    ("waste", "Waste", "%", "%", 10, 10, "15% for diagonal or herringbone."),
    ("box", "Tiles per box", "", "", 8, 8, "From the box label."),
  ],
  "video": "A2ahtESv6kg",
  "body": """
<p>Tile layout starts with square reference lines. If the first row is out of square, every grout line after it wanders, and the error is obvious at the far wall. Snap two perpendicular lines through the centre of the room and check them with 3-4-5 before setting a single tile. Then use this calculator to buy the right number of boxes.</p>
<h2>Method</h2>
<p>Each tile covers (tile length + joint) × (tile width + joint). Area ÷ coverage per tile gives the count; the waste factor covers cuts, breakage and spares. Divide by tiles per box and round up.</p>
<h2>Waste factors</h2>
<table><thead><tr><th>Pattern</th><th>Waste</th></tr></thead><tbody><tr><td>Straight lay, simple room</td><td>10%</td></tr><tr><td>Brick / offset</td><td>10–12%</td></tr><tr><td>Diagonal</td><td>15%</td></tr><tr><td>Herringbone</td><td>15–20%</td></tr></tbody></table>
<p>Keep at least one unopened box from the same lot for future repairs — dye lots change and a matching tile can be impossible to find later.</p>""",
  "faqs": [
    ("How do I square tile lines in a room?", "Snap a centreline along the room, mark 3 ft from the centre point on that line and 4 ft on a perpendicular line, and adjust until the diagonal reads 5 ft. Use 6-8-10 for larger rooms."),
    ("Does grout width really change the count?", "With small tiles, yes. A 1/4\" joint on 4\" tile adds about 12% coverage per tile, so you need noticeably fewer tiles."),
    ("Should I buy extra for a backsplash?", "Yes. Backsplashes have many cuts around outlets and windows; 15% is a safer waste allowance."),
  ],
  "related": ["flooring-calculator", "square-footage-calculator", "3-4-5-squaring-calculator", "paint-calculator"],
 },
 {
  "slug": "flooring-calculator", "fn": "flooring", "cat": "Finishes", "project": "flooring",
  "title": "Flooring Calculator", "short": "Boxes of laminate, vinyl plank or hardwood plus underlayment.",
  "desc": "Flooring calculator for laminate, vinyl plank and hardwood. Enter room size, waste and box coverage to get boxes and underlayment.",
  "inputs": [("l", "Room length", "ft", "m", 14, 4.2, ""), ("w", "Room width", "ft", "m", 12, 3.6, ""),
             ("waste", "Waste", "%", "%", 10, 10, ""), ("box", "Coverage per box", "ft²", "m²", 20, 1.9, "From the box label.")],
  "video": None,
  "body": """
<p>Plank flooring is sold by the box, and each product lists coverage per box. Measure the room, add waste for end cuts, and divide by the box coverage. For L-shaped rooms, split the room into rectangles and add them in the <a href="square-footage-calculator.html">square footage calculator</a> first.</p>
<h2>Before you install</h2>
<ul><li>Check that the room is square: measure both diagonals. A room that is out of square needs the first row scribed to the wall, not set tight against it.</li>
<li>Leave the expansion gap the manufacturer specifies at every wall, usually 1/4–1/2" (6–12 mm).</li>
<li>Stagger end joints by at least 6–12" (150–300 mm) between rows.</li></ul>""",
  "faqs": [("How much waste for flooring?", "Use 5–10% for straight installs in simple rooms and 15% for diagonal installs or rooms with many corners."),
           ("Do I need underlayment?", "Most laminate and many floating floors require it unless the planks have it pre-attached. Glue-down and nail-down floors use different preparation.")],
  "related": ["tile-calculator", "square-footage-calculator", "paint-calculator", "drywall-calculator"],
 },
 {
  "slug": "paint-calculator", "fn": "paint", "cat": "Finishes", "project": "painting",
  "title": "Paint Calculator", "short": "Gallons or litres of paint and primer for a room.",
  "desc": "Room paint calculator: enter room size, doors, windows and coats to get the paint and primer needed in gallons or litres.",
  "inputs": [("l", "Room length", "ft", "m", 14, 4.2, ""), ("w", "Room width", "ft", "m", 12, 3.6, ""), ("h", "Wall height", "ft", "m", 8, 2.4, ""),
             ("doors", "Doors", "", "", 1, 1, ""), ("windows", "Windows", "", "", 2, 2, ""), ("coats", "Coats", "", "", 2, 2, ""),
             ("select", "ceil", "Include ceiling", [("0", "No"), ("1", "Yes")], ""),
             ("cov", "Coverage", "ft²/gal", "m²/L", 350, 10, "350–400 ft² per gallon is typical.")],
  "video": None,
  "body": """
<p>Paint coverage depends on surface area, not floor area. This calculator works out the wall area from the room perimeter and height, subtracts standard door and window sizes, optionally adds the ceiling, and multiplies by the number of coats.</p>
<h2>Formula</h2>
<p>Wall area = 2 × (length + width) × height − openings. Paint = area × coats ÷ coverage. A 14 × 12 ft room with 8 ft walls has 416 ft² of wall; less one door and two windows leaves 344 ft². Two coats at 350 ft²/gal needs just under 2 gallons.</p>
<h2>Tips</h2><ul><li>Prime new drywall, patched areas and strong colour changes.</li><li>Buy all paint for one room at once so the tint matches.</li><li>Dark or saturated colours often need a third coat.</li></ul>""",
  "faqs": [("How much does a gallon of paint cover?", "Most interior paints list 350–400 ft² per gallon (about 9–10 m² per litre) for one coat on smooth, primed walls."),
           ("Should I paint the ceiling the same colour?", "Usually ceilings get flat white ceiling paint. Set 'Include ceiling' to yes only if you are using the same paint.")],
  "related": ["drywall-calculator", "square-footage-calculator", "flooring-calculator", "tile-calculator"],
 },
 {
  "slug": "drywall-calculator", "fn": "drywall", "cat": "Finishes", "project": "drywall",
  "title": "Drywall Calculator", "short": "Sheets, tape, compound and screws for a room.",
  "desc": "Drywall calculator: enter room dimensions and sheet size to get drywall sheets, joint tape, ready-mix compound and screws.",
  "inputs": [("l", "Room length", "ft", "m", 14, 4.2, ""), ("w", "Room width", "ft", "m", 12, 3.6, ""), ("h", "Wall height", "ft", "m", 8, 2.4, ""),
             ("select", "ceil", "Include ceiling", [("1", "Yes"), ("0", "No")], ""),
             ("select", "sheet", "Sheet size", [("1", "4×8 ft / 1.2×2.4 m"), ("2", "4×12 ft / 1.2×3.0 m")], ""),
             ("open", "Openings to deduct", "ft²", "m²", 40, 4, "Doors and windows combined.")],
  "video": None,
  "body": """
<p>Drywall estimates start with surface area: every wall plus the ceiling, minus large openings. Divide by the sheet area and add 10% for cuts. Longer 12 ft sheets mean fewer butt joints and less finishing, but they are heavier to hang.</p>
<h2>Finishing materials</h2>
<p>For finishing, a long-standing industry ratio is roughly 370 ft of tape and 138 lb of ready-mixed joint compound per 1,000 ft² of board. A 4.5 gal pail of ready-mix weighs about 62 lb. Screws run around 32 per 4×8 sheet on walls with 16" framing.</p>
<h2>Square framing helps</h2>
<p>Out-of-square wall corners leave tapered gaps at inside corners and make taping harder. Check corners with 3-4-5 when framing and fix them before the board goes up.</p>""",
  "faqs": [("What thickness of drywall should I use?", "1/2\" is standard for walls; 5/8\" is common for ceilings with wide joist spacing and for fire-rated assemblies."),
           ("How many screws per sheet?", "Roughly 28–32 for a 4×8 sheet on walls; ceilings use closer spacing, so plan on more.")],
  "related": ["paint-calculator", "square-footage-calculator", "flooring-calculator", "board-feet-calculator"],
 },
 {
  "slug": "gravel-calculator", "fn": "gravel", "cat": "Landscape", "project": "landscaping",
  "title": "Gravel, Mulch & Soil Calculator", "short": "Cubic yards, tonnes and bags of gravel, mulch, topsoil or sand.",
  "desc": "Gravel calculator for driveways, paths and garden beds. Get cubic yards or cubic metres, weight in tons or tonnes, and bag counts for gravel, mulch, topsoil or sand.",
  "inputs": [("l", "Length", "ft", "m", 20, 6, ""), ("w", "Width", "ft", "m", 10, 3, ""), ("depth", "Depth", "in", "cm", 4, 10, "Compacted base: 4–6\" (10–15 cm)."),
             ("select", "mat", "Material", [("1", "Gravel / crushed stone"), ("2", "Mulch"), ("3", "Topsoil"), ("4", "Sand")], "")],
  "video": "QDKLkD4uDFE",
  "body": """
<p>Bulk landscape material is ordered by volume (cubic yards or cubic metres) or by weight (tons or tonnes). This calculator gives both, using typical dry densities, plus a bag count for smaller jobs.</p>
<h2>Typical densities used</h2>
<table><thead><tr><th>Material</th><th>US tons per yd³</th><th>Tonnes per m³</th></tr></thead><tbody>
<tr><td>Gravel / crushed stone</td><td>1.4</td><td>1.66</td></tr><tr><td>Mulch</td><td>0.4</td><td>0.47</td></tr>
<tr><td>Topsoil</td><td>1.1</td><td>1.3</td></tr><tr><td>Sand</td><td>1.35</td><td>1.6</td></tr></tbody></table>
<h2>Depth guide</h2><ul><li>Base under pavers or slabs: 4–6" compacted.</li><li>Gravel path: 2–3" over a base.</li><li>Mulch beds: 2–3".</li><li>New lawn topsoil: 4–6".</li></ul>
<p>Compacted crushed stone shrinks by roughly 15–20%, so add that when the material will be compacted.</p>""",
  "faqs": [("How many tons is a cubic yard of gravel?", "About 1.4 US tons for typical crushed stone, though it ranges from 1.2 to 1.7 depending on stone type and moisture."),
           ("How many bags of mulch equal a yard?", "A cubic yard is 27 ft³, so about 13.5 bags of 2 ft³ mulch.")],
  "related": ["concrete-slab-calculator", "square-footage-calculator", "fence-calculator", "3-4-5-squaring-calculator"],
 },
 {
  "slug": "square-footage-calculator", "fn": "area", "cat": "Layout", "project": "general",
  "title": "Square Footage Calculator", "short": "Area of rooms and L-shapes, in ft² and m², with cost.",
  "desc": "Square footage calculator: add up to three rectangles and a triangle to get total area in square feet and square metres, plus project cost.",
  "inputs": [("l1", "Rectangle 1 length", "ft", "m", 14, 4.2, ""), ("w1", "Rectangle 1 width", "ft", "m", 12, 3.6, ""),
             ("l2", "Rectangle 2 length", "ft", "m", 0, 0, "Optional."), ("w2", "Rectangle 2 width", "ft", "m", 0, 0, ""),
             ("l3", "Rectangle 3 length", "ft", "m", 0, 0, "Optional."), ("w3", "Rectangle 3 width", "ft", "m", 0, 0, ""),
             ("tb", "Triangle base", "ft", "m", 0, 0, "Optional."), ("th", "Triangle height", "ft", "m", 0, 0, ""),
             ("price", "Price per unit area", "$/ft²", "$/m²", 0, 0, "Optional.")],
  "video": "pbf4lcJhIfI",
  "body": """
<p>Most rooms are rectangles or combinations of rectangles. Break the space into pieces, measure each, and add them together. A bay or angled wall can be handled as a triangle (base × height ÷ 2).</p>
<h2>Measuring tips</h2><ul><li>Measure at floor level, wall to wall, and round up to the next inch or centimetre.</li>
<li>For an L-shaped room, split it into two rectangles that do not overlap.</li><li>1 m² = 10.764 ft².</li></ul>
<p>Once you know the area, take it to the <a href="flooring-calculator.html">flooring</a>, <a href="tile-calculator.html">tile</a> or <a href="paint-calculator.html">paint</a> calculators.</p>""",
  "faqs": [("How do I find the square footage of an L-shaped room?", "Divide it into two rectangles, multiply length by width for each, and add the results."),
           ("How do I convert square feet to square metres?", "Divide square feet by 10.764. To go the other way, multiply square metres by 10.764.")],
  "related": ["flooring-calculator", "tile-calculator", "paint-calculator", "concrete-slab-calculator"],
 },
 {
  "slug": "board-feet-calculator", "fn": "boardfeet", "cat": "Framing", "project": "framing",
  "title": "Board Feet Calculator", "short": "Board feet, cubic volume and cost of lumber.",
  "desc": "Board foot calculator for lumber and hardwood. Enter thickness, width, length and quantity to get board feet, volume and total cost.",
  "inputs": [("t", "Thickness", "in", "mm", 2, 50, "Nominal for rough hardwood (4/4 = 1)."), ("w", "Width", "in", "mm", 6, 150, ""),
             ("l", "Length", "ft", "m", 8, 2.4, ""), ("q", "Quantity", "", "", 10, 10, ""), ("price", "Price", "$/bd ft", "$/m³", 0, 0, "Optional.")],
  "video": "pbf4lcJhIfI",
  "body": """
<p>A board foot is a volume of wood 1" thick, 12" wide and 12" long — 144 cubic inches. Hardwood and many lumber yards price by the board foot, so knowing the count lets you compare prices and estimate a project.</p>
<h2>Formula</h2><p>Board feet = thickness (in) × width (in) × length (ft) ÷ 12. Ten 2×6 boards 8 ft long: 2 × 6 × 8 ÷ 12 × 10 = 80 board feet.</p>
<p>One cubic metre equals about 423.8 board feet.</p>""",
  "faqs": [("Do I use nominal or actual size?", "For rough hardwood, use the nominal thickness (4/4, 8/4). Many yards also price dimensional softwood on nominal sizes. Check how your supplier quotes."),
           ("What does 4/4 mean?", "Quarter-inch notation: 4/4 is 1\" rough, 5/4 is 1-1/4\", 8/4 is 2\".")],
  "related": ["rafter-length-calculator", "stair-calculator", "deck-board-calculator", "drywall-calculator"],
 },
 {
  "slug": "brick-calculator", "fn": "brick", "cat": "Masonry", "project": "masonry",
  "title": "Brick Calculator", "short": "Bricks and mortar for a wall, with openings deducted.",
  "desc": "Brick calculator: enter wall size, openings, brick size and mortar joint to get the number of bricks and an estimate of mortar bags.",
  "inputs": [("l", "Wall length", "ft", "m", 20, 6, ""), ("h", "Wall height", "ft", "m", 4, 1.2, ""), ("open", "Openings to deduct", "ft²", "m²", 0, 0, ""),
             ("bl", "Brick length", "in", "mm", 7.625, 215, "US modular 7-5/8\"; UK/EU 215 mm."), ("bh", "Brick height", "in", "mm", 2.25, 65, ""),
             ("j", "Mortar joint", "in", "mm", 0.375, 10, "3/8\" (10 mm) standard."), ("waste", "Waste", "%", "%", 5, 5, "")],
  "video": "8m-G9qrDpng",
  "body": """
<p>Bricks per unit area depend on brick face size plus one mortar joint in each direction. A US modular brick (7-5/8" × 2-1/4") with 3/8" joints lays at roughly 6.75–6.9 bricks per ft² depending on the exact joint; a metric 215 × 65 mm brick with 10 mm joints lays at about 59 per m².</p>
<h2>Square the corners</h2><p>Masonry corners are built first and the wall is strung between them, so an out-of-square corner shifts the whole wall. Lay out corners with 3-4-5 on the footing and check diagonals before the first course.</p>
<p>Mortar here uses a common rule of thumb of around seven bags of masonry cement per 1,000 bricks; your mix, joint size and brick type change this, so treat it as a starting estimate.</p>""",
  "faqs": [("How many bricks in a square metre?", "About 60 standard UK/EU bricks (215 × 65 mm) with 10 mm joints, for a single-skin wall."),
           ("How many bricks per square foot?", "Roughly 6.75–6.9 US modular bricks with 3/8\" joints, single wythe, depending on the exact joint size.")],
  "related": ["concrete-slab-calculator", "3-4-5-squaring-calculator", "footing-concrete-calculator", "square-footage-calculator"],
 },
]
