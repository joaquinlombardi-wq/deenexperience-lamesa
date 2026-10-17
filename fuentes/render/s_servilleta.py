import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from lib import *
random.seed(4)
reset(); setup(1800, 1200, samples=128, exposure=-0.3, look='AgX - Medium High Contrast')
world_color(hexc('#140F22'), 0.04)

# --- tablecloth (dark ink linen) ---
tc = grid('Mantel', 2.4, 2.4, 160, 160)
displace_noise(tc, 0.35, 0.006, depth=2)
mt = m_linen('Mantel', hexc('#17122B'), threads=2600, sheen=0.6, rough=0.9, bump=0.5, color_var=0.12, heather=0.16)
assign(tc, mt.m)

# --- napkin ---
nap = grid('Servilleta', 0.46, 0.46, 360, 360, loc=(-0.075, 0.0, 0.0042), rot=(0, 0, math.radians(-11)))
displace_img(nap, TEX + 'napkin_crease.png', 0.0078, mid=0.5)
displace_noise(nap, 0.09, 0.0018, depth=2)
solidify(nap, 0.0009); subsurf(nap, 1)

mb = m_linen('Servilleta', hexc('#F0EDF6'), threads=620, sheen=0.55, rough=0.86, bump=0.6, color_var=0.06, heather=0.09)
uv = mb.coord('UV')
# hem: 1 cm double-fold border with a stitch groove
sep = mb.n('ShaderNodeSeparateXYZ'); mb.L(uv, sep.inputs[0])
u, v = sep.outputs[0], sep.outputs[1]
du = mb.math('MINIMUM', u, mb.math('SUBTRACT', 1.0, u)); dv = mb.math('MINIMUM', v, mb.math('SUBTRACT', 1.0, v))
d = mb.math('MINIMUM', du, dv)
hem = mb.maprange(d, 0.0205, 0.0232, 1.0, 0.0)
groove = mb.math('EXPONENT', mb.math('MULTIPLY', -1.0, mb.math('POWER', mb.math('DIVIDE', mb.math('SUBTRACT', d, 0.0192), 0.0009), 2.0)))
# ink (felt tip): soft mask, broken by the weave
ink_t = mb.img(TEX + 'napkin_ink_soft.png', uv)
ink_n = mb.noise(mb.coord('Object'), 260, detail=3)
ink = mb.math('MULTIPLY', ink_t.outputs['Color'], mb.maprange(mb.math('ADD', mb.math('MULTIPLY', mb.weave, 0.6), mb.math('MULTIPLY', ink_n, 0.4)), 0.2, 0.75, 0.82, 1.08))
ink = mb.math('MINIMUM', mb.math('MULTIPLY', ink, 1.9), 1.0)
# embroidery: satin stitch, raised, violet thread
emb_t = mb.img(TEX + 'napkin_emb_l.png', uv); emb = emb_t.outputs['Color']
emb_s = mb.img(TEX + 'napkin_emb_soft.png', uv).outputs['Color']
satin = mb.wave(mb.coord('UV', scale=(1, 1, 1), rot=(0, 0, math.radians(38))), 260, 'X', distortion=0.6, detail=1)
# base colour stack
base_link = mb.b.inputs['Base Color'].links[0].from_socket
col = mb.mixc(mb.math('MULTIPLY', hem, 0.35), base_link, hexc('#DAD4E2'))
col = mb.mixc(ink, col, hexc('#17141F'))
thread = mb.mixc(satin, hexc('#2A1E8C'), hexc('#4B3BC6'))
# raised thread casts a fine shadow away from the key (key comes from -x,+y)
emb_sh = mb.img(TEX + 'napkin_emb_soft.png', mb.coord('UV', scale=(1, 1, 1))).outputs['Color']
mp_sh = mb.n('ShaderNodeMapping'); mp_sh.inputs['Location'].default_value = (-0.0024, 0.0024, 0)
tc_sh = mb.n('ShaderNodeTexCoord'); mb.L(tc_sh.outputs['UV'], mp_sh.inputs['Vector'])
sh_t = mb.img(TEX + 'napkin_emb_soft.png', mp_sh.outputs['Vector']).outputs['Color']
shadow = mb.math('MULTIPLY', mb.math('MAXIMUM', mb.math('SUBTRACT', sh_t, emb), 0.0), 0.55)
col = mb.mixc(shadow, col, hexc('#8E87A0'))
col = mb.mixc(emb, col, thread)
mb.to('Base Color', col)
mb.to('Roughness', mb.mixf(emb, mb.mixf(ink, 0.86, 0.74), 0.5))
mb.to('Sheen Weight', mb.mixf(emb, 0.55, 0.18))
mb.to('Anisotropic', mb.mixf(emb, 0.0, 0.75))
mb.b.inputs['Anisotropic Rotation'].default_value = 0.105
# height stack: weave -> hem/groove -> embroidery
h = mb.math('ADD', mb.math('MULTIPLY', hem, 0.6), mb.math('MULTIPLY', groove, -0.5))
h = mb.math('ADD', h, mb.math('MULTIPLY', emb_s, 2.6))
h = mb.math('ADD', h, mb.math('MULTIPLY', mb.math('MULTIPLY', emb, satin), 0.9))
n2 = mb.bump(h, 0.9, 0.0016, normal=mb.nrm)
mb.to('Normal', n2)
assign(nap, mb.m)

