import numpy as np
from gym import utils
from gym.envs.mujoco import mujocoimage_env

DEFAULT_SIZE = mujocoimage_env.DEFAULT_SIZE
rgb2grey = mujocoimage_env.rgb2grey


class ReacherImageEnv(mujocoimage_env.MujocoImageEnv, utils.EzPickle):
    def __init__(self):
        self.framenumber = 2
        self.stackbuffer = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE, 3*self.framenumber]) # stack 4 frames as obs
        utils.EzPickle.__init__(self)
        mujocoimage_env.MujocoImageEnv.__init__(self, 'reacher.xml', 2)

    def step(self, a):
        vec = self.get_body_com("fingertip")-self.get_body_com("target")
        reward_dist = - np.linalg.norm(vec)
        reward_ctrl = - np.square(a).sum()
        reward = reward_dist + reward_ctrl
        self.do_simulation(a, self.frame_skip)
        ob = self._get_obs()
        done = False
        return ob, reward, done, dict(reward_dist=reward_dist, reward_ctrl=reward_ctrl)

    def viewer_setup(self):
        self.viewer.cam.trackbodyid = 0

    def reset_model(self):
        qpos = self.np_random.uniform(low=-0.1, high=0.1, size=self.model.nq) + self.init_qpos
        while True:
            self.goal = self.np_random.uniform(low=-.2, high=.2, size=2)
            if np.linalg.norm(self.goal) < 2:
                break
        qpos[-2:] = self.goal
        qvel = self.init_qvel + self.np_random.uniform(low=-.005, high=.005, size=self.model.nv)
        qvel[-2:] = 0
        self.set_state(qpos, qvel)
        # clear buffer
        self.stackbuffer = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE, 3*self.framenumber]) # stack 4 frames as obs
        return self._get_obs()

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
