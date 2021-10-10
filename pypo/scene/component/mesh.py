class MeshComponent(object):
    """
    Mesh component, used to define volume (2D/3D).
    Mesh id is a reference to VBO located in related manager.
    """
    __slots__ = [ "vbo_id" ]

    def __init__(self, vbo_id):
        self.vbo_id = vbo_id
        # self.ibo_id = ibo_id