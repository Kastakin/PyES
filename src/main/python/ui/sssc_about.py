# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lorenzo/Coding/SSSC/src/main/python/ui/sssc_about.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogAbout(object):
    def setupUi(self, dialogAbout):
        dialogAbout.setObjectName("dialogAbout")
        dialogAbout.resize(473, 256)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogAbout.sizePolicy().hasHeightForWidth())
        dialogAbout.setSizePolicy(sizePolicy)
        dialogAbout.setMinimumSize(QtCore.QSize(473, 256))
        dialogAbout.setMaximumSize(QtCore.QSize(473, 256))
        self.verticalLayout = QtWidgets.QVBoxLayout(dialogAbout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(dialogAbout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setWordWrap(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(dialogAbout)
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.verticalLayout.addWidget(self.dialogButtonBox)

        self.retranslateUi(dialogAbout)
        self.dialogButtonBox.accepted.connect(dialogAbout.accept)
        self.dialogButtonBox.rejected.connect(dialogAbout.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogAbout)

    def retranslateUi(self, dialogAbout):
        _translate = QtCore.QCoreApplication.translate
        dialogAbout.setWindowTitle(_translate("dialogAbout", "About"))
        self.label_3.setText(_translate("dialogAbout", "<html><head/><body><p>PyES4 is a sotware created by the chemistry department of the University of Turin.</p><p>Heavly inspired by previous work of Professor Sammartano of the University of Messina, PyES4 aims to empower researchers with the ability to easly compute species distribution and simulate titration curves even for complex systems.</p><p>PyBSTAC is licensed under GPL3 and its source code is aviable on its entirety on <a href=\"https://github.com/Kastakin/PyES4\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a>.</p></body></html>"))
import resources_rc
