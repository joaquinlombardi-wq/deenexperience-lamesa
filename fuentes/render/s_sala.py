import sys, json; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from props import *
from bpy_extras.object_utils import world_to_camera_view
random.seed(41)
reset(); setup(2000, 1125, samples=96, exposure=-0.4, look='AgX - Medium High Contrast', glass=True)
world_color(hexc('#1C1440'), 0.10)

floor = grid('Piso', 16, 12, 10, 10, loc=(0, 0, -0.75))
fm = MB('Piso'); fm.set(Base_Color=hexc('#131018'), Roughness=0.42, Coat_Weight=0.25, Coat_Roughness=0.2)
fm.to('Normal', fm.bump(fm.noise(fm.coord('Object'), 40, detail=4), 0.03, 0.002))
assign(floor, fm.m)
vel_ceo = m_velvet('TercioCEO', hexc('#2C1A78'), sheen_tint=hexc('#8C76EE'), scale=30).m
vel_exp = m_linen('LinoExperto', hexc('#E9E4F2'), threads=900, sheen=0.5, rough=0.85, bump=0.4, heather=0.06).m

def chair(name, mat):
    objs = []
    seat = box(name+'S', (0.46, 0.44, 0.07), loc=(0, 0, -0.30), bevel=0.03, segs=5); subsurf(seat, 1); assign(seat, mat); objs.append(seat)
    back = box(name+'B', (0.46, 0.06, 0.40), loc=(0, 0.21, -0.06), rot=(math.radians(-8), 0, 0), bevel=0.025, segs=5); subsurf(back, 1); assign(back, mat); objs.append(back)
    for sx in (-1, 1):
        for sy in (-1, 1):
            lg = cyl(name+'P', 0.012, 0.42, loc=(sx*0.19, sy*0.17, -0.54), seg=24); assign(lg, M('brass_satin')); objs.append(lg)
    return parent_all(name, objs)

TABLES = [(-2.75, 0.18), (0.0, -0.22), (2.75, 0.18)]
EXPERT_SEAT = 0          # seat index (k) of the expert chair at every table
marks = []
for ti, (tx, ty) in enumerate(TABLES):
    for o in round_table('Mesa%d' % ti, r=0.80):
        o.location.x += tx; o.location.y += ty
    for k in range(6):
        a = math.pi/2 + k*2*math.pi/6 + (0.0 if ti != 1 else math.pi/6)
        cxp, cyp = tx + 0.56*math.cos(a), ty + 0.56*math.sin(a)
        ps = place_setting('C%d%d' % (ti, k), menu=True, placecard=None, glasses=True, cutlery=True, water=(k % 2 == 0), napkin_rot=random.uniform(-5, 5))
        ps.location = (cxp, cyp, 0); ps.rotation_euler = (0, 0, a + math.pi/2)
        ch = chair('Silla%d%d' % (ti, k), vel_exp if k == EXPERT_SEAT else vel_ceo)
        rr = 0.93
        ch.location = (tx + rr*math.cos(a), ty + rr*math.sin(a), 0); ch.rotation_euler = (0, 0, a - math.pi/2)
        if k == EXPERT_SEAT: marks.append(('seat', ti, (tx + rr*math.cos(a), ty + rr*math.sin(a), -0.25)))
    tb = tablet_on_stand('Pant%d' % ti); tb.location = (tx + 0.06, ty - 0.02, 0); tb.rotation_euler = (0, 0, math.radians(random.uniform(-30, 30)))
    for i, (dx, dy, h) in enumerate([(-0.12, 0.08, 0.12), (0.1, 0.1, 0.16), (-0.02, -0.14, 0.09)]):
        c = candle('V%d%d' % (ti, i), r=0.028, h=h, holder=True); c.location = (tx + dx, ty + dy, 0)
    spot('Colg%d' % ti, (tx, ty, 3.2), (tx, ty, 0), 380, 52, blend=0.6, radius=0.15, temp=3500)
    marks.append(('table', ti, (tx, ty, 0.0)))

H = 17.0
camera((0.0, -0.0, H), (0.0, 0.0001, 0.0), lens=70)
cam = bpy.context.scene.camera
bpy.context.view_layer.update()
sc = bpy.context.scene
pts = {'tables': []}
for kind, ti, p in marks:
    v = world_to_camera_view(sc, cam, Vector(p))
    if kind == 'table':
        edge = world_to_camera_view(sc, cam, Vector((p[0] + 0.80, p[1], 0)))
        pts['tables'].append({'i': ti, 'x': round(v.x*100, 2), 'y': round((1 - v.y)*100, 2), 'r': round((edge.x - v.x)*100, 2)})
    else:
        pts.setdefault('seats', {})[ti] = {'x': round(v.x*100, 2), 'y': round((1 - v.y)*100, 2)}
json.dump(pts, open(OUT + 'sala_plan.json', 'w'), indent=1); print('PLAN', pts)
render('sala')
