# Shared helpers for the La Mesa photoreal set (Blender 5.2 / Cycles CPU)
import bpy, bmesh, math, random, os, sys, warnings
from mathutils import Vector, Matrix, Euler
warnings.filterwarnings('ignore')
ROOT = os.path.dirname(os.path.abspath(__file__)) + '/'
TEX = ROOT + 'tex/'
OUT = ROOT + 'out/'
PREVIEW = '--preview' in sys.argv

def srgb2lin(c): return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
def hexc(h, a=1.0):
    h = h.lstrip('#'); return (srgb2lin(int(h[0:2],16)/255), srgb2lin(int(h[2:4],16)/255), srgb2lin(int(h[4:6],16)/255), a)

def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    return bpy.context.scene

def setup(w, h, samples=160, exposure=0.0, look='AgX - Medium High Contrast', glass=False, volume=False, seed=1):
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    cy = sc.cycles; cy.device = 'CPU'
    if PREVIEW: w, h, samples = w//3, h//3, 24
    CROP = [a for a in sys.argv if a.startswith('--crop=')]
    if CROP:
        x0, y0, x1, y1 = [float(t) for t in CROP[0][7:].split(',')]
        sc.render.use_border = True; sc.render.use_crop_to_border = True
        sc.render.border_min_x, sc.render.border_min_y, sc.render.border_max_x, sc.render.border_max_y = x0, y0, x1, y1
        samples = 48
    cy.samples = samples
    cy.use_adaptive_sampling = True; cy.adaptive_threshold = 0.012
    cy.use_denoising = True; cy.denoiser = 'OPENIMAGEDENOISE'
    try: cy.denoising_input_passes = 'RGB_ALBEDO_NORMAL'
    except Exception: pass
    cy.max_bounces = 16 if glass else 8
    cy.diffuse_bounces = 3; cy.glossy_bounces = 6 if glass else 4
    cy.transmission_bounces = 16 if glass else 4
    cy.volume_bounces = 1 if volume else 0
    cy.transparent_max_bounces = 8
    cy.caustics_reflective = False; cy.caustics_refractive = False
    cy.blur_glossy = 0.5; cy.seed = seed
    sc.render.resolution_x = w; sc.render.resolution_y = h; sc.render.resolution_percentage = 100
    vs = sc.view_settings; vs.view_transform = 'AgX'; vs.look = look; vs.exposure = exposure
    sc.render.image_settings.file_format = 'PNG'; sc.render.image_settings.color_depth = '16'
    wd = bpy.data.worlds.new('W'); sc.world = wd; wd.use_nodes = True
    bg = wd.node_tree.nodes['Background']; bg.inputs[0].default_value = (0, 0, 0, 1); bg.inputs[1].default_value = 0
    return sc

def world_color(col, strength):
    bg = bpy.context.scene.world.node_tree.nodes['Background']
    bg.inputs[0].default_value = col; bg.inputs[1].default_value = strength

def render(name):
    sc = bpy.context.scene
    tag = '_prev' if PREVIEW else ('_crop' if sc.render.use_border else '')
    sc.render.filepath = OUT + name + tag + '.png'
    import time; t = time.time()
    bpy.ops.render.render(write_still=True)
    print('RENDERED', sc.render.filepath, round(time.time()-t, 1), 's')

# ---------- objects ----------
def link_obj(ob):
    bpy.context.scene.collection.objects.link(ob); return ob

def mesh_obj(name, verts, faces, smooth=True):
    me = bpy.data.meshes.new(name); me.from_pydata(verts, [], faces); me.update()
    ob = bpy.data.objects.new(name, me); link_obj(ob)
    if smooth:
        for p in me.polygons: p.use_smooth = True
    return ob

def lathe(name, prof, seg=96, smooth=True):
    """prof: list of (r, z) from bottom-center outward and around. r==0 points become poles."""
    verts, faces = [], []
    rings = []
    for (r, z) in prof:
        if r < 1e-6:
            rings.append([len(verts)]); verts.append((0, 0, z))
        else:
            idx = []
            for i in range(seg):
                a = 2*math.pi*i/seg
                idx.append(len(verts)); verts.append((r*math.cos(a), r*math.sin(a), z))
            rings.append(idx)
    for A, B in zip(rings[:-1], rings[1:]):
        if len(A) == 1 and len(B) > 1:
            for i in range(seg): faces.append((A[0], B[i], B[(i+1) % seg]))
        elif len(B) == 1 and len(A) > 1:
            for i in range(seg): faces.append((A[i], B[0], A[(i+1) % seg]))
        elif len(A) > 1:
            for i in range(seg): faces.append((A[i], B[i], B[(i+1) % seg], A[(i+1) % seg]))
    ob = mesh_obj(name, verts, faces, smooth)
    # normals outward
    bm = bmesh.new(); bm.from_mesh(ob.data); bmesh.ops.recalc_face_normals(bm, faces=bm.faces); bm.to_mesh(ob.data); bm.free()
    return ob

