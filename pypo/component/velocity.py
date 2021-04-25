class Velocity(object):
    """
    Velocity component, used to describe movement speed of an entity.
    """
    __slots__ = [ "x", "y", "z" ]

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z