import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from PyQt5.QtCore import QCoreApplication
from Action.OpenFileDir import OpenFileDir
from GUI.test import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    openFileDir = OpenFileDir(mainWindow)
    mainWindow.browseButton.clicked.connect(openFileDir.openfile)
    mainWindow.show()
    sys.exit(app.exec_())

    # stop until 2020.12.25