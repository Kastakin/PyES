# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyES_pyqtgraphPlotExport.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from pyqtgraph import *  # type: ignore
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        if not PlotWindow.objectName():
            PlotWindow.setObjectName("PlotWindow")
        PlotWindow.resize(800, 600)
        PlotWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(PlotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 5, 2, 2)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.select_all = QPushButton(self.widget_2)
        self.select_all.setObjectName("select_all")

        self.gridLayout.addWidget(self.select_all, 2, 0, 1, 1)

        self.tabWidget_2 = QTabWidget(self.widget_2)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy1)
        self.species = QWidget()
        self.species.setObjectName("species")
        self.horizontalLayout_4 = QHBoxLayout(self.species)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.speciesView = QTableView(self.species)
        self.speciesView.setObjectName("speciesView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.speciesView.sizePolicy().hasHeightForWidth())
        self.speciesView.setSizePolicy(sizePolicy2)
        self.speciesView.setAlternatingRowColors(True)
        self.speciesView.horizontalHeader().setVisible(False)

        self.horizontalLayout_4.addWidget(self.speciesView)

        self.tabWidget_2.addTab(self.species, "")
        self.solids = QWidget()
        self.solids.setObjectName("solids")
        self.horizontalLayout_3 = QHBoxLayout(self.solids)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.solidsView = QTableView(self.solids)
        self.solidsView.setObjectName("solidsView")
        sizePolicy2.setHeightForWidth(self.solidsView.sizePolicy().hasHeightForWidth())
        self.solidsView.setSizePolicy(sizePolicy2)
        self.solidsView.setAlternatingRowColors(True)
        self.solidsView.horizontalHeader().setVisible(False)

        self.horizontalLayout_3.addWidget(self.solidsView)

        self.tabWidget_2.addTab(self.solids, "")

        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 2)

        self.deselect_all = QPushButton(self.widget_2)
        self.deselect_all.setObjectName("deselect_all")

        self.gridLayout.addWidget(self.deselect_all, 2, 1, 1, 1)

        self.filter = QPushButton(self.widget_2)
        self.filter.setObjectName("filter")

        self.gridLayout.addWidget(self.filter, 3, 0, 1, 2)

        self.regions_check = QCheckBox(self.widget_2)
        self.regions_check.setObjectName("regions_check")

        self.gridLayout.addWidget(self.regions_check, 1, 0, 1, 2)

        self.verticalLayout.addWidget(self.widget_2)

        self.horizontalLayout.addWidget(self.widget)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.perc_tab = QWidget()
        self.perc_tab.setObjectName("perc_tab")
        self.verticalLayout_2 = QVBoxLayout(self.perc_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.perc_graph = PlotWidget(self.perc_tab)
        self.perc_graph.setObjectName("perc_graph")

        self.verticalLayout_2.addWidget(self.perc_graph)

        self.verticalLayout_2.setStretch(0, 1)
        self.tabWidget.addTab(self.perc_tab, "")
        self.conc_tab = QWidget()
        self.conc_tab.setObjectName("conc_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.conc_tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.conc_graph = PlotWidget(self.conc_tab)
        self.conc_graph.setObjectName("conc_graph")

        self.horizontalLayout_2.addWidget(self.conc_graph)

        self.tabWidget.addTab(self.conc_tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.horizontalLayout.setStretch(1, 1)
        PlotWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlotWindow)
        self.deselect_all.clicked.connect(PlotWindow.deselectAll)
        self.select_all.clicked.connect(PlotWindow.selectAll)
        self.filter.clicked.connect(PlotWindow.filterSpecies)
        self.regions_check.clicked.connect(PlotWindow.changeSolidsGraphics)

        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(PlotWindow)

    # setupUi

    def retranslateUi(self, PlotWindow):
        PlotWindow.setWindowTitle(
            QCoreApplication.translate("PlotWindow", "Export Plot", None)
        )
        self.select_all.setText(
            QCoreApplication.translate("PlotWindow", "Select All", None)
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.species),
            QCoreApplication.translate("PlotWindow", "Species", None),
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.solids),
            QCoreApplication.translate("PlotWindow", "Solids", None),
        )
        self.deselect_all.setText(
            QCoreApplication.translate("PlotWindow", "Deselect All", None)
        )
        self.filter.setText(QCoreApplication.translate("PlotWindow", "Filter", None))
        self.regions_check.setText(
            QCoreApplication.translate("PlotWindow", "Solids as regions", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.perc_tab),
            QCoreApplication.translate("PlotWindow", "Percentages", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.conc_tab),
            QCoreApplication.translate("PlotWindow", "Concentrations", None),
        )

    # retranslateUi
