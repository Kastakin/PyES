# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lorenzo/Coding/SSSC/src/main/python/ui/sssc_plotExport.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_plotWindow(object):
    def setupUi(self, plotWindow):
        plotWindow.setObjectName("plotWindow")
        plotWindow.resize(765, 550)
        plotWindow.setMinimumSize(QtCore.QSize(765, 550))
        self.horizontalLayout = QtWidgets.QHBoxLayout(plotWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(plotWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.exportButton = QtWidgets.QPushButton(self.widget)
        self.exportButton.setObjectName("exportButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.exportButton)
        self.horizontalLayout.addWidget(self.widget)
        self.line = QtWidgets.QFrame(plotWindow)
        self.line.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.plot = WidgetPlot(plotWindow)
        self.plot.setObjectName("plot")
        self.horizontalLayout.addWidget(self.plot)

        self.retranslateUi(plotWindow)
        self.exportButton.clicked.connect(plotWindow.exportPlot)
        QtCore.QMetaObject.connectSlotsByName(plotWindow)

    def retranslateUi(self, plotWindow):
        _translate = QtCore.QCoreApplication.translate
        plotWindow.setWindowTitle(_translate("plotWindow", "Export Plot..."))
        self.label.setText(_translate("plotWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Options:</span></p></body></html>"))
        self.exportButton.setText(_translate("plotWindow", "Export"))
from canvas import WidgetPlot
