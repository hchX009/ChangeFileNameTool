#!/usr/bin/python3
#coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class IcoWindowTest(QWidget):

   def __init__(self):
       super().__init__()
       self.initUI()

   def initUI(self):
       self.setGeometry(400, 400, 300, 300)
       self.setWindowTitle('测试窗口')
       self.setWindowIcon(QIcon('../Documents/CASC_test.ico'))

       self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = IcoWindowTest()

    sys.exit(app.exec_())