def smooth_profile(pts, n=6):
    """Chaikin smoothing of a polyline, keeping endpoints."""
    for _ in range(n):
        out = [pts[0]]
        for a, b in zip(pts[:-1], pts[1:]):
            out.append((0.75*a[0]+0.25*b[0], 0.75*a[1]+0.25*b[1]))
            out.append((0.25*a[0]+0.75*b[0], 0.25*a[1]+0.75*b[1]))
        out.append(pts[-1]); pts = out
    return pts

def box(name, size, loc=(0,0,0), rot=(0,0,0), bevel=0.002, segs=3, subsurf=0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    ob = bpy.context.object; ob.name = name; ob.scale = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if bevel > 0:
        m = ob.modifiers.new('bev', 'BEVEL'); m.width = bevel; m.segments = segs; m.limit_method = 'ANGLE'; m.harden_normals = False
    if subsurf:
        m = ob.modifiers.new('sub', 'SUBSURF'); m.levels = subsurf; m.render_levels = subsurf
    bpy.ops.object.shade_smooth()
    return ob

def cyl(name, r, h, loc=(0,0,0), rot=(0,0,0), seg=64, bevel=0.0005):
    bpy.ops.mesh.primitive_cylinder_add(vertices=seg, radius=r, depth=h, location=loc, rotation=rot)
    ob = bpy.context.object; ob.name = name
    if bevel > 0:
        m = ob.modifiers.new('bev', 'BEVEL'); m.width = bevel; m.segments = 3; m.limit_method = 'ANGLE'
    bpy.ops.object.shade_smooth()
    try: ob.data.set_sharp_from_angle(angle=math.radians(40))
    except Exception: pass
    return ob

def grid(name, sx, sy, nx, ny, loc=(0,0,0), rot=(0,0,0)):
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=nx, y_subdivisions=ny, size=1, location=loc, rotation=rot)
    ob = bpy.context.object; ob.name = name; ob.scale = (sx, sy, 1)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.shade_smooth()
    return ob

def displace_img(ob, path, strength, mid=0.5, coords='UV'):
    t = bpy.data.textures.new(os.path.basename(path), 'IMAGE')
    t.image = bpy.data.images.load(path); t.image.colorspace_settings.name = 'Non-Color'
    t.extension = 'EXTEND'
    m = ob.modifiers.new('dispimg', 'DISPLACE'); m.texture = t; m.strength = strength; m.mid_level = mid; m.texture_coords = coords
    return m

def displace_noise(ob, scale, strength, depth=2, kind='CLOUDS', coords='LOCAL', seed_obj=None):
    t = bpy.data.textures.new('n%d' % len(bpy.data.textures), kind)
    if kind == 'CLOUDS': t.noise_scale = scale; t.noise_depth = depth
    m = ob.modifiers.new('dispn', 'DISPLACE'); m.texture = t; m.strength = strength; m.mid_level = 0.5; m.texture_coords = coords
    return m

def solidify(ob, th, offset=-1):
    m = ob.modifiers.new('sol', 'SOLIDIFY'); m.thickness = th; m.offset = offset; return m

def subsurf(ob, lv=1):
    m = ob.modifiers.new('sub', 'SUBSURF'); m.levels = lv; m.render_levels = lv; return m

def assign(ob, m):
    ob.data.materials.clear(); ob.data.materials.append(m); return ob

# ---------- lights / camera ----------
def area(name, loc, look_at, energy, size, size_y=None, temp=None, color=None, spread=None, shape='RECTANGLE', visible=False):
    L = bpy.data.lights.new(name, 'AREA'); L.energy = energy; L.shape = shape
    L.size = size; L.size_y = size_y if size_y else size
    if temp: L.use_temperature = True; L.temperature = temp
    if color: L.color = color[:3]
    if spread is not None: L.spread = math.radians(spread)
    ob = bpy.data.objects.new(name, L); link_obj(ob); ob.location = loc
    aim(ob, look_at)
    ob.visible_camera = visible
    return ob

def spot(name, loc, look_at, energy, size_deg, blend=0.3, radius=0.05, temp=None, color=None):
    L = bpy.data.lights.new(name, 'SPOT'); L.energy = energy; L.spot_size = math.radians(size_deg); L.spot_blend = blend
    L.shadow_soft_size = radius
    if temp: L.use_temperature = True; L.temperature = temp
    if color: L.color = color[:3]
    ob = bpy.data.objects.new(name, L); link_obj(ob); ob.location = loc; aim(ob, look_at); return ob

