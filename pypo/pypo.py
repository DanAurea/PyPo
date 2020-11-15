from PySide2.QtCore import Qt
from PySide2.QtWidgets import QAction, QApplication, QHBoxLayout, QMainWindow, QMenuBar, QPushButton, QStyle, QTabWidget, QWidget
from core.configuration.application import ApplicationConfiguration
from gui.viewer import Viewer

import sys

class PyPo(QApplication):
    
    def __init__(self, *argv):
        super(PyPo, self).__init__(*argv)
        
        self.application_configuration = ApplicationConfiguration()
        self.main_window               = QMainWindow()
        self.central_widget            = Viewer(parent = self.main_window)
        self._menu_bar                  = self.main_window.menuBar()

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
        normal_icon = style.standardIcon(QStyle.SP_TitleBarNormalButton)
        close_icon    = style.standardIcon(QStyle.SP_TitleBarCloseButton)

        minimize_button = QPushButton(self._menu_bar)
        normal_button = QPushButton(self._menu_bar)
        close_button    = QPushButton(self._menu_bar)
        
        minimize_button.setIcon(minimize_icon)
        normal_button.setIcon(normal_icon)
        close_button.setIcon(close_icon)

        minimize_button.clicked.connect(self.main_window.showMinimized)
        normal_button.clicked.connect(self.main_window.showNormal)
        close_button.clicked.connect(self.main_window.close)

        window_button_layout.setSpacing(0)
        window_button_layout.addWidget(minimize_button)
        window_button_layout.addWidget(normal_button)
        window_button_layout.addWidget(close_button)

        window_button_layout.setAlignment(Qt.AlignTop)
        self._menu_bar.setCornerWidget(window_button, Qt.TopRightCorner)

    def run(self):
        """
        Run application by creating interface and load configuration.
        """
        self._create_menu()

        self.application_configuration.load()
        
        self.main_window.setWindowTitle(self.application_configuration.application_name)
        # TODO: Enable when TitleBar will be properly handled
        # self.main_window.setWindowFlags(Qt.FramelessWindowHint)
        self.main_window.setCentralWidget(self.central_widget)

        self.main_window.showMaximized()

if __name__ == '__main__':    
    pypo = PyPo(sys.argv)
    pypo.run()

    pypo.setStyleSheet(pypo.application_configuration.style)

    res = pypo.exec_()
    sys.exit(res)