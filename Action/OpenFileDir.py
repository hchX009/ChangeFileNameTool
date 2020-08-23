from PyQt5.QtWidgets import QFileDialog


class OpenFileDir(object):
    def __init__(self, type):
        self.mainWindow = type

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self.mainWindow, '选择文件', '.', '')
        print(openfile_name[0])
        self.mainWindow.fileRouteLineEdit.setText(openfile_name[0])