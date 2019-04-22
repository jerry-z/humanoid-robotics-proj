import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
from gym.envs.mujoco.ant import AntPOMDPEnv

class AntFourMassesEnv(AntPOMDPEnv):
    def __init__(self):
        AntPOMDPEnv.__init__(self)
        self.leglist = ['front_right_leg','front_left_leg','back_leg','right_back_leg']

    def reset_model(self):
        # reset the mass to be the original mass
        for idx in [2,5,8,11]:
            self.sim.model.body_mass[idx] = 0.03647693
        # reset the mass randomly (legs)
        idx = np.random.randint(0,4,size=1)[0]
        legname = self.leglist[idx]
        legidx = self.sim.model.body_name2id(legname)
        self.sim.model.body_mass[legidx] = 0.03647693 / 10.0 
        # reset everything else
        qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-.1, high=.1)
        qvel = self.init_qvel + self.np_random.randn(self.model.nv) * .1
        self.set_state(qpos, qvel)
        return self._get_obs()
