import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from lib import *
random.seed(5)
reset(); setup(2400, 1350, samples=160, exposure=-0.5, look='AgX - Medium High Contrast', glass=True)
world_color(hexc('#0A0812'), 0.02)

slab = box('Marmol', (1.4, 0.7, 0.03), loc=(0, 0.05, -0.015), bevel=0.002)
assign(slab, m_marble('Marmol', base=hexc('#0B0A10'), vein=hexc('#3E3A4A')).m)

crystal = m_glass('Cristal', tint=(0.99, 0.995, 0.995, 1), smudge=True)
bglass = m_glass('VidrioBotella', tint=(0.93, 0.97, 0.965, 1), smudge=True)
water = m_liquid_vol('Agua', (0.75, 0.92, 0.95, 1), 0.6)
wine = m_liquid_vol('Vino', (0.62, 0.035, 0.09, 1), 85.0, ior=1.345)

b = bottle('Botella', loc=(-0.095, 0.075, 0)); assign(b, bglass.m)
bw = bottle_water('AguaBotella', 0.205, loc=(-0.095, 0.075, 0)); assign(bw, water.m)
# stopper: brushed steel cap
cap = cyl('Tapa', 0.0168, 0.018, loc=(-0.095, 0.075, 0.2905), seg=96, bevel=0.0012)
assign(cap, m_metal('Acero', hexc('#B9B7BE'), rough=0.22, var=0.05, aniso=0.6).m)

wg = wine_glass('Copa', loc=(0.072, 0.03, 0)); assign(wg, crystal.m)
wl = wine_glass_liquid('VinoCopa', 0.1335, loc=(0.072, 0.03, 0)); assign(wl, wine.m)

tb = tumbler('Vaso', loc=(-0.005, -0.075, 0)); assign(tb, crystal.m)
tw = tumbler_water('AguaVaso', loc=(-0.005, -0.075, 0)); assign(tw, water.m)

# violet field far behind (defocused), strip lights for edges, warm glint
emissive_plane('Fondo', (0.05, 1.8, 0.30), (math.radians(90), 0, 0), (2.2, 1.2), hexc('#7547D8'), 0.6)
area('StripL', (-0.55, 0.35, 0.28), (-0.05, 0.03, 0.12), 26, 0.07, 0.9, temp=6200)
area('StripR', (0.55, 0.38, 0.30), (0.05, 0.03, 0.12), 22, 0.07, 0.9, temp=6200)
area('Top', (0.0, -0.1, 0.9), (0, 0.02, 0.0), 18, 0.9, 0.5, temp=5000, spread=50)
area('Warm', (0.45, -0.2, 0.25), (0.072, 0.03, 0.13), 1.6, 0.12, temp=2300)

camera((0.0, -1.32, 0.19), (-0.008, 0.0, 0.142), lens=75, fstop=7.1, focus=1.33)
render('copas')
