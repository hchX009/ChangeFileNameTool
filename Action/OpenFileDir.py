from PyQt5.QtWidgets import QFileDialog
from GUI.test import MainWindow

class OpenFileDir(MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

    def openfile(self):
        openfile_name = "null"
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls)')
        self.fileRouteLineEdit.setText(openfile_name)