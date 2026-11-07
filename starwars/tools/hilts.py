"""The six hilts (one per film, I to VI), stood upright (emitter on top), trimmed and sized alike: img/hilts/<key>.png, at 2x the size they're shown.
Source renders (Wookieepedia / Lucasfilm databank) are in src/hilts/. emitter: where the blade end is in the source picture."""
import json, os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(HERE, "..", "src", "hilts"); OUT = os.path.join(HERE, "..", "img", "hilts")
HILTS = {   # key: (source, which end the emitter is in the source, length on screen in px)
    "maul":   ("darth_maul_lightsaber_db.png", "right", 470),
    "yoda":   ("yodaslightsaber_databank.png", "left", 205),        # Yoda's is short, as in the films
    "windu":  ("windu_lightsaber_db.png", "right", 300),
    "kenobi": ("kenobithirdlightsaber_db.png", "topleft", 300),
    "vader":  ("vaderslightsaber_db.png", "left", 300),
    "luke6":  ("lukeskywalkerlightsaber_swe.png", "topleft", 300),
}
# not used: skywalker.png is the Skywalker saber as rebuilt for The Force Awakens (the wrap over the clamp), not the Empire prop
HINT = {"right": (1, 0), "left": (-1, 0), "top": (0, -1), "topleft": (-1, -1)}
meta = {}
for key, (src, end, length) in HILTS.items():
    im = Image.open(os.path.join(SRC, src)).convert("RGBA")
    a = np.asarray(im)[..., 3] > 40
    ys, xs = np.nonzero(a)
    pts = np.stack([xs, ys], 1).astype(float); c = pts.mean(0)
    w, v = np.linalg.eigh(np.cov((pts - c).T)); axis = v[:, np.argmax(w)]            # the hilt's long axis
    if axis @ np.array(HINT[end], float) < 0: axis = -axis                           # point it at the emitter
    ang = np.degrees(np.arctan2(axis[1], axis[0]))                                   # image coords: y down
    # rotate so the emitter points straight up (-90 degrees)
    rot = im.rotate(ang + 90, resample=Image.BICUBIC, expand=True)
    bb = rot.getbbox(); rot = rot.crop(bb)
    k = (length * 2) / rot.height
    rot = rot.resize((max(1, round(rot.width * k)), length * 2), Image.LANCZOS)
    rot.save(os.path.join(OUT, key + ".png"), optimize=True)
    meta[key] = {"w": rot.width / 2, "h": rot.height / 2}
    print(key, "turned", round(ang + 90, 1), "deg ->", rot.size)
json.dump(meta, open(os.path.join(OUT, "hilts.json"), "w"))
