class ScaleComponent(object):
    
    __slots__ = [ "x", "y", "z" ]

    def __init__(self, x = 1.0, y = 1.0, z = 1.0):
        self.x = x
        self.y = y
        self.z = z