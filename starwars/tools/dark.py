"""The dark side's pictures: Vader on the bridge of a star destroyer, and through its windows a different place for each title.
img/dark/bridge.png    the bridge and Vader with the window glass cut out (src/gen/vader_green.png: vader_nb1.png with the
                       windows made flat green, so the glass is exactly the green)
img/dark/view-N.jpg    what's outside, one per title, in story order (edits of the empty bridge, src/gen/bridge2.png): Mustafar
                       (Obi-Wan Kenobi), Coruscant at night (Andor S1), the battle station being built (Andor S2), Scarif
                       (Rogue One). Only their windows are kept, lined up with the bridge and spread out past
                       the frames, so none of their own frames can show at the edge of the glass.
Prints where the glass is, for the page."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEN, OUT = os.path.join(ROOT, "src", "gen"), os.path.join(ROOT, "img", "dark")
VIEWS = ["vmust1.png", "vcity1.png", "vbuild3.png", "vscarif4b.png"]
W, H = 2560, 1440                                                     # 1.33x the 1920 stage


def wide(src):
    im = Image.open(os.path.join(GEN, src)).convert("RGB")
    w, h = im.size
    cw = round(h * 16 / 9); x0 = (w - cw) // 2
    return np.asarray(im.crop((x0, 0, x0 + cw, h)).resize((W, H), Image.LANCZOS), np.float32)


# ---------------------------------------------------------------- the bridge: key out the green
fg = wide("vader_green.png")
r, g, b = fg[..., 0], fg[..., 1], fg[..., 2]
green = g - np.maximum(r, b)                                          # the glass reads ~250; the frames, Vader and the room under 20
m = Image.fromarray(((green > 110) * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3))
# keep only the six panes (the consoles have small green lamps)
lab = m.copy(); panes = []
for y in range(8, H // 2, 16):
    for x in range(8, W, 16):
        if lab.getpixel((x, y)) != 255: continue
        ImageDraw.floodfill(lab, (x, y), 128)
        region = np.asarray(lab) == 128
        if region.sum() > 20000: panes.append(region)
        ImageDraw.floodfill(lab, (x, y), 0)
panes.sort(key=lambda p: np.nonzero(p)[1].mean())
glass = np.any(panes, axis=0)
# soft edge from the green itself, only around the panes
near = np.asarray(Image.fromarray((glass * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(7))) > 0
key = np.clip((green - 30) / 150, 0, 1) * near
key = np.maximum(key, glass * 1.0)
alpha = 1 - np.asarray(Image.fromarray((key * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.7)), np.float32) / 255
# the green spills onto the edges of the frames and Vader's cape: take it back out there
band = np.asarray(Image.fromarray((glass * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(13))) > 0
cap = np.maximum(r, b) * 1.02
fg[..., 1] = np.where(band, np.minimum(g, cap), g)
os.makedirs(OUT, exist_ok=True)
Image.fromarray(np.dstack([fg, alpha * 255]).astype(np.uint8)).save(os.path.join(OUT, "bridge.png"), optimize=True)

# each pane filled across its width row by row, so the glass behind Vader counts too
whole = np.zeros((H, W), bool)
for p in panes:
    for y in np.nonzero(p.any(1))[0]:
        xs = np.nonzero(p[y])[0]; whole[y, xs[0]:xs[-1] + 1] = True
inner = np.asarray(Image.fromarray((whole * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(9))) > 0   # a hair inside their frames


def spread(img, ok):
    """Fill everything outside `ok` from the nearest pixels inside it (push-pull), so the picture carries on past its windows."""
    ps, ms = [img * ok[..., None]], [ok.astype(np.float32)]
    while ms[-1].shape[0] > 6:
        h, w = ms[-1].shape; size = (max(1, w // 2), max(1, h // 2))
        ms.append(np.asarray(Image.fromarray(ms[-1]).resize(size, Image.BOX)))
        ps.append(np.dstack([np.asarray(Image.fromarray(ps[-1][..., c]).resize(size, Image.BOX)) for c in range(3)]))
    res = ps[-1] / np.maximum(ms[-1], 1e-4)[..., None]
    for p, mm in zip(ps[-2::-1], ms[-2::-1]):
        h, w = mm.shape
        up = np.dstack([np.asarray(Image.fromarray(res[..., c]).resize((w, h), Image.BILINEAR)) for c in range(3)])
        res = p + up * (1 - mm)[..., None]
    return res


# ---------------------------------------------------------------- the views
gray = lambda a: a.mean(2)
fgg = gray(fg)
room = ~np.asarray(Image.fromarray((whole * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(41))).astype(bool)
room[:, int(W * .55):int(W * .72)] = False                            # not Vader
room[:int(H * .1)] = False
for n, src in enumerate(VIEWS):
    v = wide(src)
    vg = gray(v)
    # line the view's own room up with the bridge's (they're edits of one picture, but drift by a few pixels)
    best = None
    for dy in range(-16, 17, 2):
        for dx in range(-16, 17, 2):
            e = np.abs(np.roll(vg, (dy, dx), (0, 1))[room] - fgg[room]).mean()
            if best is None or e < best[0]: best = (e, dx, dy)
    _, bx, by = best
    for dy in range(by - 1, by + 2):
        for dx in range(bx - 1, bx + 2):
            e = np.abs(np.roll(vg, (dy, dx), (0, 1))[room] - fgg[room]).mean()
            if e < best[0]: best = (e, dx, dy)
    e, dx, dy = best
    v = np.roll(v, (dy, dx), (0, 1))
    out = spread(v, inner)
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(os.path.join(OUT, f"view-{n}.jpg"), quality=88, optimize=True, progressive=True)
    print(f"view-{n}.jpg  {src}  shift {dx:+d} {dy:+d}  (room error {e:.1f})")

# where the glass is, on the 1920 stage
s = 1920 / W
ys, xs = np.nonzero(whole)
print("glass: x %d-%d, y %d-%d, centre (%d, %d)" % (xs.min() * s, xs.max() * s, ys.min() * s, ys.max() * s, xs.mean() * s, ys.mean() * s))
for i, p in enumerate(panes):
    py, px = np.nonzero(p)
    print("pane", i, "x %d-%d y %d-%d" % (px.min() * s, px.max() * s, py.min() * s, py.max() * s))
