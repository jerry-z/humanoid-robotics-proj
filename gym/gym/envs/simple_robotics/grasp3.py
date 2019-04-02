import numpy as np
from gym import utils
from gym.envs.simple_robotics import simple_robotics_env
from gym.envs.simple_robotics.grasp_relative import GraspRelativeEnv
from gym.envs.simple_robotics import rotations

TORQUE_LIMIT_P = 0.25
TORQUE_LIMIT_D = 0.50 
TORQUE_LIMIT = [TORQUE_LIMIT_P, TORQUE_LIMIT_D, TORQUE_LIMIT_P, TORQUE_LIMIT_D]


class Grasp3Env(GraspRelativeEnv):
    # penalize on moving object
    def __init__(self, *args, **kwargs):
        self.old_object_pos = np.zeros(3)
        GraspRelativeEnv.__init__(self, *args, **kwargs)

    def compute_reward(self, version='naive'):
        four_torques = self.compute_torques()
        if version == 'naive':
            return four_torques
        elif version == 'strict_tips':
            if self.distal_contact() and self.fingers_contact():
                #return 5.0 - np.linalg.norm(four_torques - TORQUE_LIMIT)  # make sure this reward is positive ow the agent will pre-terminate the episode
                return np.exp(-np.linalg.norm(four_torques - TORQUE_LIMIT) / 0.035)
            else:
                return 0


class GraspCube3Env(Grasp3Env):
    def __init__(self):
        Grasp3Env.__init__(self, 'seahand/manipulate_block.xml', 1)


class GraspEgg3Env(Grasp3Env):
    def __init__(self):
        Grasp3Env.__init__(self, 'seahand/manipulate_egg.xml', 1)


class GraspPen3Env(Grasp3Env):
    def __init__(self):
        Grasp3Env.__init__(self, 'seahand/manipulate_pen.xml', 1)


class GraspBall3Env(Grasp3Env):
    def __init__(self):
        Grasp3Env.__init__(self, 'seahand/manipulate_ball.xml', 1)


class GraspCylinder3Env(Grasp3Env):
    def __init__(self):
        Grasp3Env.__init__(self, 'seahand/manipulate_cylinder.xml', 1)
