from PySide2.QtWidgets import QTabWidget, QPushButton
from gui.views.observer import Observer 

class Viewer(QTabWidget):

    def __init__(self, parent = None):
        super(Viewer, self).__init__(parent = parent)
        
        self.observer = Observer(parent = self)
        
        self.addTab(self.observer, "Point Cloud Observer")