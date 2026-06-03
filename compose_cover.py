"""Compose the A4 cover: Scarfe cover art + overlaid title typography."""
from PIL import Image, ImageDraw, ImageFont, ImageChops
from pathlib import Path

D = Path("/home/iman/data-management/figures-draft")
art = Image.open(D / "00_cover_art.png").convert("RGB")

# --- crop to the bright CREAM PAGE interior, excluding the grey mat AND its
#     drop-shadow gradient (cream is bright >205; mat & shadow are darker) ---
gray = art.convert("L")
bbox = gray.point(lambda p: 255 if p > 205 else 0).getbbox()
if bbox:
    x0, y0, x1, y1 = bbox
    pad = max(3, int(0.006 * art.size[0]))     # inset past any soft shadow at the page edge
    art = art.crop((x0 + pad, y0 + pad, x1 - pad, y1 - pad))

cream = art.getpixel((art.size[0] // 2, 8))   # cream from the clean top band

# A4 @150dpi canvas in cream; reserve a clean top band for the title, fit art below it
W, H = 1240, 1754
TOP_BAND = 560
canvas = Image.new("RGB", (W, H), cream)
aw, ah = art.size
avail_h = H - TOP_BAND
scale = avail_h / ah
nw, nh = int(aw * scale), int(ah * scale)
if nw > W:                                       # don't exceed page width
    scale = W / aw; nw, nh = W, int(ah * scale)
art_s = art.resize((nw, nh), Image.LANCZOS)
canvas.paste(art_s, ((W - nw) // 2, H - nh))     # centre-x, bottom-aligned; cream band on top
d = ImageDraw.Draw(canvas)

def font(paths, size):
    for p in paths:
        try: return ImageFont.truetype(p, size)
        except OSError: continue
    return ImageFont.load_default()

TITLE_PATHS = ["/usr/share/fonts/truetype/adf/BerenisADFPro-Bold.otf",
               "/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Bold.ttf",
               "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"]
SUB  = font(["/usr/share/fonts/truetype/adf/BerenisADFPro-Italic.otf",
             "/usr/share/fonts/truetype/paratype/PTF56F.ttf",
             "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"], 48)
AUTH = font(["/usr/share/fonts/truetype/adf/BerenisADFPro-Regular.otf",
             "/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Regular.ttf",
             "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"], 44)

INK, TEAL = (26, 24, 22), (24, 110, 108)
MAXW = W * 0.84
TRACK = 3

def line_w(txt, fnt, track):
    return sum(d.textlength(c, font=fnt) for c in txt) + track * (len(txt) - 1)

# largest title size whose widest line fits MAXW
size = 176
while size > 90:
    t = font(TITLE_PATHS, size)
    if max(line_w("THE SEMANTIC", t, TRACK), line_w("ENTERPRISE", t, TRACK)) <= MAXW:
        break
    size -= 4
TITLE = font(TITLE_PATHS, size)

def centre(txt, fnt, y, fill, track=0):
    total = line_w(txt, fnt, track)
    x = (W - total) / 2
    for c in txt:
        d.text((x, y), c, font=fnt, fill=fill); x += d.textlength(c, font=fnt) + track

asc = int(size * 1.12)
centre("THE SEMANTIC", TITLE, 56, INK, TRACK)
centre("ENTERPRISE",   TITLE, 56 + asc, INK, TRACK)
y2 = 56 + 2 * asc + 26
centre("Data Architecture for the Agentic Era", SUB, y2, TEAL)
d.line([(W/2 - 170, y2 + 74), (W/2 + 170, y2 + 74)], fill=TEAL, width=3)
centre("Iman Poernomo", AUTH, y2 + 98, INK)

out = D / "00_cover_final.png"
canvas.save(out)
print(f"ok {out} ({out.stat().st_size//1024} KB, {canvas.size}, title={size}px)")
