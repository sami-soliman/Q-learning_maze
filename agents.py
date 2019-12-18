import pyglet
from pyglet.gl import *
import properties
from score import Score

class Player:
    def __init__(self,cellsize,off_setX,off_setYtop,off_setYbottom,rowsbycols,initial_state):
        self.cellsize = cellsize
        self.off_setX = off_setX
        self.off_setYtop = off_setYtop
        self.off_setYbottom = off_setYbottom
        self.rowsbycols = rowsbycols
        self.cell_off_set = 10

        self.player_img = pyglet.image.load('images/player.png')
        self.player = self.player_img.get_texture()
        
        # (row , column) tuple
        self.state = initial_state
        self.state_location=properties.state_space[self.state]

        self.playerXcordinate = (self.off_setX+self.cell_off_set/2) + (self.cellsize*((self.state_location[1])-1))
        self.playerYcordinate = (self.off_setYbottom+self.cell_off_set/2) + (self.cellsize*((self.state_location[0])-1))

        # length for both width and height
        self.player_length = self.cellsize-self.cell_off_set


    def draw(self):
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        self.player.blit(self.playerXcordinate,self.playerYcordinate,0,width=self.player_length, height=self.player_length)


    def update_player(self,next_state):
        self.state = next_state
        self.state_location=properties.state_space[self.state]

        self.playerXcordinate = (self.off_setX+self.cell_off_set/2) + (self.cellsize*((self.state_location[1])-1))
        self.playerYcordinate = (self.off_setYbottom+self.cell_off_set/2) + (self.cellsize*((self.state_location[0])-1))

    def update(self,next_state):
        self.update_player(next_state)



class Enemy:
    def __init__(self,cellsize,off_setX,off_setYtop,off_setYbottom,rowsbycols,row,column):
        self.cellsize = cellsize
        self.off_setX = off_setX
        self.off_setYtop = off_setYtop
        self.off_setYbottom = off_setYbottom
        self.rowsbycols = rowsbycols
        self.cell_off_set = 10

        self.enemy_img = pyglet.image.load('images/enemy.png')
        self.enemy = self.enemy_img.get_texture()
        
        # columns for left to right
        # rows from bottom to top
        self.column = column
        self.row = row
        self.enemyXcordinate = (self.off_setX+self.cell_off_set/2) + (self.cellsize*(self.column-1))
        self.enemyYcordinate = (self.off_setYbottom+self.cell_off_set/2) + (self.cellsize*(self.row-1))

        # length for both width and height
        self.enemy_length = self.cellsize-self.cell_off_set

    def draw(self):
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        self.enemy.blit(self.enemyXcordinate,self.enemyYcordinate,0,width=self.enemy_length, height=self.enemy_length)


class Treasure:
    def __init__(self,cellsize,off_setX,off_setYtop,off_setYbottom,rowsbycols,row,column,treasure_img):
        self.cellsize = cellsize
        self.off_setX = off_setX
        self.off_setYtop = off_setYtop
        self.off_setYbottom = off_setYbottom
        self.rowsbycols = rowsbycols
        self.cell_off_set = 10

        self.treasure_img = pyglet.image.load(treasure_img)
        self.treasure = self.treasure_img.get_texture()
        
        # columns for left to right
        # rows from bottom to top
        self.column = column
        self.row = row
        self.treasureXcordinate = (self.off_setX+self.cell_off_set/2) + (self.cellsize*(self.column-1))
        self.treasureYcordinate = (self.off_setYbottom+self.cell_off_set/2) + (self.cellsize*(self.row-1))

        # length for both width and height
        self.treasure_length = self.cellsize-self.cell_off_set

    def draw(self):
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        self.treasure.blit(self.treasureXcordinate,self.treasureYcordinate,0,width=self.treasure_length, height=self.treasure_length)
