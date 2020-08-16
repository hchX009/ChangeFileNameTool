import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from PyQt5.QtCore import QCoreApplication

from GUI.test import MainWindow


class Test(MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

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