class Entity(object):
    """
    Entities are related to collection of components and define 
    in an indirect way objects that can be found in a world.
    """
    __slots__ = [ "id" ]

    def __init__(self):
        self.id = id