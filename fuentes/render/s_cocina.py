import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from props import *
random.seed(51)
reset(); setup(2000, 1125, samples=96, exposure=-0.6, look='AgX - Medium High Contrast', glass=False)
world_color(hexc('#0D0A14'), 0.02)

steel = m_metal('AceroCepillado', hexc('#9C9AA3'), rough=0.28, var=0.06, aniso=0.75, aniso_rot=0.0, scale=4).m
steel_pol = m_metal('AceroPulido', hexc('#C9C8CE'), rough=0.06, var=0.03, scale=6).m
# the pass: counter + heat-lamp gantry + ticket rail
counter = box('Mesada', (3.2, 0.75, 0.05), loc=(0, 0, -0.025), bevel=0.004); assign(counter, steel)
front = box('Frente', (3.2, 0.03, 0.9), loc=(0, -0.39, -0.47), bevel=0.003); assign(front, steel)
gantry = box('Puente', (3.0, 0.32, 0.07), loc=(0, 0.06, 0.62), bevel=0.006); assign(gantry, steel)
for sx in (-1.45, 1.45):
    post = box('Poste', (0.04, 0.04, 0.62), loc=(sx, 0.18, 0.31), bevel=0.003); assign(post, steel)
heat = MB('LamparaCalor'); e = heat.n('ShaderNodeEmission'); bb = heat.n('ShaderNodeBlackbody'); bb.inputs['Temperature'].default_value = 1750
heat.L(bb.outputs['Color'], e.inputs['Color']); e.inputs['Strength'].default_value = 26; heat.L(e.outputs['Emission'], heat.out.inputs['Surface'])
for i, x in enumerate([-0.95, 0.0, 0.95]):
    tube = cyl('Tubo%d' % i, 0.016, 0.82, loc=(x, 0.06, 0.552), rot=(0, math.radians(90), 0), seg=32, bevel=0); assign(tube, heat.m)
    area('Calor%d' % i, (x, 0.06, 0.53), (x, 0.06, 0.0), 42, 0.8, 0.06, temp=1900)
rail = box('Riel', (2.9, 0.02, 0.035), loc=(0, -0.105, 0.565), bevel=0.003); assign(rail, steel_pol)

# tickets hanging from the rail (thermal paper, slight curl)
tk_m = m_paper('Comanda', hexc('#EFEDE8'), print_img=TEX + 'tickets.png', fiber=0.08, rough=0.7)
for i, x in enumerate([-0.55, -0.32, -0.09]):
    t = grid('Comanda%d' % i, 0.08, 0.15, 16, 30, loc=(x, -0.118, 0.47), rot=(math.radians(90 + random.uniform(-4, 4)), 0, math.radians(random.uniform(-3, 3))))
    # map one third of the atlas per ticket
    uv = t.data.uv_layers.active.data
    for l in uv:
        u, v = l.uv; l.uv = ((u + i) / 3.0, 0.32 + v * 0.68)
    b = t.modifiers.new('curl', 'SIMPLE_DEFORM'); b.deform_method = 'BEND'; b.angle = math.radians(random.uniform(14, 26)); b.deform_axis = 'X'
    solidify(t, 0.00015); assign(t, tk_m.m)

# plates under cloches on the pass
def cloche(name):
    p = [(0, 0.118), (0.03, 0.116), (0.07, 0.105), (0.10, 0.083), (0.118, 0.052), (0.126, 0.02), (0.128, 0.004), (0.131, 0.0), (0.1335, 0.002),
         (0.1335, 0.006), (0.1295, 0.006), (0.1255, 0.02), (0.1175, 0.051), (0.0995, 0.082), (0.0695, 0.1035), (0.0295, 0.1145), (0, 0.1165)]
    d = lathe(name, smooth_profile(p, 2), seg=128); assign(d, steel_pol)
    k1 = cyl(name+'K', 0.006, 0.018, loc=(0, 0, 0.126), seg=32, bevel=0.001); assign(k1, steel_pol)
    k2 = lathe(name+'Pomo', smooth_profile([(0, 0.133), (0.016, 0.134), (0.019, 0.141), (0.012, 0.148), (0, 0.149)], 2), seg=48); assign(k2, steel_pol)
    return [d, k1, k2]
for i, x in enumerate([-1.05, -0.62, -0.2, 0.22, 0.64, 1.06]):
    pl = dinner_plate('Pl%d' % i, z=0.0); 
    objs = [pl] + cloche('Cl%d' % i)
    for o in objs[1:]: o.location.z += 0.0095
    r = parent_all('Pase%d' % i, objs, loc=(x + random.uniform(-0.02, 0.02), 0.02 + random.uniform(-0.03, 0.03), 0.0))

# background kitchen (out of focus): back wall of dark tile, a shelf with pots, a hood
wall = grid('Pared', 6, 3, 4, 4, loc=(0, 1.9, 0.8), rot=(math.radians(90), 0, 0)); assign(wall, m_concrete('Azulejo', hexc('#1E1B24'), rough=0.25, var=0.1).m)
shelf = box('Estante', (2.6, 0.32, 0.03), loc=(0.2, 1.7, 1.02), bevel=0.003); assign(shelf, steel)
for i, (x, r, h) in enumerate([(-0.6, 0.12, 0.16), (-0.25, 0.09, 0.12), (0.15, 0.14, 0.2), (0.6, 0.1, 0.1), (0.95, 0.11, 0.14)]):
    pot = cyl('Olla%d' % i, r, h, loc=(x, 1.7, 1.035 + h/2), seg=64, bevel=0.004); assign(pot, steel_pol)
area('Tubo', (0.2, 1.5, 1.6), (0.2, 1.2, 0.5), 60, 2.4, 0.08, temp=5600)

# dining-room side: violet spill, soft front fill
area('SalaVioleta', (-1.4, -2.2, 0.6), (0, 0, 0.1), 60, 1.6, 0.8, color=hexc('#6A55F0'))
area('Frontal', (0.9, -2.0, 1.0), (0, 0, 0.1), 14, 1.4, temp=4200)

cl = (0.62, -1.95, 0.40)
camera(cl, (-0.05, 0.05, 0.31), lens=40, fstop=2.8)
cam = bpy.context.scene.camera; cam.data.dof.focus_distance = (Vector(cl) - Vector((-0.3, -0.1, 0.4))).length
render('cocina')
