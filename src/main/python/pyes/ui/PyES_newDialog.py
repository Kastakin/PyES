# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyES_newDialog.ui'
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
    QAbstractButton,
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_dialogNew(object):
    def setupUi(self, dialogNew):
        if not dialogNew.objectName():
            dialogNew.setObjectName("dialogNew")
        dialogNew.resize(367, 99)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogNew.sizePolicy().hasHeightForWidth())
        dialogNew.setSizePolicy(sizePolicy)
        dialogNew.setMinimumSize(QSize(367, 99))
        dialogNew.setMaximumSize(QSize(367, 99))
        self.verticalLayout = QVBoxLayout(dialogNew)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(dialogNew)
        self.label.setObjectName("label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(dialogNew)
        self.label_2.setObjectName("label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_2)

        self.buttonBox = QDialogButtonBox(dialogNew)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialogNew)
        self.buttonBox.accepted.connect(dialogNew.accept)
        self.buttonBox.rejected.connect(dialogNew.reject)

        QMetaObject.connectSlotsByName(dialogNew)

    # setupUi

    def retranslateUi(self, dialogNew):
        dialogNew.setWindowTitle(QCoreApplication.translate("dialogNew", "New", None))
        self.label.setText(
            QCoreApplication.translate(
                "dialogNew", "Do you want to create a new blank project?", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "dialogNew",
                "Any unsaved changes to the current one will be lost.",
                None,
            )
        )

    # retranslateUi
