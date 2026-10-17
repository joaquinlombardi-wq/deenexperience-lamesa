# Generated maps used by the scenes: napkin fold creases, soft ink/embroidery masks, wax-seal heightmap, logo mask.
# Run from fuentes/render/tex after rendering the HTML textures (see ../README.md).
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
rng = np.random.default_rng(3)
n = 2048; y, x = np.mgrid[0:n, 0:n] / n
def wob(t, k, a):
    s = np.zeros_like(t)
    for i in range(1, 4): s += np.sin(t*np.pi*2*i*k + rng.uniform(0, 6.28))*a/i
    return s
def crease(d, w, amp): return amp*np.exp(-(d/w)**2)
h = np.zeros((n, n))
h += crease(x-0.5-wob(y, 1.3, .004), 0.010, -1.0)
h += crease(y-0.5-wob(x, 1.1, .004), 0.012, 0.85)
h += crease(x-0.25-wob(y, 1.7, .003), 0.008, 0.45) + crease(x-0.75-wob(y, 1.5, .003), 0.008, 0.40)
h += crease(y-0.25-wob(x, 1.9, .003), 0.007, -0.35)
h += 0.25*np.sin(x*np.pi*4)**2*np.sin(y*np.pi*2)**2
h = (h-h.min())/(h.max()-h.min())
Image.fromarray((h*65535).astype(np.uint16)).save('napkin_crease.png')
Image.open('napkin_ink.png').convert('L').filter(ImageFilter.GaussianBlur(1.6)).save('napkin_ink_soft.png')
emb = Image.open('napkin_emb.png').convert('L'); emb.save('napkin_emb_l.png'); emb.filter(ImageFilter.GaussianBlur(7)).save('napkin_emb_soft.png')
# wax seal
rng = np.random.default_rng(11); n = 1024
yy, xx = (np.mgrid[0:n, 0:n]-n/2)/(n/2); rho = np.hypot(xx, yy); th = np.arctan2(yy, xx)
r = 0.80 + sum(rng.uniform(.006, .022)*np.sin(k*th + rng.uniform(0, 6.3)) for k in range(2, 9))
t = np.clip(rho/r, 0, 1.2)
with np.errstate(invalid='ignore'): hs = np.where(t < 1, (1-t**5)**0.33, 0)*0.62
inner = 0.56; press = np.clip((rho-inner)/0.02, 0, 1)
hs = np.where(rho < inner+0.02, 0.46+0.14*press, hs)
hs = hs + np.exp(-((rho-(inner-0.035))/0.012)**2)*0.10*(rho < inner)
img = Image.new('L', (n, n), 0); d = ImageDraw.Draw(img)
f = ImageFont.truetype('../fonts/InstrumentSerif-Italic.ttf', 430)
bb = d.textbbox((0, 0), 'LM', font=f); w = bb[2]-bb[0]; hh = bb[3]-bb[1]
d.text(((n-w)/2-bb[0]-6, (n-hh)/2-bb[1]-10), 'LM', font=f, fill=255)
hs = hs + np.array(img.filter(ImageFilter.GaussianBlur(2.2)))/255.0*0.12*(rho < inner)
hs = np.clip(hs + np.where(rho < r, rng.normal(0, 0.002, (n, n)), 0), 0, 1)
Image.fromarray((hs*65535).astype(np.uint16)).save('seal_h.png')
Image.fromarray(((rho < r)*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1)).save('seal_mask.png')
# logo mask (white on transparent) for the blind deboss on the invitation
a = np.array(Image.open('../../../assets/img/deenex-wordmark-ink.png').convert('RGBA')); a[..., :3] = 255
Image.fromarray(a).save('deenex-mask.png')
print('textures ok')
