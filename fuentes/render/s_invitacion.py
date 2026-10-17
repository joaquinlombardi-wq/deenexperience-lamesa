import sys; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from lib import *
random.seed(2)
reset(); setup(1800, 1200, samples=128, exposure=-0.4, look='AgX - Medium High Contrast')
world_color(hexc('#120E20'), 0.03)

# --- velvet ground with soft folds ---
vel = grid('Terciopelo', 1.2, 1.2, 220, 220, loc=(0, 0, -0.002))
displace_noise(vel, 0.16, 0.012, depth=2); displace_noise(vel, 0.05, 0.0025, depth=1); subsurf(vel, 1)
assign(vel, m_velvet('Terciopelo', hexc('#26124F'), sheen_tint=hexc('#9A7CF0'), scale=60).m)

# --- envelope (lilac cotton) ---
EW, EH, ET = 0.195, 0.138, 0.0016
env = grid('Sobre', EW, EH, 40, 30, loc=(0.035, 0.03, ET), rot=(0, 0, math.radians(-14)))
solidify(env, ET); m = env.modifiers.new('bev', 'BEVEL'); m.width = 0.0004; m.segments = 2
envm = m_paper('Sobre', hexc('#DCD2F6'), fiber=0.22, rough=0.9)
assign(env, envm.m)
# flap: triangle lying on top, tip toward -y (toward camera after rotation)
fv = [(-EW/2, EH/2 - 0.001, 0), (EW/2, EH/2 - 0.001, 0), (0, -0.012, 0)]
flap = mesh_obj('Solapa', fv, [(0, 1, 2)], smooth=False)
flap.parent = env; flap.location = (0, 0, 0.0012)
solidify(flap, 0.0005); m = flap.modifiers.new('bev', 'BEVEL'); m.width = 0.00035; m.segments = 2
assign(flap, envm.m)
# wax seal on the flap tip
seal = grid('Lacre', 0.042, 0.042, 220, 220)
seal.parent = env; seal.location = (0.0, -0.006, 0.0016); seal.rotation_euler = (0, 0, math.radians(9))
displace_img(seal, TEX + 'seal_h.png', 0.0042, mid=0.0); subsurf(seal, 1)
smb = MB('Lacre')
mask = smb.img(TEX + 'seal_mask.png', smb.coord('UV')).outputs['Color']
smb.set(Base_Color=hexc('#3E2DB0'), Roughness=0.32, Coat_Weight=0.6, Coat_Roughness=0.12, Subsurface_Weight=0.25, Subsurface_Scale=0.002,
        Subsurface_Radius=(0.5, 0.35, 1.0))
smb.to('Roughness', rough_var(smb, 0.3, 0.12, 120))
smb.to('Alpha', mask)
assign(seal, smb.m)

# --- the card: ink cotton board, lilac-silver foil, painted violet edges, blind deboss ---
CW, CH, CT = 0.127, 0.178, 0.0017
card = grid('Invitacion', CW, CH, 60, 80, loc=(-0.028, -0.006, ET*2 + 0.0026 + CT), rot=(0, 0, math.radians(6)))
card.rotation_euler = (math.radians(-1.2), math.radians(0.6), math.radians(6))
sol = solidify(card, CT); sol.material_offset_rim = 1
m = card.modifiers.new('bev', 'BEVEL'); m.width = 0.00025; m.segments = 2
cm = m_paper('Cartulina', hexc('#17131F'), deboss_img=TEX + 'invite_deboss.png', deboss_strength=0.9,
             foil_img=TEX + 'invite_foil.png', fiber=0.3, rough=0.86)
foil = cm.foil_mask
cm.nrm  # foil sits pressed into the board
h2 = cm.math('SUBTRACT', cm.height, cm.math('MULTIPLY', foil, 0.35))
n2 = cm.bump(h2, 0.6, 0.0004)
cm.to('Normal', n2); cm.nrm = n2
cm.set(Specular_IOR_Level=0.18, Sheen_Weight=0.08)
foil_overlay(cm, foil, hexc('#CFC4F7'), rough=0.17)
edge = MB('Canto'); edge.set(Base_Color=hexc('#5B49D8'), Roughness=0.55, Sheen_Weight=0.3)
card.data.materials.append(cm.m); card.data.materials.append(edge.m)

# --- light ---
area('Window', (-0.55, 0.42, 0.62), (0, 0, 0), 5.5, 0.7, 0.45, temp=5400, spread=70)
area('FoilKick', (-0.05, 0.55, 0.5), (-0.03, 0.02, 0.0), 4, 0.32, 0.12, temp=6000)
area('Fill', (0.6, -0.5, 0.4), (0, 0, 0), 0.6, 0.6, temp=3200)
area('VioletRim', (0.55, 0.45, 0.12), (0, 0, 0), 1.6, 0.6, 0.2, color=hexc('#6C5AE6'))

camera((-0.005, -0.385, 0.56), (-0.012, 0.004, 0.0), lens=85, fstop=3.2, focus=None)
render('invitacion')
