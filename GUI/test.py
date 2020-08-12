import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI.ui_changeFilesNameWindows import *

from PyQt5.QtCore import QCoreApplication


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.browseButton.clicked.connect(QCoreApplication.instance().quit)
    mainWindow.show()
    sys.exit(app.exec_())