from gui.views.observer import ObserverView
from plugin.plugin import Plugin

class Observer(Plugin):
    
    def __init__(self):
        self.name = "Point cloud observer"
        self.view = ObserverView()

    def render(self):
        pass