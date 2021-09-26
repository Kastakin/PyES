import sys
from itertools import cycle
from re import match

import pyqtgraph as pg
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QInputDialog, QMainWindow

from ui.PyES4_pyqtgraphPlotExport import Ui_PlotWindow

# Setup white background and black axis for the plot
# THIS NEEDS TO BE DONE BOFORE LOADING THE UI FILE
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

# Colour cycle to use for plotting currencies.
BREWER12PAIRED = cycle(
    [
        "#ebac23",
        "#b80058",
        "#008cf9",
        "#006e00",
        "#00bbad",
        "#d163e6",
        "#b24502",
        "#ff9287",
        "#5954d6",
        "#00c6f8",
        "#878500",
        "#00a76c",
    ]
)


class PlotWindow(QMainWindow, Ui_PlotWindow):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)

        # Inherit the required informations from the primary window
        if parent.dmode.currentIndex() == 0:
            self.distribution = False
        else:
            self.distribution = True

        self.result = parent.result["species_distribution"]
        self.comps = parent.result["comp_info"]
        if self.distribution:
            self.indipendent_comp_name = parent.indComp.currentText()
        self.comp_names = list(self.comps.index)

        # Get values for the x from the index
        self.x = self.result.index.get_level_values(0)

        # Store a reference to lines on the plot, and items in our
        # data viewer we can update rather than redraw.
        self._data_lines = dict()
        self._data_colors = dict()
        self._data_visible = []

        # Initialize a Model for species
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Species"])
        self.model.itemChanged.connect(self.check_checked_state)

        self.tableView.setModel(self.model)

        # Each colum holds a checkbox and the species name
        for column in self.result.columns:
            item = QStandardItem()
            item.setText(column)
            item.setForeground(QBrush(QColor(self.get_species_color(column))))
            item.setColumnCount(2)
            item.setCheckable(True)
            self.model.appendRow([item])

        # Resize column to newly added species
        self.tableView.resizeColumnToContents(0)

        self.graphWidget.setTitle("Distribution of Species")
        
        self.graphWidget.setLabel(
            "left",
            text="Concentration [mol/l]",
        )
        if self.distribution:
            self.graphWidget.setLabel(
                "bottom",
                text="Indipendent Component [-log[{}]]".format(self.indipendent_comp_name),
            )
        else:
            self.graphWidget.setLabel(
                "bottom",
                text="Volume of Titrant [l]",
            )

        self.graphWidget.enableAutoRange()

        self.legend = pg.LegendItem()
        self.legend.setParentItem((self.graphWidget.graphicsItem()))

    def check_checked_state(self, i):
        if not i.isCheckable():  # Skip data columns.
            return

        species = i.text()
        checked = i.checkState() == Qt.Checked

        if species in self._data_visible:
            if not checked:
                self._data_visible.remove(species)
                self.redraw()
                if self._data_visible == []:
                    self.graphWidget.clear()
                    self.legend = pg.LegendItem()
                self.legend.setParentItem((self.graphWidget.graphicsItem()))
        else:
            if checked:
                self._data_visible.append(species)
                self.redraw()

    def get_species_color(self, species):
        if species not in self._data_colors:
            self._data_colors[species] = next(BREWER12PAIRED)

        return self._data_colors[species]

    def redraw(self):
        y_min, y_max = sys.maxsize, 0
        x_min, x_max = min(self.x), max(self.x)

        for species in self.result.columns:
            values = self.result[species].to_numpy(dtype=float)
            if species in self._data_visible:
                if species not in self._data_lines:
                    self._data_lines[species] = self.graphWidget.plot(
                        self.x,
                        values,
                        pen=pg.mkPen(self.get_species_color(species), width=2),
                        name=species,
                    )
                    self.legend.addItem(self._data_lines[species], species)
                else:
                    self._data_lines[species].setData(self.x, values)

                y_min, y_max = min(y_min, *values), max(y_max, *values)
            else:
                if species in self._data_lines:
                    self.legend.removeItem(self._data_lines[species])
                    self._data_lines[species].clear()
                    self._data_lines.pop(species)

        self.graphWidget.setLimits(
            yMin=y_min * 0.5, yMax=y_max * 1.1, xMin=x_min - 0.25, xMax=x_max + 0.25
        )

    def selectAll(self):
        """
        Select all species.
        """
        for row in range(self.model.rowCount()):
            item = self.model.item(row)
            if item.checkState() != Qt.Checked:
                item.setCheckState(Qt.Checked)

    def deselectAll(self):
        """
        Deselect all species.
        """
        for row in range(self.model.rowCount()):
            item = self.model.item(row)
            if item.checkState() == Qt.Checked:
                item.setCheckState(Qt.Unchecked)

    def filterSpecies(self):
        """
        Select only species that contain some components.
        """
        choice, ok = QInputDialog.getItem(
            self, "Pick Component", "Component:", self.comp_names
        )
        if ok:
            self.deselectAll()
            for row in range(self.model.rowCount()):
                item = self.model.item(row)
                if choice in item.text():
                    item.setCheckState(Qt.Checked)
