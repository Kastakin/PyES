import sys
from itertools import cycle

import pandas as pd
import pyqtgraph as pg
from MainWindow import MainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QInputDialog, QMainWindow
from ui.PyES_pyqtgraphPlotExport import Ui_PlotWindow

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
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.setupUi(self)
        # Inherit the required informations from the primary window
        if parent.dmode.currentIndex() == 0:
            self.distribution = False
        else:
            self.distribution = True

        if "solid_distribution" in parent.result:
            self.with_solids = True
        else:
            self.with_solids = False

        conc_species_result = parent.result["species_distribution"]
        perc_species_result = parent.result["species_percentages"]
        perc_species_result.columns = conc_species_result.columns

        if self.with_solids:
            conc_solid_result = parent.result["solid_distribution"]
            conc_solid_result.columns = [
                column + "_(s)" for column in conc_solid_result.columns
            ]
            perc_solid_result = parent.result["solid_percentages"]
            perc_solid_result.columns = conc_solid_result.columns
            self.conc_result = pd.concat(
                (conc_species_result, conc_solid_result), axis=1
            )
            self.perc_result = pd.concat(
                (perc_species_result, perc_solid_result), axis=1
            )
        else:
            self.conc_result = conc_species_result
            self.perc_result = perc_species_result

        self.comps = parent.result["comp_info"]
        if self.distribution:
            self.indipendent_comp_name = parent.indComp.currentText()
        self.comp_names = list(self.comps.index)

        # Get values for the x from the index
        self.x = conc_species_result.index.get_level_values(0)

        # Store a reference to lines on the plot, and items in our
        # data viewer we can update rather than redraw.
        self._data_lines = dict()
        self._data_colors = dict()
        self._data_visible = []

        # Initialize a Model for species_conc
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Species"])
        self.model.itemChanged.connect(self.check_checked_state)

        self.tableView.setModel(self.model)

        # Each colum holds a checkbox and the species name
        for column in conc_species_result.columns:
            item = QStandardItem()
            item.setText(column)
            item.setForeground(QBrush(QColor(self.get_species_color(column))))
            item.setColumnCount(2)
            item.setCheckable(True)
            self.model.appendRow([item])

        if self.with_solids:
            for column in conc_solid_result.columns:
                item = QStandardItem()
                item.setText(column)
                item.setForeground(QBrush(QColor(self.get_species_color(column))))
                item.setColumnCount(2)
                item.setCheckable(True)
                self.model.appendRow([item])

        # Resize column to newly added species
        self.tableView.resizeColumnToContents(0)

        self._initGraphs()

    def check_checked_state(self, i):
        if not i.isCheckable():  # Skip data columns.
            return

        name = i.text()
        checked = i.checkState() == Qt.Checked

        if name in self._data_visible:
            if not checked:
                self._data_visible.remove(name)
                self.redraw()
                if self._data_visible == []:
                    self._resetGraphs()

        else:
            if checked:
                self._data_visible.append(name)
                self.redraw()

    def get_species_color(self, species):
        if species not in self._data_colors:
            self._data_colors[species] = next(BREWER12PAIRED)

        return self._data_colors[species]

    def redraw(self):
        conc_y_min, conc_y_max = 0, sys.maxsize
        perc_y_min, perc_y_max = 0, sys.maxsize
        x_min, x_max = min(self.x), max(self.x)

        for name in self.conc_result.columns:
            line_style = Qt.DashLine if name.endswith("(s)") else Qt.SolidLine
            values = [
                self.conc_result[name].to_numpy(dtype=float),
                self.perc_result[name].to_numpy(dtype=float),
            ]
            if name in self._data_visible:
                if name not in self._data_lines:
                    self._addPlotLines(values, name, line_style)
                else:
                    for i, plot in enumerate(self._data_lines[name]):
                        plot.setData(self.x, values[i])

                conc_y_min, conc_y_max = min(conc_y_min, *values[0]), max(
                    conc_y_max, *values[0]
                )
                perc_y_min, perc_y_max = min(perc_y_min, *values[1]), max(
                    perc_y_max, *values[1]
                )
            else:
                if name in self._data_lines:
                    self._removePlotLines(name)

        self.conc_graph.setLimits(
            yMin=conc_y_min * 0.5,
            yMax=conc_y_max * 1.1,
            xMin=x_min - 0.25,
            xMax=x_max + 0.25,
        )
        self.perc_graph.setLimits(
            yMin=perc_y_min * 0.5,
            yMax=perc_y_max * 1.1,
            xMin=x_min - 0.25,
            xMax=x_max + 0.25,
        )

    def _initGraphs(self):
        self.conc_graph.setTitle("Distribution of Species")
        self.conc_graph.setLabel(
            "left",
            text="Concentration [mol/l]",
        )

        self.perc_graph.setTitle("Relative Percentage")
        self.perc_graph.setLabel(
            "left",
            text="Percentage %",
        )

        if self.distribution:
            self.conc_graph.setLabel(
                "bottom",
                text="Indipendent Component -log[{}]".format(
                    self.indipendent_comp_name
                ),
            )
            self.perc_graph.setLabel(
                "bottom",
                text="Indipendent Component -log[{}]".format(
                    self.indipendent_comp_name
                ),
            )
        else:
            self.conc_graph.setLabel(
                "bottom",
                text="Volume of Titrant [l]",
            )
            self.perc_graph.setLabel(
                "bottom",
                text="Volume of Titrant [l]",
            )

        self.conc_graph.enableAutoRange()
        self.perc_graph.enableAutoRange()

        self._createLegend()

    def _removePlotLines(self, name):
        self._removeLegendItem(name)
        for plot in self._data_lines[name]:
            plot.clear()
        self._data_lines.pop(name)

    def _addPlotLines(self, values, name, line_style):
        self._data_lines[name] = [
            self.conc_graph.plot(
                self.x,
                values[0],
                pen=pg.mkPen(self.get_species_color(name), width=2, style=line_style),
                name=name,
            ),
            self.perc_graph.plot(
                self.x,
                values[1],
                pen=pg.mkPen(self.get_species_color(name), width=2, style=line_style),
                name=name,
            ),
        ]
        self._addLegendItem(name)

    def _addLegendItem(self, name):
        self.conc_legend.addItem(self._data_lines[name][0], name)
        self.perc_legend.addItem(self._data_lines[name][1], name)

    def _removeLegendItem(self, name):
        self.conc_legend.removeItem(self._data_lines[name][0])
        self.perc_legend.removeItem(self._data_lines[name][1])

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

    def _createLegend(self):
        self.conc_legend = pg.LegendItem()
        self.perc_legend = pg.LegendItem()
        self.conc_legend.setParentItem((self.conc_graph.graphicsItem()))
        self.perc_legend.setParentItem((self.perc_graph.graphicsItem()))

    def _resetGraphs(self):
        self.conc_graph.clear()
        self.perc_graph.clear()
        self.conc_legend = pg.LegendItem()
        self.perc_legend = pg.LegendItem()
        self.conc_legend.setParentItem((self.conc_graph.graphicsItem()))
        self.perc_legend.setParentItem((self.perc_graph.graphicsItem()))
