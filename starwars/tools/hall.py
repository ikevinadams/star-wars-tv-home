"""The saga's room: img/hall.jpg, a dark hall in the Jedi Temple with a long stone ledge (generated: src/gen/hall1.png),
cropped to 16:9. The ledge's top runs at y 672-705 and x 135-1785 on the 1920 stage; the hilts stand on it at y 692."""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = Image.open(os.path.join(ROOT, "src", "gen", "hall1.png")).convert("RGB")
w, h = im.size
cw = round(h * 16 / 9); x0 = (w - cw) // 2
im.crop((x0, 0, x0 + cw, h)).resize((2560, 1440), Image.LANCZOS).save(os.path.join(ROOT, "img", "hall.jpg"), quality=86, optimize=True, progressive=True)
print("ok")
