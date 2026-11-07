"""The cockpit: the Millennium Falcon's cockpit (generated from a film reference) with its windows cut out, so the space
drawn behind it shows through the canopy. Two versions: python3 cockpit.py 1 (img/cockpit.png, from the back of the
cockpit) or 2 (img/cockpit2.png, from the pilots' seats, more canopy). Prints where the glass is, row by row.
The windows were generated pure black: they're the large, near-black areas in the top of the picture."""
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = sys.argv[1] if len(sys.argv) > 1 else "1"
SRC = os.path.join(ROOT, "src", "gen", {"1": "cockpit1.png", "2": "pilot1.png"}[V])
OUT = os.path.join(ROOT, "img", {"1": "cockpit.png", "2": "cockpit2.png"}[V])
GLASS_TO = {"1": .64, "2": .84}[V]                                    # how far down the picture the glass can reach
W, H = 2560, 1440                                                     # 1.33x the 1920 stage

im = Image.open(SRC).convert("RGB")
w, h = im.size
cw = round(h * 16 / 9); x0 = (w - cw) // 2
im = im.crop((x0, 0, x0 + cw, h)).resize((W, H), Image.LANCZOS)
a = np.asarray(im, np.float32)
# the glass reads 0-4; the shadowed walls beside the console 6-30, so judge each spot by its neighbourhood
mx = Image.fromarray(a.max(axis=2).astype(np.uint8)).filter(ImageFilter.GaussianBlur(4))
limit = np.full((H, 1), 4.5)
if V == "2": limit[:] = 8; limit[:int(H * .42)] = 10                  # this one's glass has a faint haze (up to 9); its walls read 12 and up
dark = (np.asarray(mx) <= limit) & (np.arange(H)[:, None] < H * GLASS_TO)
if V == "1": dark[int(H * .445):int(H * .6), int(W * .26):int(W * .352)] = False   # a shadowed wall left of the centre pane, not glass
if V == "2":                                                           # below the middle, glass only inside the canopy: the side walls are dark too
    yy, xx = np.mgrid[0:H, 0:W]
    inside = ((xx - W * .5) / (W * .172)) ** 2 + ((yy - H * .48) / (H * .345)) ** 2 < 1      # the round outer frame
    dark &= (yy < H * .5) | inside
m = Image.fromarray((dark * 255).astype(np.uint8))
m = m.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))        # close up the film grain inside the panes

# keep only the big areas (the panes); drop dark specks on the frames and console
lab = m.copy(); keep = Image.new("L", (W, H), 0)
arr = np.asarray(lab)
for y in range(8, int(H * GLASS_TO), 16):
    for x in range(8, W, 16):
        if lab.getpixel((x, y)) != 255: continue
        ImageDraw.floodfill(lab, (x, y), 128)
        region = np.asarray(lab) == 128
        if region.sum() > 4000:
            keep.paste(255, mask=Image.fromarray((region * 255).astype(np.uint8)))
        ImageDraw.floodfill(lab, (x, y), 0)
# a hair inside the frame's edge, softened, so the frames keep their own dark rim
keep = keep.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.1))
alpha = 255 - np.asarray(keep)
Image.fromarray(np.dstack([np.asarray(im), alpha]).astype(np.uint8)).save(OUT, optimize=True)

k = np.asarray(keep) > 128
print(os.path.basename(OUT), W, H, "glass %.0f%%" % (k.mean() * 100))
s = 1920 / W
for y in range(80, 1080, 40):
    row = k[int(y / s)]; runs = []; x = 0
    while x < W:
        if row[x]:
            x0 = x
            while x < W and row[x]: x += 1
            if x - x0 > 20: runs.append((int(x0 * s), int(x * s)))
        else: x += 1
    print(y, runs)
