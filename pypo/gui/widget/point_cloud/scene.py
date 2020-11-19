from OpenGL.GL import *
from PySide2.QtGui import QKeyEvent
from PySide2.QtCore import Qt, QEvent
from PySide2.QtWidgets import QOpenGLWidget

from scene.camera.camera import Camera2D, Camera3D
from scene.camera.camera_3d.fly_camera import FlyCamera
from scene.camera.camera_3d.fps_camera import FPSCamera

class Scene(QOpenGLWidget):

    def __init__(self, parent = None):
        super(Scene, self).__init__(parent = parent)
        
        self._cameras         = []
        self._control_binding = {}
        self._key_pressed     = set()

        self._framerate   = 60
        self._invalid     = True
        self._auto_update = True

        self.setFocusPolicy(Qt.StrongFocus)

    @property
    def auto_update(self):
        return self._auto_update

    @auto_update.setter
    def auto_update(self, state):
        self._auto_update = state

    def add_object(self):
        pass

    def render(self):
        pass

    def initializeGL(self):
        glClearColor(0.04, 0.04, 0.06, 1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        # glEnable(GL_SMOOTH_POINT)
        # glEnable(GL_POINT_SPRITE)
        glEnable(GL_PROGRAM_POINT_SIZE)

    def keyPressEvent(self, event):
        if not event.isAutoRepeat():
            self._key_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        if not event.isAutoRepeat():
            self._key_pressed.remove(event.key())
        
        # TODO : Retrigger key press event so release event won't interfer with keys still hold
        # if self._key_pressed:
        #     self.keyPressEvent(QKeyEvent(QEvent.KeyPress, self._key_pressed.pop(), Qt.NoModifier, autorep = True ))

    def _invalidate(self):
        self._invalid = True

"""
Scene 2D
"""
class Scene2D(Scene):

    def __init__(self, parent = None):
        super(Scene2D, self).__init__(parent = parent)

        self._cameras.append(Camera2D())
        
        self._current_camera = self._cameras[0]

        self._bind_controls()

    def _bind_controls(self):
        """
        Bind input controls to callback function
        """
        self._control_binding[Qt.Key_Z] = self._current_camera.move_forward
        self._control_binding[Qt.Key_S] = self._current_camera.move_backward
        self._control_binding[Qt.Key_Q] = self._current_camera.move_left
        self._control_binding[Qt.Key_D] = self._current_camera.move_right

    def keyPressEvent(self, event):
        super(Scene2D, self).keyPressEvent(event)
        for key in self._key_pressed:
            if key in self._control_binding:
                self._control_binding[key]()

        self._invalidate()

    def initializeGL(self):
        """
        Initializes GL widget with default state
        """
        super(Scene2D, self).initializeGL()

    def paintGL(self):
        """
        Paint scene
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

"""
Scene 3D
"""
class Scene3D(Scene):

    def __init__(self, parent = None):
        super(Scene3D, self).__init__(parent = parent)

        self._cameras.append(FlyCamera())
        self._current_camera = self._cameras[0]

        self._bind_controls()

    def _bind_controls(self):
        """
        Bind input controls to callback function
        """
        self._control_binding[Qt.Key_Z] = self._current_camera.move_forward
        self._control_binding[Qt.Key_S] = self._current_camera.move_backward
        self._control_binding[Qt.Key_Q] = self._current_camera.move_left
        self._control_binding[Qt.Key_D] = self._current_camera.move_right

    def keyPressEvent(self, event):
        super(Scene3D, self).keyPressEvent(event)
        for key in self._key_pressed:
            if key in self._control_binding:
                self._control_binding[key]()

    def mousePressEvent(self, event):
        pass
    
    def mouseReleaseEvent(self, event):
        pass

    def wheelEvent(self, event):
        pass

    def initializeGL(self):
        """
        Initializes GL widget with default state
        """
        super(Scene3D, self).initializeGL()

    def paintGL(self):
        """
        Paint scene
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)