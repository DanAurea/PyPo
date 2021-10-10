from PySide2.QtCore import Qt, QTimer
from PySide2.QtWidgets import QAction, QApplication, QHBoxLayout, QMainWindow, QMenuBar, QPushButton, QStyle, QTabWidget, QWidget
from core.configuration.application import ApplicationConfiguration
from core.io.loader_factory import LoaderFactory
from core.io.logger import Logger
from gui.viewer import Viewer

import numpy as np
import sys

class PyPo(QApplication):

    def __init__(self, *argv):
        super(PyPo, self).__init__(*argv)
        
        self.application_configuration = ApplicationConfiguration()
        self.main_window               = QMainWindow()
        self._viewer                   = Viewer(parent = self.main_window)
        self.central_widget            = self._viewer
        
        self._logger                   = Logger()
        self._loader_factory           = LoaderFactory()
        self._record                   = None

        self._menu_bar                 = self.main_window.menuBar()
        self.application_configuration.load()
    
    def dropEvent(self, event):
        """
        Drop event of main window (should be included in another class otherwise it creates a dependency).
        
        :param      event:  The event
        :type       event:  { type_description }
        """
        mime_data = event.mimeData()

        if mime_data.hasUrls():
            urls = mime_data.urls()

            for url in urls:
                record = self._loader_factory.load(url.toLocalFile())

            if record:
                self._viewer.record = record

    def dragEnterEvent(self, event):
        """
        Drag enter event of main window (should be included in another class otherwise it creates a dependency).
        
        :param      event:  The event
        :type       event:  { type_description }
        """
        event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        """
        Drag leave event of main window (should be included in another class otherwise it creates a dependency).
        
        :param      event:  The event
        :type       event:  { type_description }
        """
        event.accept()

    def _create_action(self):
        """
        Create actions of menu bar.
        """
        self.new_session_action = QAction("New session")
        self.load_action        = QAction("Load")
        self.about_action       = QAction("About")

    def _create_menu(self):
        """
        Create application's menu.
        """
        self._create_action()

        """ Define menu's actions """
        file_menu = self._menu_bar.addMenu("&File")
        file_menu.addAction(self.new_session_action)
        file_menu.addAction(self.load_action)
        self._menu_bar.addMenu(file_menu)
        
        edit_menu = self._menu_bar.addMenu("&Edit")
        self._menu_bar.addMenu(edit_menu)
        
        plugin_menu = self._menu_bar.addMenu("&Plugin")
        self._menu_bar.addMenu(plugin_menu)

        help_menu = self._menu_bar.addMenu("&Help")
        help_menu.addAction(self.about_action)
        self._menu_bar.addMenu(help_menu)

        """ TODO: Create a MenuBar class instead to allow event handling (mouse moving the window...) """
        """ Define window's buttons because application is frameless """
        window_button_layout = QHBoxLayout()

        window_button = QWidget(parent = self.main_window)
        window_button.setLayout(window_button_layout)
        
        window_button_layout.setContentsMargins(0, 0, 0, 0)

        style = self.style()

        minimize_icon = style.standardIcon(QStyle.SP_TitleBarMinButton)
        maximize_icon = style.standardIcon(QStyle.SP_TitleBarMaxButton)
        close_icon    = style.standardIcon(QStyle.SP_TitleBarCloseButton)

        minimize_button = QPushButton(self._menu_bar)
        maximize_button = QPushButton(self._menu_bar)
        close_button    = QPushButton(self._menu_bar)
        
        minimize_button.setIcon(minimize_icon)
        maximize_button.setIcon(maximize_icon)
        close_button.setIcon(close_icon)

        minimize_button.clicked.connect(self.main_window.showMinimized)
        maximize_button.clicked.connect(self.main_window.showMaximized)
        close_button.clicked.connect(self.main_window.close)

        window_button_layout.setSpacing(0)
        window_button_layout.addWidget(minimize_button)
        window_button_layout.addWidget(maximize_button)
        window_button_layout.addWidget(close_button)

        window_button_layout.setAlignment(Qt.AlignTop)
        self._menu_bar.setCornerWidget(window_button, Qt.TopRightCorner)

    def load(self, file):
        """
        Load dataset
        
        :param      file:  The file
        :type       file:  { type_description }
        """
        if self.application_configuration.debug:
            print("Load " + file)

    def run(self):
        """
        Run application by creating interface and load configuration.
        """
        self._create_menu()
        
        self.setApplicationVersion(str(self.application_configuration.version["major"]) + "." + str(self.application_configuration.version["minor"]))
        self.setOrganizationName(self.application_configuration.organization_name)

        self._logger.debug = self.application_configuration.debug
        self._viewer.debug = self.application_configuration.debug
        
        self.main_window.setWindowTitle(self.application_configuration.application_name)
        # TODO: Enable when MenuBar will be properly handled
        self.main_window.setWindowFlag(Qt.FramelessWindowHint)
        self.main_window.setCentralWidget(self.central_widget)
        self.main_window.show()
        
        self._viewer.show()

        self.main_window.dragEnterEvent = self.dragEnterEvent
        self.main_window.dragLeaveEvent = self.dragLeaveEvent
        self.main_window.dropEvent      = self.dropEvent

        self.main_window.setAcceptDrops(True)

        # Using a QTimer will delay call to showMaximized and avoid issues     
        QTimer.singleShot(0, self.main_window.showMaximized)

        if self.application_configuration.debug:
            self._viewer.record = np.random.uniform(low=0.0, high=102.4, size = (15000,4)).astype('f')

if __name__ == '__main__':
    pypo = PyPo(sys.argv)
    pypo.run()

    pypo.setStyleSheet(pypo.application_configuration.style)

    res = pypo.exec_()
    sys.exit(res)