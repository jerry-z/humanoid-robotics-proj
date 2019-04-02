import numpy as np
from gym import utils
from gym.envs.mujoco import mujocoimage_env

DEFAULT_SIZE = mujocoimage_env.DEFAULT_SIZE
rgb2grey = mujocoimage_env.rgb2grey


class AntTargetImageEnv(mujocoimage_env.MujocoImageEnv, utils.EzPickle):
    def __init__(self):
        self.framenumber = 2
        self.stackbuffer = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE, 3*self.framenumber]) # stack 4 frames as obs
        mujocoimage_env.MujocoImageEnv.__init__(self, 'anttarget.xml', 5)
        utils.EzPickle.__init__(self)

    def step(self, a):
        #xposbefore = self.get_body_com("torso")[0]
        self.do_simulation(a, self.frame_skip)
        #xposafter = self.get_body_com("torso")[0]
        #forward_reward = (xposafter - xposbefore)/self.dt
        xpos = self.get_body_com("torso")[:2]
        xpostarget = np.array([2.0, 0.0])
        #distance_reward = np.exp(-np.linalg.norm(xpos - xpostarget))
        distance_reward = -np.linalg.norm(xpos - xpostarget)
        ctrl_cost = .5 * np.square(a).sum()
        contact_cost = 0.5 * 1e-3 * np.sum(
            np.square(np.clip(self.sim.data.cfrc_ext, -1, 1)))
        survive_reward = 1.0
        #reward = distance_reward - ctrl_cost - contact_cost + survive_reward
        reward = distance_reward
        state = self.state_vector()
        notdone = np.isfinite(state).all() \
            and state[2] >= 0.2 and state[2] <= 1.0
        #done = not notdone
        done = False
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
        qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-.1, high=.1)
        qvel = self.init_qvel + self.np_random.randn(self.model.nv) * .1
        self.set_state(qpos, qvel)
        # clear buffer
        self.stackbuffer = np.zeros([DEFAULT_SIZE, DEFAULT_SIZE, 3*self.framenumber]) # stack 4 frames as obs
        return self._get_obs()

    def viewer_setup(self):
        #pass
        self.viewer.cam.distance = self.model.stat.extent * 0.5
