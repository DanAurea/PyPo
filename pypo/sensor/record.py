from OpenGL.GL import *

class Record(object):

    def __init__(self):
        self.frame         = []
        self.current_frame = 0
        self.vbo           = glGenBuffers(1)
        self.ibo           = None

    def add_frame(self, frame):
        self.frame.append(frame)
        
    def previous_frame(self):
        if self.current_frame > 0:
            self.current_frame -= 1

    def next_frame(self):
        if self.current_frame < len(self.frame) - 1:
            self.current_frame +=1