import json

import pandas as pd
from PyQt5.QtCore import QThreadPool, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QFileDialog, QHeaderView, QMainWindow

from dialogs import aboutDialog, newDialog, wrongFileDialog
from ExportWindow import ExportWindow
from PlotWindow_pyqtgraph import PlotWindow
from ui.PyES4_main import Ui_MainWindow
from utils_func import cleanData, indCompUpdater, returnDataDict
from viewmodels.delegate import CheckBoxDelegate, ComboBoxDelegate
from viewmodels.model_proxy import ProxyModel
from viewmodels.models import (
    ComponentsModel,
    SolidSpeciesModel,
    SpeciesModel,
    TitrationComponentsModel,
)
from workers import optimizeWorker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set window title and project path as defaults
        self.setWindowTitle("PyES4 - New Project")
        self.project_path = None

        # Setup for secondary windows
        self.PlotWindow = None
        self.ExportWindow = None

        # Initiate threadpool
        self.threadpool = QThreadPool()

        # Generate clean data for tableviews
        (
            self.conc_data,
            self.comp_data,
            self.species_data,
            self.solid_species_data,
        ) = cleanData()

        # Conncect slots for actions
        self.actionNew.triggered.connect(self.file_new)
        self.actionSave.triggered.connect(self.file_save)
        self.actionOpen.triggered.connect(self.file_open)

        self.actionCalculate.triggered.connect(self.calculate)
        self.actionExport_Results.triggered.connect(self.exportDist)
        self.actionPlot_Results.triggered.connect(self.plotDist)

        self.actionAbout.triggered.connect(self.help_about)
        self.actionWebsite.triggered.connect(self.help_website)

        # Sets the tabelview for the component concentrations in titration
        # FIXME: we are using two views for the same model, we could probably do with a single view
        self.concModel = TitrationComponentsModel(self.conc_data)
        self.dmode0_concProxy = ProxyModel(self)
        self.dmode0_concProxy.setSourceModel(self.concModel)
        self.dmode1_concProxy = ProxyModel(self)
        self.dmode1_concProxy.setSourceModel(self.concModel)

        self.dmode0_concView.setModel(self.dmode0_concProxy)
        d0header = self.dmode0_concView.horizontalHeader()
        d0header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.dmode1_concView.setModel(self.dmode1_concProxy)
        d1header = self.dmode1_concView.horizontalHeader()
        d1header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.dmode1_concView.setColumnHidden(1, True)
        self.dmode1_concView.setColumnHidden(3, True)

        # Sets the tableview for the components
        self.compModel = ComponentsModel(self.comp_data)
        self.compProxy = ProxyModel(self)
        self.compProxy.setSourceModel(self.compModel)
        self.compView.setModel(self.compProxy)
        compHeader = self.compView.horizontalHeader()
        compHeader.setSectionResizeMode(QHeaderView.ResizeToContents)
        # Connect the dataChanged signal to the corresponding slot
        # used to update header of species with components names
        self.compModel.dataChanged.connect(self.updateCompName)

        # Sets the tableview for the species
        self.speciesModel = SpeciesModel(self.species_data)
        self.speciesProxy = ProxyModel(self)
        self.speciesProxy.setSourceModel(self.speciesModel)
        self.speciesView.setModel(self.speciesProxy)
        self.speciesView.setItemDelegateForColumn(0, CheckBoxDelegate(self.speciesView))
        # assign combobox delegate to last column
        self.speciesView.setItemDelegateForColumn(
            self.speciesModel.columnCount() - 1,
            ComboBoxDelegate(
                self, self.speciesView, self.compModel._data["Name"].tolist()
            ),
        )
        speciesHeader = self.speciesView.horizontalHeader()
        speciesHeader.setSectionResizeMode(QHeaderView.ResizeToContents)

        # Sets the tableview for the solid species
        self.solidSpeciesModel = SolidSpeciesModel(self.solid_species_data)
        self.solidSpeciesProxy = ProxyModel(self)
        self.solidSpeciesProxy.setSourceModel(self.solidSpeciesModel)
        self.solidSpeciesView.setModel(self.solidSpeciesProxy)
        self.solidSpeciesView.setItemDelegateForColumn(
            0, CheckBoxDelegate(self.solidSpeciesView)
        )
        # assign combobox delegate to last column
        self.solidSpeciesView.setItemDelegateForColumn(
            self.solidSpeciesModel.columnCount() - 1,
            ComboBoxDelegate(
                self, self.solidSpeciesView, self.compModel._data["Name"].tolist()
            ),
        )
        solidSpeciesHeader = self.solidSpeciesView.horizontalHeader()
        solidSpeciesHeader.setSectionResizeMode(QHeaderView.ResizeToContents)

        # Interface is populated with empty basic data
        self.resetFields()

        # Sets the components names in the QComboBox
        indCompUpdater(self)

        # declare the checkline used to validate project files
        self.check_line = {"check": "PyES4 project file --- DO NOT MODIFY THIS LINE!"}

    def file_new(self):
        """
        Display a prompt asking if you want to create a new project
        """
        dialog = newDialog(self)
        if dialog.exec_():
            self.resetFields()
            self.project_path = None
            self.setWindowTitle("PyES4 - New Project")

            # Resets results
            self.result = {}

            # Disable results windows
            if self.PlotWindow:
                self.PlotWindow.close()
            if self.ExportWindow:
                self.ExportWindow.close()

            # Disable buttons to show results
            self.exportButton.setEnabled(False)
            self.plotDistButton.setEnabled(False)
            self.actionExport_Results.setEnabled(False)
            self.actionPlot_Results.setEnabled(False)
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
        if self.project_path:
            output_path, _ = QFileDialog.getSaveFileName(
                self, "Save Project", self.project_path, "JSON (*.json)"
            )
        else:
            output_path, _ = QFileDialog.getSaveFileName(
                self, "Save Project", "", "JSON (*.json)"
            )

        if output_path:
            file_name = output_path.split(".")

            # Store the file path
            self.project_path = output_path

            # Set window title accordingly
            self.setWindowTitle("PyES4 - " + self.project_path)

            # dictionary that holds all the relevant data locations
            data_list = returnDataDict(self)
            data = {**self.check_line, **data_list}

            with open(
                file_name[0] + ".json",
                "w",
            ) as out_file:
                json.dump(data, out_file)

    def file_open(self):
        """
        Load a previously saved project
        """
        input_path, _ = QFileDialog.getOpenFileName(
            self, "Open Project", "~", "JSON (*.json)"
        )

        if input_path:
            with open(
                input_path,
                "r",
            ) as input_file:
                jsdata = json.load(input_file)

            # TODO: better and more robust validation of project files
            # The loaded file has to be a valid project file, discard it if not
            if jsdata["check"] != self.check_line["check"]:
                dialog = wrongFileDialog(self)
                dialog.exec_()
                return False

            # Resets results
            self.result = {}
            # Get file path from the open project file
            self.project_path = input_path
            # Set window title accordingly
            self.setWindowTitle("PyES4 - " + self.project_path)

            # Disable results windows
            if self.PlotWindow:
                self.PlotWindow.close()
            if self.ExportWindow:
                self.ExportWindow.close()

            # Disable buttons to show results
            self.exportButton.setEnabled(False)
            self.plotDistButton.setEnabled(False)
            self.actionExport_Results.setEnabled(False)
            self.actionPlot_Results.setEnabled(False)

            try:
                self.numComp.setValue(jsdata["nc"])
            except:
                self.numComp.setValue(1)

            try:
                self.numSpecies.setValue(jsdata["ns"])
            except:
                self.numSpecies.setValue(1)

            try:
                self.numPhases.setValue(jsdata["np"])
            except:
                self.numPhases.setValue(0)

            try:
                self.relErrorMode.setCurrentIndex(jsdata["emode"])
            except:
                self.relErrorMode.setCurrentIndex(1)

            try:
                self.imode.setCurrentIndex(jsdata["imode"])
            except:
                self.imode.setCurrentIndex(0)

            try:
                self.refIonicStr.setValue(jsdata["ris"])
            except:
                self.refIonicStr.setValue(0)

            try:
                self.A.setValue(jsdata["a"])
            except:
                self.A.setValue(0)

            try:
                self.B.setValue(jsdata["b"])
            except:
                self.B.setValue(0)

            try:
                self.c0.setValue(jsdata["c0"])
            except:
                self.c0.setValue(0)

            try:
                self.c1.setValue(jsdata["c1"])
            except:
                self.c1.setValue(0)

            try:
                self.d0.setValue(jsdata["d0"])
            except:
                self.d0.setValue(0)

            try:
                self.d1.setValue(jsdata["d1"])
            except:
                self.d1.setValue(0)

            try:
                self.e0.setValue(jsdata["e0"])
            except:
                self.e0.setValue(0)

            try:
                self.dmode.setCurrentIndex(jsdata["dmode"])
            except:
                self.dmode.setCurrentIndex(0)

            try:
                self.v0.setValue(jsdata["v0"])
            except:
                self.v0.setValue(0)

            try:
                self.initv.setValue(jsdata["initv"])
            except:
                self.initv.setValue(0)

            try:
                self.vinc.setValue(jsdata["vinc"])
            except:
                self.vinc.setValue(0)

            try:
                self.nop.setValue(jsdata["nop"])
            except:
                self.nop.setValue(1)

            try:
                self.c0back.setValue(jsdata["c0back"])
            except:
                self.c0back.setValue(0)

            try:
                self.ctback.setValue(jsdata["ctback"])
            except:
                self.ctback.setValue(0)

            try:
                self.initialLog.setValue(jsdata["initialLog"])
            except:
                self.initialLog.setValue(0)

            try:
                self.finalLog.setValue(jsdata["finalLog"])
            except:
                self.finalLog.setValue(0)

            try:
                self.logInc.setValue(jsdata["logInc"])
            except:
                self.logInc.setValue(0)

            try:
                self.cback.setValue(jsdata["cback"])
            except:
                self.cback.setValue(0)

            # TODO: Find a way to handle missing model data
            try:
                self.compModel._data = pd.DataFrame.from_dict(jsdata["compModel"])
                self.compModel._data.index = range(jsdata["nc"])
            except:
                self.compModel._data = self.comp_data

            try:
                self.speciesModel._data = pd.DataFrame.from_dict(jsdata["speciesModel"])
                self.speciesModel._data.index = range(jsdata["ns"])
            except:
                self.speciesModel._data = self.species_data

            try:
                self.solidSpeciesModel._data = pd.DataFrame.from_dict(
                    jsdata["solidSpeciesModel"]
                )
                self.solidSpeciesModel._data.index = range(jsdata["np"])
            except:
                self.solidSpeciesModel._data = self.solid_species_data

            try:
                self.concModel._data = pd.DataFrame.from_dict(jsdata["concModel"])
            except:
                self.concModel._data = self.conc_data

            try:
                ind_comp = jsdata["ind_comp"]
            except:
                ind_comp = 0

            indCompUpdater(self)
            self.indComp.setCurrentIndex(ind_comp)
            self.speciesView.setItemDelegateForColumn(
                self.speciesModel.columnCount() - 1,
                ComboBoxDelegate(
                    self, self.speciesView, self.compModel._data["Name"].tolist()
                ),
            )

            # The model layout changed so it has to be updated
            self.compModel.layoutChanged.emit()
            self.speciesModel.layoutChanged.emit()
            self.solidSpeciesModel.layoutChanged.emit()
            self.concModel.layoutChanged.emit()

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
            titr_curve = dialog.previewModel._data[[vcol, ecol]]
            titr_curve.columns = ["Volume", "Potential"]
            self.titrModel._data = titr_curve
            self.titrModel.layoutChanged.emit()

    def resetFields(self):
        """
        Initializes the input fields as new "empty" values
        """
        (
            self.conc_data,
            self.comp_data,
            self.species_data,
            self.solid_species_data,
        ) = cleanData()

        # Reset number of comp/species/phases
        self.numComp.setValue(1)
        self.numSpecies.setValue(1)
        self.numPhases.setValue(0)

        # at init phases are 0 so disable the modelview
        self.solidSpeciesView.setEnabled(False)

        # Reset rel. error settings
        self.relErrorMode.setCurrentIndex(1)
        self.relErrorsUpdater(1)

        # Reset Ionic strenght params
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
        self.imodeUpdater(0)

        # Set dmode as 0 (titration)
        # and display the correct associated widget
        self.dmode.setCurrentIndex(0)
        self.dmodeUpdater(0)

        # Resets fields for both dmodes
        self.v0.setValue(0)
        self.initv.setValue(0)
        self.vinc.setValue(0)
        self.nop.setValue(1)
        self.c0back.setValue(0)
        self.ctback.setValue(0)
        self.initialLog.setValue(0)
        self.finalLog.setValue(0)
        self.logInc.setValue(0)
        self.cback.setValue(0)

        # No results should be aviable so
        # grayout export and plot buttons
        self.plotDistButton.setEnabled(False)
        self.exportButton.setEnabled(False)
        self.actionExport_Results.setEnabled(False)
        self.actionPlot_Results.setEnabled(False)
        # Clear logger output
        self.consoleOutput.clear()

        # Clear previous stored results
        self.result = {}

        # if the function is called after
        # first initialization when models are already
        # declared update them to the empty values
        try:
            self.concModel._data = self.conc_data
            self.compModel._data = self.comp_data
            self.speciesModel._data = self.species_data
            self.solidSpeciesModel._data = self.solid_species_data
            self.concModel.layoutChanged.emit()
            self.compModel.layoutChanged.emit()
            self.speciesModel.layoutChanged.emit()
            self.solidSpeciesModel.layoutChanged.emit()
            indCompUpdater(self)
        except:
            pass

    def updateComp(self, rows):
        """
        Handles the updating to species and components models
        due to changes in the components present
        """
        if self.compModel.rowCount() < rows:
            added_rows = rows - self.compModel.rowCount()
            self.compModel.insertRows(self.compModel.rowCount(), added_rows)
            self.speciesView.setItemDelegateForColumn(
                self.speciesModel.columnCount() - 1, None
            )
            self.speciesModel.insertColumns(
                self.speciesModel.columnCount() - 1, added_rows
            )
            self.speciesView.setItemDelegateForColumn(
                self.speciesModel.columnCount() - 1,
                ComboBoxDelegate(
                    self, self.speciesView, self.compModel._data["Name"].tolist()
                ),
            )
            self.solidSpeciesView.setItemDelegateForColumn(
                self.solidSpeciesModel.columnCount() - 1, None
            )
            self.solidSpeciesModel.insertColumns(
                self.solidSpeciesModel.columnCount() - 1, added_rows
            )
            self.solidSpeciesView.setItemDelegateForColumn(
                self.solidSpeciesModel.columnCount() - 1,
                ComboBoxDelegate(
                    self, self.solidSpeciesView, self.compModel._data["Name"].tolist()
                ),
            )
            self.concModel.insertRows(self.concModel.rowCount(), added_rows)
        elif self.compModel.rowCount() > rows:
            removed_rows = self.compModel.rowCount() - rows
            self.compModel.removeRows(self.compModel.rowCount(), removed_rows)
            self.speciesView.setItemDelegateForColumn(
                self.speciesModel.columnCount() - 1, None
            )
            self.speciesModel.removeColumns(
                self.speciesModel.columnCount() - 1, removed_rows
            )
            self.speciesView.setItemDelegateForColumn(
                self.speciesModel.columnCount() - 1,
                ComboBoxDelegate(
                    self, self.speciesView, self.compModel._data["Name"].tolist()
                ),
            )
            self.solidSpeciesView.setItemDelegateForColumn(
                self.solidSpeciesModel.columnCount() - 1, None
            )
            self.solidSpeciesModel.removeColumns(
                self.solidSpeciesModel.columnCount(), removed_rows
            )
            self.solidSpeciesView.setItemDelegateForColumn(
                self.solidSpeciesModel.columnCount() - 1,
                ComboBoxDelegate(
                    self, self.solidSpeciesView, self.compModel._data["Name"].tolist()
                ),
            )
            self.concModel.removeRows(self.concModel.rowCount(), removed_rows)
        else:
            pass
        self.updateCompName()
        indCompUpdater(self)

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
        updated_comps = self.compModel._data["Name"].tolist()

        self.speciesView.setItemDelegateForColumn(
            self.speciesModel.columnCount() - 1,
            ComboBoxDelegate(self, self.speciesView, updated_comps),
        )
        self.speciesModel.updateHeader(updated_comps)
        self.speciesModel.updateCompName(updated_comps)

        self.solidSpeciesView.setItemDelegateForColumn(
            self.solidSpeciesModel.columnCount() - 1,
            ComboBoxDelegate(self, self.solidSpeciesView, updated_comps),
        )
        self.solidSpeciesModel.updateHeader(updated_comps)
        self.solidSpeciesModel.updateCompName(updated_comps)

        self.concModel.updateIndex(updated_comps)
        indCompUpdater(self)

    def calculate(self):
        # Disable the button, one omptimization calculation at the time
        self.calcButton.setEnabled(False)
        self.plotDistButton.setEnabled(False)
        self.exportButton.setEnabled(False)
        self.actionExport_Results.setEnabled(False)
        self.actionPlot_Results.setEnabled(False)

        # Clear old results and secondary windows
        self.result = {}
        self.PlotWindow = None
        self.ExportWindow = None

        # Clear Logger
        self.consoleOutput.setText("")
        data_list = returnDataDict(self, saving=False)
        debug = self.debug.isChecked()
        worker = optimizeWorker(data_list, debug)

        # Conncect worker signals to slots
        worker.signals.finished.connect(self.worker_complete)
        worker.signals.result.connect(self.storeResults)
        worker.signals.log.connect(self.logger)
        worker.signals.aborted.connect(self.aborted)

        # Execute
        self.threadpool.start(worker)

    def worker_complete(self):
        self.calcButton.setEnabled(True)
        self.plotDistButton.setEnabled(True)
        self.exportButton.setEnabled(True)
        self.actionExport_Results.setEnabled(True)
        self.actionPlot_Results.setEnabled(True)

    def aborted(self, error):
        self.consoleOutput.append("### ERROR ###")
        self.consoleOutput.append(error)
        self.consoleOutput.append("### ABORTED ###")

        self.calcButton.setEnabled(True)

    def logger(self, log):
        self.consoleOutput.append(log)

    def imodeUpdater(self, imode):
        """
        Enables and disables Debye-Huckle parameters fields
        while making it clear grayingout also the corresponding
        fields in the modelviews
        """
        if imode == 1:
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

            self.c0back.setEnabled(True)
            self.c0back_label.setEnabled(True)
            self.ctback.setEnabled(True)
            self.ctback_label.setEnabled(True)
            self.cback.setEnabled(True)
            self.cback_label.setEnabled(True)

            self.speciesView.model().setColumnReadOnly(range(4, 8), False)
            self.solidSpeciesView.model().setColumnReadOnly(range(3, 7), False)

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

            self.c0back.setEnabled(False)
            self.c0back_label.setEnabled(False)
            self.ctback.setEnabled(False)
            self.ctback_label.setEnabled(False)
            self.cback.setEnabled(False)
            self.cback_label.setEnabled(False)

            self.speciesView.model().setColumnReadOnly(range(4, 8), True)
            self.solidSpeciesView.model().setColumnReadOnly(range(3, 7), True)

    def exportDist(self):
        """
        Export calculated distribution in csv/excel format
        """
        if self.ExportWindow is None:
            self.ExportWindow = ExportWindow(self)
        else:
            self.ExportWindow.result = self.result
        self.ExportWindow.show()

    def storeResults(self, data, location):
        """
        Store result for exporting.
        """
        self.result[location] = data

    def plotDist(self, data):
        """
        Plot the distribution of species obtained from the optimization
        """
        if self.PlotWindow is None:
            self.PlotWindow = PlotWindow(self)
        self.PlotWindow.show()

    def dmodeUpdater(self, mode):
        """
        Conditionally show one settings input or another
        if we want to work in distribution or titration mode.
        """
        if mode == 0:
            self.dmode0Input.show()
            self.dmode1Input.hide()
        else:
            self.dmode0Input.hide()
            self.dmode1Input.show()

    def indipendentUpdater(self, comp):
        """
        If working in "distribution mode"
        gray out indipendent component.
        """
        try:
            self.dmode1_concView.model().setRowReadOnly([self.previousIndComp], False)
        except:
            pass
        self.previousIndComp = self.indComp.currentIndex()
        self.dmode1_concView.model().setRowReadOnly([comp], True)

    def relErrorsUpdater(self, mode):
        """
        If relative errors aren't requested
        gray out the corresponding columns in tableviews.
        """
        if mode == 0:
            self.speciesView.model().setColumnReadOnly([3], False)
            self.solidSpeciesView.model().setColumnReadOnly([3], False)
            self.dmode1_concView.model().setColumnReadOnly([2, 3], False)
            self.dmode0_concView.model().setColumnReadOnly([2, 3], False)
        else:
            self.speciesView.model().setColumnReadOnly([3], True)
            self.solidSpeciesView.model().setColumnReadOnly([3], True)
            self.dmode1_concView.model().setColumnReadOnly([2, 3], True)
            self.dmode0_concView.model().setColumnReadOnly([2, 3], True)

    def v0Updater(self, value):
        self.initv.setMinimum(value)

    def closeEvent(self, event):
        """
        Cleanup before closing.
        """
        # Close any secondary window still open
        if self.ExportWindow:
            self.ExportWindow.close()
        if self.PlotWindow:
            self.PlotWindow.close()

        event.accept()
