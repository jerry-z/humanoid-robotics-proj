import gym
import numpy as np, os

from gym.envs.mujoco import Walker2dNotDoneEnv
from gym.envs.mujoco.hill import HillEnv
from gym.envs.mujoco.hill import terrain
from gym.utils.overrides import overrides


class Walker2DHillEnv(HillEnv):

    MODEL_CLASS = Walker2dNotDoneEnv

    @overrides
    def _mod_hfield(self, hfield):
        # clear a flat patch for the robot to start off from
        return terrain.clear_patch(
            hfield,
            gym.spaces.Box(
                np.array([-2.0, -2.0]),
                np.array([-0.5, -0.5]), dtype=np.float32))


FIELD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fielddata'))

class Walker2DXUpHillEnv(Walker2DHillEnv):
    def __init__(self, difficulty=1.0, 
                 texturedir=FIELD_DIR + '/mujoco_textures_xup', 
                 hfield_dir=FIELD_DIR + '/mujoco_terrains_xup'):
        Walker2DHillEnv.__init__(self, difficulty=difficulty, texturedir=texturedir, hfield_dir=hfield_dir)


class Walker2DXDownHillEnv(Walker2DHillEnv):
    def __init__(self, difficulty=1.0, 
                 texturedir=FIELD_DIR + '/mujoco_textures_xdown', 
                 hfield_dir=FIELD_DIR + '/mujoco_terrains_xdown'):
        Walker2DHillEnv.__init__(self, difficulty=difficulty, texturedir=texturedir, hfield_dir=hfield_dir)