from PySide2.QtWidgets import QTabWidget, QPushButton
from plugin.observer import Observer 

class Viewer(QTabWidget):

    def __init__(self, parent = None):
        super(Viewer, self).__init__(parent = parent)
        
        self.plugins = [Observer()]
        self._record   = None
        self._debug  = False

    @property
    def debug(self):
        return self._debug
    
    @debug.setter
    def debug(self, state):
        self._debug = state

    @property
    def record(self):
        return self._record
    
    @record.setter
    def record(self, dataset):
        self._record = dataset
        self.update()

    def animate(self):
        pass

    def previous_frame(self):
        pass
    
    def next_frame(self):
        pass

    def show(self):
        """
        Show views loaded in the viewer
        """
        for plugin in self.plugins:
            plugin.debug = self._debug
            self.addTab(plugin.view, plugin.name)

    def update(self):
        """
        Update state of current viewer.
        """
        for plugin in self.plugins:
            if plugin.view.isVisible():
                plugin.render()