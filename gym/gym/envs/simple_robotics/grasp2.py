import numpy as np
from gym import utils
from gym.envs.simple_robotics import simple_robotics_env
from gym.envs.simple_robotics.grasp import GraspEnv
from gym.envs.simple_robotics import rotations


class Grasp2Env(GraspEnv):
    # penalize on moving object
    def __init__(self, *args, **kwargs):
        self.old_object_pos = np.zeros(3)
        GraspEnv.__init__(self, *args, **kwargs)

    def reset_model(self):
        # qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-.01, high=.01)
        failed = True
        while failed:
            qvel = self.init_qvel # + self.np_random.randn(self.model.nv) * .01
            # random object com
            initial_obj_com = self.init_objpos[:3] + self.np_random.uniform(size=3, low=-.01, high=.01)
            # random object z rotation
            angle = self.np_random.uniform(-np.pi, np.pi)
            axis = np.array([0., 0., 1.])
            offset_quat = rotations.quat_from_angle_and_axis(angle, axis)
            initial_obj_quat = self.init_objpos[3:].copy()
            initial_obj_quat = rotations.quat_mul(initial_obj_quat, offset_quat)
            initial_obj_quat /= np.linalg.norm(initial_obj_quat)
            qpos = np.concatenate((self.init_handpos, initial_obj_com, initial_obj_quat))
            # set state
            self.set_state(qpos, qvel)
            failed = not self.in_reach()
        return self._get_obs()

    def step(self, action, render=True):
        action = action.flatten()
        # assert np.shape(a) == (4,)
        # reward = 0  # yet to specify
        # self.do_simulation(a, self.frame_skip)
        # done = False
        # ob = self._get_obs()
        action = np.clip(action, self.action_space.low, self.action_space.high)
        self._set_action(action)
        # weird thing here: it seems that old_object_pos == new_object_pos in the following
        # probably has to do with the fact that we use position control?
        #old_object_pos = self.sim.data.get_body_xpos("object")
        #self.sim.step()
        #new_object_pos = self.sim.data.get_body_xpos("object")
        self.sim.step()
        new_object_pos = self.sim.data.get_body_xpos('object').copy()
        object_vel = np.linalg.norm(new_object_pos - self.old_object_pos) / self.dt
        self.old_object_pos = new_object_pos.copy()
        obs = self._get_obs()
        if not render:
            done = not self.in_reach()
        else:
            done = False
        info = {}
        reward = self.compute_reward(version='strict_tips')
        reward -= 10.0 * object_vel # penalize on moving object
        #print(reward)
        #print(object_vel)
        return obs, reward, done, info


class GraspCube2Env(Grasp2Env):
    def __init__(self):
        Grasp2Env.__init__(self, 'seahand/manipulate_block.xml', 1)


class GraspEgg2Env(Grasp2Env):
    def __init__(self):
        Grasp2Env.__init__(self, 'seahand/manipulate_egg.xml', 1)


class GraspPen2Env(Grasp2Env):
    def __init__(self):
        Grasp2Env.__init__(self, 'seahand/manipulate_pen.xml', 1)


class GraspBall2Env(Grasp2Env):
    def __init__(self):
        Grasp2Env.__init__(self, 'seahand/manipulate_ball.xml', 1)


class GraspCylinder2Env(Grasp2Env):
    def __init__(self):
        Grasp2Env.__init__(self, 'seahand/manipulate_cylinder.xml', 1)
