from OpenGL.GL import *
from PySide2.QtWidgets import QOpenGLWidget

class SceneView(QOpenGLWidget):

    def __init__(self, parent = None):
        super(SceneView, self).__init__(parent = parent)