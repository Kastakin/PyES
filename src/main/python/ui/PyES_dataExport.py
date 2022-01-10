# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyES_dataExport.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import resources_rc

class Ui_ExportWindow(object):
    def setupUi(self, ExportWindow):
        if not ExportWindow.objectName():
            ExportWindow.setObjectName(u"ExportWindow")
        ExportWindow.resize(498, 237)
        ExportWindow.setMinimumSize(QSize(498, 237))
        icon = QIcon()
        icon.addFile(u":/icons/application-export.png", QSize(), QIcon.Normal, QIcon.Off)
        ExportWindow.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(ExportWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.export_type = QTabWidget(ExportWindow)
        self.export_type.setObjectName(u"export_type")
        self.excel_tab = QWidget()
        self.excel_tab.setObjectName(u"excel_tab")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excel_tab.sizePolicy().hasHeightForWidth())
        self.excel_tab.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.excel_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 10)
        self.widget_3 = QWidget(self.excel_tab)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 5, 1, 5)
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.formLayout = QFormLayout(self.widget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setContentsMargins(5, 0, 0, 0)
        self.input_check_excel = QCheckBox(self.widget_2)
        self.input_check_excel.setObjectName(u"input_check_excel")
        self.input_check_excel.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.input_check_excel)

        self.distribution_check_excel = QCheckBox(self.widget_2)
        self.distribution_check_excel.setObjectName(u"distribution_check_excel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.distribution_check_excel)

        self.perc_check_excel = QCheckBox(self.widget_2)
        self.perc_check_excel.setObjectName(u"perc_check_excel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.perc_check_excel)

        self.adjlogb_check_excel = QCheckBox(self.widget_2)
        self.adjlogb_check_excel.setObjectName(u"adjlogb_check_excel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.adjlogb_check_excel)

        self.options_label_excel = QLabel(self.widget_2)
        self.options_label_excel.setObjectName(u"options_label_excel")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.options_label_excel)

        self.errors_check_excel = QCheckBox(self.widget_2)
        self.errors_check_excel.setObjectName(u"errors_check_excel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.errors_check_excel)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.export_button_excel = QPushButton(self.excel_tab)
        self.export_button_excel.setObjectName(u"export_button_excel")
        self.export_button_excel.setEnabled(True)
        self.export_button_excel.setAutoDefault(False)
        self.export_button_excel.setFlat(False)

        self.verticalLayout_2.addWidget(self.export_button_excel)

        icon1 = QIcon()
        icon1.addFile(u":/icons/document-excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_type.addTab(self.excel_tab, icon1, "")
        self.csv_tab = QWidget()
        self.csv_tab.setObjectName(u"csv_tab")
        self.verticalLayout_3 = QVBoxLayout(self.csv_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 10)
        self.widget_4 = QWidget(self.csv_tab)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 5, 1, 5)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.formLayout_2 = QFormLayout(self.widget_5)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(3)
        self.formLayout_2.setContentsMargins(5, 0, 0, 0)
        self.input_check_csv = QCheckBox(self.widget_5)
        self.input_check_csv.setObjectName(u"input_check_csv")
        self.input_check_csv.setChecked(True)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.input_check_csv)

        self.distribution_check_csv = QCheckBox(self.widget_5)
        self.distribution_check_csv.setObjectName(u"distribution_check_csv")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.distribution_check_csv)

        self.perc_check_csv = QCheckBox(self.widget_5)
        self.perc_check_csv.setObjectName(u"perc_check_csv")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.perc_check_csv)

        self.adjlogb_check_csv = QCheckBox(self.widget_5)
        self.adjlogb_check_csv.setObjectName(u"adjlogb_check_csv")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.adjlogb_check_csv)

        self.options_label_csv = QLabel(self.widget_5)
        self.options_label_csv.setObjectName(u"options_label_csv")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.options_label_csv)

        self.errors_check_csv = QCheckBox(self.widget_5)
        self.errors_check_csv.setObjectName(u"errors_check_csv")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.errors_check_csv)


        self.horizontalLayout_2.addWidget(self.widget_5)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.export_button_csv = QPushButton(self.csv_tab)
        self.export_button_csv.setObjectName(u"export_button_csv")
        self.export_button_csv.setEnabled(True)
        self.export_button_csv.setAutoDefault(False)
        self.export_button_csv.setFlat(False)

        self.verticalLayout_3.addWidget(self.export_button_csv)

        icon2 = QIcon()
        icon2.addFile(u":/icons/table.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_type.addTab(self.csv_tab, icon2, "")

        self.verticalLayout.addWidget(self.export_type)


        self.retranslateUi(ExportWindow)
        self.export_button_excel.clicked.connect(ExportWindow.ExcelExport)
        self.export_button_csv.clicked.connect(ExportWindow.CsvExport)

        self.export_type.setCurrentIndex(0)
        self.export_button_excel.setDefault(False)
        self.export_button_csv.setDefault(False)


        QMetaObject.connectSlotsByName(ExportWindow)
    # setupUi

    def retranslateUi(self, ExportWindow):
        ExportWindow.setWindowTitle(QCoreApplication.translate("ExportWindow", u"Export Results", None))
        self.input_check_excel.setText(QCoreApplication.translate("ExportWindow", u"Input info", None))
        self.distribution_check_excel.setText(QCoreApplication.translate("ExportWindow", u"Distribution", None))
        self.perc_check_excel.setText(QCoreApplication.translate("ExportWindow", u"% with respect to component", None))
        self.adjlogb_check_excel.setText(QCoreApplication.translate("ExportWindow", u"Adjusted formation constants", None))
        self.options_label_excel.setText(QCoreApplication.translate("ExportWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Options:</span></p></body></html>", None))
        self.errors_check_excel.setText(QCoreApplication.translate("ExportWindow", u"Std. Deviation of concentration", None))
        self.export_button_excel.setText(QCoreApplication.translate("ExportWindow", u"Export", None))
        self.export_type.setTabText(self.export_type.indexOf(self.excel_tab), QCoreApplication.translate("ExportWindow", u"Excel", None))
        self.input_check_csv.setText(QCoreApplication.translate("ExportWindow", u"Input info", None))
        self.distribution_check_csv.setText(QCoreApplication.translate("ExportWindow", u"Distribution", None))
        self.perc_check_csv.setText(QCoreApplication.translate("ExportWindow", u"% with respect to component", None))
        self.adjlogb_check_csv.setText(QCoreApplication.translate("ExportWindow", u"Adjusted formation constants", None))
        self.options_label_csv.setText(QCoreApplication.translate("ExportWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Options:</span></p></body></html>", None))
        self.errors_check_csv.setText(QCoreApplication.translate("ExportWindow", u"Std. Deviation of concentration", None))
        self.export_button_csv.setText(QCoreApplication.translate("ExportWindow", u"Export", None))
        self.export_type.setTabText(self.export_type.indexOf(self.csv_tab), QCoreApplication.translate("ExportWindow", u"CSV", None))
    # retranslateUi

