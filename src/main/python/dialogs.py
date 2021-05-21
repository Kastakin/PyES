# This file handles the creation of all the custom dialogs
# used by the software

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from ui.sssc_about import Ui_dialogAbout
from ui.sssc_newDialog import Ui_dialogNew


class newDialog(QDialog):
    def __init__(self, parent=None):
        """
        Dialog asking if you want to save before initializing new project.
        """
        super().__init__(parent)
        self.ui = Ui_dialogNew()
        self.ui.setupUi(self)


class aboutDialog(QDialog):
    def __init__(self, parent=None):
        """
        Dialog reporting info about the program and liceses involved in its creation.
        """
        super().__init__(parent)
        self.ui = Ui_dialogAbout()
        self.ui.setupUi(self)


class wrongFileDialog(QMessageBox):
    def __init__(self, parent=None):
        """
        Dialog signaling that the selected file is not a valid project file.
        """
        super().__init__(parent)
        self.setWindowTitle("Error")
        self.setText("The file you tried to open is not a valid PyBSTAC project file")
        self.setIcon(QMessageBox.Warning)
