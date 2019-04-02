import gym
import numpy as np, os

from gym.envs.mujoco import HopperNotDoneEnv
from gym.envs.mujoco.hill import HillEnv
from gym.envs.mujoco.hill import terrain
from gym.utils.overrides import overrides


class HopperHillEnv(HillEnv):

    MODEL_CLASS = HopperNotDoneEnv

    @overrides
    def _mod_hfield(self, hfield):
        # clear a flat patch for the robot to start off from
        return terrain.clear_patch(
            hfield,
            gym.spaces.Box(
                np.array([-2.0, -2.0]),
                np.array([-0.5, -0.5]), dtype=np.float32))

FIELD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fielddata'))

class HopperXUpHillEnv(HopperHillEnv):
    def __init__(self, difficulty=1.0, 
                 texturedir=FIELD_DIR + '/mujoco_textures_xup', 
                 hfield_dir=FIELD_DIR + '/mujoco_terrains_xup'):
        HopperHillEnv.__init__(self, difficulty=difficulty, texturedir=texturedir, hfield_dir=hfield_dir)


class HopperXDownHillEnv(HopperHillEnv):
    def __init__(self, difficulty=1.0, 
                 texturedir=FIELD_DIR + '/mujoco_textures_xdown', 
                 hfield_dir=FIELD_DIR + '/mujoco_terrains_xdown'):
        HopperHillEnv.__init__(self, difficulty=difficulty, texturedir=texturedir, hfield_dir=hfield_dir)
