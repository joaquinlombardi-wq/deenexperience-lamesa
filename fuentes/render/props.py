# Reusable props for La Mesa scenes
from lib import *

_M = {}
def M(key):
    """Shared material cache."""
    if key in _M: return _M[key]
    if key == 'porcelain': m = m_porcelain('Porcelana').m
    elif key == 'stoneware': m = m_stoneware('Gres', hexc('#141218')).m
    elif key == 'crystal': m = m_glass('Cristal', tint=(0.99, 0.995, 0.995, 1)).m
    elif key == 'water': m = m_liquid_vol('Agua', (0.8, 0.92, 0.95, 1), 0.6).m
    elif key == 'brass': m = m_metal('Bronce', hexc('#C6A260'), rough=0.16, var=0.06).m
    elif key == 'brass_satin': m = m_metal('BronceSatinado', hexc('#B8955A'), rough=0.3, var=0.08).m
    elif key == 'napkin_violet':
        mb = m_linen('ServilletaVioleta', hexc('#4A38B8'), threads=700, sheen=0.75, rough=0.82, bump=0.5, color_var=0.08, heather=0.10)
        m = mb.m
    elif key == 'cloth_ink':
        m = m_linen('MantelTinta', hexc('#120E1E'), threads=2600, sheen=0.6, rough=0.9, bump=0.5, color_var=0.12, heather=0.16).m
    elif key == 'wax': m = m_wax('Cera').m
    elif key == 'flame': m = m_flame('Llama', 55).m
    elif key == 'smoked':
        m = m_glass('VidrioAhumado', tint=(0.74, 0.71, 0.78, 1), rough=0.02).m
    elif key == 'tablet_body':
        mb = MB('Tablet'); mb.set(Base_Color=hexc('#1A1A1E'), Metallic=0.9, Roughness=0.35); m = mb.m
    elif key == 'tablet_screen': m = m_emit('Pantalla', img=TEX + 'tablet.png', strength=2.0).m
    else: raise KeyError(key)
    _M[key] = m; return m

def parent_all(name, objs, loc=(0,0,0), rot=(0,0,0)):
    rig = bpy.data.objects.new(name, None); link_obj(rig)
    for o in objs: o.parent = rig
    rig.location = loc; rig.rotation_euler = rot
    return rig

def charger(name='BajoPlato'):
    p = [(0, 0.0062), (0.118, 0.0062), (0.146, 0.0098), (0.157, 0.0118), (0.1612, 0.0112), (0.1606, 0.0094), (0.150, 0.0068),
         (0.126, 0.0030), (0.108, 0.0004), (0.100, 0.0), (0.094, 0.0), (0.090, 0.0026), (0, 0.0026)]
    ob = lathe(name, smooth_profile(p, 2), seg=160); assign(ob, M('stoneware')); return ob

def dinner_plate(name='Plato', z=0.0062):
    p = [(0, 0.0095), (0.080, 0.0095), (0.096, 0.0120), (0.118, 0.0175), (0.1325, 0.0205), (0.1352, 0.0198), (0.1345, 0.0178),
         (0.118, 0.0142), (0.096, 0.0085), (0.080, 0.0058), (0.072, 0.0040), (0.066, 0.0), (0.060, 0.0), (0.057, 0.0045), (0, 0.0045)]
    ob = lathe(name, smooth_profile(p, 2), seg=160); ob.location.z = z; assign(ob, M('porcelain')); return ob

def napkin_flat(name='Servilleta', L=0.30, W=0.118, T=0.011, bend_deg=24, mat='napkin_violet'):
    ob = box(name, (L, W, T), bevel=0.0045, segs=4)
    s = ob.modifiers.new('sub', 'SUBSURF'); s.levels = 2; s.render_levels = 2
    displace_noise(ob, 0.05, 0.0012, depth=1)
    if bend_deg:
        b = ob.modifiers.new('bend', 'SIMPLE_DEFORM'); b.deform_method = 'BEND'; b.angle = math.radians(bend_deg); b.deform_axis = 'Y'
    # flat UVs for the weave
    bpy.context.view_layer.objects.active = ob
    return assign(ob, M(mat))

def card(name, w, h, tex, color=None, thick=0.0006, bend_deg=0, deboss=None):
    ob = grid(name, w, h, 40, 80)
    solidify(ob, thick)
    if bend_deg:
        b = ob.modifiers.new('bend', 'SIMPLE_DEFORM'); b.deform_method = 'BEND'; b.angle = math.radians(bend_deg); b.deform_axis = 'X'
    m = m_paper(name, color or hexc('#F3F0F6'), print_img=tex, deboss_img=deboss, fiber=0.18, rough=0.9)
    return assign(ob, m.m)

