import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from lib import *
random.seed(9)
reset(); setup(2000, 1125, samples=80, exposure=-0.6, look='AgX - Medium High Contrast', volume=True)
world_color(hexc('#0D0A16'), 0.01)

# room
floor = grid('Piso', 9, 9, 10, 10); assign(floor, m_concrete('Piso', hexc('#1A1720'), rough=0.32).m)
wall = grid('Pared', 9, 4, 10, 10, loc=(0, 1.9, 2.0), rot=(math.radians(90), 0, 0))
assign(wall, m_concrete('Pared', hexc('#1C1826'), rough=0.85).m)

# haze volume
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.2, 2.0)); hz = bpy.context.object; hz.name = 'Bruma'; hz.scale = (8, 6, 4)
vmb = MB('Bruma'); vmb.nt.nodes.remove(vmb.b)
pv = vmb.n('ShaderNodeVolumePrincipled'); pv.inputs['Density'].default_value = 0.05; pv.inputs['Anisotropy'].default_value = 0.55
pv.inputs['Color'].default_value = (0.92, 0.9, 1.0, 1)
vmb.L(pv.outputs['Volume'], vmb.out.inputs['Volume']); assign(hz, vmb.m)
hz.visible_shadow = False

# --- lounge chair, violet velvet ---
def m_velvet2(name, color, sheen_tint):
    """Velvet with pile patches (brushed in different directions), crevice darkening and a fine fibre bump."""
    mb = MB(name)
    v = mb.coord('Object')
    patch = mb.noise(v, 4.5, detail=3, rough=0.55)           # 20-cm patches of pile direction
    crush = mb.noise(v, 38, detail=8, rough=0.7)             # crushed-velvet mottling
    ao = mb.n('ShaderNodeAmbientOcclusion'); ao.inputs['Distance'].default_value = 0.05; ao.samples = 8
    tone = mb.maprange(mb.math('ADD', mb.math('MULTIPLY', patch, 0.6), mb.math('MULTIPLY', crush, 0.4)), 0.3, 0.7, 0.0, 1.0)
    base = mb.mixc(tone, tuple(c*0.62 for c in color[:3]) + (1,), tuple(min(1, c*1.12) for c in color[:3]) + (1,))
    occl = mb.maprange(ao.outputs['AO'], 0.0, 1.0, 0.38, 1.0)
    mul = mb.n('ShaderNodeMix'); mul.data_type = 'RGBA'; mul.blend_type = 'MULTIPLY'; mul.inputs[0].default_value = 1.0
    mb.L(base, mul.inputs[6]); mb.L(occl, mul.inputs[7])
    mb.to('Base Color', mul.outputs[2])
    mb.set(Roughness=0.95, Specular_IOR_Level=0.18, Sheen_Tint=sheen_tint)
    mb.to('Sheen Weight', mb.math('MULTIPLY', mb.maprange(patch, 0.25, 0.75, 0.55, 1.0), ao.outputs['AO']))
    mb.to('Sheen Roughness', mb.maprange(patch, 0.25, 0.75, 0.28, 0.5))
    fib = mb.noise(v, 2400, detail=2, rough=0.5)
    mb.to('Normal', mb.bump(mb.math('ADD', mb.math('MULTIPLY', crush, 0.7), mb.math('MULTIPLY', fib, 0.3)), 0.18, 0.0015))
    return mb
velvet = m_velvet2('Terciopelo', hexc('#22135F'), hexc('#A08CF7'))
def cushion(name, size, loc, rot=(0,0,0), bev=0.05, puff=0.006):
    ob = box(name, size, loc=loc, rot=rot, bevel=bev, segs=6, subsurf=0)
    s = ob.modifiers.new('sub', 'SUBSURF'); s.levels = 2; s.render_levels = 2
    displace_noise(ob, 0.18, puff, depth=1)
    displace_noise(ob, 0.035, 0.0016, depth=2)
    assign(ob, velvet.m); return ob
parts = []
parts.append(cushion('Base', (0.80, 0.66, 0.15), (0, 0.01, 0.255), bev=0.04, puff=0.003))
parts.append(cushion('Asiento', (0.585, 0.60, 0.13), (0, -0.015, 0.385), bev=0.055, puff=0.007))
back = cushion('Respaldo', (0.80, 0.16, 0.50), (0, 0.29, 0.60), rot=(math.radians(-13), 0, 0), bev=0.06, puff=0.006)
bend = back.modifiers.new('bend', 'SIMPLE_DEFORM'); bend.deform_method = 'BEND'; bend.angle = math.radians(-28); bend.deform_axis = 'Z'
back.modifiers.move(len(back.modifiers)-1, 0)
parts.append(back)
for sx in (-1, 1):
    parts.append(cushion('Brazo', (0.11, 0.66, 0.31), (sx*0.345, 0.01, 0.43), rot=(0, 0, 0), bev=0.05, puff=0.004))
brass = m_metal('Bronce', hexc('#B89155'), rough=0.24, var=0.08)
for sx in (-1, 1):
    for sy in (-1, 1):
        lg = lathe('Pata', [(0, 0.0), (0.009, 0.0), (0.0095, 0.004), (0.013, 0.17), (0.0135, 0.19), (0, 0.19)], seg=40)
        lg.location = (sx*0.33, sy*0.28, 0.0); lg.rotation_euler = (sy*math.radians(6), -sx*math.radians(6), 0)
        assign(lg, brass.m); parts.append(lg)
rig = bpy.data.objects.new('Sillon', None); link_obj(rig)
for p in parts: p.parent = rig
rig.location = (0.05, 0.25, 0); rig.rotation_euler = (0, 0, math.radians(-16))

# side table with a glass of water
top = cyl('Mesita', 0.21, 0.025, loc=(0.78, 0.18, 0.545), seg=96, bevel=0.004)
assign(top, m_marble('Marmol', base=hexc('#0E0C12'), vein=hexc('#55505F')).m)
stem = cyl('Pie', 0.018, 0.53, loc=(0.78, 0.18, 0.265), seg=48, bevel=0.002); assign(stem, brass.m)
foot = cyl('Base', 0.15, 0.012, loc=(0.78, 0.18, 0.006), seg=96, bevel=0.003); assign(foot, brass.m)
crystal = m_glass('Cristal'); water = m_liquid_vol('Agua', (0.8, 0.92, 0.95, 1), 0.6)
tb = tumbler('Vaso', loc=(0.83, 0.13, 0.5575), r=0.034, h=0.09); assign(tb, crystal.m)
tw = tumbler_water('AguaVaso', loc=(0.83, 0.13, 0.5575), r=0.034, level=0.058); assign(tw, water.m)

# light: one hard-ish spot from above-front, violet wash on the wall, faint warm bounce
spot('Cenital', (0.12, -0.25, 3.7), (0.06, 0.22, 0.35), 1500, 26, blend=0.3, radius=0.05, temp=4700)
mv = area('MuroVioleta', (0.0, 1.55, 0.05), (0.0, 1.9, 1.6), 45, 2.6, 0.25, color=hexc('#5B49D8')); mv.visible_volume_scatter = False
rb = area('Rebote', (-1.6, -1.2, 0.8), (0, 0.2, 0.5), 3, 1.2, temp=2800); rb.visible_volume_scatter = False

co = area('Contra', (-0.9, 1.3, 1.5), (0.05, 0.3, 0.6), 22, 0.6, 0.6, temp=5200); co.visible_volume_scatter = False
camera((-0.15, -3.4, 1.0), (0.12, 0.2, 0.62), lens=50, fstop=2.8, focus=3.62)
render('confesionario')
