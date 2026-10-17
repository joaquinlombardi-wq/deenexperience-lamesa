import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from props import *
random.seed(31)
reset(); setup(1800, 1350, samples=96, exposure=-0.7, look='AgX - Medium High Contrast', glass=True)
world_color(hexc('#0B0913'), 0.01)

cloth = grid('Mantel', 3, 3, 120, 120); displace_noise(cloth, 0.3, 0.004, depth=2); assign(cloth, M('cloth_ink'))
tb = tablet_on_stand('Deenex'); tb.location = (0.0, 0.0, 0.0); tb.rotation_euler = (0, 0, math.radians(-22))
# props around: a cover to the right, candles behind, a glass in the left foreground
ps = place_setting('Cub', menu=True, placecard=None, glasses=True, cutlery=True); ps.location = (0.42, -0.30, 0); ps.rotation_euler = (0, 0, math.radians(-8))
for i, (x, y, h) in enumerate([(-0.28, 0.32, 0.12), (-0.12, 0.42, 0.16), (0.30, 0.45, 0.09)]):
    c = candle('Vela%d' % i, r=0.03, h=h); c.location = (x, y, 0)
g = wine_glass('CopaF', loc=(-0.30, -0.42, 0)); assign(g, M('crystal'))
wl = wine_glass_liquid('VinoF', 0.128, loc=(-0.30, -0.42, 0)); assign(wl, m_liquid_vol('Vino', (0.62, 0.035, 0.09, 1), 85.0, ior=1.345).m)
for (x, y, z) in [(-1.6, 2.6, 0.1), (-1.3, 2.9, 0.14), (1.2, 3.2, 0.12), (1.5, 3.0, 0.1), (0.2, 4.2, 0.3)]:
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.012, location=(x, y, z)); sp = bpy.context.object; sp.visible_shadow = False
    em = MB('bk'); e = em.n('ShaderNodeEmission'); e.inputs['Color'].default_value = kelvin_rgb(1900); e.inputs['Strength'].default_value = 60
    em.L(e.outputs['Emission'], em.out.inputs['Surface']); assign(sp, em.m)

spot('Colgante', (0.15, 0.1, 1.5), (0.05, -0.05, 0.0), 120, 70, blend=0.7, radius=0.12, temp=2700)
pg = area('PantallaGlow', (0.0, -0.08, 0.1), (0.0, -0.4, 0.0), 1.6, 0.24, 0.17, color=hexc('#6A55F0')); pg.visible_transmission = False; pg.visible_glossy = False
ct = area('Contra', (-0.5, 1.4, 0.6), (0, 0, 0.1), 30, 1.0, 0.4, color=hexc('#7F6CF2')); ct.visible_transmission = False
area('Relleno', (0.8, -1.0, 0.7), (0, 0, 0.05), 4, 1.0, temp=3400)

cam_loc = (0.20, -0.62, 0.30)
camera(cam_loc, (0.0, 0.0, 0.095), lens=50, fstop=2.0)
c = bpy.context.scene.camera; c.data.dof.focus_distance = (Vector(cam_loc) - Vector((0.0, 0.0, 0.095))).length
render('pantalla')