def point(name, loc, energy, radius=0.02, temp=None, color=None):
    L = bpy.data.lights.new(name, 'POINT'); L.energy = energy; L.shadow_soft_size = radius
    if temp: L.use_temperature = True; L.temperature = temp
    if color: L.color = color[:3]
    ob = bpy.data.objects.new(name, L); link_obj(ob); ob.location = loc; return ob

def aim(ob, target):
    d = Vector(target) - ob.location
    ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

def camera(loc, look_at, lens=50, fstop=None, focus=None, sensor=36, shift=(0,0), roll=0):
    cd = bpy.data.cameras.new('Cam'); cd.lens = lens; cd.sensor_width = sensor
    cd.shift_x, cd.shift_y = shift
    ob = bpy.data.objects.new('Cam', cd); link_obj(ob); ob.location = loc; aim(ob, look_at)
    if roll: ob.rotation_euler.rotate_axis('Z', math.radians(roll))
    if fstop:
        cd.dof.use_dof = True; cd.dof.aperture_fstop = fstop
        cd.dof.focus_distance = focus if focus else (Vector(look_at) - Vector(loc)).length
        cd.dof.aperture_blades = 7; cd.dof.aperture_rotation = math.radians(12)
    bpy.context.scene.camera = ob
    return ob

# ---------- materials ----------
class MB:
    """Tiny node builder around a Principled BSDF."""
    def __init__(self, name):
        self.m = bpy.data.materials.new(name); self.m.use_nodes = True
        self.nt = self.m.node_tree; self.b = self.nt.nodes['Principled BSDF']; self.out = self.nt.nodes['Material Output']
        self._x = -400
    def n(self, t, **props):
        node = self.nt.nodes.new(t); node.location = (self._x, random.uniform(-600, 600)); self._x -= 12
        for k, v in props.items(): setattr(node, k, v)
        return node
    def L(self, a, b): self.nt.links.new(a, b)
    def set(self, **kw):
        for k, v in kw.items(): self.b.inputs[k.replace('_', ' ')].default_value = v
        return self
    def coord(self, kind='UV', scale=(1,1,1), rot=(0,0,0)):
        tc = self.n('ShaderNodeTexCoord'); mp = self.n('ShaderNodeMapping'); mp.vector_type = 'POINT'
        mp.inputs['Scale'].default_value = scale; mp.inputs['Rotation'].default_value = rot
        self.L(tc.outputs[kind], mp.inputs['Vector']); return mp.outputs['Vector']
    def noise(self, vec, scale, detail=4, rough=0.55, distortion=0.0):
        nz = self.n('ShaderNodeTexNoise'); nz.inputs['Scale'].default_value = scale; nz.inputs['Detail'].default_value = detail
        nz.inputs['Roughness'].default_value = rough; nz.inputs['Distortion'].default_value = distortion
        if vec is not None: self.L(vec, nz.inputs['Vector'])
        return nz.outputs['Factor']
    def wave(self, vec, scale, axis='X', distortion=0.0, detail=0.0, kind='BANDS', profile='SIN'):
        w = self.n('ShaderNodeTexWave'); w.wave_type = kind
        if kind == 'BANDS': w.bands_direction = axis
        else: w.rings_direction = axis
        w.wave_profile = profile
        w.inputs['Scale'].default_value = scale; w.inputs['Distortion'].default_value = distortion; w.inputs['Detail'].default_value = detail
        if vec is not None: self.L(vec, w.inputs['Vector'])
        return w.outputs['Factor']
    def img(self, path, vec=None, noncolor=True, interp='Cubic', ext='EXTEND'):
        t = self.n('ShaderNodeTexImage'); im = bpy.data.images.load(path, check_existing=True)
        if noncolor: im.colorspace_settings.name = 'Non-Color'
        t.image = im; t.interpolation = interp; t.extension = ext
        if vec is not None: self.L(vec, t.inputs['Vector'])
        return t
    def maprange(self, val, a, b, c, d, clamp=True):
        mr = self.n('ShaderNodeMapRange'); mr.clamp = clamp
        self.L(val, mr.inputs[0]); mr.inputs[1].default_value = a; mr.inputs[2].default_value = b; mr.inputs[3].default_value = c; mr.inputs[4].default_value = d
        return mr.outputs[0]
    def math(self, op, a, b=None, clamp=False):
        mt = self.n('ShaderNodeMath'); mt.operation = op; mt.use_clamp = clamp
        for i, v in enumerate((a, b)):
            if v is None: continue
            if isinstance(v, (int, float)): mt.inputs[i].default_value = v
            else: self.L(v, mt.inputs[i])
        return mt.outputs[0]
    def mixc(self, fac, a, b):
        mx = self.n('ShaderNodeMix'); mx.data_type = 'RGBA'; mx.clamp_factor = True
        if isinstance(fac, (int, float)): mx.inputs[0].default_value = fac
        else: self.L(fac, mx.inputs[0])
        for idx, v in ((6, a), (7, b)):
            if isinstance(v, tuple): mx.inputs[idx].default_value = v
            else: self.L(v, mx.inputs[idx])
        return mx.outputs[2]
    def mixf(self, fac, a, b):
        mx = self.n('ShaderNodeMix'); mx.data_type = 'FLOAT'; mx.clamp_factor = True
        for idx, v in ((0, fac), (2, a), (3, b)):
            if isinstance(v, (int, float)): mx.inputs[idx].default_value = v
            else: self.L(v, mx.inputs[idx])
        return mx.outputs[0]
    def bump(self, height, strength, distance=0.001, normal=None):
        bp = self.n('ShaderNodeBump'); bp.inputs['Strength'].default_value = strength; bp.inputs['Distance'].default_value = distance
        self.L(height, bp.inputs['Height'])
        if normal is not None: self.L(normal, bp.inputs['Normal'])
        return bp.outputs['Normal']
    def to(self, socket_name, out):
        if isinstance(out, (int, float, tuple)): self.b.inputs[socket_name].default_value = out
        else: self.L(out, self.b.inputs[socket_name])

