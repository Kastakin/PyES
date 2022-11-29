# This file handles the creation of all the custom dialogs
# used by the software

from PySide6.QtWidgets import QDialog, QMessageBox
from ui.PyES_about import Ui_dialogAbout
from ui.PyES_newDialog import Ui_dialogNew


class NewDialog(QDialog):
    def __init__(self, parent=None):
        """
        Dialog asking if you want to save before initializing new project.
        """
        super().__init__(parent)
        self.ui = Ui_dialogNew()
        self.ui.setupUi(self)


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        """
        Dialog reporting info about the program and liceses involved in its creation.
        """
        super().__init__(parent)
        self.ui = Ui_dialogAbout()
        self.ui.setupUi(self)


class WrongFileDialog(QMessageBox):
    def __init__(self, parent=None):
        """
        Dialog signaling that the selected file is not a valid project file.
        """
        super().__init__(parent)
        self.setWindowTitle("Error")
        self.setText("The file you tried to open is not a valid PyES project file")
        self.setIcon(QMessageBox.Warning)


class CompletedCalculation(QMessageBox):
    def __init__(self, succesful: bool, parent=None):
        """
        Dialog signaling that the selected file is not a valid project file.
        """
        super().__init__(parent)
        if succesful:
            self.setWindowTitle("Completed")
            self.setText("Calculation was completed succesfully.")
            self.setIcon(QMessageBox.Information)
        else:
            self.setWindowTitle("Failure")
            self.setText(
                'Calculation was aborted, see the "Calculate" Tab for more info.'
            )
            self.setIcon(QMessageBox.Critical)
