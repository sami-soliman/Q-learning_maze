window_length = 600
frame_rate = 30/60.0


#####  Grid ##########
rowsbycols = 5

off_setX = 10
off_setYtop = 50
off_setYbottom = 10

window_width = window_length + (2*off_setX)
window_height = window_length + off_setYtop + off_setYbottom

grid_length = window_length
cell_size = int( grid_length / rowsbycols)

####################
player_initial_state = 0
#player_initial_row = 5
#player_initial_column = 1

score_initial_value = 0

####################
#row , column
state_space = [
    (5,1),(5,2),(5,3),(5,4),(5,5),
    (4,1),(4,2),(4,3),(4,4),(4,5),
    (3,1),(3,2),(3,3),(3,4),(3,5),
    (2,1),(2,2),(2,3),(2,4),(2,5),
    (1,1),(1,2),(1,3),(1,4),(1,5),
    ] 

#up , right , down,left
action_space = [0,1,2,3]

# state : (nextstate,reward,done)
reward_table = [
    # 0
    {0:(0,-1,False),
     1:(1,-1,False),
     2:(5,-1,False),
     3:(0,-1,False)},
    # 1
    {0:(1,-1,False),
     1:(2,-1,False),
     2:(6,-100,True),
     3:(0,-1,False)},
    # 2
    {0:(2,-1,False),
     1:(3,-1,False),
     2:(7,-1,False),
     3:(1,-1,False)},
    # 3
    {0:(3,-1,False),
     1:(4,-1,False),
     2:(8,-100,True),
     3:(2,-1,False)},
    # 4
    {0:(4,-1,False),
     1:(4,-1,False),
     2:(9,-1,False),
     3:(3,-1,False)},
    # 5
    {0:(0,-1,False),
     1:(6,-100,True),
     2:(10,-1,False),
     3:(5,-1,False)},
    # 6
    {0:(1,-1,False),
     1:(7,-1,False),
     2:(11,-1,False),
     3:(5,-1,False)},
    # 7
    {0:(2,-1,False),
     1:(8,-100,True),
     2:(12,-1,False),
     3:(6,-100,True)},
    # 8
    {0:(3,-1,False),
     1:(9,-1,False),
     2:(13,-1,False),
     3:(7,-1,False)},
    # 9
    {0:(4,-1,False),
     1:(9,-1,False),
     2:(14,-1,False),
     3:(8,-100,True)},
    # 10
    {0:(5,-1,False),
     1:(11,-1,False),
     2:(15,-1,False),
     3:(10,-1,False)},
    # 11
    {0:(6,-100,True),
     1:(12,-1,False),
     2:(16,-100,True),
     3:(10,-1,False)},
    # 12
    {0:(7,-1,False),
     1:(13,-1,False),
     2:(17,-1,False),
     3:(11,-1,False)},
    # 13
    {0:(8,-100,True),
     1:(14,-1,False),
     2:(18,-100,True),
     3:(12,-1,False)},
    # 14
    {0:(9,-1,False),
     1:(14,-1,False),
     2:(19,-1,False),
     3:(13,-1,False)},
    # 15
    {0:(10,-1,False),
     1:(16,-100,True),
     2:[20,30,False],
     3:(15,-1,False)},
    # 16
    {0:(11,-1,False),
     1:(17,-1,False),
     2:(21,-1,False),
     3:(15,-1,False)},
    # 17
    {0:(12,-1,False),
     1:(18,-100,True),
     2:(22,-1,False),
     3:(16,-100,True)},
    # 18
    {0:(13,-1,False),
     1:(19,-1,False),
     2:(23,-1,False),
     3:(17,-1,False)},
    # 19
    {0:(14,-1,False),
     1:(19,-1,False),
     2:(24,100,True),
     3:(18,-100,True)},
    # 20
    {0:(15,-1,False),
     1:(21,-1,False),
     2:(20,-1,False),
     3:(20,-1,False)},
    # 21
    {0:(16,-100,True),
     1:(22,-1,False),
     2:(21,-1,False),
     3:[20,30,False]},
    # 22
    {0:(17,-1,False),
     1:(23,-1,False),
     2:(22,-1,False),
     3:(21,-1,False)},
    # 23
    {0:(18,-100,True),
     1:(24,100,True),
     2:(23,-1,False),
     3:(22,-1,False)},
    # 24
    {0:(19,-1,False),
     1:(24,100,True),
     2:(24,100,True),
     3:(23,-1,False)},    
]

# get next state , reward , end env or not
def get_observation(current_state,action):
    observation = (reward_table[current_state])[action]
    return observation 