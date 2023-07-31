import sys
import typing
from itertools import cycle

import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QInputDialog, QMainWindow
from ui.PyES_pyqtgraphPlotExport import Ui_PlotWindow
from viewmodels.delegate import ColorPickerDelegate

if typing.TYPE_CHECKING:
    from windows.window import MainWindow

# Setup white background and black axis for the plot
# THIS NEEDS TO BE DONE BOFORE LOADING THE UI FILE
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

PALETTE = [
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


class PlotWindow(QMainWindow, Ui_PlotWindow):
    def __init__(self, parent: "MainWindow"):
        super().__init__()
        self.setupUi(self)

        # Colour cycle to use for plotting species.
        self.color_palette = cycle(PALETTE)

        self.color_palette_solids = cycle(PALETTE)

        # Inherit the required informations from the primary window
        self.distribution = parent.dmode.currentIndex() == 1
        print(self.distribution)
        self.with_solids = "solid_distribution" in parent.result
        self.with_errors = parent.uncertaintyMode.isChecked()

        self.conc_result = parent.result["species_distribution"]
        self.perc_result = parent.result["species_percentages"]
        self.perc_result.columns = self.conc_result.columns

        if not self.with_errors:
            self.errors_check.setEnabled(False)

        self.conc_sd = parent.result["species_sigma"]
        self.solid_sd = parent.result["solid_sigma"]
        self.solid_sd.columns = [column + "_(s)" for column in self.solid_sd.columns]

        if self.with_solids:
            self.solid_conc_result = parent.result["solid_distribution"][
                [
                    column
                    for column in parent.result["solid_distribution"]
                    if not (column.startswith("Prec.") or column.startswith("SI"))
                ]
            ]
            self.solid_conc_result.columns = [
                column + "_(s)" for column in self.solid_conc_result.columns
            ]

            self.solid_perc_result = parent.result["solid_percentages"]
            self.solid_perc_result.columns = self.solid_conc_result.columns

        self.comps = parent.result["comp_info"]
        if self.distribution:
            self.independent_comp_name = parent.indComp.currentText()
        self.comp_names = list(self.comps.index)

        # Get values for the x from the index
        self.x = self.conc_result.index.get_level_values(0)

        # Store a reference to lines on the plot, and items in our
        # data viewer we can update rather than redraw.
        self._data_lines = dict()
        self._data_colors = dict()
        self._data_visible = []

        # Initialize a Model for species_conc
        self.speciesModel = QStandardItemModel()
        self.solidsModel = QStandardItemModel()
        self.speciesModel.setHorizontalHeaderLabels(["Species", "Color"])
        self.solidsModel.setHorizontalHeaderLabels(["Species", "Color"])
        self.speciesModel.itemChanged.connect(self.check_checked_state)
        self.solidsModel.itemChanged.connect(self.check_checked_state)

        self.speciesView.setModel(self.speciesModel)
        self.solidsView.setModel(self.solidsModel)

        self.speciesView.setItemDelegateForColumn(1, ColorPickerDelegate(self))
        self.solidsView.setItemDelegateForColumn(1, ColorPickerDelegate(self))

        # Each colum holds a checkbox and the species name
        for column in self.conc_result.columns:
            item = QStandardItem()
            item.setText(column)
            item.setColumnCount(2)
            item.setCheckable(True)
            item.setEditable(False)

            item2 = QStandardItem()
            item2.setText(self.get_species_color(column, new=True))
            self.speciesModel.appendRow([item, item2])

        if self.with_solids:
            for column in self.solid_conc_result.columns:
                item = QStandardItem()
                item.setText(column)
                item.setColumnCount(2)
                item.setCheckable(True)
                item.setEditable(False)

                item2 = QStandardItem()
                item2.setText(self.get_solids_color(column, new=True))
                self.solidsModel.appendRow([item, item2])

        # Resize column to newly added species
        # self.speciesView.resizeColumnsToContents()
        self.speciesView.resizeColumnToContents(0)
        self.speciesView.setColumnWidth(1, self.speciesView.rowHeight(0))
        self.solidsView.resizeColumnToContents(0)
        self.solidsView.setColumnWidth(1, self.solidsView.rowHeight(0))

        self._initGraphs()

    def check_checked_state(self, i):
        if i.isCheckable():  # Skip data columns.
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
        else:
            self.redraw()

    def get_species_color(self, species, new=False):
        if new:
            color = next(self.color_palette)
        else:
            color = self.speciesModel.item(
                self.speciesModel.findItems(species, Qt.MatchFlag.MatchExactly, 0)[0]
                .index()
                .row(),
                1,
            ).text()

        return color

    def get_solids_color(self, solids, new=False):
        if new:
            color = next(self.color_palette_solids)
        else:
            color = self.solidsModel.item(
                self.solidsModel.findItems(solids, Qt.MatchFlag.MatchExactly, 0)[0]
                .index()
                .row(),
                1,
            ).text()

        return color

    def redraw(self):
        conc_y_min, conc_y_max = 0, sys.maxsize
        perc_y_min, perc_y_max = 0, sys.maxsize
        x_min, x_max = min(self.x), max(self.x)

        for name in self.conc_result.columns:
            values = [
                self.conc_result[name].to_numpy(dtype=float),
                self.perc_result[name].to_numpy(dtype=float),
            ]
            if self.with_errors and self.errors_check.isChecked():
                errors = [
                    self.conc_sd[name].to_numpy(dtype=float) + values[0],
                    -self.conc_sd[name].to_numpy(dtype=float) + values[0],
                ]
            if name in self._data_visible:
                line_style = Qt.PenStyle.SolidLine
                errorline_style = Qt.PenStyle.DashDotDotLine
                color = self.get_species_color(name)
                if name not in self._data_lines:
                    self._addPlotLines(values, name, color, line_style)
                    if self.with_errors and self.errors_check.isChecked():
                        self._addErrorLines(errors, name, color, errorline_style)
                else:
                    for i, plot in enumerate(self._data_lines[name]):
                        if i < 2:
                            plot.setPen(pg.mkPen(color, width=2, style=line_style))
                        else:
                            plot.setPen(pg.mkPen(color, width=2, style=errorline_style))

                conc_y_min, conc_y_max = min(conc_y_min, *values[0]), max(
                    conc_y_max, *values[0]
                )
                perc_y_min, perc_y_max = min(perc_y_min, *values[1]), max(
                    perc_y_max, *values[1]
                )
            else:
                if name in self._data_lines:
                    self._removePlotLines(name)
        if self.with_solids:
            for name in self.solid_conc_result.columns:
                if self.regions_check.isChecked():
                    solid_regions = np.reshape(
                        np.diff(
                            np.r_[0, (self.solid_conc_result[name] > 0).astype(int), 0]
                        ).nonzero()[0],
                        (-1, 2),
                    )

                    if name in self._data_visible:
                        color = self.get_solids_color(name) + "66"
                        if name not in self._data_lines:
                            self._addRegionLines(solid_regions, name, color)
                        else:
                            for plot in self._data_lines[name]:
                                for region in plot:
                                    region.setBrush(pg.mkBrush(color))
                    else:
                        if name in self._data_lines:
                            self._removeRegionLines(name)
                else:
                    values = [
                        self.solid_conc_result[name].to_numpy(dtype=float),
                        self.solid_perc_result[name].to_numpy(dtype=float),
                    ]
                    if self.with_errors and self.errors_check.isChecked():
                        errors = [
                            self.solid_sd[name].to_numpy(dtype=float) + values[0],
                            -self.solid_sd[name].to_numpy(dtype=float) + values[0],
                        ]
                    if name in self._data_visible:
                        line_style = Qt.PenStyle.DashLine
                        errorline_style = Qt.PenStyle.DashDotDotLine
                        color = self.get_solids_color(name)
                        if name not in self._data_lines:
                            self._addPlotLines(values, name, color, line_style)
                            if self.with_errors and self.errors_check.isChecked():
                                self._addErrorLines(
                                    errors, name, color, errorline_style
                                )
                        else:
                            for i, plot in enumerate(self._data_lines[name]):
                                if i < 2:
                                    plot.setPen(
                                        pg.mkPen(color, width=2, style=line_style)
                                    )
                                else:
                                    plot.setPen(
                                        pg.mkPen(color, width=2, style=errorline_style)
                                    )

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
                text=f"Independent Component -log[{self.independent_comp_name}]",
            )
            self.perc_graph.setLabel(
                "bottom",
                text=f"Independent Component -log[{self.independent_comp_name}]",
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

    def _removeErrorLines(self, name):
        for plot in self._data_lines[name][2:]:
            plot.clear()

    def _addPlotLines(self, values, name, color, line_style):
        self._data_lines[name] = [
            self.conc_graph.plot(
                self.x,
                values[0],
                pen=pg.mkPen(color, width=2, style=line_style),
                name=name,
            ),
            self.perc_graph.plot(
                self.x,
                values[1],
                pen=pg.mkPen(color, width=2, style=line_style),
                name=name,
            ),
        ]
        self._addLegendItem(name)

    def _addErrorLines(self, values, name, color, line_style):
        self._data_lines[name] += [
            self.conc_graph.plot(
                self.x,
                values[0],
                pen=pg.mkPen(color, width=2, style=line_style),
                name=name + "_ub_error",
            ),
            self.conc_graph.plot(
                self.x,
                values[1],
                pen=pg.mkPen(color, width=2, style=line_style),
                name=name + "_lb_error",
            ),
        ]

    def _removeRegionLines(self, name):
        for region in self._data_lines[name]:
            self.conc_graph.removeItem(region[0])
            self.perc_graph.removeItem(region[1])
        self._data_lines.pop(name)

    def _addRegionLines(self, solid_regions, name, color):
        regions_list = []
        for region in solid_regions:
            line_region_conc = pg.LinearRegionItem(
                values=[self.x[region[0]], self.x[region[1] - 1]],
                movable=False,
                pen=pg.mkPen(None),
                brush=pg.mkBrush(color),
            )
            line_region_perc = pg.LinearRegionItem(
                values=[self.x[region[0]], self.x[region[1] - 1]],
                movable=False,
                pen=pg.mkPen(None),
                brush=pg.mkBrush(color),
            )

            self.conc_graph.addItem(line_region_conc)
            self.perc_graph.addItem(line_region_perc)

            pg.InfLineLabel(
                line_region_conc.lines[1],
                name,
                position=0.75,
                rotateAxis=(1, 0),
                anchor=(1, 1),
                color="k",
            )
            pg.InfLineLabel(
                line_region_perc.lines[1],
                name,
                position=0.75,
                rotateAxis=(1, 0),
                anchor=(1, 1),
                color="k",
            )

            regions_list.append([line_region_conc, line_region_perc])

        self._data_lines[name] = regions_list

    def _addLegendItem(self, name):
        self.conc_legend.addItem(self._data_lines[name][0], name)
        self.perc_legend.addItem(self._data_lines[name][1], name)

    def _removeLegendItem(self, name):
        self.conc_legend.removeItem(name)
        self.perc_legend.removeItem(name)

    def changeSolidsGraphics(self):
        if self.regions_check.isChecked():
            for name in self.solid_conc_result.columns:
                if name in self._data_visible:
                    self._removePlotLines(name)
        else:
            for name in self.solid_conc_result.columns:
                if name in self._data_visible:
                    self._removeRegionLines(name)

        self.redraw()

    def changeErrorsGraphics(self):
        if self.errors_check.isChecked():
            for name in self.conc_result.columns:
                if name in self._data_visible:
                    values = [
                        self.conc_result[name].to_numpy(dtype=float),
                        self.perc_result[name].to_numpy(dtype=float),
                    ]
                    errors = [
                        self.conc_sd[name].to_numpy(dtype=float) + values[0],
                        -self.conc_sd[name].to_numpy(dtype=float) + values[0],
                    ]
                    color = self.get_species_color(name)

                    self._addErrorLines(
                        errors, name, color, line_style=Qt.PenStyle.DashDotDotLine
                    )
            for name in self.solid_conc_result.columns:
                if name in self._data_visible:
                    values = [
                        self.solid_conc_result[name].to_numpy(dtype=float),
                        self.solid_perc_result[name].to_numpy(dtype=float),
                    ]
                    errors = [
                        self.solid_sd[name].to_numpy(dtype=float) + values[0],
                        -self.solid_sd[name].to_numpy(dtype=float) + values[0],
                    ]
                    color = self.get_solids_color(name)

                    self._addErrorLines(
                        errors, name, color, line_style=Qt.PenStyle.DashDotDotLine
                    )
        else:
            for name in list(self.solid_conc_result.columns) + list(
                self.conc_result.columns
            ):
                if name in self._data_visible:
                    self._removeErrorLines(name)

        self.redraw()

    def selectAll(self):
        """
        Select all species.
        """
        for row in range(self.speciesModel.rowCount()):
            item = self.speciesModel.item(row)
            if item.checkState() != Qt.Checked:
                item.setCheckState(Qt.Checked)

        for row in range(self.solidsModel.rowCount()):
            item = self.solidsModel.item(row)
            if item.checkState() != Qt.Checked:
                item.setCheckState(Qt.Checked)

    def deselectAll(self):
        """
        Deselect all species.
        """
        for row in range(self.speciesModel.rowCount()):
            item = self.speciesModel.item(row)
            if item.checkState() == Qt.Checked:
                item.setCheckState(Qt.Unchecked)

        for row in range(self.solidsModel.rowCount()):
            item = self.solidsModel.item(row)
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
            for row in range(self.speciesModel.rowCount()):
                item = self.speciesModel.item(row)
                if choice in item.text():
                    item.setCheckState(Qt.Checked)

            for row in range(self.solidsModel.rowCount()):
                item = self.solidsModel.item(row)
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
