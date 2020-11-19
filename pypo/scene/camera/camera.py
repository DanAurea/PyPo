from pyrr import Matrix44, Quaternion, Vector3, Vector4, vector

class Camera(object):
    def __init__(self, pos = Vector3([0.0, 1.0, 0.0]), orientation = Vector4([1.0, 0.0, 0.0, 0.0])):
        self._invalid     = True
        self._auto_update = True

        self._aspect = 16.0 / 9.0
        self._near   = 0.1
        self._far    = 1000
        
        self._fov          = 90
        self._pos          = pos
        self._orientation  = orientation

    @property
    def auto_update(self):
        return self._auto_update

    @auto_update.setter
    def auto_update(self, state):
        self._auto_update = state

    def move_forward(self):
        self._invalidate()

    def move_backward(self):
        self._invalidate()

    def move_left(self):
        self._invalidate()

    def move_right(self):
        self._invalidate()

    def update(self):
        """
        Update camera parameters
        """

        if self._invalid:
            pass

        self._invalid = False

    def _invalidate(self):
        self._invalid = True

class Camera2D(Camera):

    def __init__(self, pos = Vector3([0.0, 1.0, 0.0]), orientation = Vector4([1.0, 0.0, 0.0, 0.0])):
        super(Camera2D, self).__init__(pos = pos, orientation = orientation)

class Camera3D(Camera):
    
    def __init__(self, pos = Vector3([0.0, 1.0, 0.0]), orientation = Vector4([1.0, 0.0, 0.0, 0.0])):
        super(Camera3D, self).__init__(pos = pos, orientation = orientation)