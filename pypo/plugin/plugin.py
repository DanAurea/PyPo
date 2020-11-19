from gui.views.view import View

class Plugin(object):
    
    def __init__(self):
        self.name = "Default plugin"
        self.view = View

    def render(self):
        pass