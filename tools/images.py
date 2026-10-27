"""Generate raster images (Open Graph card + apple touch icon). Requires Pillow."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
os.makedirs(IMG, exist_ok=True)

def font(bold, size):
    for p in (["/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"] if bold
              else ["/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    try:
        return ImageFont.load_default(size)
    except TypeError:
        return ImageFont.load_default()

W, H = 1200, 630
im = Image.new("RGB", (W, H), "#EDEFF0")
d = ImageDraw.Draw(im)
d.rectangle([0, 0, W, 40], fill="#F5B800")
for x in range(0, W, 12):
    d.line([x, 0, x, 10 if x % 96 else 28], fill="#1D2329", width=2 if x % 96 == 0 else 1)
d.text((70, 120), "000345", font=font(True, 150), fill="#1D2329")
d.text((74, 300), "Start at zero. Square it with 3-4-5.", font=font(True, 52), fill="#1D2329")
d.text((74, 380), "Free construction & layout calculators  ·  ft + m", font=font(False, 36), fill="#4A535C")
ox, oy = 860, 560
d.line([ox, oy, ox + 280, oy], fill="#1D2329", width=10)
d.line([ox, oy, ox, oy - 210], fill="#1D2329", width=10)
d.line([ox, oy - 210, ox + 280, oy], fill="#2357C6", width=6)
d.text((ox + 120, oy + 8), "4", font=font(True, 40), fill="#1D2329")
d.text((ox - 40, oy - 130), "3", font=font(True, 40), fill="#1D2329")
d.text((ox + 150, oy - 150), "5", font=font(True, 40), fill="#2357C6")
d.line([ox + 28, oy, ox + 28, oy - 28, ox, oy - 28], fill="#1E7A46", width=4)
im.save(os.path.join(IMG, "og.png"), optimize=True)

ic = Image.new("RGB", (180, 180), "#F5B800")
d = ImageDraw.Draw(ic)
d.line([40, 140, 40, 40], fill="#1D2329", width=14)
d.line([40, 140, 140, 140], fill="#1D2329", width=14)
d.line([40, 40, 140, 140], fill="#1D2329", width=14)
d.line([40, 112, 68, 112, 68, 140], fill="#2357C6", width=10)
ic.save(os.path.join(IMG, "apple-touch-icon.png"))
print("images written")
