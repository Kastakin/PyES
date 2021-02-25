# This script handles the creation of all the required dialogs
# used by the software

import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from models import PreviewModel
from ui.pystac_about import Ui_dialogAbout
from ui.pystac_load import Ui_loadCurve
from ui.pystac_newDialog import Ui_dialogNew


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


class loadCurveDialog(QDialog):
    def __init__(self, parent=None):
        """
        Frontend for the Pandas load_csv function.
        """
        super().__init__(parent)
        self.ui = Ui_loadCurve()
        self.ui.setupUi(self)

        # Generate a preview view/model
        self.previewModel = PreviewModel()
        self.ui.preview.setModel(self.previewModel)

        # No file is being opened yet
        self.fileName = None

        # Get initial settings
        self.updateSettings()

    def updateSettings(self):
        self.settings = {
            "sep": self.ui.separator.currentText(),
            "dec": self.ui.decimal.currentText(),
            "head": self.ui.head.value(),
            "footer": self.ui.footer.value(),
            "vcol": self.ui.vCol.value(),
            "ecol": self.ui.eCol.value(),
        }

        if self.ui.separator.isEnabled() == False:
            self.settings["sep"] = None

        if self.ui.decimal.isEnabled() == False:
            self.settings["dec"] = None

        self._updateModel()

    def autodetectSep(self, s):
        if s == Qt.Checked:
            self.ui.separator.setEnabled(False)
        else:
            self.ui.separator.setEnabled(True)
        self.updateSettings()

    def autodetectDec(self, s):
        if s == Qt.Checked:
            self.ui.decimal.setEnabled(False)
        else:
            self.ui.decimal.setEnabled(True)
        self.updateSettings()

    def loadFile(self):
        self.fileName, _ = QFileDialog.getOpenFileName(
            self, "Open CSV", "~", "CSV (*.csv)"
        )
        self._updateModel()

    def _updateModel(self):
        if self.fileName:
            self.ui.filePath.setText(self.fileName)
            self.previewModel._data = pd.read_csv(
                self.fileName,
                sep=self.settings["sep"],
                decimal=self.settings["dec"],
                skiprows=self.settings["head"],
                skipfooter=self.settings["footer"],
                header=None,
            )
            self.previewModel.layoutChanged.emit()
