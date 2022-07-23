# Step by step guide to create a custom environment inside gym_minigrid

1. Create a my_custom_environmet.py file inside **gym-minigrid/gym_minigrid/envs**
2. Check **proof.py** and **empty.py** to see and understand the easiest environments available
3. You need to create a class inside `my_custom_environment.py`
   ```python
   class MyEnv(MiniGridEnv):
    ...
   ```
   - The constructor method `__init__(self, size, agent_start_pos,agent_start_dir)` will create the mesh, put and set the agent.
   -  The method `_gen_grid(self, width, height)` will set the walls, obstacles and objetives on the grid.
4. Also is necessary create another class and a register:
   ```python
   class MyCustomEnv(MyEnv):
    def __init__(self, **kwargs):
        super().__init__(size,**kwargs)
   register(
    id='MiniGrid-my_custom_environment',
    entry_point='gym_minigrid.envs:MyCustomEnv'
    )
   ````
### Notes
1. You must specify the size of your grid in both classes
2. Please note id **always starts** with MiniGrid-
3. The entry point must match with the name of the second class

When you are finished, don't forget add your new module to `__init__.py` file located inside **gym-minigrid/gym_minigrid/envs**:
````python
from gym_minigrid.envs.my_custom_environment import *
````
### More notes
1. Keep simple the name of your classes and files. A single or maybe two words is enought
2. Modify proof.py could be easier than create a new hole script.

## Check the environment quickly
In your terminal:
````bash
$ cd <<path_to_gym-minigrid_repo>>
$ python
>>> import gym
>>> import gym_minigrid
>>> env=gym.make('id_of_your_environment')
>>> obs = env.reset()
>>> env.render()
>>> env.close()
````
An .py example [here](https://github.com/EnriqueGap/gym-minigrid/blob/nmaproject/actions.py)

Now you are ready!. You can create scripts or jupyternotebooks inside gym-minigrid repo and load your environments!!
