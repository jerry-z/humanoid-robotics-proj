import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env

class SimpleHumanoidRllabEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self, vel_deviation_cost_coeff=1e-2, alive_bonus=0.2, ctrl_cost_coeff=1e-3, impact_cost_coeff=1e-5,
        filename='simple_humanoid_rllab.xml'):
        self.vel_deviation_cost_coeff = vel_deviation_cost_coeff
        self.alive_bonus = alive_bonus
        self.ctrl_cost_coeff = ctrl_cost_coeff
        self.impact_cost_coeff = impact_cost_coeff
        mujoco_env.MujocoEnv.__init__(self, filename, 5)
        utils.EzPickle.__init__(self)

    def get_current_obs(self):
        data = self.sim.data
        return np.concatenate([data.qpos.flat,
                               data.qvel.flat,
                               np.clip(data.cfrc_ext, -1, 1).flat,
                               self.get_body_com("torso").flat,])

    def _get_com(self):
        data = self.sim.data
        mass = self.model.body_mass
        xpos = data.xipos
        return (np.sum(mass * xpos, 0) / np.sum(mass))[0]

    def step(self, action):
        self.do_simulation(action, self.frame_skip)
        next_obs = self.get_current_obs()

        alive_bonus = self.alive_bonus
        data = self.sim.data

        comvel = self.get_body_com("torso")

        lin_vel_reward = comvel[0]
        lb, ub = self.action_bounds
        scaling = (ub - lb) * 0.5
        ctrl_cost = .5 * self.ctrl_cost_coeff * np.sum(
            np.square(action / scaling))
        impact_cost = .5 * self.impact_cost_coeff * np.sum(
            np.square(np.clip(data.cfrc_ext, -1, 1)))
        vel_deviation_cost = 0.5 * self.vel_deviation_cost_coeff * np.sum(
            np.square(comvel[1:]))
        reward = lin_vel_reward + alive_bonus - ctrl_cost - \
            impact_cost - vel_deviation_cost
        done = data.qpos[2] < 0.8 or data.qpos[2] > 2.0

        return next_obs, reward, done, {}

    def _get_obs(self):
        return np.concatenate([
            self.sim.data.qpos.flat[2:],
            self.sim.data.qvel.flat,
            np.clip(self.sim.data.cfrc_ext, -1, 1).flat,
        ])

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-.1, high=.1)
        qvel = self.init_qvel + self.np_random.randn(self.model.nv) * .1
        self.set_state(qpos, qvel)
        return self.get_current_obs()

    def viewer_setup(self):
        self.viewer.cam.distance = self.model.stat.extent * 0.5 


class SimpleHumanoidRllabPOMDPEnv(SimpleHumanoidRllabEnv):
    def __init__(self):
        SimpleHumanoidRllabEnv.__init__(self)

    def _get_obs(self):
        return np.concatenate([
            self.sim.data.qpos.flat,
            np.clip(self.sim.data.cfrc_ext, -1, 1).flat,
        ])        
