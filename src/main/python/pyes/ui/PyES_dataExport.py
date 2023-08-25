# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyES_dataExport.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import resources_rc
from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_ExportWindow(object):
    def setupUi(self, ExportWindow):
        if not ExportWindow.objectName():
            ExportWindow.setObjectName("ExportWindow")
        ExportWindow.resize(498, 237)
        ExportWindow.setMinimumSize(QSize(498, 237))
        icon = QIcon()
        icon.addFile(":/icons/application-export.png", QSize(), QIcon.Normal, QIcon.Off)
        ExportWindow.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(ExportWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.export_type = QTabWidget(ExportWindow)
        self.export_type.setObjectName("export_type")
        self.excel_tab = QWidget()
        self.excel_tab.setObjectName("excel_tab")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excel_tab.sizePolicy().hasHeightForWidth())
        self.excel_tab.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.excel_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 10)
        self.widget_3 = QWidget(self.excel_tab)
        self.widget_3.setObjectName("widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 5, 1, 5)
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.formLayout = QFormLayout(self.widget_2)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setContentsMargins(5, 0, 0, 0)
        self.input_check_excel = QCheckBox(self.widget_2)
        self.input_check_excel.setObjectName("input_check_excel")
        self.input_check_excel.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.input_check_excel)

        self.distribution_check_excel = QCheckBox(self.widget_2)
        self.distribution_check_excel.setObjectName("distribution_check_excel")

        self.formLayout.setWidget(
            2, QFormLayout.LabelRole, self.distribution_check_excel
        )

        self.perc_check_excel = QCheckBox(self.widget_2)
        self.perc_check_excel.setObjectName("perc_check_excel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.perc_check_excel)

        self.adjlogb_check_excel = QCheckBox(self.widget_2)
        self.adjlogb_check_excel.setObjectName("adjlogb_check_excel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.adjlogb_check_excel)

        self.options_label_excel = QLabel(self.widget_2)
        self.options_label_excel.setObjectName("options_label_excel")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.options_label_excel)

        self.errors_check_excel = QCheckBox(self.widget_2)
        self.errors_check_excel.setObjectName("errors_check_excel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.errors_check_excel)

        self.horizontalLayout.addWidget(self.widget_2)

        self.verticalLayout_2.addWidget(self.widget_3)

        self.export_button_excel = QPushButton(self.excel_tab)
        self.export_button_excel.setObjectName("export_button_excel")
        self.export_button_excel.setEnabled(True)
        self.export_button_excel.setAutoDefault(False)
        self.export_button_excel.setFlat(False)

        self.verticalLayout_2.addWidget(self.export_button_excel)

        icon1 = QIcon()
        icon1.addFile(":/icons/document-excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_type.addTab(self.excel_tab, icon1, "")
        self.csv_tab = QWidget()
        self.csv_tab.setObjectName("csv_tab")
        self.verticalLayout_3 = QVBoxLayout(self.csv_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 10)
        self.widget_4 = QWidget(self.csv_tab)
        self.widget_4.setObjectName("widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 5, 1, 5)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName("widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.formLayout_2 = QFormLayout(self.widget_5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(3)
        self.formLayout_2.setContentsMargins(5, 0, 0, 0)
        self.input_check_csv = QCheckBox(self.widget_5)
        self.input_check_csv.setObjectName("input_check_csv")
        self.input_check_csv.setChecked(True)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.input_check_csv)

        self.distribution_check_csv = QCheckBox(self.widget_5)
        self.distribution_check_csv.setObjectName("distribution_check_csv")

        self.formLayout_2.setWidget(
            2, QFormLayout.LabelRole, self.distribution_check_csv
        )

        self.perc_check_csv = QCheckBox(self.widget_5)
        self.perc_check_csv.setObjectName("perc_check_csv")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.perc_check_csv)

        self.adjlogb_check_csv = QCheckBox(self.widget_5)
        self.adjlogb_check_csv.setObjectName("adjlogb_check_csv")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.adjlogb_check_csv)

        self.options_label_csv = QLabel(self.widget_5)
        self.options_label_csv.setObjectName("options_label_csv")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.options_label_csv)

        self.errors_check_csv = QCheckBox(self.widget_5)
        self.errors_check_csv.setObjectName("errors_check_csv")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.errors_check_csv)

        self.horizontalLayout_2.addWidget(self.widget_5)

        self.verticalLayout_3.addWidget(self.widget_4)

        self.export_button_csv = QPushButton(self.csv_tab)
        self.export_button_csv.setObjectName("export_button_csv")
        self.export_button_csv.setEnabled(True)
        self.export_button_csv.setAutoDefault(False)
        self.export_button_csv.setFlat(False)

        self.verticalLayout_3.addWidget(self.export_button_csv)

        icon2 = QIcon()
        icon2.addFile(":/icons/table.png", QSize(), QIcon.Normal, QIcon.Off)
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
        ExportWindow.setWindowTitle(
            QCoreApplication.translate("ExportWindow", "Export Results", None)
        )
        self.input_check_excel.setText(
            QCoreApplication.translate("ExportWindow", "Input info", None)
        )
        self.distribution_check_excel.setText(
            QCoreApplication.translate("ExportWindow", "Distribution", None)
        )
        self.perc_check_excel.setText(
            QCoreApplication.translate(
                "ExportWindow", "% with respect to component", None
            )
        )
        self.adjlogb_check_excel.setText(
            QCoreApplication.translate(
                "ExportWindow", "Adjusted formation constants", None
            )
        )
        self.options_label_excel.setText(
            QCoreApplication.translate(
                "ExportWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Options:</span></p></body></html>',
                None,
            )
        )
        self.errors_check_excel.setText(
            QCoreApplication.translate(
                "ExportWindow", "Std. Deviation of concentration", None
            )
        )
        self.export_button_excel.setText(
            QCoreApplication.translate("ExportWindow", "Export", None)
        )
        self.export_type.setTabText(
            self.export_type.indexOf(self.excel_tab),
            QCoreApplication.translate("ExportWindow", "Excel", None),
        )
        self.input_check_csv.setText(
            QCoreApplication.translate("ExportWindow", "Input info", None)
        )
        self.distribution_check_csv.setText(
            QCoreApplication.translate("ExportWindow", "Distribution", None)
        )
        self.perc_check_csv.setText(
            QCoreApplication.translate(
                "ExportWindow", "% with respect to component", None
            )
        )
        self.adjlogb_check_csv.setText(
            QCoreApplication.translate(
                "ExportWindow", "Adjusted formation constants", None
            )
        )
        self.options_label_csv.setText(
            QCoreApplication.translate(
                "ExportWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Options:</span></p></body></html>',
                None,
            )
        )
        self.errors_check_csv.setText(
            QCoreApplication.translate(
                "ExportWindow", "Std. Deviation of concentration", None
            )
        )
        self.export_button_csv.setText(
            QCoreApplication.translate("ExportWindow", "Export", None)
        )
        self.export_type.setTabText(
            self.export_type.indexOf(self.csv_tab),
            QCoreApplication.translate("ExportWindow", "CSV", None),
        )

    # retranslateUi
