from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from GUI.Ui_changeFilesNameWindows import *


class MainWindow(QMainWindow, Ui_changeFilesNameWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
