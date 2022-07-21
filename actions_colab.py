#!/usr/bin/env python3

import time
import gym
import gym_minigrid
from colabgymrender.recorder import Recorder
from pyvirtualdisplay import Display

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
display = Display(visible=0, size=(400, 300))
display.start();
#load the environment and create the object
env = gym.make('MiniGrid-Empty-8x8-v0')
env = Recorder(env, './video', fps=60)
obs = env.reset()
#actions "random"
for i in range(0,100):
	print("step {}".format(i))
	#actions
	make_action(i)
	time.sleep(0.05)
env.release()
env.play()
#end
env.close()

"""
more environments:



more actions:
env.actions.toggle
env.actions.pickup
env.actions.drop
"""
