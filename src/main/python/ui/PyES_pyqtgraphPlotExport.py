# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyES_pyqtgraphPlotExport.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from pyqtgraph import *  # type: ignore

class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        if not PlotWindow.objectName():
            PlotWindow.setObjectName(u"PlotWindow")
        PlotWindow.resize(800, 600)
        self.centralwidget = QWidget(PlotWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 5, 2, 2)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy1)
        self.tableView.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.tableView)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.deselect_all = QPushButton(self.widget_2)
        self.deselect_all.setObjectName(u"deselect_all")

        self.gridLayout.addWidget(self.deselect_all, 0, 1, 1, 1)

        self.select_all = QPushButton(self.widget_2)
        self.select_all.setObjectName(u"select_all")

        self.gridLayout.addWidget(self.select_all, 0, 0, 1, 1)

        self.filter = QPushButton(self.widget_2)
        self.filter.setObjectName(u"filter")

        self.gridLayout.addWidget(self.filter, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.widget)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.conc_tab = QWidget()
        self.conc_tab.setObjectName(u"conc_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.conc_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.conc_graph = PlotWidget(self.conc_tab)
        self.conc_graph.setObjectName(u"conc_graph")

        self.horizontalLayout_2.addWidget(self.conc_graph)

        self.tabWidget.addTab(self.conc_tab, "")
        self.perc_tab = QWidget()
        self.perc_tab.setObjectName(u"perc_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.perc_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.widget_3 = QWidget(self.perc_tab)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.widget_3)

        self.perc_graph = PlotWidget(self.perc_tab)
        self.perc_graph.setObjectName(u"perc_graph")

        self.horizontalLayout_3.addWidget(self.perc_graph)

        self.tabWidget.addTab(self.perc_tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        PlotWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlotWindow)
        self.deselect_all.clicked.connect(PlotWindow.deselectAll)
        self.select_all.clicked.connect(PlotWindow.selectAll)
        self.filter.clicked.connect(PlotWindow.filterSpecies)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PlotWindow)
    # setupUi

    def retranslateUi(self, PlotWindow):
        PlotWindow.setWindowTitle(QCoreApplication.translate("PlotWindow", u"Export Plot", None))
        self.deselect_all.setText(QCoreApplication.translate("PlotWindow", u"Deselect All", None))
        self.select_all.setText(QCoreApplication.translate("PlotWindow", u"Select All", None))
        self.filter.setText(QCoreApplication.translate("PlotWindow", u"Filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.conc_tab), QCoreApplication.translate("PlotWindow", u"Concentrations", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.perc_tab), QCoreApplication.translate("PlotWindow", u"Percentages", None))
    # retranslateUi

