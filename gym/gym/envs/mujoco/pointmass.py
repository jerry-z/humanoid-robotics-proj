import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
import math

target = np.array([2.0, 2.0])

class PointMassEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self, file_path='pointmass.xml'):
        mujoco_env.MujocoEnv.__init__(self, file_path, 2)
        utils.EzPickle.__init__(self)

    def step(self, action):
        #posbefore = self.sim.data.qpos[0]
        self.do_simulation(action, self.frame_skip)
        dist = np.linalg.norm(self.sim.data.qpos[:2].copy() - target)
        #reward = (posafter - posbefore) / self.dt
        reward = -dist - 1e-3 * np.square(action).sum()
        done = False
        ob = self._get_obs()
        return ob, reward, done, {}

    def _get_obs(self):
        return np.concatenate([
            self.sim.data.qpos.flat,
            self.sim.data.qvel.flat,
        ])

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(low=-.1, high=.1, size=self.model.nq)
        qvel = self.init_qvel + self.np_random.randn(self.model.nv) * .1
        self.set_state(qpos, qvel)
        return self._get_obs()

    def viewer_setup(self):
        self.viewer.cam.distance = self.model.stat.extent * 0.5
