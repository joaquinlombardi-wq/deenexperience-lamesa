import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from props import *
random.seed(21)
reset(); setup(2000, 1125, samples=96, exposure=-0.75, look='AgX - Medium High Contrast', glass=True)
world_color(hexc('#0B0913'), 0.01)

TC = (0.0, 0.58)   # table centre; our cover sits at the near edge, centred on origin
for o in round_table('Mesa', r=0.86): o.location.x += TC[0]; o.location.y += TC[1]

# hero cover
place_setting('Cubierto', menu=True, placecard=TEX + 'placecard.png', glasses=True, cutlery=True)

# other covers around the table (out of focus)
for k in range(1, 6):
    a = -math.pi/2 + k*2*math.pi/6
    cx, cy = TC[0] + 0.58*math.cos(a), TC[1] + 0.58*math.sin(a)
    ps = place_setting('Cub%d' % k, menu=False, placecard=None, glasses=True, cutlery=False, water=(k % 2 == 0), napkin_rot=random.uniform(-4, 4))
    ps.location = (cx, cy, 0); ps.rotation_euler = (0, 0, a + math.pi/2)

# centre: candles + Deenex tablet on its stand
for i, (dx, dy, h) in enumerate([(-0.10, 0.06, 0.13), (-0.03, -0.03, 0.09), (0.09, 0.07, 0.16)]):
    c = candle('Vela%d' % i, r=0.03, h=h); c.location = (TC[0] + dx + 0.06, TC[1] + dy + 0.02, 0)
tb = tablet_on_stand('Deenex'); tb.location = (TC[0] - 0.20, TC[1] - 0.10, 0); tb.rotation_euler = (0, 0, math.radians(14))

# far room: other tables suggested by candle points and violet screens (bokeh)
for (x, y, z, kind) in [(-2.2, 3.4, 0.12, 'c'), (-1.9, 3.6, 0.1, 'c'), (-2.05, 3.3, 0.15, 'v'), (1.6, 4.2, 0.12, 'c'), (1.8, 4.0, 0.16, 'c'),
                        (1.45, 4.1, 0.13, 'v'), (0.2, 6.0, 0.4, 'c'), (-0.6, 6.4, 0.5, 'c'), (2.8, 6.8, 0.6, 'c')]:
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012 if kind == 'c' else 0.05, location=(x, y, z))
    sp = bpy.context.object; sp.visible_shadow = False
    em = MB('bk'); e = em.n('ShaderNodeEmission')
    e.inputs['Color'].default_value = kelvin_rgb(1900) if kind == 'c' else hexc('#6A55F0')
    e.inputs['Strength'].default_value = 60 if kind == 'c' else 6
    em.L(e.outputs['Emission'], em.out.inputs['Surface']); assign(sp, em.m)

# lights: warm pendant over the table, violet glow from the tablet, cool-violet back rim for the crystal
spot('Colgante', (0.05, 0.45, 1.55), (0.0, 0.42, 0.0), 170, 70, blend=0.7, radius=0.12, temp=2700)
pg = area('PantallaGlow', (TC[0] - 0.20, TC[1] - 0.16, 0.11), (0.0, -0.2, 0.04), 2.2, 0.24, 0.17, color=hexc('#6A55F0')); pg.visible_transmission = False; pg.visible_glossy = False
ct = area('Contra', (0.6, 1.9, 0.55), (0.08, 0.15, 0.1), 40, 1.2, 0.4, color=hexc('#7F6CF2')); ct.visible_transmission = False
area('Relleno', (-1.2, -0.9, 0.9), (0, 0, 0), 5, 1.2, temp=3200)

camera((0.40, -0.72, 0.31), (0.03, 0.05, 0.03), lens=52, fstop=1.8, focus=None)
cam = bpy.context.scene.camera; cam.data.shift_x = -0.21; cam.data.dof.focus_distance = (Vector((0.40, -0.72, 0.31)) - Vector((0.0, 0.0, 0.02))).length
render('mesa')