def rough_var(mb, base, amt, scale=6.0, vec=None):
    """roughness = base +/- amt with low-frequency smudge variation (object space)."""
    v = vec if vec is not None else mb.coord('Object')
    nz = mb.noise(v, scale, detail=6, rough=0.6)
    return mb.maprange(nz, 0.3, 0.7, base-amt, base+amt)

def m_linen(name, color, threads=900, sheen=0.5, rough=0.88, bump=0.35, slub=True, uv=True, aspect=1.0, color_var=0.06, extra_normal=None, heather=0.10):
    """Linen: plain weave + slubs + heathered yarn streaks at a multi-thread scale (what a camera actually resolves)."""
    mb = MB(name)
    K = 'UV' if uv else 'Object'
    v = mb.coord(K, scale=(threads, threads*aspect, 1))
    wx = mb.wave(v, 1.0/3.18, 'X', distortion=1.0, detail=1.0)
    wy = mb.wave(v, 1.0/3.18, 'Y', distortion=1.0, detail=1.0)
    # streaks: vary slowly ALONG a thread, quickly ACROSS threads (every ~3-6 threads)
    st_x = mb.noise(mb.coord(K, scale=(threads*0.012, threads*0.22*aspect, 1)), 1.0, detail=2, rough=0.5)
    st_y = mb.noise(mb.coord(K, scale=(threads*0.22, threads*0.012*aspect, 1)), 1.0, detail=2, rough=0.5)
    if slub:
        sl_x = mb.maprange(st_x, 0.58, 0.78, 0.75, 1.45)
        sl_y = mb.maprange(st_y, 0.58, 0.78, 0.75, 1.45)
        wx = mb.math('MULTIPLY', wx, sl_y)
        wy = mb.math('MULTIPLY', wy, sl_x)
    weave = mb.math('MAXIMUM', wx, wy)
    heath = mb.math('MULTIPLY', mb.math('ADD', st_x, st_y), 0.5)
    lo = tuple(c*(1-heather) for c in color[:3]) + (1,)
    hi = tuple(min(1, c*(1+heather*0.8)) for c in color[:3]) + (1,)
    base = mb.mixc(mb.maprange(heath, 0.3, 0.7, 0, 1), lo, hi)
    cdark = tuple(c*(1-color_var*2) for c in color[:3]) + (1,)
    base = mb.mixc(mb.math('MULTIPLY', mb.math('SUBTRACT', 1.0, weave), 0.6), base, cdark)
    mb.to('Base Color', base)
    mb.to('Roughness', rough)
    mb.set(Sheen_Weight=sheen, Sheen_Roughness=0.35, Sheen_Tint=(1,1,1,1), Specular_IOR_Level=0.35)
    hgt = mb.math('ADD', weave, mb.math('MULTIPLY', heath, 0.8))
    nrm = mb.bump(hgt, bump, 0.0008, extra_normal)
    mb.to('Normal', nrm)
    mb.weave = weave; mb.nrm = nrm; mb.heath = heath
    return mb

def m_velvet(name, color, sheen_tint=None, scale=40):
    mb = MB(name)
    v = mb.coord('Object')
    crush = mb.noise(v, scale, detail=8, rough=0.7)
    base = mb.mixc(mb.maprange(crush, 0.35, 0.65, 0, 1), tuple(c*0.7 for c in color[:3])+(1,), color)
    mb.to('Base Color', base)
    mb.set(Roughness=0.95, Sheen_Weight=1.0, Sheen_Roughness=0.42, Specular_IOR_Level=0.2)
    mb.to('Sheen Tint', sheen_tint if sheen_tint else tuple(min(1, c*2.2+0.08) for c in color[:3])+(1,))
    mb.to('Normal', mb.bump(crush, 0.15, 0.002))
    return mb

