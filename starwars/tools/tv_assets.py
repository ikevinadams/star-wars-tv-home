"""Copies the Star Wars home into the TV app (starwars-tv/app/src/main/assets/www), sized for a 1080p TV:
  - the page, its settings (config.js), the logos, the hilts and the holograms as they are
  - the 2560 px pictures at the size the screen shows them: the cockpit at 1960 px (it's drawn 2% larger than the
    screen), the hall, the camp and the bridge at 1920, and of the views through its windows only the part behind the glass
  - only the cockpit the page uses on the TV (img/cockpit.png; cockpit2 needs a keyboard to pick)
Also makes the app's banner (the bridge over Mustafar). Run by build.sh before the APK is built."""
import os, re, shutil, subprocess, sys, tempfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, ".."))
APP = os.path.normpath(os.path.join(SRC, "..", "starwars-tv", "app", "src", "main"))
OUT = os.path.join(APP, "assets", "www")

# never ship a page whose script doesn't parse: on the TV that's a frozen screen
page = open(os.path.join(SRC, "index.html")).read()
with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as js:
    js.write(open(os.path.join(SRC, "config.js")).read() + "\n" + "\n".join(re.findall(r"<script>(.*?)</script>", page, re.S)))
try:
    check = subprocess.run(["node", "--check", js.name], capture_output=True, text=True)
except FileNotFoundError:
    check = None
    print("node not found: skipping the script check")
os.unlink(js.name)
if check and check.returncode:
    sys.exit("index.html has a script error, not building:\n" + check.stderr)

shutil.rmtree(OUT, ignore_errors=True)
for d in ("img/logos", "img/hilts", "img/mando", "img/dark"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)


def copy(rel):
    shutil.copy2(os.path.join(SRC, rel), os.path.join(OUT, rel))


copy("index.html")
copy("config.js")
for d in ("img/logos", "img/hilts"):
    for f in os.listdir(os.path.join(SRC, d)):
        if f.endswith(".png"): copy(f"{d}/{f}")
for k in ("s1", "s2", "s3", "film"):
    copy(f"img/mando/holo-{k}.png")


def sized(rel, w, h, **save):
    Image.open(os.path.join(SRC, rel)).resize((w, h), Image.LANCZOS).save(os.path.join(OUT, rel), **save)


sized("img/cockpit.png", 1960, 1102, optimize=True)            # 1920 x 1.0208 (OVER in the page)
sized("img/dark/bridge.png", 1920, 1080, optimize=True)
for rel in ("img/hall.jpg", "img/mando/camp.jpg"):
    sized(rel, 1920, 1080, quality=88, optimize=True, progressive=True)
for i in range(4):                                             # only what can show through the glass (VIEW in the page)
    rel = f"img/dark/view-{i}.jpg"
    Image.open(os.path.join(SRC, rel)).resize((1920, 1080), Image.LANCZOS).crop((368, 136, 1920, 604)).save(
        os.path.join(OUT, rel), quality=90, optimize=True, progressive=True)

# the banner in the TV's app list
fg = Image.open(os.path.join(SRC, "img/dark/bridge.png")).convert("RGBA")
bg = Image.open(os.path.join(SRC, "img/dark/view-0.jpg")).convert("RGBA")
Image.alpha_composite(bg, fg).convert("RGB").resize((320, 180), Image.LANCZOS).save(
    os.path.join(APP, "res", "drawable-nodpi", "banner.jpg"), quality=92)

size = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(OUT) for f in fs)
print("www:", round(size / 1e6, 1), "MB")
