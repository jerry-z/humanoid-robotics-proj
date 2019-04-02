"""
Classic cart-pole system implemented by Rich Sutton et al.
Copied from https://webdocs.cs.ualberta.ca/~sutton/book/code/pole.c
"""

import logging
import math
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np

logger = logging.getLogger(__name__)

class BallContEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second' : 50
    }

    def __init__(self):
        self.gra_dim = 4
        self.act_dim = 20
        self.direction = np.ones(self.act_dim)

        self.gra_set = self.gravity_set(self.act_dim)
        self.mass = 1.0
        self.tau = 0.02  # seconds between state updates
        self.gravity = None
        # Angle limit set to 2 * theta_threshold_radians so failing observation is still within bounds
        high = np.array([np.inf] * self.act_dim)
        action_limit = np.array([1.0] * self.act_dim)
        self.action_space = spaces.Box(-action_limit, action_limit)
        self.observation_space = spaces.Box(-high, high)

        self.seed()

    def gravity_set(self, act_dim):
        gravity = []
        gravity = [np.eye(act_dim),-np.eye(act_dim), np.eye(act_dim), -np.eye(act_dim), np.eye(act_dim)]
        gravity[2][:int(act_dim/2)][:int(act_dim/2)] *= -1
        gravity[3][:int(act_dim/2)][:int(act_dim/2)] *= -1
        return gravity

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        #assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))
        state = self.state
        x = state[:self.act_dim]
        x_dot = state[self.act_dim:]

        force = np.dot(self.gravity, action)
        xacc = force / self.mass
        x = x + self.tau * x_dot
        x_dot = x_dot + self.tau * xacc
        
        self.state = np.concatenate([x,x_dot])
        #print(x_dot, reward)
        reward = np.dot(self.direction, x_dot)
        done = False
        return x, reward, done, {}

    def reset(self):
        # state include position and velocity
        self.state = np.zeros(self.act_dim * 2)
        self.steps_beyond_done = None
        self.gravity = self.gra_set[np.random.randint(self.gra_dim)]
        return self.state[:self.act_dim]

    def render(self, mode='human', close=False):
        raise NotImplementedError
