import pyglet
from pyglet.gl import *

class Grid:
    def __init__(self ,rowsbycols,off_setX,off_setYtop,off_setYbottom,grid_length,cell_size):
        self.off_setX = off_setX
        self.off_setYtop = off_setYtop
        self.off_setYbottom = off_setYbottom
        self.rowsbycols = rowsbycols
        self.grid_length = grid_length
        self.cell_size = cell_size

    def draw(self):

        reached_rows_end = False
        # the change in rows is y 
        index_row = self.off_setYbottom
        while not reached_rows_end :
            vertices = [self.off_setX,index_row,self.grid_length+self.off_setX,index_row]
            color = [38, 58, 87 ,38, 58, 87]
            row =  pyglet.graphics.vertex_list( 2 , ('v2i/stream',vertices) , ('c3B',color) )
            glLineWidth(5);
            row.draw(pyglet.gl.GL_LINES)
            index_row += self.cell_size

            if index_row > self.grid_length+10:
                reached_rows_end = True
        ##############################################
        reached_cols_end = False
        # im colmuns the x changes and y is constant
        index_col = self.off_setX
        while not reached_cols_end :
            vertices = [index_col,self.off_setYbottom,index_col,self.grid_length+self.off_setYbottom]
            color = [38, 58, 87 ,38, 58, 87]
            row =  pyglet.graphics.vertex_list( 2 , ('v2i/stream',vertices) , ('c3B',color) )
            row.draw(pyglet.gl.GL_LINES)
            index_col += self.cell_size
    
            if index_col > self.grid_length+10:
                reached_cols_end = True
            
