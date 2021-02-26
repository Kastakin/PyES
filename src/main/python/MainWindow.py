import json

import pandas as pd
from PyQt5.QtCore import QThreadPool, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QFileDialog, QHeaderView, QMainWindow

from dialogs import aboutDialog, loadCurveDialog, newDialog, wrongFileDialog
from model_proxy import ProxyModel
from models import (
    ComponentsModel,
    SpeciesModel,
    SolidSpeciesModel,
    TritationComponentsModel,
    TritationModel,
)
from ui.sssc_main import Ui_MainWindow
from utils_func import cleanData, potCompUpdater, returnDataDict
from workers import optimizeWorker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.threadpool = QThreadPool()

        (
            self.trit_csv,
            self.tritconc_data,
            self.comp_data,
            self.species_data,
            self.solid_species_data,
        ) = cleanData()

        # Conncect slots for actions
        self.actionNew.triggered.connect(self.file_new)
        self.actionSave.triggered.connect(self.file_save)
        self.actionOpen.triggered.connect(self.file_open)

        self.actionAbout.triggered.connect(self.help_about)
        self.actionWebsite.triggered.connect(self.help_website)

        # Sets the modelview for the tritation curve data
        self.tritModel = TritationModel(self.trit_csv)
        self.tritView.setModel(self.tritModel)
        # Connect the layoutChanged signal to the slot used to plot that data
        self.tritModel.layoutChanged.connect(self.plot_trit)

        # Sets the modelview for the components in tritation
        self.tritCompModel = TritationComponentsModel(self.tritconc_data)
        self.tritCompView.setModel(self.tritCompModel)
        tritCompHeader = self.tritCompView.horizontalHeader()
        tritCompHeader.setSectionResizeMode(QHeaderView.ResizeToContents)

        # Sets the modelview for the components
        self.compModel = ComponentsModel(self.comp_data)
        self.compProxy = ProxyModel(self)
        self.compProxy.setSourceModel(self.compModel)
        self.compView.setModel(self.compProxy)
        compHeader = self.compView.horizontalHeader()
        compHeader.setSectionResizeMode(QHeaderView.ResizeToContents)
        # Connect the dataChanged signal to the corresponding slot
        # used to update header of species with components names
        self.compModel.dataChanged.connect(self.updateCompName)

        # Sets the modelview for the species
        self.speciesModel = SpeciesModel(self.species_data)
        self.speciesProxy = ProxyModel(self)
        self.speciesProxy.setSourceModel(self.speciesModel)
        self.speciesView.setModel(self.speciesProxy)
        speciesHeader = self.speciesView.horizontalHeader()
        speciesHeader.setSectionResizeMode(QHeaderView.ResizeToContents)

        # Sets the modelview for the solid species
        self.solidSpeciesModel = SolidSpeciesModel(self.solid_species_data)
        self.solidSpeciesProxy = ProxyModel(self)
        self.solidSpeciesProxy.setSourceModel(self.solidSpeciesModel)
        self.solidSpeciesView.setModel(self.solidSpeciesProxy)
        solidSpeciesHeader = self.solidSpeciesView.horizontalHeader()
        solidSpeciesHeader.setSectionResizeMode(QHeaderView.ResizeToContents)

        # Interface is populated with empty basic data
        self.resetFields()

        # Sets the components names in the QComboBox
        potCompUpdater(self)

        # declare the checkline used to validate project files
        self.check_line = {"check": "SSSC project file --- DO NOT MODIFY THIS LINE!"}

    def file_new(self):
        """
        Display a prompt asking if you want to create a new project
        """
        dialog = newDialog(self)
        if dialog.exec_():
            self.resetFields()
        else:
            pass

    def help_about(self):
        """
        Display about dialog
        """
        dialog = aboutDialog(self)
        dialog.exec_()

    def file_save(self):
        """
        Saves current project as json file that can be later reopened
        """
        outputFile, _ = QFileDialog.getSaveFileName(
            self, "Save Project", "ProjectName", "JSON (*.json)"
        )
        if outputFile:
            fileName = outputFile.split(".")
            # dict that holds all the relevant data locations
            data_list = returnDataDict(self)
            data = {**self.check_line, **data_list}

            with open(
                fileName[0] + ".json",
                "w",
            ) as outFile:
                json.dump(data, outFile)

    def file_open(self):
        """
        Load a previously saved project
        """
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open Project", "~", "JSON (*.json)"
        )
        if fileName:
            with open(
                fileName,
                "r",
            ) as inputFile:
                jsdata = json.load(inputFile)

            # TODO: better and more robust validation of project files
            # The loaded file has to be a valid project file, discard it if not
            if jsdata["check"] != self.check_line["check"]:
                dialog = wrongFileDialog(self)
                dialog.exec_()
                return False

            try:
                self.numComp.setValue(jsdata["nc"])
            except:
                self.numComp.setValue(1)

            try:
                self.numSpecies.setValue(jsdata["ns"])
            except:
                self.numSpecies.setValue(1)

            try:
                self.vesselVolume.setValue(jsdata["v0"])
            except:
                self.vesselVolume.setValue(0)

            try:
                self.sd_v.setValue(jsdata["sv"])
            except:
                self.sd_v.setValue(0)

            try:
                self.finalph.setValue(jsdata["ph_range"][0])
            except:
                self.finalph.setValue(1)

            try:
                self.finalph.setValue(jsdata["ph_range"][1])
            except:
                self.finalph.setValue(14)

            try:
                self.electrodeSP.setValue(jsdata["std_pot"])
            except:
                self.electrodeSP.setValue(0)

            try:
                self.sd_e.setValue(jsdata["se"])
            except:
                self.sd_e.setValue(0)

            # TODO: Find a way to handle missing model data
            try:
                self.compModel._data = pd.DataFrame.from_dict(jsdata["compModel"])
            except:
                pass

            try:
                self.speciesModel._data = pd.DataFrame.from_dict(jsdata["speciesModel"])
            except:
                pass

            try:
                self.tritModel._data = pd.DataFrame.from_dict(jsdata["tritModel"])
            except:
                pass

            try:
                self.tritCompModel._data = pd.DataFrame.from_dict(
                    jsdata["tritCompModel"]
                )
            except:
                pass

            try:
                comp_pot = jsdata["comp_pot"]
            except:
                comp_pot = 0
            potCompUpdater(self)
            self.potComp.setCurrentIndex(comp_pot)

            try:
                self.wmode.setCurrentIndex(jsdata["wmode"])
            except:
                self.wmode.setCurrentIndex(0)

            # The model layout changed so it has to be updated
            self.compModel.layoutChanged.emit()
            self.speciesModel.layoutChanged.emit()
            self.tritModel.layoutChanged.emit()
            self.tritCompModel.layoutChanged.emit()

            # Clear logger output
            self.consoleOutput.clear()

    def help_website(self):
        """
        Opens the project website in the web
        """
        url = QUrl("https://www.google.com/")
        QDesktopServices.openUrl(url)

    def loadCurve(self):
        dialog = loadCurveDialog(self)
        if dialog.exec_():
            vcol = dialog.settings["vcol"]
            ecol = dialog.settings["ecol"]
            trit_curve = dialog.previewModel._data[[vcol, ecol]]
            trit_curve.columns = ["Volume", "Potential"]
            self.tritModel._data = trit_curve
            self.tritModel.layoutChanged.emit()

    def resetFields(self):
        """
        Initializes the input fields as new "empty" values
        """
        (
            self.trit_csv,
            self.tritconc_data,
            self.comp_data,
            self.species_data,
            self.solid_species_data,
        ) = cleanData()

        self.numComp.setValue(1)
        self.numSpecies.setValue(1)
        self.numPhases.setValue(0)
        self.vesselVolume.setValue(0)
        self.sd_v.setValue(0)
        self.initialph.setValue(1)
        self.finalph.setValue(14)
        self.electrodeSP.setValue(0)
        self.sd_e.setValue(0)

        self.imode.setCurrentIndex(0)
        self.refIonicStr.setValue(0)
        self.A.setValue(0)
        self.B.setValue(0)
        self.c0.setValue(0)
        self.c1.setValue(0)
        self.d0.setValue(0)
        self.d1.setValue(0)
        self.e0.setValue(0)
        self.e1.setValue(0)
        self.imodeUpdater()

        self.SpeciesDistPlot.canvas.axes.cla()
        self.SpeciesDistPlot.canvas.draw()
        self.TitrationPlot.canvas.axes.cla()
        self.TitrationPlot.canvas.draw()

        # at init phases are 0 so disable the modelview
        self.solidSpeciesView.setEnabled(False)

        # No results should be aviable so
        # grayout export and plot buttons
        self.plotDistButton.setEnabled(False)
        self.exportButton.setEnabled(False)
        # Clear logger output
        self.consoleOutput.clear()

        # if the function is called after first initialization when models are already
        # declared update them to the empty values
        try:
            self.tritModel._data = self.trit_csv
            self.tritCompModel._data = self.tritconc_data
            self.compModel._data = self.comp_data
            self.speciesModel._data = self.species_data
            self.tritModel.layoutChanged.emit()
            self.tritCompModel.layoutChanged.emit()
            self.compModel.layoutChanged.emit()
            self.speciesModel.layoutChanged.emit()
            potCompUpdater(self)
        except:
            pass

    def updateComp(self, s):
        """
        Handles the updating to species and components models
        due to changes in the components present
        """
        if self.compModel.rowCount() < s:
            added_rows = s - self.compModel.rowCount()
            self.compModel.insertRows(self.compModel.rowCount(), added_rows)
            self.speciesModel.insertColumns(self.speciesModel.columnCount(), added_rows)
            self.solidSpeciesModel.insertColumns(
                self.solidSpeciesModel.columnCount(), added_rows
            )
            self.tritCompModel.insertRows(self.tritCompModel.rowCount(), added_rows)
            self.updateCompName()
            potCompUpdater(self)
        elif self.compModel.rowCount() > s:
            removed_rows = self.compModel.rowCount() - s
            self.compModel.removeRows(self.compModel.rowCount(), removed_rows)
            self.speciesModel.removeColumns(
                self.speciesModel.columnCount(), removed_rows
            )
            self.solidSpeciesModel.removeColumns(
                self.solidSpeciesModel.columnCount(), removed_rows
            )
            self.tritCompModel.removeRows(self.tritCompModel.rowCount(), removed_rows)
            self.updateCompName()
            potCompUpdater(self)
        else:
            pass

    def updateSpecies(self, s):
        """
        Handles the updating species model due to changes in the number of species present.
        """
        if self.speciesModel.rowCount() < s:
            added_rows = s - self.speciesModel.rowCount()
            self.speciesModel.insertRows(self.speciesModel.rowCount(), added_rows)
        elif self.speciesModel.rowCount() > s:
            removed_rows = self.speciesModel.rowCount() - s
            self.speciesModel.removeRows(self.speciesModel.rowCount(), removed_rows)
        else:
            pass

    def updatePhase(self, s):
        """
        Handles the updating solid species model due to changes in the number of solid phases present.
        """
        if self.solidSpeciesModel.rowCount() < s:
            added_rows = s - self.solidSpeciesModel.rowCount()
            self.solidSpeciesModel.insertRows(
                self.solidSpeciesModel.rowCount(), added_rows
            )
        elif self.solidSpeciesModel.rowCount() > s:
            removed_rows = self.solidSpeciesModel.rowCount() - s
            self.solidSpeciesModel.removeRows(
                self.solidSpeciesModel.rowCount(), removed_rows
            )
        else:
            pass
        if self.solidSpeciesModel.rowCount() == 0:
            self.solidSpeciesView.setEnabled(False)
        else:
            self.solidSpeciesView.setEnabled(True)

    def updateCompName(self):
        """
        Handles the displayed names in the species table when edited in the components one
        """
        updated_comp = self.compModel._data["Name"].tolist()
        self.speciesModel.updateHeader(updated_comp)
        self.solidSpeciesModel.updateHeader(updated_comp)
        self.tritCompModel.updateIndex(updated_comp)
        potCompUpdater(self)

    def plot_trit(self):
        """
        Plot imported tritation data
        """
        self.TitrationPlot.plot(
            [self.tritModel._data.iloc[:, 0]],
            [self.tritModel._data.iloc[:, 1]],
            ["Original Curve"],
            "Titrant Volume [ml]",
            "Potential",
            "Titration Curve",
            new=True,
        )

    def calculate(self):
        # Disable the button, one omptimization calculation at the time
        self.calcButton.setEnabled(False)
        # Clear Logger
        self.consoleOutput.setText("")
        data_list = returnDataDict(self, saving=False)
        worker = optimizeWorker(data_list)

        # Conncect worker signals to slots
        worker.signals.finished.connect(self.worker_complete)
        worker.signals.result.connect(self.plotDist)
        worker.signals.log.connect(self.logger)
        worker.signals.aborted.connect(self.aborted)

        # Execute
        self.threadpool.start(worker)

    def worker_complete(self):
        self.calcButton.setEnabled(True)
        self.plotDistButton.setEnabled(True)
        self.exportButton.setEnabled(True)

    def aborted(self, error):
        self.consoleOutput.append("### ERROR ###")
        self.consoleOutput.append(error)
        self.consoleOutput.append("### ABORTED ###")

        self.calcButton.setEnabled(True)

    def logger(self, log):
        self.consoleOutput.append(log)

    def imodeUpdater(self):
        """
        Enables and disables Debye-Huckle parameters fields
        while making it clear grayingout also the corresponding
        fields in the modelviews
        """
        if self.imode.currentIndex() == 1:
            self.refIonicStr.setEnabled(True)
            self.refIonicStr_label.setEnabled(True)
            self.A.setEnabled(True)
            self.A_label.setEnabled(True)
            self.B.setEnabled(True)
            self.B_label.setEnabled(True)
            self.c0.setEnabled(True)
            self.c0_label.setEnabled(True)
            self.c1.setEnabled(True)
            self.c1_label.setEnabled(True)
            self.d0.setEnabled(True)
            self.d0_label.setEnabled(True)
            self.d1.setEnabled(True)
            self.d1_label.setEnabled(True)
            self.e0.setEnabled(True)
            self.e0_label.setEnabled(True)
            self.e1.setEnabled(True)
            self.e1_label.setEnabled(True)

            self.speciesView.model().setColumnReadOnly(range(2, 6), False)
            self.solidSpeciesView.model().setColumnReadOnly(range(2, 6), False)

        else:
            self.refIonicStr.setEnabled(False)
            self.refIonicStr_label.setEnabled(False)
            self.A.setEnabled(False)
            self.A_label.setEnabled(False)
            self.B.setEnabled(False)
            self.B_label.setEnabled(False)
            self.c0.setEnabled(False)
            self.c0_label.setEnabled(False)
            self.c1.setEnabled(False)
            self.c1_label.setEnabled(False)
            self.d0.setEnabled(False)
            self.d0_label.setEnabled(False)
            self.d1.setEnabled(False)
            self.d1_label.setEnabled(False)
            self.e0.setEnabled(False)
            self.e0_label.setEnabled(False)
            self.e1.setEnabled(False)
            self.e1_label.setEnabled(False)

            self.speciesView.model().setColumnReadOnly(range(2, 6), True)
            self.solidSpeciesView.model().setColumnReadOnly(range(2, 6), True)

    def displayCurve(self):
        """
        Display the titration Curve
        """
        # TODO: move this feature from the dedicated tab to a dialog
        # Maybe do this in a separated thread?
        pass

    def exportDist(self):
        """
        Export calculated distribution in csv/excel format
        """
        # TODO: implement this feature
        # Maybe do this in a separated thread?
        pass

    # FIXME: DUPLICATE
    def plotDist(self):
        """
        Display a form to graph the calculated distribution
        """
        # TODO: implement this feature
        # Maybe do this in a separated thread?
        pass

    def plotDist(self, data):
        """
        Plot the distribution of species obtained from the optimization
        """
        self.SpeciesDistPlot.plot(
            [data.index for i in range(data.shape[0])],
            [data[i] for i in data.columns],
            data.columns,
            "Titrant Volume [ml]",
            "Concentration [mol/L]",
            "Distribution Curve",
            new=True,
        )
