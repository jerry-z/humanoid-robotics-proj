import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env

class Swimmer3dRllabEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self):
        mujoco_env.MujocoEnv.__init__(self, 'swimmer3drllab.xml', 4)
        utils.EzPickle.__init__(self)

    def step(self, a):
        ctrl_cost_coeff = 1e-2
        posbefore = self.sim.data.qpos
        self.do_simulation(a, self.frame_skip)
        posafter = self.sim.data.qpos
        # compute com vel
        reward_fwd = np.linalg.norm((posafter - posbefore) / self.dt)
        reward_ctrl = - ctrl_cost_coeff * 0.5 * np.square(a).sum()
        reward = reward_fwd + reward_ctrl
        ob = self._get_obs()
        return ob, reward, False, dict(reward_fwd=reward_fwd, reward_ctrl=reward_ctrl)

    def _get_obs(self):
        return np.concatenate([
            self.sim.data.qpos.flat,
            self.sim.data.qvel.flat,
            self.get_body_com("torso").flat,
        ]).reshape(-1)

    def reset_model(self):
        self.set_state(
            self.init_qpos + self.np_random.uniform(low=-.1, high=.1, size=self.model.nq),
            self.init_qvel + self.np_random.uniform(low=-.1, high=.1, size=self.model.nv)
        )
        return self._get_obs()
