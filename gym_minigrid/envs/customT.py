from gym_minigrid.minigrid import *
from gym_minigrid.register import register
import itertools as itt
import numpy as np

class TEnv(MiniGridEnv):
    # Our environment
    def __init__(self,size=9, agent_pos=None):
        # Coordinates:
        # (column, row)
        #Agent start direction:
        # 0 -> right
        # 1 -> down
        # 2 -> left
        # 3 -> up
        self.agent_default_pos=agent_pos

        super().__init__(
            grid_size=size,
            max_steps=4*size*size,
            # white shadow over the board
            see_through_walls=True
        )
    # Set grid
    def _gen_grid(self, width, height):
        self.grid = Grid(width,height)
        # Margin walls
        self.grid.wall_rect(0,0,width,height)
        #============================================================
        # Set walls T env
        a=width//3
        b=height//3
        #vertical walls
        for i in (a-1,2*a):
            for j in range(2*b):
                self.put_obj(Wall(), i, j+1)
        #horizontal walls
        for i in range(1,a):
            self.put_obj(Wall(), i, 2*b)
        for i in range(2*a+1,height-1):
            self.put_obj(Wall(), i, 2*b)                    
        #============================================================
        # Objetives
        self.put_obj(HighGoal(),width-2, height-2)
        self.put_obj(LowGoal(),1, height-2)
        # Place the agent
        if self.agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent(top=(a,1),size=(a,2*b))

        self.mission = "T environment"

# Create the class, initiate
class TEnv9x9(TEnv):
    def __init__(self, **kwargs):
        super().__init__(size=9,**kwargs)
# This lines is for the flags ./manual_control.py --env NAME_OF_THE_ENVIRONMENT
# and for create the environment using env.create('NAME_OF_THE_ENVIRONMENT')
register(
    id='MiniGrid-T-9x9-v0',
    entry_point='gym_minigrid.envs:TEnv9x9'
)
# If you create a new class for a new environment in a new .py file inside envs directory
# you must include the name of the script in __init__.py (just check the file)
class TEnv12x12(TEnv):
    def __init__(self, **kwargs):
        super().__init__(size=12,**kwargs)
register(
    id='MiniGrid-T-12x12-v0',
    entry_point='gym_minigrid.envs:TEnv12x12'
)
class TEnv15x15(TEnv):
    def __init__(self, **kwargs):
        super().__init__(size=15,**kwargs)
register(
    id='MiniGrid-T-15x15-v0',
    entry_point='gym_minigrid.envs:TEnv15x15'
)
class TEnv18x18(TEnv):
    def __init__(self, **kwargs):
        super().__init__(size=18,**kwargs)
register(
    id='MiniGrid-T-18x18-v0',
    entry_point='gym_minigrid.envs:TEnv18x18'
)