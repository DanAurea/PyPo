from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDockWidget, QGridLayout, QPushButton, QSlider, QSplitter, QVBoxLayout, QWidget

from gui.views.view import View
from gui.widget.point_cloud.scene import Scene3D
from gui.widget.point_cloud.scene_2d.topview import TopView
from gui.widget.point_cloud.scene_2d.sideview import SideView

class ObserverView(View):

    def __init__(self, parent = None):
        super(ObserverView, self).__init__(parent)

        self._layout         = QGridLayout()
        
        self._scene_splitter = QSplitter(Qt.Horizontal, parent = self)
        self._dock_top_view  = QDockWidget("Top view", parent = self)
        self._dock_side_view = QDockWidget("Side view", parent = self)
        self._dock_scene_3d  = QDockWidget("World view",parent = self)
        
        self._scene_2d       = QSplitter(Qt.Vertical, parent = self)
        self._scene_3d       = Scene3D(parent = self)
        
        self._top_view       = TopView(parent = self._scene_2d)
        self._side_view      = SideView(parent = self._scene_2d)
        
        self._side_bar       = QDockWidget("Point cloud parameters", parent = self)
        self._record_control = QWidget()

        self._setup()

    def _setup_scene_2d(self):
        """
        Set layout of 2D scenes 
        """
        self._dock_top_view.setWidget(self._top_view)
        self._dock_side_view.setWidget(self._side_view)

        self._dock_top_view.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self._dock_side_view.setFeatures(QDockWidget.AllDockWidgetFeatures)

        self._scene_2d.addWidget(self._dock_top_view)
        self._scene_2d.addWidget(self._dock_side_view)

    def _create_side_bar(self):
        """
        Creates a side bar (tools/parameters...).
        """
        layout = QVBoxLayout(parent = self)

        self._side_bar.setLayout(layout)
        self._side_bar.setMaximumWidth(250)

    def _create_record_controls(self):
        """
        Creates controls for manipulation of the current record (play,stop, next frame, previous frame...) 
        """
        layout = QGridLayout(parent = self)
        self._record_control.setLayout(layout)

        self._frame_slider      = QSlider(Qt.Horizontal, parent = self)
        
        layout_button = QGridLayout()

        self._reward_button     = QPushButton("Reward")
        self._forward_button    = QPushButton("Forward")
        self._play_pause_button = QPushButton()
        self._stop_button       = QPushButton("Stop")
        self._record_button     = QPushButton("Record")

        self._play_pause_button.setObjectName("play")
        # self._play_pause_button.setIcon(QIcon(r"..\res\icons\play.png"))
        # self._play_pause_button.setIconSize(QSize(24, 24))
        # self._play_pause_button.setStyleSheet("border: none;");

        layout_button.addWidget(self._reward_button, 0, 0) 
        layout_button.addWidget(self._play_pause_button, 0, 1) 
        layout_button.addWidget(self._forward_button, 0, 2) 
        layout_button.addWidget(self._stop_button, 0, 3) 
        
        layout.addWidget(self._frame_slider, 0, 0)
        layout.addLayout(layout_button, 1, 0)

    def _setup(self):
        """
        Set up widget with its components.
        """
        self._create_side_bar()
        self._create_record_controls()

        self._setup_scene_2d()

        self._dock_scene_3d.setWidget(self._scene_3d)
        self._dock_scene_3d.setFeatures(QDockWidget.AllDockWidgetFeatures)

        self._scene_splitter.addWidget(self._dock_scene_3d)
        self._scene_splitter.addWidget(self._scene_2d)

        self._layout.addWidget(self._side_bar, 0, 0)
        self._layout.addWidget(self._scene_splitter, 0, 1)
        self._layout.addWidget(self._record_control, 1, 1)

        self.setLayout(self._layout)