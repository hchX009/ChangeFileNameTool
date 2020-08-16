import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from PyQt5.QtCore import QCoreApplication
from Action.test import Test
from GUI.test import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    testAction = Test()
    mainWindow.browseButton.clicked.connect(QCoreApplication.instance().quit)
    mainWindow.editByTimeButton.clicked.connect(testAction.showMessage)
    mainWindow.show()
    sys.exit(app.exec_())