# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lorenzo/Coding/SSSC/src/main/python/ui/sssc_dataExport.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExportWindow(object):
    def setupUi(self, ExportWindow):
        ExportWindow.setObjectName("ExportWindow")
        ExportWindow.resize(498, 237)
        ExportWindow.setMinimumSize(QtCore.QSize(498, 237))
        ExportWindow.setMaximumSize(QtCore.QSize(498, 237))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/application-export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExportWindow.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(ExportWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.export_type = QtWidgets.QTabWidget(ExportWindow)
        self.export_type.setObjectName("export_type")
        self.excel_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excel_tab.sizePolicy().hasHeightForWidth())
        self.excel_tab.setSizePolicy(sizePolicy)
        self.excel_tab.setObjectName("excel_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.excel_tab)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.excel_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(1, 5, 1, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.formLayout = QtWidgets.QFormLayout(self.widget_2)
        self.formLayout.setContentsMargins(5, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setObjectName("formLayout")
        self.input_check = QtWidgets.QCheckBox(self.widget_2)
        self.input_check.setChecked(True)
        self.input_check.setObjectName("input_check")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.input_check)
        self.distribution_check = QtWidgets.QCheckBox(self.widget_2)
        self.distribution_check.setObjectName("distribution_check")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.distribution_check)
        self.perc_check = QtWidgets.QCheckBox(self.widget_2)
        self.perc_check.setObjectName("perc_check")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.perc_check)
        self.adjlogb_check = QtWidgets.QCheckBox(self.widget_2)
        self.adjlogb_check.setObjectName("adjlogb_check")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.adjlogb_check)
        self.options_label = QtWidgets.QLabel(self.widget_2)
        self.options_label.setObjectName("options_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.options_label)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.export_button = QtWidgets.QPushButton(self.excel_tab)
        self.export_button.setEnabled(True)
        self.export_button.setAutoDefault(False)
        self.export_button.setDefault(False)
        self.export_button.setFlat(False)
        self.export_button.setObjectName("export_button")
        self.verticalLayout_2.addWidget(self.export_button)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/document-excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_type.addTab(self.excel_tab, icon1, "")
        self.csv_tab = QtWidgets.QWidget()
        self.csv_tab.setObjectName("csv_tab")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_type.addTab(self.csv_tab, icon2, "")
        self.verticalLayout.addWidget(self.export_type)

        self.retranslateUi(ExportWindow)
        self.export_type.setCurrentIndex(0)
        self.export_button.clicked.connect(ExportWindow.ExcelExport)
        QtCore.QMetaObject.connectSlotsByName(ExportWindow)

    def retranslateUi(self, ExportWindow):
        _translate = QtCore.QCoreApplication.translate
        ExportWindow.setWindowTitle(_translate("ExportWindow", "Export Results"))
        self.input_check.setText(_translate("ExportWindow", "Input info"))
        self.distribution_check.setText(_translate("ExportWindow", "Distribution"))
        self.perc_check.setText(_translate("ExportWindow", "% with respect to component"))
        self.adjlogb_check.setText(_translate("ExportWindow", "Adjusted formation constants"))
        self.options_label.setText(_translate("ExportWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Options:</span></p></body></html>"))
        self.export_button.setText(_translate("ExportWindow", "Export"))
        self.export_type.setTabText(self.export_type.indexOf(self.excel_tab), _translate("ExportWindow", "Excel"))
        self.export_type.setTabText(self.export_type.indexOf(self.csv_tab), _translate("ExportWindow", "CSV"))
import resources_rc
