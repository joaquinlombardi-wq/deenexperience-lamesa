# Photographic finish for the La Mesa set: violet split-tone in the shadows, vignette, highlight bloom, fine grain → WebP.
import sys, numpy as np
from PIL import Image, ImageFilter
src, dst = sys.argv[1], sys.argv[2]
maxw = int(sys.argv[3]) if len(sys.argv) > 3 else 2000
vig = float(sys.argv[4]) if len(sys.argv) > 4 else 0.20
im = Image.open(src)
a = np.asarray(im).astype(np.float32)
a = a / (65535.0 if a.max() > 255 else 255.0)
a = a[..., :3]
H, W, _ = a.shape
luma = (0.2126*a[..., 0] + 0.7152*a[..., 1] + 0.0722*a[..., 2])[..., None]
# split tone: shadows lean to Deenex violet, highlights stay neutral
violet = np.array([0x5B, 0x49, 0xD8], np.float32)/255.0
w = np.clip(1.0 - luma*2.2, 0, 1)**2 * 0.10
a = a*(1-w) + (a*0.5 + violet*luma*0.9 + violet*0.025)*w
# bloom on highlights
hi = np.clip((luma - 0.78)/0.22, 0, 1) * a
bl = np.asarray(Image.fromarray((np.clip(hi, 0, 1)*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(W*0.012))).astype(np.float32)/255.0
a = 1 - (1 - a)*(1 - bl*0.22)
# vignette
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
r = np.sqrt(((xx - W/2)/(W/2))**2 + ((yy - H/2)/(H/2))**2) / np.sqrt(2)
a = a * (1 - vig*np.clip(r, 0, 1)**2.2)[..., None]
# resize then grain (grain at output pixel scale)
img = Image.fromarray((np.clip(a, 0, 1)*255 + 0.5).astype(np.uint8))
if W > maxw: img = img.resize((maxw, round(H*maxw/W)), Image.LANCZOS)
b = np.asarray(img).astype(np.float32)/255.0
rng = np.random.default_rng(7)
g = rng.normal(0, 1, b.shape[:2]).astype(np.float32)
g = np.asarray(Image.fromarray(((g*0.5+0.5)*255).clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.45))).astype(np.float32)/255.0 - 0.5
lum = b.mean(axis=2, keepdims=True)
b = b + g[..., None]*0.028*(0.35 + 0.65*np.sin(np.pi*np.clip(lum, 0, 1)))
out = Image.fromarray((np.clip(b, 0, 1)*255 + 0.5).astype(np.uint8))
out.save(dst, 'WEBP', quality=90, method=6)
print(dst, out.size)
