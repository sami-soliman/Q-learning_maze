import pyglet
from pyglet.gl import *
from pyglet.window import key
from grid import Grid
from agents import Player ,Enemy ,Treasure
from score import Score
import properties
import random
from random import choice
import numpy as np

class MyWindow(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # background color red green blue alpha
        glClearColor(1,1,1,0)

        # creating the grid
        self.grid = Grid(5,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.grid_length,properties.cell_size)

        # creating the player 
        self.player = Player(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,properties.player_initial_state)

        #creating the score 
        self.score = Score(properties.score_initial_value,properties.off_setX,"Score")

        #creating the score 
        self.episode = Score(properties.score_initial_value,properties.off_setX+properties.window_width/2,"Episode")

        # adding 4 enemies
        self.enemy_list = []
        self.enemy_list.append( Enemy(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,2,2) )
        self.enemy_list.append( Enemy(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,4,2) )
        self.enemy_list.append( Enemy(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,2,4) )
        self.enemy_list.append( Enemy(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,4,4) )


        # adding treasure
        self.treasure = Treasure(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,1,5,'images/treasure.png')

        # adding small treasure
        self.small_treasure = Treasure(properties.cell_size,properties.off_setX,properties.off_setYtop,
        properties.off_setYbottom,properties.rowsbycols,1,1,'images/coins.png')

        self.end = False
        self.taked_small_treasure = False
        self.q_table = np.zeros([25, 4])
        
        # Hyperparameters
        self.alpha = 0.7
        self.gamma = 0.6
        self.epsilon = 1
        self.min_epsilon = 0.01
        self.max_epsilon = 1.0
        self.decay_rate = 0.01


    def take_action(self,action):
        observation = properties.get_observation(self.player.state,action)
        next_state = observation[0]
        reward = observation[1]
        done = observation[2]

        self.player.update(next_state)
        self.score.update(reward)
        self.end = done
        if self.player.state == 20:
            ((properties.reward_table[15])[2])[1] = -1
            ((properties.reward_table[21])[3])[1] = -1
            self.taked_small_treasure = True
        self.on_draw()

        return observation

    def draw(self):
        self.grid.draw()
        self.player.draw()
        self.score.draw()
        self.episode.draw()
        for enemy in self.enemy_list:
            enemy.draw()
        self.treasure.draw()
        if not self.taked_small_treasure:
            self.small_treasure.draw()
    

    def game_start(self):
        pyglet.app.run()
    
    def game_restart(self):
        print("score:" + str(self.score.score))
        self.episode.update(1)
        if self.episode.score > 10000:
            self.game_over()

        self.epsilon = self.min_epsilon + (self.max_epsilon -self.min_epsilon)*np.exp(-self.decay_rate*self.episode.score)
        initial_state_space = [ 0,1,2,3,4,
                                5,7,9,
                                10,11,12,13,14,
                                15,17,19,
                                21,22,23]
        self.player.update(choice(initial_state_space))
        self.score.reset()
        self.end == False

        ((properties.reward_table[15])[2])[1] = 30
        ((properties.reward_table[21])[3])[1] = 30
        self.taked_small_treasure = False


    def game_over(self):
        pyglet.app.exit()

    
    def on_draw(self):
        self.clear()
        self.draw()


    def start_Qlearning(self,dt):
        state = self.player.state

        if random.uniform(0, 1) > self.epsilon:
            action = np.argmax(self.q_table[state]) # Exploit learned values

        else:
            action = random.randint(0,3) # Explore action space

        observation = self.take_action(action)
        next_state = observation[0]
        reward = observation[1]
        
        old_value = self.q_table[state, action]
        next_max = np.max(self.q_table[next_state])
        
        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)
        self.q_table[state, action] = new_value

        if self.end == True:
            self.game_restart()

    def exploiting(self,dt):
        state = self.player.state

        action = np.argmax(self.q_table[state]) # Exploit learned values


        observation = self.take_action(action)
        next_state = observation[0]
        reward = observation[1]
    

        if self.end == True:
            self.game_restart()

    


if __name__=="__main__":
    window = MyWindow(properties.window_width,properties.window_height,"one peace",resizable = False)
    window.set_location(300, 50)
    
    # enable when exploiting
    pyglet.clock.schedule_interval(window.exploiting ,properties.frame_rate)
    window.q_table = np.loadtxt('qtable1.txt')

    # enable when learning
    ''' 
    pyglet.clock.schedule_interval(window.start_Qlearning ,1/60.0)
    '''
    window.game_start()

    # enable when learning
    #np.savetxt('qtable.txt', window.q_table)
