from PySide2.QtWidgets import QTabWidget, QPushButton
from plugin.observer import Observer 

class Viewer(QTabWidget):

    def __init__(self, parent = None):
        super(Viewer, self).__init__(parent = parent)
        
        self.plugins = [Observer()]
        self._data   = None
        self._debug  = False

    @property
    def debug(self):
        return self._debug
    
    @debug.setter
    def debug(self, state):
        self._debug = state

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, dataset):
        self._data = dataset
        self.render()

    def show(self):
        """
        Show views loaded in the viewer
        """
        for plugin in self.plugins:
            plugin.debug = self._debug
            self.addTab(plugin.view, plugin.name)

    def render(self):
        """
        Renders data in plugins visible.
        """
        for plugin in self.plugins:
            if plugin.view.isVisible():
                plugin.render()