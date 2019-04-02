import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
from gym.envs.mujoco import mujoco_calibrator_env

class HopperEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self, file_path='hopper.xml'):
        mujoco_env.MujocoEnv.__init__(self, file_path, 4)
        utils.EzPickle.__init__(self)

    def step(self, a):
        posbefore = self.sim.data.qpos[0]
        self.do_simulation(a, self.frame_skip)
        posafter, height, ang = self.sim.data.qpos[0:3]
        alive_bonus = 1.0
        reward = (posafter - posbefore) / self.dt
        reward += alive_bonus
        reward -= 1e-3 * np.square(a).sum()
        s = self.state_vector()
        done = not (np.isfinite(s).all() and (np.abs(s[2:]) < 100).all() and
                    (height > .7) and (abs(ang) < .2))
        ob = self._get_obs()
        return ob, reward, done, {}

    def _get_obs(self):
        return np.concatenate([
            self.sim.data.qpos.flat[1:],
            np.clip(self.sim.data.qvel.flat, -10, 10)
        ])

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(low=-.005, high=.005, size=self.model.nq)
        qvel = self.init_qvel + self.np_random.uniform(low=-.005, high=.005, size=self.model.nv)
        self.set_state(qpos, qvel)
        return self._get_obs()

    def viewer_setup(self):
        self.viewer.cam.trackbodyid = 2
        self.viewer.cam.distance = self.model.stat.extent * 0.75
        self.viewer.cam.lookat[2] += .8
        self.viewer.cam.elevation = -20

<<<<<<< HEAD
class HopperNotDoneEnv(mujoco_calibrator_env.MujocoEnv, utils.EzPickle):
    def __init__(self, file_path='hopper.xml'):
        mujoco_calibrator_env.MujocoEnv.__init__(self, file_path, 4)
        utils.EzPickle.__init__(self)

    def step(self, a):
        """
        xposbefore = self.get_body_com("torso")[0]

        # add additional position controls to calibrator
        # read com of current object
        currentcom = self.get_body_com("torso")[:2].copy()
        a = np.append(a, currentcom)

        # do simulation
        self.do_simulation(a, self.frame_skip)

        # get the height of calibrator
        calibrator_height = self.get_body_com("calibrator")[2].copy()
        """
        posbefore = self.sim.data.qpos[0]

        # add additional position controls to calibrator
        # read com of current object
        currentcom = self.get_body_com("torso")[:2].copy()
        a = np.append(a, currentcom)

        # do simulation
        self.do_simulation(a, self.frame_skip)

        # after simulation
        # get the height of calibrator
        calibrator_height = self.get_body_com("calibrator")[2].copy()

        posafter, height, ang = self.sim.data.qpos[0:3]
        alive_bonus = 1.0
        reward = (posafter - posbefore) / self.dt
        reward += alive_bonus
        reward -= 1e-3 * np.square(a).sum()
        s = self.state_vector()
        #done = not (np.isfinite(s).all() and (np.abs(s[2:]) < 100).all() and
        #            (height > .7) and (abs(ang) < .2))
        done = not (np.isfinite(s).all() and (height - calibrator_height > .7) and (abs(ang) < .2))
        #print(height, calibrator_height)
        ob = self._get_obs()
        return ob, reward, done, {}

    def _get_obs(self):
        return np.concatenate([
            self.sim.data.qpos.flat[1:-3],
            np.clip(self.sim.data.qvel[:-3].flat, -10, 10)
        ])

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(low=-.005, high=.005, size=self.model.nq)
        qvel = self.init_qvel + self.np_random.uniform(low=-.005, high=.005, size=self.model.nv)
        self.set_state(qpos, qvel)
        return self._get_obs()

    def viewer_setup(self):
        self.viewer.cam.trackbodyid = 2
        #self.viewer.cam.distance = self.model.stat.extent * 0.75
        #self.viewer.cam.lookat[2] += .8
        #self.viewer.cam.elevation = -20

=======
>>>>>>> 44c77177a09363660f47cedaa7ed66e3b833f57b

class HopperPOMDPEnv(HopperEnv):
    def __init__(self):
        HopperEnv.__init__(self)

    def _get_obs(self):
        return np.concatenate([
            self.sim.data.qpos.flat[:]
        ])