# --- pen: black lacquer barrel, brass trims ---
prof = [(0, 0), (0.0030, 0.0004), (0.0052, 0.004), (0.0062, 0.012), (0.0064, 0.060), (0.0066, 0.0612), (0.0066, 0.0636), (0.0064, 0.0648),
        (0.0062, 0.110), (0.0056, 0.128), (0.0040, 0.1365), (0.0012, 0.1395), (0, 0.1398)]
pen = lathe('Pluma', smooth_profile(prof, 3), seg=64)
pmb = MB('Laca'); pmb.set(Base_Color=hexc('#0B0A0E'), Roughness=0.25, Coat_Weight=1.0, Coat_Roughness=0.02)
assign(pen, pmb.m)
brass = m_metal('Bronce', hexc('#C9A462'), rough=0.18, var=0.07)
ring = lathe('Anillo', [(0.00655, 0.0598), (0.00675, 0.0600), (0.00675, 0.0648), (0.00655, 0.0650)], seg=64); assign(ring, brass.m)
clip = box('Clip', (0.0026, 0.0012, 0.045), loc=(0, 0.0071, 0.112), bevel=0.0005); assign(clip, brass.m)
cap_top = lathe('Remate', smooth_profile([(0, 0.1394), (0.0032, 0.1393), (0.0036, 0.1405), (0, 0.1412)], 2), seg=48); assign(cap_top, brass.m)
pen_parts = [pen, ring, clip, cap_top]
empty = bpy.data.objects.new('PenRig', None); link_obj(empty)
for p in pen_parts: p.parent = empty
empty.rotation_euler = (math.radians(90), 0, math.radians(-28 + 90))
empty.location = (0.255, -0.115, 0.0066)
empty.rotation_euler = Euler((math.radians(-90), 0, math.radians(68)), 'XYZ')

# --- wine glass with a little red wine (top-left, partly out of frame) ---
gp = [(0, 0), (0.038, 0.0), (0.040, 0.0015), (0.036, 0.003), (0.012, 0.006), (0.0045, 0.012), (0.0036, 0.03), (0.0036, 0.085),
      (0.006, 0.095), (0.030, 0.115), (0.045, 0.150), (0.046, 0.175), (0.040, 0.215), (0.0375, 0.228), (0.0368, 0.2285),
      (0.0362, 0.228), (0.0388, 0.214), (0.0445, 0.175), (0.0438, 0.150), (0.029, 0.117), (0.006, 0.0985), (0, 0.098)]
g = lathe('Copa', smooth_profile(gp, 3), seg=128)
g.location = (0.315, 0.215, 0.0)
assign(g, m_glass('Cristal', tint=(0.985, 0.99, 0.99, 1)).m)
wp = [(0, 0.0988), (0.0062, 0.0993), (0.0295, 0.1172), (0.0402, 0.134), (0, 0.134)]
wine = lathe('Vino', smooth_profile(wp, 2), seg=128); wine.location = g.location
wmb = m_liquid('Vino', hexc('#3B0614')); wmb.set(Roughness=0.0)
assign(wine, wmb.m)

# --- light: soft window from upper-left, warm low fill, grazing kicker for thread sheen ---
area('Key', (-0.75, 0.6, 0.9), (-0.05, 0, 0), 26, 0.9, 0.6, temp=5200, spread=60)
area('Fill', (0.9, -0.6, 0.9), (0, 0, 0), 10, 1.2, temp=3000)
area('Kick', (0.9, -0.15, 0.16), (0.1, 0.0, 0.0), 5, 0.5, 0.2, temp=3400)
area('Violet', (-0.8, -0.9, 0.35), (0, 0, 0), 9, 0.8, color=hexc('#5B49D8'))

camera((0.0, -0.14, 1.3), (0.01, 0.0, 0.0), lens=50, fstop=4.0)
render('servilleta')
