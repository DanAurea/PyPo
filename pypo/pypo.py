from PySide2.QtWidgets import QAction, QApplication, QMainWindow, QMenuBar, QTabWidget
from core.configuration.application import ApplicationConfiguration
from gui.viewer import Viewer

import sys

class PyPo(QApplication):
    
    def __init__(self, *argv):
        super(PyPo, self).__init__(*argv)
        
        self.application_configuration = ApplicationConfiguration()
        self.central_widget            = Viewer()
        self.main_window               = QMainWindow()
        self.menu_bar                  = self.main_window.menuBar()

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

        file_menu = self.menu_bar.addMenu("&File")
        file_menu.addAction(self.new_session_action)
        file_menu.addAction(self.load_action)
        self.menu_bar.addMenu(file_menu)

        help_menu = self.menu_bar.addMenu("&Help")
        help_menu.addAction(self.about_action)
        self.menu_bar.addMenu(help_menu)

    def run(self):
        """
        Run application by creating interface and load configuration.
        """
        self._create_menu()

        self.application_configuration.load()
        
        self.main_window.setWindowTitle(self.application_configuration.application_name)
        self.main_window.setCentralWidget(self.central_widget)

        self.main_window.showMaximized()

if __name__ == '__main__':    
    pypo = PyPo(sys.argv)
    pypo.run()

    pypo.setStyleSheet(pypo.application_configuration.style)

    res = pypo.exec_()
    sys.exit(res)