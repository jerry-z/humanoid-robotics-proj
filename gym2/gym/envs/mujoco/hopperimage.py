import numpy as np
from gym import utils
from gym.envs.mujoco import mujocoimage_env

DEFAULT_SIZE = mujocoimage_env.DEFAULT_SIZE
rgb2grey = mujocoimage_env.rgb2grey


class HopperImageEnv(mujocoimage_env.MujocoImageEnv, utils.EzPickle):
    def __init__(self):
        self.framenumber = 2
        self.stackbuffer = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE, 3*self.framenumber]) # stack 4 frames as obs
        mujocoimage_env.MujocoImageEnv.__init__(self, 'hopper.xml', 4)
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
        qpos = self.init_qpos + self.np_random.uniform(low=-.005, high=.005, size=self.model.nq)
        qvel = self.init_qvel + self.np_random.uniform(low=-.005, high=.005, size=self.model.nv)
        self.set_state(qpos, qvel)
        # clear buffer
        self.stackbuffer = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE, 3*self.framenumber]) # stack 4 frames as obs
        return self._get_obs()

    def viewer_setup(self):
        self.viewer.cam.trackbodyid = 2
        self.viewer.cam.distance = self.model.stat.extent * 0.75
        self.viewer.cam.lookat[2] += .8
        self.viewer.cam.elevation = -20
