# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyES_inputTitrationOpt.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTableView, QVBoxLayout, QWidget)

class Ui_inputTitrationOpt(object):
    def setupUi(self, inputTitrationOpt):
        if not inputTitrationOpt.objectName():
            inputTitrationOpt.setObjectName(u"inputTitrationOpt")
        inputTitrationOpt.resize(1068, 572)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(inputTitrationOpt.sizePolicy().hasHeightForWidth())
        inputTitrationOpt.setSizePolicy(sizePolicy)
        inputTitrationOpt.setFocusPolicy(Qt.ClickFocus)
        self.horizontalLayout = QHBoxLayout(inputTitrationOpt)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, -1, 0, -1)
        self.test1Label = QLabel(inputTitrationOpt)
        self.test1Label.setObjectName(u"test1Label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.test1Label)

        self.test1LineEdit = QLineEdit(inputTitrationOpt)
        self.test1LineEdit.setObjectName(u"test1LineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.test1LineEdit)

        self.test2Label = QLabel(inputTitrationOpt)
        self.test2Label.setObjectName(u"test2Label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.test2Label)

        self.test2SpinBox = QSpinBox(inputTitrationOpt)
        self.test2SpinBox.setObjectName(u"test2SpinBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.test2SpinBox)

        self.importDataLabel = QLabel(inputTitrationOpt)
        self.importDataLabel.setObjectName(u"importDataLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.importDataLabel)

        self.pushButton = QPushButton(inputTitrationOpt)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pushButton)


        self.horizontalLayout.addLayout(self.formLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(inputTitrationOpt)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(inputTitrationOpt)

        QMetaObject.connectSlotsByName(inputTitrationOpt)
    # setupUi

    def retranslateUi(self, inputTitrationOpt):
        inputTitrationOpt.setWindowTitle(QCoreApplication.translate("inputTitrationOpt", u"Form", None))
        self.test1Label.setText(QCoreApplication.translate("inputTitrationOpt", u"Test1", None))
        self.test2Label.setText(QCoreApplication.translate("inputTitrationOpt", u"Test2", None))
        self.importDataLabel.setText(QCoreApplication.translate("inputTitrationOpt", u"Import Data", None))
        self.pushButton.setText(QCoreApplication.translate("inputTitrationOpt", u"Import", None))
    # retranslateUi

