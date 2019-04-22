import numpy as np
import terrain
import gym
from gym.spaces import Box

HFIELD_FNAME = 'hills.png'
TEXTURE_FNAME = 'hills_texture.png'
hfield_dir = 'fielddata/mujoco_terrains_walker2dxdown'
texturedir = 'fielddata/mujoco_textures_walker2dxdown'

def gen_terrain(regen=True):
    # logger.log("Process {0} generating terrain...".format(os.getpid()))
    #x, y, hfield = terrain.generate_hills(40, 40, 500)
    x, y, hfield = terrain.generate_x_uphill(40, 40, 500)
    hfield *= -1.0
    #hfield = mod_hfield(hfield)
    terrain.save_heightfield(
         x, y, hfield, HFIELD_FNAME, path=hfield_dir)
    terrain.save_texture(
            x, y, hfield, TEXTURE_FNAME, path=texturedir)

def mod_hfield(hfield):
    # clear a flat patch for the robot to start off from
    hfield = terrain.clear_patch(
        hfield,
        Box(
            np.array([-2.0, -2.0]),
            np.array([-0.5, -0.5]), dtype=np.float32))
    print(hfield.max(), hfield.min())
    return hfield

gen_terrain()