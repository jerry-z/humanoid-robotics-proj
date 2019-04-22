import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
from gym.envs.mujoco import mujoco_calibrator_env

class Walker2dEnv(mujoco_env.MujocoEnv, utils.EzPickle):

    def __init__(self, file_path="walker2d.xml"):
        mujoco_env.MujocoEnv.__init__(self, file_path, 4)
        utils.EzPickle.__init__(self)

    def step(self, a):
        posbefore = self.sim.data.qpos[0]
        self.do_simulation(a, self.frame_skip)
        posafter, height, ang = self.sim.data.qpos[0:3]
        alive_bonus = 1.0
        reward = ((posafter - posbefore) / self.dt)
        reward += alive_bonus
        reward -= 1e-3 * np.square(a).sum()
        done = not (height > 0.8 and height < 2.0 and
                    ang > -1.0 and ang < 1.0)
        ob = self._get_obs()
        return ob, reward, done, {}

    def _get_obs(self):
        qpos = self.sim.data.qpos
        qvel = self.sim.data.qvel
        return np.concatenate([qpos[1:], np.clip(qvel, -10, 10)]).ravel()

    def reset_model(self):
        self.set_state(
            self.init_qpos + self.np_random.uniform(low=-.005, high=.005, size=self.model.nq),
            self.init_qvel + self.np_random.uniform(low=-.005, high=.005, size=self.model.nv)
        )
        return self._get_obs()

    def viewer_setup(self):
        self.viewer.cam.trackbodyid = 2
        self.viewer.cam.distance = self.model.stat.extent * 0.5
        self.viewer.cam.lookat[2] += .8
        self.viewer.cam.elevation = -20

<<<<<<< HEAD
class Walker2dNotDoneEnv(mujoco_calibrator_env.MujocoEnv, utils.EzPickle):

    def __init__(self, file_path="walker2d.xml"):
        mujoco_calibrator_env.MujocoEnv.__init__(self, file_path, 4)
        utils.EzPickle.__init__(self)

    def step(self, a):
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

        # get obs
        posafter, height, ang = self.sim.data.qpos[0:3]
        alive_bonus = 1.0
        reward = ((posafter - posbefore) / self.dt)
        reward += alive_bonus
        reward -= 1e-3 * np.square(a).sum()
        done = not (height - calibrator_height > 0.8 and height - calibrator_height < 2.0 and
                    ang > -1.0 and ang < 1.0)
        #done = False
        ob = self._get_obs()
        return ob, reward, done, {}

    def _get_obs(self):
        qpos = self.sim.data.qpos[:-3]
        qvel = self.sim.data.qvel[:-3]
        return np.concatenate([qpos[1:], np.clip(qvel, -10, 10)]).ravel()

    def reset_model(self):
        self.set_state(
            self.init_qpos + self.np_random.uniform(low=-.005, high=.005, size=self.model.nq),
            self.init_qvel + self.np_random.uniform(low=-.005, high=.005, size=self.model.nv)
        )
        return self._get_obs()

    def viewer_setup(self):
        self.viewer.cam.trackbodyid = 2
        #self.viewer.cam.distance = self.model.stat.extent * 0.5
        #self.viewer.cam.lookat[2] += .8
        #self.viewer.cam.elevation = -20
=======

>>>>>>> 44c77177a09363660f47cedaa7ed66e3b833f57b

class Walker2dPOMDPEnv(Walker2dEnv):
    def __init__(self):
        Walker2dEnv.__init__(self)

    def _get_obs(self):
        qpos = self.sim.data.qpos
        return np.concatenate([qpos[:]]).ravel()
