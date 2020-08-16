import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from GUI.ui_changeFilesNameWindows import *

from PyQt5.QtCore import QCoreApplication


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.num = randint(1, 100)
        self.fileRouteLineEdit.setFocus()

    def showMessage(self):
        guessnumber = int(self.fileRouteLineEdit.text())
        print(self.num)

        if guessnumber > self.num:
            QMessageBox.about(self, '看结果', '猜大了!')
            self.fileRouteLineEdit.setFocus()
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果', '猜小了!')
            self.fileRouteLineEdit.setFocus()
        else:
            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')
            self.num = randint(1, 100)
            self.fileRouteLineEdit.clear()
            self.fileRouteLineEdit.setFocus()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.browseButton.clicked.connect(QCoreApplication.instance().quit)
    mainWindow.editByTimeButton.clicked.connect(mainWindow.showMessage)
    mainWindow.show()
    sys.exit(app.exec_())