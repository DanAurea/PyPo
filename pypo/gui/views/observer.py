from PySide2.QtWidgets import QWidget, QGridLayout, QVBoxLayout
from gui.widget.scene.scene_3d import Scene3D

class Observer(QWidget):

    def __init__(self, parent = None):
        super(Observer, self).__init__(parent)

        self.layout   = QGridLayout()
        self.scene_3d = Scene3D()
        self.side_bar = QWidget()

        self._set_up()

    def _create_side_bar(self):
        """
        Creates a side bar (tools/parameters...).
        """
        self.side_bar.setLayout(QVBoxLayout())

    def _set_up(self):
        """
        Set up widget with its components.
        """
        # self._create_side_bar()

        self.layout.addWidget(self.scene_3d, 0, 0)
        # self.layout.addWidget(self.side_bar, 0, 1)
        self.setLayout(self.layout)