def tent_card(name, tex, w=0.09, h=0.05, angle=62):
    """folded place card: front face carries the print."""
    a = math.radians(angle/2)
    front = grid(name+'F', w, h, 20, 12); solidify(front, 0.0005)
    back = grid(name+'B', w, h, 20, 12); solidify(back, 0.0005)
    mf = m_paper(name, hexc('#F3F0F6'), print_img=tex, fiber=0.18, rough=0.9)
    mb = m_paper(name+'b', hexc('#F3F0F6'), fiber=0.18, rough=0.9)
    assign(front, mf.m); assign(back, mb.m)
    # hinge at top: rotate each leaf around X
    front.rotation_euler = (math.pi/2 - a, 0, 0); front.location = (0, -math.sin(a)*h/2, math.cos(a)*h/2)
    back.rotation_euler = (math.pi/2 + a, 0, math.pi); back.location = (0, math.sin(a)*h/2, math.cos(a)*h/2)
    return parent_all(name, [front, back])

def candle(name, r=0.032, h=0.11, holder=True):
    objs = []
    wax = cyl(name+'Cera', r, h, loc=(0, 0, h/2), seg=64, bevel=0.003); assign(wax, M('wax')); objs.append(wax)
    # melted dip at the top
    dip = lathe(name+'Pozo', [(0, h - 0.004), (r*0.75, h - 0.002), (r*0.95, h + 0.0004), (r*0.951, h - 0.0002)], seg=64); assign(dip, M('wax')); objs.append(dip)
    wick = cyl(name+'Mecha', 0.0009, 0.012, loc=(0, 0, h + 0.002), seg=12, bevel=0); 
    wm = MB('Mecha'); wm.set(Base_Color=hexc('#111111'), Roughness=0.8); assign(wick, wm.m); objs.append(wick)
    fl = lathe(name+'Llama', smooth_profile([(0, 0), (0.0042, 0.006), (0.0048, 0.012), (0.0028, 0.022), (0, 0.032)], 3), seg=32)
    fl.location = (0, 0, h + 0.004); assign(fl, M('flame')); fl.visible_shadow = False; objs.append(fl)
    pl = point(name+'Luz', (0, 0, h + 0.016), 1.2, radius=0.006, temp=1900); objs.append(pl)
    if holder:
        hp = [(0, 0), (r + 0.010, 0), (r + 0.012, 0.002), (r + 0.012, h*0.72), (r + 0.0095, h*0.72), (r + 0.0095, 0.006), (0, 0.006)]
        hd = lathe(name+'Vaso', hp, seg=96); assign(hd, M('smoked')); objs.append(hd)
    return parent_all(name, objs)

def tablet_on_stand(name, tilt=68):
    objs = []
    W, H, T = 0.247, 0.178, 0.0072
    body = box(name+'Cuerpo', (W, T, H), loc=(0, 0, 0), bevel=0.0035, segs=5); assign(body, M('tablet_body')); objs.append(body)
    scr = grid(name+'Pantalla', W - 0.016, H - 0.016, 2, 2, loc=(0, -T/2 - 0.0002, 0), rot=(math.radians(90), 0, 0)); assign(scr, M('tablet_screen')); objs.append(scr)
    tab = parent_all(name+'T', objs)
    tab.rotation_euler = (math.radians(90 - tilt), 0, 0); tab.location = (0, 0.02, 0.098)
    st = []
    base = box(name+'Base', (0.12, 0.10, 0.008), loc=(0, 0.035, 0.004), bevel=0.002); assign(base, M('brass_satin')); st.append(base)
    arm = box(name+'Brazo', (0.02, 0.008, 0.11), loc=(0, 0.065, 0.055), rot=(math.radians(-22), 0, 0), bevel=0.0015); assign(arm, M('brass_satin')); st.append(arm)
    lip = box(name+'Tope', (0.16, 0.014, 0.008), loc=(0, -0.008, 0.012), bevel=0.002); assign(lip, M('brass_satin')); st.append(lip)
    return parent_all(name, [tab] + st)

def outline_extrude(name, outline, thick, bevel=0.0005, curve=None):
    verts = [(x, y, 0) for (x, y) in outline]
    ob = mesh_obj(name, verts, [list(range(len(verts)))], smooth=False)
    bm = bmesh.new(); bm.from_mesh(ob.data)
    res = bmesh.ops.extrude_face_region(bm, geom=bm.faces[:])
    for v in [g for g in res['geom'] if isinstance(g, bmesh.types.BMVert)]: v.co.z += thick
    if curve:
        bmesh.ops.subdivide_edges(bm, edges=[e for e in bm.edges if abs(e.verts[0].co.x - e.verts[1].co.x) > 0.02], cuts=6, use_grid_fill=False)
        for v in bm.verts: v.co.z += curve(v.co.x)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(ob.data); bm.free()
    m = ob.modifiers.new('bev', 'BEVEL'); m.width = bevel; m.segments = 3; m.limit_method = 'ANGLE'
    for p in ob.data.polygons: p.use_smooth = True
    try: ob.data.set_sharp_from_angle(angle=math.radians(50))
    except Exception: pass
    return ob

def _halfwidth_poly(profile, n=60):
    """profile(x)->half width; returns closed outline along x."""
    xs = [i/(n) for i in range(n+1)]
    return xs

