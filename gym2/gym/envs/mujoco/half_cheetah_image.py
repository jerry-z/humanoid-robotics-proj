import numpy as np
from gym import utils
from gym.envs.mujoco import mujocoimage_env

DEFAULT_SIZE = mujocoimage_env.DEFAULT_SIZE
rgb2grey = mujocoimage_env.rgb2grey

class HalfCheetahImageEnv(mujocoimage_env.MujocoImageEnv, utils.EzPickle):
    def __init__(self):
        self.framenumber = 2
        self.stackbuffer = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE, 3*self.framenumber]) # stack 4 frames as obs
        mujocoimage_env.MujocoImageEnv.__init__(self, 'half_cheetah.xml', 5)
        utils.EzPickle.__init__(self)

    def step(self, action):
        xposbefore = self.sim.data.qpos[0]
        self.do_simulation(action, self.frame_skip)
        xposafter = self.sim.data.qpos[0]
        ob = self._get_obs()
        reward_ctrl = - 0.1 * np.square(action).sum()
        reward_run = (xposafter - xposbefore)/self.dt
        reward = reward_ctrl + reward_run
        done = False
        return ob, reward, done, dict(reward_run=reward_run, reward_ctrl=reward_ctrl)

    def _get_obs(self):
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

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(low=-.1, high=.1, size=self.model.nq)
        qvel = self.init_qvel + self.np_random.randn(self.model.nv) * .1
        # clear buffer
        self.stackbuffer = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE, 3*self.framenumber]) # stack 4 frames as obs
        return self._get_obs()

    def viewer_setup(self):
        self.viewer.cam.distance = self.model.stat.extent * 0.5
