# This file handles the creation of all the custom dialogs
# used by the software

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox
from ui.PyES_about import Ui_dialogAbout
from ui.PyES_ionicStrengthInfo import Ui_IonicStrengthInfoDialog
from ui.PyES_newDialog import Ui_dialogNew
from ui.PyES_uncertaintyInfo import Ui_UncertaintyInfoDialog


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
        self.setWindowTitle("Wrong File")
        self.setText("The file you tried to open is not a valid PyES project file")
        self.setIcon(QMessageBox.Icon.Critical)


class IssuesLoadingDialog(QMessageBox):
    def __init__(self, parent=None):
        """
        Dialog signaling that the selected file is not a valid project file.
        """
        super().__init__(parent)
        self.setWindowTitle("Issues in Project File")
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


class IonicStrengthInfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_IonicStrengthInfoDialog()
        self.ui.setupUi(self)

        self.ui.widget.load(":/equations/dh_equation.svg")
        self.ui.widget.renderer().setAspectRatioMode(Qt.KeepAspectRatio)

        self.ui.widget_2.load(":/equations/dh_expansion.svg")
        self.ui.widget_2.renderer().setAspectRatioMode(Qt.KeepAspectRatio)


class UncertaintyInfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_UncertaintyInfoDialog()
        self.ui.setupUi(self)

        self.ui.widget.load(":/equations/error_components.svg")
        self.ui.widget.renderer().setAspectRatioMode(Qt.KeepAspectRatio)

        self.ui.widget_2.load(":/equations/error_soluble.svg")
        self.ui.widget_2.renderer().setAspectRatioMode(Qt.KeepAspectRatio)

        self.ui.widget_3.load(":/equations/error_precipitate.svg")
        self.ui.widget_3.renderer().setAspectRatioMode(Qt.KeepAspectRatio)
