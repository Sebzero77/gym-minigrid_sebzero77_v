from gym_minigrid.minigrid import *
from gym_minigrid.register import register
import itertools as itt
import numpy as np

class SharpEnv(MiniGridEnv):
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
        # Set walls  in + + env
        #               + +
        a=width//3
        b=height//3
        # vertical walls
        for i in (a-1,2*a):
            for j in range(1,b-1):
                self.put_obj(Wall(), i, j)
        for i in (a-1,2*a):
            for j in range(2*b,width-1):
                self.put_obj(Wall(), i, j+1)                
        #horizontal walls
        for i in range(1,a):
            self.put_obj(Wall(), i, 2*b)
            self.put_obj(Wall(), i, b-1)
        for i in range(2*a,height-1):
            self.put_obj(Wall(), i, 2*b)
            self.put_obj(Wall(), i, b-1)
        #============================================================
        # Objetives
        self.put_obj(HighGoal(),width//2, 1) #superior medio
        self.put_obj(LowGoal(),width//2, height-2) # inferior medio
        self.put_obj(MidGoal(),1, height//2) #medio izquierda
        self.put_obj(MidGoal(),width-2, height//2) #medio derecha
        # Place the agent
        if self.agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent(top=(a,b),size=(a,b))

        self.mission = "Sharp environment"

# Create the class, initiate
class SharpEnv9x9(SharpEnv):
    def __init__(self, **kwargs):
        super().__init__(size=9,**kwargs)
register(
    id='MiniGrid-Sharp-9x9-v0',
    entry_point='gym_minigrid.envs:SharpEnv9x9'
)
class SharpEnv12x12(SharpEnv):
    def __init__(self, **kwargs):
        super().__init__(size=12,**kwargs)
register(
    id='MiniGrid-Sharp-12x12-v0',
    entry_point='gym_minigrid.envs:SharpEnv12x12'
)
class SharpEnv15x15(SharpEnv):
    def __init__(self, **kwargs):
        super().__init__(size=15,**kwargs)
register(
    id='MiniGrid-Sharp-15x15-v0',
    entry_point='gym_minigrid.envs:SharpEnv15x15'
)
class SharpEnv18x18(SharpEnv):
    def __init__(self, **kwargs):
        super().__init__(size=18,**kwargs)
register(
    id='MiniGrid-Sharp-18x18-v0',
    entry_point='gym_minigrid.envs:SharpEnv18x18'
)
class SharpEnv27x27(SharpEnv):
    def __init__(self, **kwargs):
        super().__init__(size=27,**kwargs)
register(
    id='MiniGrid-Sharp-27x27-v0',
    entry_point='gym_minigrid.envs:SharpEnv27x27'
)
