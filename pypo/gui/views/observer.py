from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDockWidget, QGridLayout, QSplitter, QVBoxLayout, QWidget

from gui.widget.point_cloud.scene import Scene3D
from gui.widget.point_cloud.scene_2d.topview import TopView
from gui.widget.point_cloud.scene_2d.sideview import SideView

class Observer(QWidget):

    def __init__(self, parent = None):
        super(Observer, self).__init__(parent)

        self._layout   = QGridLayout()
        
        self._scene_splitter = QSplitter(Qt.Horizontal, parent = self)
        self._dock_top_view = QDockWidget("Top view", parent = self)
        self._dock_side_view = QDockWidget("Side view", parent = self)
        self._dock_scene_3d = QDockWidget("World view",parent = self)

        self._scene_2d = QWidget(parent = self)
        self._scene_3d = Scene3D(parent = self)
        
        self._top_view = TopView(parent = self._scene_2d)
        self._side_view = SideView(parent = self._scene_2d)

        self._scene_2d_layout = QGridLayout()
        self._setup()

    def _setup_scene_2d(self):
        """
        Set layout of 2D scenes 
        """
        self._dock_top_view.setWidget(self._top_view)
        self._dock_side_view.setWidget(self._side_view)

        self._dock_top_view.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self._dock_side_view.setFeatures(QDockWidget.AllDockWidgetFeatures)

        self._scene_2d_layout.addWidget(self._dock_top_view, 0, 0)
        self._scene_2d_layout.addWidget(self._dock_side_view, 1, 0)

        self._scene_2d.setLayout(self._scene_2d_layout)

    def _create_side_bar(self):
        """
        Creates a side bar (tools/parameters...).
        """
        self._side_bar.setLayout(QVBoxLayout())

    def _setup(self):
        """
        Set up widget with its components.
        """
        # self._create_side_bar()
        
        self._setup_scene_2d()

        self._dock_scene_3d.setWidget(self._scene_3d)
        self._dock_scene_3d.setFeatures(QDockWidget.AllDockWidgetFeatures)

        self._scene_splitter.addWidget(self._dock_scene_3d)
        self._scene_splitter.addWidget(self._scene_2d)

        self._layout.addWidget(self._scene_splitter, 0, 0)
        # self.layout.addWidget(self._side_bar, 0, 1)
        self.setLayout(self._layout)