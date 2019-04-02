import numpy as np
from gym import utils
from gym.envs.mujoco import mujocoimage_env

DEFAULT_SIZE = mujocoimage_env.DEFAULT_SIZE
rgb2grey = mujocoimage_env.rgb2grey


class SimpleHumanoidRllabImageEnv(mujocoimage_env.MujocoImageEnv, utils.EzPickle):
    def __init__(self, vel_deviation_cost_coeff=1e-2, alive_bonus=0.2, ctrl_cost_coeff=1e-3, impact_cost_coeff=1e-5,
        filename='simple_humanoid_rllab_image.xml'):
        self.framenumber = 2
        self.stackbuffer = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE, 3*self.framenumber]) # stack 4 frames as obs
        self.vel_deviation_cost_coeff = vel_deviation_cost_coeff
        self.alive_bonus = alive_bonus
        self.ctrl_cost_coeff = ctrl_cost_coeff
        self.impact_cost_coeff = impact_cost_coeff
        mujocoimage_env.MujocoImageEnv.__init__(self, filename, 5)
        utils.EzPickle.__init__(self)

    def get_current_obs(self):
        """image observations"""
        img = self.sim.render(width=DEFAULT_SIZE, height=DEFAULT_SIZE)
        img = np.float32(img)
        #img_grey = rgb2grey(img)
        img /= 255.0
        # put new frame into the buffer
        newstackbuffer = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE, 3*self.framenumber])
        for i in range(self.framenumber-1):
            newstackbuffer[:,:,3*i:3*(i+1)] = self.stackbuffer[:,:,3*(i+1):3*(i+2)]
        newstackbuffer[:,:,3*(self.framenumber-1):3*self.framenumber] = img
        self.stackbuffer = newstackbuffer.copy()
        return newstackbuffer[::4,::4,:]

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
        # clear buffer
        self.stackbuffer = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE, 3*self.framenumber]) # stack 4 frames as obs
        return self.get_current_obs()

    def viewer_setup(self):
        self.viewer.cam.distance = self.model.stat.extent * 0.5