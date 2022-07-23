#!/usr/bin/env python3

import time
import gym
import gym_minigrid

#### step function
def step(action):
    obs, reward, done, info = env.step(action)
    print('step=%s, reward=%.2f' % (env.step_count, reward))

    if done:
        print('done!')
        env.reset()
#### action function
def make_action(i):
	if i%3==0:
		step(env.actions.left)
		return
	if i%3==1:
		step(env.actions.right)
		return
	if i%3==2:
		step(env.actions.forward)
		return

#load the environment and create the object
env = gym.make('MiniGrid-T-16x16-v0')
obs = env.reset()
#actions "random"
for i in range(0,100):
	print("step {}".format(i))
	#actions
	make_action(i)
	env.render()
	time.sleep(0.05)

#end
env.close()

"""
more environments:



more actions:
env.actions.toggle
env.actions.pickup
env.actions.drop
"""
