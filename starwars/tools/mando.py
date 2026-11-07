"""The Mandalorian section's pictures: img/mando/.
camp.jpg   the scene, cropped to 16:9
holo-*.png the four posters (TMDB) as blue holograms: light where the poster is light, see-through where it's dark"""
import os
import numpy as np
from PIL import Image, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = os.path.join(ROOT, "src", "mando"), os.path.join(ROOT, "img", "mando")
os.makedirs(OUT, exist_ok=True)

# the camp: a grassy valley at night, Din Djarin and Grogu by the fire, the four pucks on a stone (src/gen/camp2.png,
# generated in two steps: the empty valley, then the two of them added in place)
im = Image.open(os.path.join(ROOT, "src", "gen", "camp2.png")).convert("RGB")
w, h = im.size
cw = round(h * 16 / 9); x0 = (w - cw) // 2
im.crop((x0, 0, x0 + cw, h)).resize((2560, 1440), Image.LANCZOS).save(os.path.join(OUT, "camp.jpg"), quality=86, optimize=True, progressive=True)

# the holograms
HW, HH = 390, 585
for key in ["s1", "s2", "s3", "film"]:
    im = Image.open(os.path.join(SRC, "posters", key + ".jpg")).convert("RGB")
    im = ImageOps.fit(im, (HW, HH), Image.LANCZOS)
    lum = np.asarray(ImageOps.autocontrast(im.convert("L"), cutoff=1), dtype=np.float32) / 255
    lum = np.clip((lum - .06) / .94, 0, 1) ** 1.15
    # every other line a little fainter, like a projected picture
    lines = np.where(np.arange(HH)[:, None] % 3 == 0, .55, 1.0)
    a = np.clip(lum * .92 * lines + .05, 0, 1)
    tint = np.array([95, 190, 255], np.float32) / 255
    rgb = tint[None, None, :] * (1 - lum[..., None] ** 2 * .7) + lum[..., None] ** 2 * .7       # the bright parts go to white
    out = np.dstack([rgb * 255, a * 255]).astype(np.uint8)
    holo = Image.fromarray(out)
    # the edges fade out
    fade = Image.new("L", (HW, HH), 0)
    fade.paste(255, (14, 14, HW - 14, HH - 14))
    fade = fade.filter(ImageFilter.GaussianBlur(10))
    holo.putalpha(Image.fromarray((np.asarray(holo.getchannel("A"), np.float32) * np.asarray(fade, np.float32) / 255).astype(np.uint8)))
    holo.save(os.path.join(OUT, f"holo-{key}.png"), optimize=True)


print("ok")
