class MeshComponent(object):
    """
    Mesh component, used to define volume (2D/3D).
    """
    __slots__ = [ "mesh" ]

    def __init__(self, mesh):
        self.mesh