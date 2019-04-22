import gym
import numpy as np, os

from gym.envs.mujoco import PointMassEnv
from gym.envs.mujoco.hill import HillEnv
from gym.envs.mujoco.hill import terrain
from gym.utils.overrides import overrides

class PointMassHillEnv(HillEnv):

    MODEL_CLASS = PointMassEnv

    @overrides
    def _mod_hfield(self, hfield):
        # clear a flat patch for the robot to start off from
        return terrain.clear_patch(
            hfield,
            gym.spaces.Box(
                np.array([-2.0, -2.0]),
                np.array([-0.5, -0.5]), dtype=np.float32))

FIELD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fielddata'))

class PointMassXUpHillEnv(PointMassHillEnv):
    def __init__(self, difficulty=10.0, 
                 texturedir=FIELD_DIR + '/mujoco_textures_xup', 
                 hfield_dir=FIELD_DIR + '/mujoco_terrains_xup'):
        PointMassHillEnv.__init__(self, difficulty=difficulty, texturedir=texturedir, hfield_dir=hfield_dir)


class PointMassXDownHillEnv(PointMassHillEnv):
    def __init__(self, difficulty=10.0, 
                 texturedir=FIELD_DIR + '/mujoco_textures_xdown', 
                 hfield_dir=FIELD_DIR + '/mujoco_terrains_xdown'):
        PointMassHillEnv.__init__(self, difficulty=difficulty, texturedir=texturedir, hfield_dir=hfield_dir)
