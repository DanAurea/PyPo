class Camera(object):
    
    def __init__(self):
        self._invalid = True

    def move_forward(self):
        print("Move forward")
        self._invalidate()

    def move_backward(self):
        print("Move backward")
        self._invalidate()

    def move_left(self):
        print("Move left")
        self._invalidate()

    def move_right(self):
        print("Move right")
        self._invalidate()

    def update(self):
        self._invalid = False

    def _invalidate(self):
        self._invalid = True

class Camera2D(Camera):

    def __init__(self):
        super(Camera2D, self).__init__()

class Camera3D(Camera):
    
    def __init__(self):
        super(Camera3D, self).__init__()