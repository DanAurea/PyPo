from pypo.scene.registry import Registry

class World(object):
    """
    The world defines what will be part of a
    scene and its interactions.

    Registry is the container that register entity 
    to be part of the scene.

    Interactions are handled by systems that modify
    components attached to any entities.
    """

    def __init__(self):
        self.registry = Registry()
        self.systems  = None

    def update(self):
        pass