def m_porcelain(name, color=None):
    mb = MB(name)
    mb.set(Base_Color=color or hexc('#F3F1F5'), Roughness=0.32, Coat_Weight=1.0, Coat_Roughness=0.03, Coat_IOR=1.5,
           Subsurface_Weight=0.08, Subsurface_Scale=0.004)
    mb.to('Coat Roughness', rough_var(mb, 0.035, 0.02, 9))
    return mb

def m_stoneware(name, color):
    mb = MB(name)
    v = mb.coord('Object'); speck = mb.noise(v, 220, detail=2, rough=0.5)
    mb.to('Base Color', mb.mixc(mb.maprange(speck, 0.62, 0.7, 0, 1), color, tuple(c*1.8 for c in color[:3])+(1,)))
    mb.set(Roughness=0.55, Coat_Weight=0.35, Coat_Roughness=0.25)
    mb.to('Normal', mb.bump(mb.noise(v, 90, 3), 0.08, 0.001))
    return mb

def m_glass(name, tint=(0.97, 0.985, 0.98, 1), rough=0.0, ior=1.5, smudge=True):
    mb = MB(name)
    mb.set(Base_Color=tint, Transmission_Weight=1.0, IOR=ior, Roughness=rough, Specular_IOR_Level=0.5)
    if smudge:
        v = mb.coord('Object'); nz = mb.noise(v, 14, detail=8, rough=0.7)
        mb.to('Roughness', mb.maprange(nz, 0.58, 0.75, rough, rough+0.06))
    return mb

def m_liquid(name, color, ior=1.333, absorb=None):
    mb = MB(name)
    mb.set(Base_Color=color, Transmission_Weight=1.0, IOR=ior, Roughness=0.0)
    return mb

def m_metal(name, color, rough=0.25, var=0.08, aniso=0.0, aniso_rot=0.0, scale=8):
    mb = MB(name)
    mb.set(Base_Color=color, Metallic=1.0, Anisotropic=aniso, Anisotropic_Rotation=aniso_rot)
    mb.to('Roughness', rough_var(mb, rough, var, scale))
    return mb

def m_paper(name, color, print_img=None, print_noncolor=False, deboss_img=None, deboss_strength=0.5, foil_img=None, foil_color=None,
            fiber=0.15, rough=0.88):
    mb = MB(name)
    v = mb.coord('Object'); uv = mb.coord('UV')
    fib = mb.noise(v, 900, detail=6, rough=0.65)
    base = mb.mixc(mb.maprange(fib, 0.3, 0.7, 0, 1), tuple(c*0.94 for c in color[:3])+(1,), color)
    height = mb.math('MULTIPLY', fib, fiber)
    rough_s = rough
    if print_img:
        t = mb.img(print_img, uv, noncolor=False)
        a = t.outputs['Alpha']
        # ink sits in the fibres: slightly broken by paper tooth
        a2 = mb.math('MULTIPLY', a, mb.maprange(fib, 0.2, 0.6, 0.82, 1.0))
        base = mb.mixc(a2, base, t.outputs['Color'])
        height = mb.math('SUBTRACT', height, mb.math('MULTIPLY', a, 0.6))  # letterpress bite
    if deboss_img:
        d = mb.img(deboss_img, uv)
        height = mb.math('SUBTRACT', height, mb.math('MULTIPLY', d.outputs['Color'], deboss_strength))
    if foil_img:
        f = mb.img(foil_img, uv)
        fm = f.outputs['Color']
        mb.foil_mask = fm
    mb.to('Base Color', base)
    mb.to('Roughness', rough_s)
    mb.set(Sheen_Weight=0.15, Sheen_Roughness=0.5, Specular_IOR_Level=0.3, Subsurface_Weight=0.04, Subsurface_Scale=0.0015)
    nrm = mb.bump(height, 0.55, 0.0004)
    mb.to('Normal', nrm)
    mb.height = height; mb.nrm = nrm
    return mb

def foil_overlay(mb, mask, foil_color, rough=0.22):
    """Mix a metallic foil BSDF over the principled using mask."""
    fb = mb.n('ShaderNodeBsdfPrincipled')
    fb.inputs['Base Color'].default_value = foil_color; fb.inputs['Metallic'].default_value = 1.0
    fb.inputs['Roughness'].default_value = rough
    mb.L(mb.nrm, fb.inputs['Normal'])
    mix = mb.n('ShaderNodeMixShader')
    mb.L(mask, mix.inputs['Fac']); mb.L(mb.b.outputs['BSDF'], mix.inputs[1]); mb.L(fb.outputs['BSDF'], mix.inputs[2])
    mb.L(mix.outputs['Shader'], mb.out.inputs['Surface'])
    return fb

