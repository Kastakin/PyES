# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lorenzo/Coding/SSSC/src/main/python/ui/PyES4_newDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogNew(object):
    def setupUi(self, dialogNew):
        dialogNew.setObjectName("dialogNew")
        dialogNew.resize(367, 99)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogNew.sizePolicy().hasHeightForWidth())
        dialogNew.setSizePolicy(sizePolicy)
        dialogNew.setMinimumSize(QtCore.QSize(367, 99))
        dialogNew.setMaximumSize(QtCore.QSize(367, 99))
        self.verticalLayout = QtWidgets.QVBoxLayout(dialogNew)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialogNew)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(dialogNew)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialogNew)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialogNew)
        self.buttonBox.accepted.connect(dialogNew.accept)
        self.buttonBox.rejected.connect(dialogNew.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogNew)

    def retranslateUi(self, dialogNew):
        _translate = QtCore.QCoreApplication.translate
        dialogNew.setWindowTitle(_translate("dialogNew", "New"))
        self.label.setText(_translate("dialogNew", "Do you want to create a new blank project?"))
        self.label_2.setText(_translate("dialogNew", "Any unsaved changes to the current one will be lost."))
import resources_rc
