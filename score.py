import pyglet
import properties


class Score:
    def __init__(self,initial_value,X,text):
        
        # player score
        self.scoreX = X
        self.text = text
        self.scoreY = properties.off_setYbottom + properties.grid_length + 15
        self.score = initial_value
        self.score_text = pyglet.text.Label(self.text + ':' + str(self.score),
        font_name='Times New Roman',font_size=20, color=(0,0,0,255),bold=True,
        x=self.scoreX, y=self.scoreY)


    def update(self,reward):

        self.score += reward
        self.score_text.text = self.text + ':' + str(self.score)

    def reset(self):
        self.score = properties.score_initial_value
        self.score_text.text = self.text + ':' + str(self.score)

    def draw(self):
        self.score_text.draw()