def m_emit(name, img=None, color=(1,1,1,1), strength=1.0, glass_coat=True):
    mb = MB(name)
    em = mb.n('ShaderNodeEmission'); em.inputs['Strength'].default_value = strength
    if img:
        t = mb.img(img, mb.coord('UV'), noncolor=False, interp='Smart')
        mb.L(t.outputs['Color'], em.inputs['Color'])
    else:
        em.inputs['Color'].default_value = color
    if glass_coat:
        gl = mb.n('ShaderNodeBsdfGlossy'); gl.inputs['Roughness'].default_value = 0.04
        lw = mb.n('ShaderNodeLayerWeight'); lw.inputs['Blend'].default_value = 0.08
        add = mb.n('ShaderNodeMixShader')
        mb.L(lw.outputs['Fresnel'], add.inputs['Fac']); mb.L(em.outputs['Emission'], add.inputs[1]); mb.L(gl.outputs['BSDF'], add.inputs[2])
        mb.L(add.outputs['Shader'], mb.out.inputs['Surface'])
    else:
        mb.L(em.outputs['Emission'], mb.out.inputs['Surface'])
    return mb

def m_wax(name, color=None):
    mb = MB(name)
    mb.set(Base_Color=color or hexc('#EDE6DA'), Roughness=0.45, Subsurface_Weight=1.0, Subsurface_Radius=(1.0, 0.6, 0.35), Subsurface_Scale=0.01)
    return mb

def m_flame(name, strength=40):
    mb = MB(name)
    em = mb.n('ShaderNodeEmission'); em.inputs['Strength'].default_value = strength
    bb = mb.n('ShaderNodeBlackbody'); bb.inputs['Temperature'].default_value = 1850
    mb.L(bb.outputs['Color'], em.inputs['Color'])
    mb.L(em.outputs['Emission'], mb.out.inputs['Surface'])
    return mb

def m_wood(name, color=None, scale=1.0):
    mb = MB(name)
    v = mb.coord('Object', scale=(1*scale, 22*scale, 1*scale))
    grain = mb.wave(v, 2.2, 'X', distortion=6, detail=4, kind='BANDS', profile='SAW')
    fine = mb.noise(mb.coord('Object', scale=(60*scale, 2*scale, 60*scale)), 3, detail=4)
    g = mb.math('MULTIPLY', grain, fine)
    c = color or hexc('#2A1E17')
    mb.to('Base Color', mb.mixc(mb.maprange(g, 0.1, 0.6, 0, 1), tuple(x*0.55 for x in c[:3])+(1,), c))
    mb.to('Roughness', mb.maprange(g, 0.1, 0.6, 0.38, 0.5))
    mb.set(Coat_Weight=0.4, Coat_Roughness=0.18)
    mb.to('Normal', mb.bump(g, 0.12, 0.001))
    return mb

def m_marble(name, base=None, vein=None):
    mb = MB(name)
    v = mb.coord('Object')
    nz = mb.noise(v, 2.2, detail=12, rough=0.62, distortion=0.8)
    w = mb.wave(v, 1.6, 'X', distortion=14, detail=8, kind='BANDS', profile='SIN')
    vv = mb.maprange(mb.math('ADD', mb.math('MULTIPLY', w, 0.55), mb.math('MULTIPLY', nz, 0.45)), 0.47, 0.5, 0, 1)
    thin = mb.math('SUBTRACT', 1.0, mb.math('ABSOLUTE', mb.math('SUBTRACT', vv, 0.5)))
    vein_m = mb.maprange(thin, 0.88, 1.0, 0, 1)
    b = base or hexc('#0E0C12'); c = vein or hexc('#8D8698')
    mb.to('Base Color', mb.mixc(vein_m, b, c))
    mb.to('Roughness', rough_var(mb, 0.08, 0.05, 3))
    mb.set(Coat_Weight=0.6, Coat_Roughness=0.02)
    return mb

def m_concrete(name, color, rough=0.45, var=0.3):
    mb = MB(name)
    v = mb.coord('Object')
    a = mb.noise(v, 1.4, detail=10, rough=0.6)
    b2 = mb.noise(v, 24, detail=6, rough=0.6)
    mb.to('Base Color', mb.mixc(mb.maprange(a, 0.35, 0.65, 0, 1), tuple(c*(1-var) for c in color[:3])+(1,), color))
    mb.to('Roughness', mb.maprange(a, 0.35, 0.65, rough-0.15, rough+0.15))
    mb.to('Normal', mb.bump(b2, 0.05, 0.002))
    return mb

