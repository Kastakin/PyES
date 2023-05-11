import json
import os
from pathlib import Path

import pandas as pd
from commands import AddSpeciesRows, RemoveSpeciesRows
from dialogs import (
    AboutDialog,
    CompletedCalculation,
    IonicStrengthInfoDialog,
    IssuesLoadingDialog,
    NewDialog,
    UncertaintyInfoDialog,
    WrongFileDialog,
)
from PySide6.QtCore import QByteArray, QSettings, QThreadPool, QUrl
from PySide6.QtGui import QDesktopServices, QKeySequence, QUndoCommand, QUndoStack
from PySide6.QtWidgets import (
    QFileDialog,
    QHeaderView,
    QMainWindow,
    QMessageBox,
    QWidget,
)
from ui.PyES_main import Ui_MainWindow
from utils_func import cleanData, indCompUpdater, returnDataDict
from viewmodels.delegate import CheckBoxDelegate, ComboBoxDelegate
from viewmodels.model_proxy import ProxyModel
from viewmodels.models import (
    ComponentsModel,
    SolidSpeciesModel,
    SpeciesModel,
    TitrationComponentsModel,
)
from windows.export import ExportWindow
from windows.plot import PlotWindow
from workers import optimizeWorker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initiate threadpool
        self.threadpool = QThreadPool()
        self.undostack = QUndoStack()

        self.actionUndo.triggered.connect(self.undostack.undo)
        self.actionUndo.setShortcut(QKeySequence.StandardKey.Undo)
        self.actionRedo.triggered.connect(self.undostack.redo)
        self.actionRedo.setShortcut(QKeySequence.StandardKey.Redo)

        # Initiate settings context
        self.settings = QSettings()
        self.settings.setValue("path/default", str(Path.home()))

        self.restoreGeometry(self.settings.value("mainwindow/geometry", QByteArray()))

        # Set window title and project path as defaults
        self.setWindowTitle("PyES - New Project")
        self.project_path = None

        # Setup for secondary windows
        self.PlotWindow = None
        self.ExportWindow = None

        self.imode_fields: list[QWidget] = [
            self.refIonicStr,
            self.refIonicStr_label,
            self.A,
            self.A_label,
            self.B,
            self.B_label,
            self.c0,
            self.c0_label,
            self.c1,
            self.c1_label,
            self.d0,
            self.d0_label,
            self.d1,
            self.d1_label,
            self.e0,
            self.e0_label,
            self.e1,
            self.e1_label,
            self.c0back,
            self.c0back_label,
            self.ctback,
            self.ctback_label,
            self.cback,
            self.cback_label,
        ]

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
        self.actionAbout_Qt.triggered.connect(self.help_about_qt)
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

        self.solidSpeciesModel.layoutChanged.connect(self.check_solid_presence)

        # declare the checkline used to validate project files
        self.check_line = {"check": "PyES project file --- DO NOT MODIFY THIS LINE!"}

    def file_new(self):
        """
        Display a prompt asking if you want to create a new project
        """
        dialog = NewDialog(self)
        if dialog.exec():
            self.resetFields()
            self.project_path = None
            self.setWindowTitle("PyES - New Project")

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
        dialog = AboutDialog(self)
        dialog.exec()

    def help_about_qt(self):
        """
        Display about dialog
        """
        dialog = QMessageBox.aboutQt(self)
        dialog.exec()

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
                self,
                "Save Project",
                self.settings.value("path/default"),
                "JSON (*.json)",
            )

        if output_path:
            file_name = Path(output_path).parents[0]
            file_name = file_name.joinpath(Path(output_path).stem)
            file_name = file_name.with_suffix(".json")

            # Store the file path
            self.project_path = output_path

            # Set window title accordingly
            self.setWindowTitle("PyES - " + self.project_path)

            # dictionary that holds all the relevant data locations
            data_list = returnDataDict(self)
            data = {**self.check_line, **data_list}

            with open(
                file_name,
                "w",
            ) as out_file:
                json.dump(data, out_file)

    def file_open(self):
        """
        Load a previously saved project
        """
        if self.project_path:
            input_path, _ = QFileDialog.getOpenFileName(
                self,
                "Open Project",
                os.path.dirname(self.project_path),
                "JSON (*.json)",
            )
        else:
            input_path, _ = QFileDialog.getOpenFileName(
                self,
                "Open Project",
                self.settings.value("path/default"),
                "JSON (*.json)",
            )

        if input_path:
            return self.load_project_file(input_path)

    def load_project_file(self, input_path):
        with open(
            input_path,
            "r",
        ) as input_file:
            try:
                jsdata: dict = json.load(input_file)

                # TODO: better and more robust validation of project files
                # The loaded file has to be a valid project file, discard it if not
                checksum = jsdata["check"]
                assert checksum == self.check_line["check"]
            except (json.JSONDecodeError, UnicodeDecodeError, KeyError, AssertionError):
                if not self.isVisible():
                    self.show()
                dialog = WrongFileDialog(self)
                dialog.exec()
                return False

        self.resetFields()
        # Resets results
        self.result = {}
        # Get file path from the open project file
        self.project_path = input_path
        # Set window title accordingly
        self.setWindowTitle("PyES - " + self.project_path)

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

        problems = []

        # Species Tab
        self.numComp.setValue(
            value_or_problem(jsdata, "nc", 1, "Number of components", problems)
        )
        self.numSpecies.setValue(
            value_or_problem(jsdata, "ns", 1, "Number of species", problems)
        )
        self.numPhases.setValue(
            value_or_problem(jsdata, "np", 0, "Number of phases", problems)
        )
        self.uncertaintyMode.setChecked(
            value_or_problem(jsdata, "emode", 1, "Uncertainty estimation", problems)
        )
        self.imode.setCurrentIndex(
            value_or_problem(jsdata, "imode", 0, "Ionic strength effect", problems)
        )
        self.refIonicStr.setValue(
            value_or_problem(jsdata, "ris", 0, "Reference ionic strength", problems)
        )
        self.A.setValue(
            value_or_problem(jsdata, "a", 0, "A parameter D-H equation", problems)
        )
        self.B.setValue(
            value_or_problem(jsdata, "b", 0, "B parameter D-H equation", problems),
        )
        self.c0.setValue(
            value_or_problem(jsdata, "c0", 0, "c0 parameter D-H equation", problems)
        )
        self.c1.setValue(
            value_or_problem(jsdata, "c1", 0, "c1 parameter D-H equation", problems)
        )
        self.d0.setValue(
            value_or_problem(jsdata, "d0", 0, "d0 parameter D-H equation", problems)
        )
        self.d1.setValue(
            value_or_problem(jsdata, "d1", 0, "d1 parameter D-H equation", problems)
        )
        self.e0.setValue(
            value_or_problem(jsdata, "e0", 0, "e0 parameter D-H equation", problems)
        )

        self.e1.setValue(
            value_or_problem(jsdata, "e1", 0, "e1 parameter D-H equation", problems)
        )

        # Settings tabs
        self.dmode.setCurrentIndex(
            value_or_problem(jsdata, "dmode", 0, "Work mode", problems)
        )

        self.v0.setValue(
            value_or_problem(jsdata, "v0", 0, "Initial titration volume", problems)
        )
        self.initv.setValue(
            value_or_problem(jsdata, "initv", 0, "First point of titration", problems),
        )
        self.vinc.setValue(
            value_or_problem(
                jsdata,
                "vinc",
                0,
                "Volume increments for each titration point",
                problems,
            )
        )
        self.nop.setValue(
            value_or_problem(jsdata, "nop", 1, "Number of titration points", problems)
        )
        self.c0back.setValue(
            value_or_problem(
                jsdata,
                "c0back",
                0,
                "Concentration of background ions in titration vessel",
                problems,
            )
        )
        self.ctback.setValue(
            value_or_problem(
                jsdata,
                "ctback",
                0,
                "Concentration of background ions in titrant",
                problems,
            )
        )

        ind_comp = value_or_problem(
            jsdata, "ind_comp", 0, "Independent component", problems
        )

        self.initialLog.setValue(
            value_or_problem(
                jsdata,
                "initialLog",
                0,
                "Initial Log of concentration of independent component",
                problems,
            )
        )
        self.finalLog.setValue(
            value_or_problem(
                jsdata,
                "finalLog",
                0,
                "Final Log of concentration of independent component",
                problems,
            )
        )
        self.logInc.setValue(
            value_or_problem(
                jsdata,
                "logInc",
                0,
                "Increments in Log of concentration of independent component",
                problems,
            )
        )
        self.cback.setValue(
            value_or_problem(
                jsdata, "cback", 0, "Concentration of background ions", problems
            )
        )

        # Models
        self.compModel._data = pd.DataFrame.from_dict(
            value_or_problem(
                jsdata, "compModel", self.comp_data, "Components model", problems
            )
        )
        self.compModel._data.index = range(self.numComp.value())

        self.speciesModel._data = pd.DataFrame.from_dict(
            value_or_problem(
                jsdata,
                "speciesModel",
                self.species_data,
                "Species model",
                problems,
            )
        )
        self.speciesModel._data.index = range(self.numSpecies.value())

        self.solidSpeciesModel._data = pd.DataFrame.from_dict(
            value_or_problem(
                jsdata,
                "solidSpeciesModel",
                self.solid_species_data,
                "Solid species model",
                problems,
            )
        )
        self.solidSpeciesModel._data.index = range(self.numPhases.value())

        self.concModel._data = pd.DataFrame.from_dict(
            value_or_problem(
                jsdata, "concModel", self.conc_data, "Concentrations model", problems
            )
        )

        indCompUpdater(self)
        updated_comps = self.compModel._data["Name"].tolist()
        self.speciesModel.updateHeader(updated_comps)
        self.speciesModel.updateCompName(updated_comps)
        self.solidSpeciesModel.updateHeader(updated_comps)
        self.solidSpeciesModel.updateCompName(updated_comps)
        self.indComp.setCurrentIndex(ind_comp)
        self.speciesView.setItemDelegateForColumn(
            self.speciesModel.columnCount() - 1,
            ComboBoxDelegate(
                self, self.speciesView, self.compModel._data["Name"].tolist()
            ),
        )
        self.solidSpeciesView.setItemDelegateForColumn(
            self.solidSpeciesModel.columnCount() - 1,
            ComboBoxDelegate(
                self, self.solidSpeciesView, self.compModel._data["Name"].tolist()
            ),
        )

        # The model layout changed so it has to be updated
        self.compModel.layoutChanged.emit()
        self.speciesModel.layoutChanged.emit()
        self.solidSpeciesModel.layoutChanged.emit()
        self.concModel.layoutChanged.emit()

        # Clear logger output
        self.consoleOutput.clear()

        # Clear undo stack after loading
        self.undostack.clear()

        if problems:
            problems_dialog = IssuesLoadingDialog(self)
            problems_dialog.setText(
                "The following fields had problems being imported:\n"
                + "\n".join([f"- {p}" for p in problems])
                + "\n" * 2
                + "Default values have been used in their place."
            )
            problems_dialog.exec()

    def help_website(self):
        """
        Opens the project website in the web
        """
        url = QUrl("https://github.com/Kastakin/PyES")
        QDesktopServices.openUrl(url)

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
        self.uncertaintyMode.setChecked(False)

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

            self.addSpeciesComp(self.speciesModel.columnCount() - 1, added_rows)
            self.concModel.insertRows(self.concModel.rowCount(), added_rows)

        elif self.compModel.rowCount() > rows:
            removed_rows = self.compModel.rowCount() - rows
            self.compModel.removeRows(self.compModel.rowCount(), removed_rows)

            self.removeSpeciesComp(self.speciesModel.columnCount() - 1, removed_rows)
            self.concModel.removeRows(self.concModel.rowCount(), removed_rows)
        else:
            pass
        self.updateCompName()
        indCompUpdater(self)

    def addSpeciesComp(self, position, added_rows):
        self.speciesView.setItemDelegateForColumn(
            self.speciesModel.columnCount() - 1, None
        )
        self.speciesModel.insertColumns(position, added_rows)
        self.speciesView.setItemDelegateForColumn(
            self.speciesModel.columnCount() - 1,
            ComboBoxDelegate(
                self, self.speciesView, self.compModel._data["Name"].tolist()
            ),
        )

        self.solidSpeciesView.setItemDelegateForColumn(
            self.solidSpeciesModel.columnCount() - 1, None
        )
        self.solidSpeciesModel.insertColumns(position, added_rows)
        self.solidSpeciesView.setItemDelegateForColumn(
            self.solidSpeciesModel.columnCount() - 1,
            ComboBoxDelegate(
                self, self.solidSpeciesView, self.compModel._data["Name"].tolist()
            ),
        )

    def removeSpeciesComp(self, position, removed_rows):
        self.speciesView.setItemDelegateForColumn(
            self.speciesModel.columnCount() - 1, None
        )
        self.speciesModel.removeColumns(position, removed_rows)
        self.speciesView.setItemDelegateForColumn(
            self.speciesModel.columnCount() - 1,
            ComboBoxDelegate(
                self, self.speciesView, self.compModel._data["Name"].tolist()
            ),
        )
        self.solidSpeciesView.setItemDelegateForColumn(
            self.solidSpeciesModel.columnCount() - 1, None
        )
        self.solidSpeciesModel.removeColumns(position, removed_rows)
        self.solidSpeciesView.setItemDelegateForColumn(
            self.solidSpeciesModel.columnCount() - 1,
            ComboBoxDelegate(
                self, self.solidSpeciesView, self.compModel._data["Name"].tolist()
            ),
        )

    def updateSpecies(self):
        """
        Handles the updating species model due to changes in the number of species present.
        """
        new_value = self.numSpecies.value()
        if self.speciesModel.rowCount() < new_value:
            added_rows = new_value - self.speciesModel.rowCount()
            self.undostack.push(
                AddSpeciesRows(
                    self.speciesModel,
                    self.numSpecies,
                    self.speciesModel.rowCount() - 1,
                    added_rows,
                    update=False,
                )
            )
        elif self.speciesModel.rowCount() > new_value:
            removed_rows = self.speciesModel.rowCount() - new_value
            self.undostack.push(
                RemoveSpeciesRows(
                    self.speciesModel,
                    self.numSpecies,
                    self.speciesModel.rowCount(),
                    removed_rows,
                    update=False,
                )
            )
        else:
            pass

    def updateSolid(self, s):
        """
        Handles the updating solid species model due to changes in the number of solid phases present.
        """
        if self.solidSpeciesModel.rowCount() < s:
            added_rows = s - self.solidSpeciesModel.rowCount()
            self.undostack.push(
                AddSpeciesRows(
                    self.solidSpeciesModel,
                    self.numPhases,
                    self.solidSpeciesModel.rowCount() - 1,
                    added_rows,
                    update=False,
                )
            )
        elif self.solidSpeciesModel.rowCount() > s:
            removed_rows = self.solidSpeciesModel.rowCount() - s
            self.undostack.push(
                RemoveSpeciesRows(
                    self.solidSpeciesModel,
                    self.numPhases,
                    self.solidSpeciesModel.rowCount(),
                    removed_rows,
                    update=False,
                )
            )
        else:
            pass

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

    def insertCompAbove(self):
        if self.compView.selectedIndexes():
            row = self.compView.selectedIndexes()[0].row()
        else:
            row = 0
        self.compModel.insertRows(row - 1, 1)
        self.addSpeciesComp(row + 8, 1)
        self.concModel.insertRows(row - 1)

        self.numComp.setValue(self.numComp.value() + 1)
        self.compView.selectRow(row)

    def insertCompBelow(self):
        if self.compView.selectedIndexes():
            row = self.compView.selectedIndexes()[0].row() + 1
        else:
            row = self.compModel.rowCount() + 1
        self.compModel.insertRows(row - 1, 1)
        self.addSpeciesComp(row + 7, 1)
        self.concModel.insertRows(row - 1)

        self.numComp.setValue(self.numComp.value() + 1)
        self.compView.selectRow(row)

    def removeComp(self):
        if self.compView.selectedIndexes() and self.compModel.rowCount() > 1:
            if (
                QMessageBox.question(
                    self,
                    "Deleting Component",
                    "Are you sure you want to delete the selected component?",
                )
                == QMessageBox.Yes
            ):
                row = self.compView.selectedIndexes()[0].row() + 1
                self.compModel.removeRows(row, 1)

                self.removeSpeciesComp(row + 8, 1)
                self.concModel.removeRows(row)

                self.numComp.setValue(self.numComp.value() - 1)

    def moveCompUp(self):
        if self.compView.selectedIndexes():
            current_ind_comp = self.indComp.currentData(0)
            row = self.compView.selectedIndexes()[0].row()
            if row == 0:
                return

            self.speciesModel.swapColumns(row + 8, row + 7)
            self.solidSpeciesModel.swapColumns(row + 8, row + 7)
            self.concModel.swapRows(row, row - 1)
            self.compModel.swapRows(row, row - 1)
            self.compView.selectRow(row - 1)

            self.updateCompName()

            self.indComp.setCurrentIndex(self.indComp.findData(current_ind_comp, 0))

    def moveCompDown(self):
        if self.compView.selectedIndexes():
            current_ind_comp = self.indComp.currentData(0)
            row = self.compView.selectedIndexes()[0].row()
            if row == self.compModel.rowCount() - 1:
                return

            self.speciesModel.swapColumns(row + 8, row + 9)
            self.solidSpeciesModel.swapColumns(row + 8, row + 9)
            self.concModel.swapRows(row, row + 1)
            self.compModel.swapRows(row, row + 1)
            self.compView.selectRow(row + 1)

            self.updateCompName()

            self.indComp.setCurrentIndex(self.indComp.findData(current_ind_comp, 0))

    def insertSpeciesAbove(self):
        if self.tablesTab.currentIndex() == 0:
            if self.speciesView.selectedIndexes():
                row = self.speciesView.selectedIndexes()[0].row()
            else:
                row = 0
            self.undostack.push(
                AddSpeciesRows(self.speciesModel, self.numSpecies, row - 1, 1)
            )
            self.speciesView.selectRow(row)
        elif self.tablesTab.currentIndex() == 1:
            if self.solidSpeciesView.selectedIndexes():
                row = self.solidSpeciesView.selectedIndexes()[0].row()
            else:
                row = 0
            self.undostack.push(
                AddSpeciesRows(self.solidSpeciesModel, self.numPhases, row - 1, 1)
            )
            self.solidSpeciesView.selectRow(row)
        else:
            pass

    def insertSpeciesBelow(self):
        if self.tablesTab.currentIndex() == 0:
            if self.speciesView.selectedIndexes():
                row = self.speciesView.selectedIndexes()[0].row()
            else:
                row = self.speciesModel.rowCount()
            self.undostack.push(
                AddSpeciesRows(self.speciesModel, self.numSpecies, row, 1)
            )
            self.speciesView.selectRow(row + 1)
        elif self.tablesTab.currentIndex() == 1:
            if self.solidSpeciesView.selectedIndexes():
                row = self.solidSpeciesView.selectedIndexes()[0].row()
            else:
                row = self.solidSpeciesModel.rowCount()

            self.undostack.push(
                AddSpeciesRows(self.solidSpeciesModel, self.numPhases, row, 1)
            )
            self.speciesView.selectRow(row + 1)
        else:
            pass

    def removeSpecies(self):
        if self.tablesTab.currentIndex() == 0:
            if self.speciesView.selectedIndexes() and self.speciesModel.rowCount() > 1:
                if (
                    QMessageBox.question(
                        self,
                        "Deleting Species",
                        "Are you sure you want to delete the selected species?",
                    )
                    == QMessageBox.Yes
                ):
                    self.undostack.push(
                        RemoveSpeciesRows(
                            self.speciesModel,
                            self.numSpecies,
                            self.speciesView.selectedIndexes()[0].row() + 1,
                            1,
                        )
                    )
        elif self.tablesTab.currentIndex() == 1:
            if self.solidSpeciesView.selectedIndexes():
                if (
                    QMessageBox.question(
                        self,
                        "Deleting Species",
                        "Are you sure you want to delete the selected species?",
                    )
                    == QMessageBox.Yes
                ):
                    self.undostack.push(
                        RemoveSpeciesRows(
                            self.solidSpeciesModel,
                            self.numPhases,
                            self.solidSpeciesView.selectedIndexes()[0].row() + 1,
                            1,
                        )
                    )
        else:
            pass

    def moveSpeciesUp(self):
        if self.tablesTab.currentIndex() == 0:
            if self.speciesView.selectedIndexes():
                row = self.speciesView.selectedIndexes()[0].row()
                self.speciesModel.swapRows(row, row - 1)
                self.speciesView.selectRow(row - 1)
        elif self.tablesTab.currentIndex() == 1:
            if self.solidSpeciesView.selectedIndexes():
                row = self.solidSpeciesView.selectedIndexes()[0].row()
                self.solidSpeciesModel.swapRows(row, row - 1)
                self.solidSpeciesView.selectRow(row - 1)
        else:
            pass

    def moveSpeciesDown(self):
        if self.tablesTab.currentIndex() == 0:
            if self.speciesView.selectedIndexes():
                row = self.speciesView.selectedIndexes()[0].row()
                self.speciesModel.swapRows(row, row + 1)
                self.speciesView.selectRow(row + 1)
        elif self.tablesTab.currentIndex() == 1:
            if self.solidSpeciesView.selectedIndexes():
                row = self.solidSpeciesView.selectedIndexes()[0].row()
                self.solidSpeciesModel.swapRows(row, row + 1)
                self.solidSpeciesView.selectRow(row + 1)
        else:
            pass

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
        worker.signals.finished.connect(self.workerComplete)
        worker.signals.result.connect(self.storeResults)
        worker.signals.log.connect(self.logger)
        worker.signals.aborted.connect(self.aborted)

        # Execute
        self.threadpool.start(worker)

    def workerComplete(self):
        self.calcButton.setEnabled(True)
        self.plotDistButton.setEnabled(True)
        self.exportButton.setEnabled(True)
        self.actionExport_Results.setEnabled(True)
        self.actionPlot_Results.setEnabled(True)
        info_dialog = CompletedCalculation(succesful=True)
        info_dialog.exec()

    def aborted(self, error):
        self.consoleOutput.append("### ERROR ###")
        self.consoleOutput.append(error)
        self.consoleOutput.append("### ABORTED ###")

        self.calcButton.setEnabled(True)
        info_dialog = CompletedCalculation(succesful=False)
        info_dialog.exec()

    def logger(self, log):
        self.consoleOutput.append(log)

    def imodeUpdater(self, imode):
        """
        Enables and disables Debye-Huckle parameters fields
        while making it clear grayingout also the corresponding
        fields in the modelviews
        """
        if imode == 1:
            for field in self.imode_fields:
                field.setEnabled(True)

            self.speciesView.model().setColumnReadOnly(range(4, 8), False)
            self.solidSpeciesView.model().setColumnReadOnly(range(4, 8), False)

        else:
            for field in self.imode_fields:
                field.setEnabled(False)

            self.speciesView.model().setColumnReadOnly(range(4, 8), True)
            self.solidSpeciesView.model().setColumnReadOnly(range(4, 8), True)

    def exportDist(self):
        """
        Export calculated distribution in csv/excel format
        """
        if self.ExportWindow is None:
            self.ExportWindow = ExportWindow(self)
        else:
            self.ExportWindow.result = self.result
        self.ExportWindow.show()

    def storeResults(self, data, name):
        """
        Store result for exporting.
        """
        self.result[name] = data

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
        self.initialLog_label.setText(f"Initial -log[{self.indComp.currentText()}]:")
        self.finalLog_label.setText(f"Final -log[f{self.indComp.currentText()}]:")

        self.logInc_label.setText(f"-log[{self.indComp.currentText()}] Increment:")

    def relErrorsUpdater(self, checked):
        """
        If relative errors aren't requested
        gray out the corresponding columns in tableviews.
        """
        if checked:
            self.speciesView.model().setColumnReadOnly([3], False)
            self.solidSpeciesView.model().setColumnReadOnly([3], False)
            self.dmode1_concView.model().setColumnReadOnly([2, 3], False)
            self.dmode0_concView.model().setColumnReadOnly([2, 3], False)
        else:
            # print(self.speciesView.model())
            # print(self.solidSpeciesView.model())
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
        self.settings.setValue("mainwindow/geometry", self.saveGeometry())

        # Close any secondary window still open
        if self.ExportWindow:
            self.ExportWindow.close()
        if self.PlotWindow:
            self.PlotWindow.close()

        event.accept()

    def check_solid_presence(self):
        if self.solidSpeciesModel.rowCount() == 0:
            self.solidSpeciesView.setEnabled(False)
        else:
            self.solidSpeciesView.setEnabled(True)

    def displayUncertaintyInfo(self):
        UncertaintyInfoDialog(parent=self).exec()

    def displayIonicStrengthInfo(self):
        IonicStrengthInfoDialog(parent=self).exec()


def value_or_problem(d: dict, field: str, default, message: str, problems: list[str]):
    value = d.get(field)
    if value is None:
        value = default
        problems.append(message + f" ({field})")
    return value
