from PySide2.QtWidgets import QTabWidget, QPushButton
from gui.views.observer import Observer 

class Viewer(QTabWidget):

    def __init__(self, *argv, **kwargs):
        super(Viewer, self).__init__(*argv, **kwargs)
        self.observer = Observer()
        
        self.addTab(self.observer, "Point Cloud Observer")