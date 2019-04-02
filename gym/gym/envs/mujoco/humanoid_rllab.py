import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
from gym.envs.mujoco import simple_humanoid_rllab

class HumanoidRllabEnv(simple_humanoid_rllab.SimpleHumanoidRllabEnv):
    def __init__(self):
        simple_humanoid_rllab.SimpleHumanoidRllabEnv.__init__(self, filename='humanoid_rllab.xml')


class HumanoidRllabPOMDPEnv(simple_humanoid_rllab.SimpleHumanoidRllabPOMDPEnv):
    def __init__(self):
        simple_humanoid_rllab.SimpleHumanoidRllabPOMDPEnv.__init__(self, filename='humanoid_rllab.xml')