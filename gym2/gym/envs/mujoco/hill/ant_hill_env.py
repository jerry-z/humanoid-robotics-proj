import gym
import numpy as np, os

from gym.envs.mujoco import AntNotDoneEnv
from gym.envs.mujoco.hill import HillEnv
from gym.envs.mujoco.hill import terrain
from gym.utils.overrides import overrides


class AntHillEnv(HillEnv):

    MODEL_CLASS = AntNotDoneEnv

    @overrides
    def _mod_hfield(self, hfield):
        # clear a flat patch for the robot to start off from
        hfield = terrain.clear_patch(
            hfield,
            gym.spaces.Box(
                np.array([-2.0, -2.0]),
                np.array([-0.5, -0.5]), dtype=np.float32))
        print(hfield.max(), hfield.min())
        return hfield

FIELD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fielddata'))

class AntXUpHillEnv(AntHillEnv):
    def __init__(self, difficulty=1.0, 
                 texturedir=FIELD_DIR + '/mujoco_textures_xup', 
                 hfield_dir=FIELD_DIR + '/mujoco_terrains_xup'):
        AntHillEnv.__init__(self, difficulty=difficulty, texturedir=texturedir, hfield_dir=hfield_dir)
        

class AntXDownHillEnv(AntHillEnv):
    def __init__(self, difficulty=1.0, 
                 texturedir=FIELD_DIR + '/mujoco_textures_xdown', 
                 hfield_dir=FIELD_DIR + '/mujoco_terrains_xdown'):
        AntHillEnv.__init__(self, difficulty=difficulty, texturedir=texturedir, hfield_dir=hfield_dir)