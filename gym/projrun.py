import gym
#import ipdb
env = gym.make('FetchPickAndPlace-v1')
#env = gym.make('SeaHandGraspCube-v0')


for i_episode in range(20):
    observation = env.reset()
   # ipdb.set_trace() 
    for t in range(3000):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break


