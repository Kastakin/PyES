# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyES_graphExport.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
    QDialog,
    QDoubleSpinBox,
    QFormLayout,
    QFrame,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from ui.widgets import ColorButton


class Ui_ExportGraphDialog(object):
    def setupUi(self, ExportGraphDialog):
        if not ExportGraphDialog.objectName():
            ExportGraphDialog.setObjectName("ExportGraphDialog")
        ExportGraphDialog.resize(311, 149)
        ExportGraphDialog.setMinimumSize(QSize(311, 149))
        ExportGraphDialog.setMaximumSize(QSize(311, 149))
        self.verticalLayout = QVBoxLayout(ExportGraphDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(2, 5, 2, 2)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.backgroundLabel = QLabel(ExportGraphDialog)
        self.backgroundLabel.setObjectName("backgroundLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.backgroundLabel)

        self.background = ColorButton(ExportGraphDialog)
        self.background.setObjectName("background")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.background)

        self.transparent_check = QCheckBox(ExportGraphDialog)
        self.transparent_check.setObjectName("transparent_check")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.transparent_check)

        self.scaleLabel = QLabel(ExportGraphDialog)
        self.scaleLabel.setObjectName("scaleLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.scaleLabel)

        self.line = QFrame(ExportGraphDialog)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.line)

        self.scaleDoubleSpinBox = QDoubleSpinBox(ExportGraphDialog)
        self.scaleDoubleSpinBox.setObjectName("scaleDoubleSpinBox")
        self.scaleDoubleSpinBox.setMaximum(100.000000000000000)
        self.scaleDoubleSpinBox.setSingleStep(0.050000000000000)
        self.scaleDoubleSpinBox.setValue(1.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.scaleDoubleSpinBox)

        self.verticalLayout.addLayout(self.formLayout)

        self.export_button = QPushButton(ExportGraphDialog)
        self.export_button.setObjectName("export_button")
        self.export_button.setEnabled(True)
        self.export_button.setAutoDefault(False)
        self.export_button.setFlat(False)

        self.verticalLayout.addWidget(self.export_button)

        self.retranslateUi(ExportGraphDialog)

        self.export_button.setDefault(False)

        QMetaObject.connectSlotsByName(ExportGraphDialog)

    # setupUi

    def retranslateUi(self, ExportGraphDialog):
        ExportGraphDialog.setWindowTitle(
            QCoreApplication.translate("ExportGraphDialog", "Export Options", None)
        )
        self.backgroundLabel.setText(
            QCoreApplication.translate("ExportGraphDialog", "Background", None)
        )
        self.background.setText("")
        self.transparent_check.setText(
            QCoreApplication.translate(
                "ExportGraphDialog", "Transparent Background?", None
            )
        )
        self.scaleLabel.setText(
            QCoreApplication.translate("ExportGraphDialog", "Scale", None)
        )
        self.export_button.setText(
            QCoreApplication.translate("ExportGraphDialog", "Export", None)
        )

    # retranslateUi
