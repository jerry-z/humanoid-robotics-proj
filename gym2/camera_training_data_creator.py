import gym
import ipdb
import numpy as np
import pandas

#env = gym.make('HandReach-v0')
#env = gym.make('FetchPickAndPlace-v1')

env = gym.make('H_FetchReach-v1')
camera_data = []
camera_label = []

for i_episode in range(3000):
    observation = env.reset()
    print(i_episode)
    for t in range(10):
        #env.env.sim.render(100,100)
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        camera_image = env.env.sim.render(width=256,height=256,camera_name='main_camera_rgb')
        camera_label_pos = env.env.sim.model.site_pos[1,:]
        camera_data.append(camera_image)
        camera_label.append(camera_label_pos)

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

df = pandas.DataFrame(data={"col1": camera_label, "col2": camera_data})
df.to_csv("./camera_training_data.csv", sep=',',index=False)