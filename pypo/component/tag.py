class TagComponent(object):
    """
    Tag component are used to put a label on entities. That could be useful for debugging
    or displaying informations about a specific entity.d
    """
    __slots__ = [ "tag" ]

    def __init__(self, tag = "Empty tag"):
        self.tag = tag