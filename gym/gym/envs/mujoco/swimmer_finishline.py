import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env

class SwimmerFinishLineEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    """
    swimmer gets reward for running fast in the first dimension
    running forward allows the agent to get a bonus reward after crossing
    a finishing line
    """
    def __init__(self):
        mujoco_env.MujocoEnv.__init__(self, 'swimmer_finishline.xml', 4)
        utils.EzPickle.__init__(self)

    def step(self, a):
        ctrl_cost_coeff = 0.0001
        xposbefore = self.sim.data.qpos[0]
        self.do_simulation(a, self.frame_skip)
        xposafter = self.sim.data.qpos[0]
        reward_fwd = (xposafter - xposbefore) / self.dt
        if xposafter > 0.0:
            reward_move = reward_fwd
        else:
            reward_move = -reward_fwd #backward
        reward_ctrl = - ctrl_cost_coeff * np.square(a).sum()
        reward = reward_fwd + reward_ctrl
        ob = self._get_obs()
        return ob, reward, False, dict(reward_fwd=reward_fwd, reward_ctrl=reward_ctrl)
         
        """
        xposbefore = self.get_body_com("torso")[0]
        self.do_simulation(a, self.frame_skip)
        xposafter = self.get_body_com("torso")[0]

        xvelocity = (xposafter - xposbefore)/self.dt
        reward = abs(xvelocity) #xvelocity ** 2
        #reward = -(xposafter)
        xpos = self.sim.data.qpos[0]
        #if xpos < -1.:
        #    reward += 10.0
        ob = self._get_obs()
        return ob, reward, False, {'pos': self.sim.data.qpos[0]}
        """
    def _get_obs(self):
        qpos = self.sim.data.qpos
        qvel = self.sim.data.qvel
        return np.concatenate([qpos.flat, qvel.flat])

    def reset_model(self):
        self.init_qpos[0] = 0.0
        self.init_qvel[0] = 0.0
        self.set_state(
            self.init_qpos + self.np_random.uniform(low=-.1, high=.1, size=self.model.nq),
            self.init_qvel + self.np_random.uniform(low=-.1, high=.1, size=self.model.nv)
        )
        return self._get_obs()
