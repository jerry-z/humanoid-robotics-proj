import gym
#import ipdb
#env = gym.make('HandReach-v0')
#env = gym.make('FetchPickAndPlace-v1')
env = gym.make('H_FetchReach-v1')
import ipdb
#env = gym.make('SeaHandGraspCube-v0')
#ipdb.set_trace()
#TEST
for i_episode in range(20):
    observation = env.reset()
   # ipdb.set_trace() 

    for t in range(3000):
        #env.env.sim.render(100,100)
        env.render()
        #env.render(mode='human')
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break