def knife(name='Cuchillo'):
    pts = []
    # (x, half-width) handle 0..0.105, bolster, blade to 0.225 with rounded tip
    top = [(0.000, 0.0060), (0.008, 0.0078), (0.040, 0.0082), (0.090, 0.0074), (0.104, 0.0050), (0.112, 0.0048), (0.120, 0.0090),
           (0.150, 0.0100), (0.190, 0.0096), (0.212, 0.0080), (0.222, 0.0050), (0.226, 0.0010)]
    bot = [(0.226, -0.0005), (0.222, -0.0030), (0.200, -0.0060), (0.150, -0.0066), (0.122, -0.0062), (0.112, -0.0048), (0.104, -0.0050),
           (0.090, -0.0074), (0.040, -0.0082), (0.008, -0.0078), (0.000, -0.0060)]
    outline = smooth_profile(top, 2) + smooth_profile(bot, 2)
    ob = outline_extrude(name, outline, 0.0028, 0.0007, curve=lambda x: 0.15 * max(0.0, 0.10 - x)**2)
    assign(ob, M('brass')); return ob

def fork(name='Tenedor'):
    up = [(0.000, 0.0062), (0.010, 0.0080), (0.060, 0.0076), (0.105, 0.0052), (0.125, 0.0036), (0.140, 0.0052), (0.158, 0.0118), (0.166, 0.0128)]
    ou = smooth_profile(up, 2)
    tines = []
    tw, gap, tip = 0.0047, 0.0019, 0.204
    xs = 0.0128
    # tines across from +y to -y
    edges = [0.0128]
    for i in range(4):
        y0 = 0.0128 - i*(tw + gap)
        y1 = y0 - tw
        tines += [(tip - 0.002 if i in (0, 3) else tip, y0 - 0.0004), (tip, y0 - tw/2), (tip - 0.002 if i in (0, 3) else tip, y1 + 0.0004)]
        if i < 3: tines += [(0.172, y1), (0.170, y1 - gap/2), (0.172, y1 - gap)]
    lo = [(x, -y) for (x, y) in reversed(ou)]
    outline = ou + tines + lo
    lift = lambda x: (0.19 * (0.125 - x)**2) if x < 0.125 else (0.48 * (x - 0.125)**2)
    ob = outline_extrude(name, outline, 0.0024, 0.0006, curve=lift)
    assign(ob, M('brass')); return ob

def round_table(name='Mesa', r=0.82, z=0.0):
    top = cyl(name+'Tapa', r, 0.03, loc=(0, 0, z - 0.015), seg=192, bevel=0.012)
    displace_noise(top, 0.4, 0.002, depth=1)
    assign(top, M('cloth_ink'))
    skirt = cyl(name+'Falda', r + 0.008, 0.72, loc=(0, 0, z - 0.39), seg=192, bevel=0.0)
    w = bpy.data.textures.new('pliegues', 'WOOD'); w.wood_type = 'BANDNOISE'; w.noise_basis_2 = 'SIN'; w.turbulence = 3
    m = skirt.modifiers.new('pl', 'DISPLACE'); m.texture = w; m.strength = 0.012; m.texture_coords = 'LOCAL'
    assign(skirt, M('cloth_ink'))
    return [top, skirt]

def place_setting(name, menu=True, placecard=None, glasses=True, wine=False, cutlery=True, water=True, napkin_rot=0):
    """A full cover centred at origin, diner at -y. Napkin left under the fork; stiff menu card bridging the plate rim."""
    objs = [charger(name+'Bajo'), dinner_plate(name+'Plato')]
    nap = napkin_flat(name+'Serv', L=0.235, W=0.105, T=0.009, bend_deg=0); nap.location = (-0.232, -0.035, 0.0047)
    nap.rotation_euler = (0, 0, math.radians(90 + napkin_rot)); objs.append(nap)
    if menu:
        mc = card(name+'Menu', 0.105, 0.21, TEX + 'menu.png'); mc.location = (0.0, -0.002, 0.0212)
        mc.rotation_euler = (math.radians(0.4), 0, math.radians(-3.0)); objs.append(mc)
    if cutlery:
        fk = fork(name+'Ten'); fk.rotation_euler = (0, 0, math.radians(90)); fk.location = (-0.232, -0.14, 0.0085); objs.append(fk)
        kn = knife(name+'Cuch'); kn.rotation_euler = (0, 0, math.radians(90)); kn.location = (0.192, -0.13, 0.0); objs.append(kn)
    if glasses:
        g = wine_glass(name+'Copa', loc=(0.125, 0.225, 0)); assign(g, M('crystal')); objs.append(g)
        if water:
            t = tumbler(name+'Vaso', loc=(0.222, 0.155, 0), r=0.036, h=0.092); assign(t, M('crystal')); objs.append(t)
            tw = tumbler_water(name+'Agua', loc=(0.222, 0.155, 0), r=0.036, level=0.064); assign(tw, M('water')); objs.append(tw)
    if placecard:
        pc = tent_card(name+'Lugar', placecard); pc.location = (-0.05, 0.215, 0.0); pc.rotation_euler = (0, 0, math.radians(4)); objs.append(pc)
    return parent_all(name, objs)
