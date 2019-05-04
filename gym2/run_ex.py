import gym
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from PIL import Image

#
# env = gym.make('H_FetchReach-v1')
# env = gym.make('H_FetchPush-v1')
#env = gym.make('H_FetchPickAndPlace-v1')

env = gym.make('H_FetchReachObs-v1')
#env = gym.make('H_FetchPushObs-v1')
#env = gym.make('H_FetchPickAndPlaceObs-v1')

fig = plt.figure(figsize=(12,7))
fig.subplots_adjust(hspace=0.4, wspace=0.3)
asdf = fig.add_subplot(1,2,1)
asdf2 = fig.add_subplot(1,2,2)


for i_episode in range(20):
    observation = env.reset()
    for t in range(3000):
        env.render()

        # camera_pixels= env.env.main_cam.render(256,256,4)
        # camera = env.env.main_cam.read_pixels(256,256, depth=False)
        # img = Image.fromarray(camera,'RGB')
        # imgplot = plt.subplot(121).imshow(img)

        # camera_pixels2= env.env.main_cam2.render(256,256,5)
        # camera2 = env.env.main_cam2.read_pixels(256,256, depth=False)
        # img2 = Image.fromarray(camera2,'RGB')
        # imgplot2 = plt.subplot(122).imshow(img2)



        # plt.pause(0.001)

        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
