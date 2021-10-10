from pypo.component.position import PositionComponent
from pypo.component.rotation import RotationComponent
from pypo.component.scale import ScaleComponent

class TransformComponent(object):
    """
    Transform component defines.
    """
    __slots__ = [ "position", "rotation", "scale" ]

    def __init__(self):
        self.position = PositionComponent()
        self.rotation = RotationComponent()
        self.scale    = ScaleComponent()