# ---------- glassware ----------
def wine_glass(name, loc=(0,0,0), seg=128):
    gp = [(0, 0), (0.039, 0.0), (0.0405, 0.0012), (0.0385, 0.0028), (0.016, 0.0055), (0.0055, 0.011), (0.0038, 0.022),
          (0.0035, 0.092), (0.0062, 0.0995), (0.024, 0.110), (0.040, 0.128), (0.0478, 0.152), (0.0472, 0.178), (0.0425, 0.212),
          (0.0372, 0.236), (0.0366, 0.2366), (0.0360, 0.2358), (0.0414, 0.212), (0.0460, 0.178), (0.0466, 0.152),
          (0.0388, 0.1295), (0.0228, 0.1118), (0.006, 0.1018), (0, 0.1012)]
    g = lathe(name, smooth_profile(gp, 3), seg=seg); g.location = loc
    return g

def wine_glass_liquid(name, level=0.135, loc=(0,0,0), seg=128):
    # follows the inner wall, 0.15 mm larger (overlap trick)
    inner = [(0, 0.1010), (0.006, 0.1016), (0.0230, 0.1116), (0.0390, 0.1293), (0.0468, 0.152), (0.0462, 0.178)]
    pts = []
    for (r, z) in smooth_profile(inner, 3):
        if z <= level: pts.append((r + (0.00015 if r > 0 else 0), z))
    # radius at level by interpolation
    prof = smooth_profile(inner, 3)
    for (r0, z0), (r1, z1) in zip(prof[:-1], prof[1:]):
        if z0 <= level <= z1:
            t = (level - z0) / (z1 - z0 + 1e-9); rl = r0 + t*(r1 - r0) + 0.00015; break
    pts.append((rl, level)); pts.append((rl*0.985, level + 0.0006)); pts.append((0, level + 0.0004))
    w = lathe(name, pts, seg=seg); w.location = loc
    return w

def tumbler(name, loc=(0,0,0), r=0.040, h=0.095, wall=0.0028, base=0.009, seg=128):
    p = [(0, 0), (r - 0.002, 0), (r - 0.0002, 0.0012), (r, 0.004), (r + 0.0012, h - 0.003), (r + 0.0011, h), (r + 0.0002, h + 0.0006),
         (r - wall + 0.0004, h), (r - wall, h - 0.002), (r - wall - 0.001, base + 0.003), (r - wall - 0.004, base), (0, base - 0.0006)]
    t = lathe(name, smooth_profile(p, 2), seg=seg); t.location = loc
    return t

def tumbler_water(name, loc=(0,0,0), r=0.040, wall=0.0028, base=0.009, level=0.062, seg=128):
    ri = r - wall + 0.00015
    p = [(0, base - 0.0006 - 0.00015), (ri - 0.004, base - 0.00015), (ri - 0.001, base + 0.003), (ri + 0.0006 * (level - base) / 0.09, level),
         (ri - 0.0012, level + 0.0012), (0, level + 0.0009)]
    w = lathe(name, smooth_profile(p, 1), seg=seg); w.location = loc
    return w

def bottle(name, loc=(0,0,0), seg=128):
    p = [(0, 0.004), (0.010, 0.0065), (0.018, 0.004), (0.036, 0.0005), (0.041, 0.0), (0.0425, 0.004), (0.0428, 0.180),
         (0.040, 0.198), (0.030, 0.222), (0.0175, 0.240), (0.0145, 0.252), (0.0145, 0.276), (0.0158, 0.279), (0.0158, 0.284),
         (0.0143, 0.2865), (0.0113, 0.286), (0.0112, 0.276), (0.0112, 0.252), (0.0142, 0.240), (0.0273, 0.222), (0.0372, 0.198),
         (0.0398, 0.180), (0.0396, 0.010), (0.034, 0.0075), (0.018, 0.0095), (0.010, 0.0125), (0, 0.0115)]
    b = lathe(name, smooth_profile(p, 3), seg=seg); b.location = loc
    return b

def bottle_water(name, level=0.205, loc=(0,0,0), seg=128):
    inner = [(0, 0.0115), (0.010, 0.0125), (0.018, 0.0095), (0.034, 0.0075), (0.0396, 0.010), (0.0398, 0.180), (0.0372, 0.198), (0.0273, 0.222)]
    prof = smooth_profile(inner, 3)
    pts = [(r + (0.00015 if r > 0 else 0), z - (0.00015 if r == 0 else 0)) for (r, z) in prof if z <= level]
    for (r0, z0), (r1, z1) in zip(prof[:-1], prof[1:]):
        if z0 <= level <= z1 and z1 > z0:
            t = (level - z0) / (z1 - z0); rl = r0 + t*(r1 - r0) + 0.00015; break
    pts.append((rl, level)); pts.append((rl*0.985, level + 0.0006)); pts.append((0, level + 0.0004))
    w = lathe(name, pts, seg=seg); w.location = loc
    return w

