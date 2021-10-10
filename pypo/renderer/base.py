import abc

class Renderer(metaclass = abc.ABCMeta):
    """
    Renderer are parts of core and are used to render specific entity based on their
    components.
    """

    def __init__(self):
        pass

    @abc.abstractmethod
    def update():
        pass