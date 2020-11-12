from OpenGL.GL import *

from gui.widget.scene.scene_view import SceneView
from scene.camera.camera_2d import Camera2D

class Scene2D(SceneView):

    def __init__(self, parent = None):
        super(Scene2D, self).__init__(parent = parent)

        self.camera = Camera2D()

    def initializeGL(self):
        """
        Initializes GL widget with default state
        """
        glClearColor(0.07, 0.07, 0.1, 1.0)
        
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        # glEnable(GL_SMOOTH_POINT)
        # glEnable(GL_POINT_SPRITE)
        glEnable(GL_PROGRAM_POINT_SIZE)

    def paintGL(self):
        """
        Paint scene
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)