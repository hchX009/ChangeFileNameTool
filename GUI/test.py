from PyQt5.QtWidgets import *
from GUI.Ui_changeFilesNameWindows import *
from Action.OpenFileDir import *


class MainWindow(QMainWindow, Ui_changeFilesNameWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
