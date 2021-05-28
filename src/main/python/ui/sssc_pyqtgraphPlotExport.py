# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lorenzo/Coding/SSSC/src/main/python/ui/sssc_pyqtgraphPlotExport.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        PlotWindow.setObjectName("PlotWindow")
        PlotWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PlotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.deselect_all = QtWidgets.QPushButton(self.widget_2)
        self.deselect_all.setObjectName("deselect_all")
        self.gridLayout.addWidget(self.deselect_all, 0, 1, 1, 1)
        self.select_all = QtWidgets.QPushButton(self.widget_2)
        self.select_all.setObjectName("select_all")
        self.gridLayout.addWidget(self.select_all, 0, 0, 1, 1)
        self.filter = QtWidgets.QPushButton(self.widget_2)
        self.filter.setObjectName("filter")
        self.gridLayout.addWidget(self.filter, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setObjectName("graphWidget")
        self.horizontalLayout.addWidget(self.graphWidget)
        PlotWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlotWindow)
        self.select_all.clicked.connect(PlotWindow.selectAll)
        self.deselect_all.clicked.connect(PlotWindow.deselectAll)
        self.filter.clicked.connect(PlotWindow.filterSpecies)
        QtCore.QMetaObject.connectSlotsByName(PlotWindow)

    def retranslateUi(self, PlotWindow):
        _translate = QtCore.QCoreApplication.translate
        PlotWindow.setWindowTitle(_translate("PlotWindow", "Export Plot"))
        self.deselect_all.setText(_translate("PlotWindow", "Deselect All"))
        self.select_all.setText(_translate("PlotWindow", "Select All"))
        self.filter.setText(_translate("PlotWindow", "Filter"))
from pyqtgraph import PlotWidget
