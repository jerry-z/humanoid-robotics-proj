import gym
import ipdb
import numpy as np
import pandas

#env = gym.make('HandReach-v0')
#env = gym.make('FetchPickAndPlace-v1')

env = gym.make('H_FetchReach-v1')
#camera_data = []
#camera_label = []

camera_label = np.array([0,0,0])
camera_data = np.zeros((1,49152))

for i_episode in range(2000):
    observation = env.reset()
    print(i_episode)
    for t in range(10):
        #env.env.sim.render(100,100)
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        camera_image = env.env.sim.render(width=128,height=128,camera_name='main_camera_rgb')
        camera_image = camera_image.flatten()
        ipdb.set_trace
        camera_label_pos = env.env.sim.model.site_pos[1,:][0]
        camera_label_pos1= env.env.sim.model.site_pos[1,:][1]
        camera_label_pos2= env.env.sim.model.site_pos[1,:][2]
        new = np.array(([camera_label_pos, camera_label_pos1, camera_label_pos2]))
        camera_label = np.vstack((camera_label.copy(), new.copy()))
        camera_data = np.vstack((camera_data, camera_image.copy()))
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

camera_data = np.delete(camera_data,(0), axis = 0) 
camera_label = np.delete(camera_label,(0), axis = 0) 

np.savetxt('camera_data.csv', camera_data, delimiter=',')
np.savetxt('camera_label.csv', camera_label, delimiter=',')