def m_liquid_vol(name, absorb_color, density, ior=1.333, tint=(1,1,1,1)):
    mb = MB(name)
    mb.set(Base_Color=tint, Transmission_Weight=1.0, IOR=ior, Roughness=0.0)
    va = mb.n('ShaderNodeVolumeAbsorption'); va.inputs['Color'].default_value = absorb_color; va.inputs['Density'].default_value = density
    mb.L(va.outputs['Volume'], mb.out.inputs['Volume'])
    return mb

def emissive_plane(name, loc, rot, size, color, strength, radial=True):
    bpy.ops.mesh.primitive_plane_add(size=1, location=loc, rotation=rot)
    ob = bpy.context.object; ob.name = name; ob.scale = (size[0], size[1], 1)
    mb = MB(name)
    em = mb.n('ShaderNodeEmission'); em.inputs['Color'].default_value = color
    if radial:
        tc = mb.n('ShaderNodeTexCoord'); sep = mb.n('ShaderNodeSeparateXYZ'); mb.L(tc.outputs['Generated'], sep.inputs[0])
        dx = mb.math('SUBTRACT', sep.outputs[0], 0.5); dy = mb.math('SUBTRACT', sep.outputs[1], 0.5)
        d = mb.math('SQRT', mb.math('ADD', mb.math('MULTIPLY', dx, dx), mb.math('MULTIPLY', dy, dy)))
        f = mb.math('POWER', mb.maprange(d, 0.0, 0.5, 1.0, 0.0), 1.8)
        mb.L(mb.math('MULTIPLY', f, strength), em.inputs['Strength'])
    else:
        em.inputs['Strength'].default_value = strength
    mb.L(em.outputs['Emission'], mb.out.inputs['Surface'])
    assign(ob, mb.m)
    ob.visible_shadow = False
    return ob

def kelvin_rgb(t):
    t = t/100.0
    if t <= 66: r = 255; g = 99.4708025861*math.log(t) - 161.1195681661
    else: r = 329.698727446*((t-60)**-0.1332047592); g = 288.1221695283*((t-60)**-0.0755148492)
    if t >= 66: b = 255
    elif t <= 19: b = 0
    else: b = 138.5177312231*math.log(t-10) - 305.0447927307
    c = [max(0, min(255, x))/255 for x in (r, g, b)]
    return tuple(srgb2lin(x) for x in c) + (1,)

def m_planks(name, color=None, plank_w=0.19, plank_l=1.4):
    """Dark smoked-oak plank floor: per-plank tone, distorted grain, fine gaps."""
    mb = MB(name)
    tc = mb.n('ShaderNodeTexCoord')
    br = mb.n('ShaderNodeTexBrick'); br.offset = 0.5; br.offset_frequency = 2; br.squash = 1.0; br.squash_frequency = 2
    br.inputs['Scale'].default_value = 1.0; br.inputs['Mortar Size'].default_value = 0.0018; br.inputs['Mortar Smooth'].default_value = 0.2
    br.inputs['Brick Width'].default_value = plank_l; br.inputs['Row Height'].default_value = plank_w; br.inputs['Bias'].default_value = 0.0
    br.inputs['Color1'].default_value = (0.78, 0.78, 0.78, 1); br.inputs['Color2'].default_value = (1.12, 1.12, 1.12, 1); br.inputs['Mortar'].default_value = (0.02, 0.02, 0.02, 1)
    mb.L(tc.outputs['Object'], br.inputs['Vector'])
    gv = mb.coord('Object', scale=(0.6, 14, 1))
    grain = mb.wave(gv, 3.0, 'X', distortion=7, detail=6, kind='BANDS', profile='SIN')
    fine = mb.noise(mb.coord('Object', scale=(3, 60, 3)), 4, detail=3)
    g = mb.math('MULTIPLY', grain, mb.maprange(fine, 0.3, 0.7, 0.7, 1.0))
    c = color or hexc('#2B211D')
    wood = mb.mixc(mb.maprange(g, 0.2, 0.8, 0, 1), tuple(x*0.55 for x in c[:3]) + (1,), c)
    mul = mb.n('ShaderNodeMix'); mul.data_type = 'RGBA'; mul.blend_type = 'MULTIPLY'; mul.inputs[0].default_value = 1.0
    mb.L(wood, mul.inputs[6]); mb.L(br.outputs['Color'], mul.inputs[7])
    mb.to('Base Color', mul.outputs[2])
    mb.to('Roughness', mb.maprange(g, 0.2, 0.8, 0.32, 0.46))
    mb.set(Coat_Weight=0.35, Coat_Roughness=0.12)
    gap = mb.math('SUBTRACT', 1.0, br.outputs['Fac'])
    mb.to('Normal', mb.bump(mb.math('ADD', mb.math('MULTIPLY', g, 0.2), mb.math('MULTIPLY', gap, 1.0)), 0.25, 0.002))
    return mb
