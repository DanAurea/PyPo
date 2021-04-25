class RotationComponent(object):
    """
    Rotation component, used to describe rotate an entity.
    Quaternion should be used for more flexibility than yaw, pitch, roll.
    """
    __slots__ = [ "x", "y", "z", "w" ]

    def __init__(self, x = 0.0, y = 0.0, z = 0.0, w = 1.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w