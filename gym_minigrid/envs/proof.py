from gym_minigrid.minigrid import *
from gym_minigrid.register import register
import itertools as itt

class TEnv(MiniGridEnv):
    # Our environment
    def __init__(
        self,
        size=16,
        # 14x14 square (2 columns and 2 rows for walls) Counts for 0 to 15
        # Coordinates:
        # (column, row) from 1 to 14
        agent_start_pos=(8,1), # Position: top middle
        # 0 -> right
        # 1 -> down
        # 2 -> left
        # 3 -> up
        agent_start_dir=1, #Direction: The agent is looking down
    ):
        # initialization
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir

        super().__init__(
            grid_size=size,
            # ???
            max_steps=4*size*size,
            # white shadow over the board
            see_through_walls=False
        )
    # Set grid
    def _gen_grid(self, width, height):
        self.grid = Grid(width,height)
        # Margin walls
        self.grid.wall_rect(0,0,width,height)
        #============================================================
        # Set walls
        #vertical walls
        for i in (6,9):
            for j in (1,2,3,4,5,6,7,8,9,10,11,12):
                self.put_obj(Wall(), i, j)
        #horizontal walls
        for i in (1,2,3,4,5,6):
            self.put_obj(Wall(), i, 12)
        for i in (9,10,11,12,13,14):
            self.put_obj(Wall(), i, 12)                    
        #============================================================
        # Objetives
        self.put_obj(Goal(),width-2, height-2)
        self.put_obj(Goal(),1, 14)
        # Place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()

        self.mission = "Finish NMA project!!"

# Create the class, initiate
class TEnv16x16(TEnv):
    def __init__(self, **kwargs):
        super().__init__(size=16,**kwargs)
# This lines is for the flags ./manual_control.py --env NAME_OF_THE_ENVIRONMENT
# and for create the environment using env.create('NAME_OF_THE_ENVIRONMENT')
register(
    id='MiniGrid-T-16x16-v0',
    entry_point='gym_minigrid.envs:TEnv16x16'
)
# If you create a new class for a new environment in a new .py file inside envs directory
# you must include the name of the script in __init__.py (just check the file)
