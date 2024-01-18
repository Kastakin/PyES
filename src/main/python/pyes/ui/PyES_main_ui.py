# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyES_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QStatusBar, QTabWidget,
    QTableView, QTextEdit, QToolBar, QToolButton,
    QVBoxLayout, QWidget)

from ui.widgets import (CustomComboBox, CustomSpinBox, inputTitrationOpt)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1283, 778)
        MainWindow.setMinimumSize(QSize(1204, 778))
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionNew.setEnabled(True)
        icon = QIcon()
        icon.addFile(u":/icons/document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u":/icons/folder-open-document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u":/icons/disk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon3 = QIcon()
        icon3.addFile(u":/icons/question-frame.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionWebsite = QAction(MainWindow)
        self.actionWebsite.setObjectName(u"actionWebsite")
        self.actionCalculate = QAction(MainWindow)
        self.actionCalculate.setObjectName(u"actionCalculate")
        icon4 = QIcon()
        icon4.addFile(u":/icons/control.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCalculate.setIcon(icon4)
        self.actionExport_Results = QAction(MainWindow)
        self.actionExport_Results.setObjectName(u"actionExport_Results")
        icon5 = QIcon()
        icon5.addFile(u":/icons/application-export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExport_Results.setIcon(icon5)
        self.actionPlot_Results = QAction(MainWindow)
        self.actionPlot_Results.setObjectName(u"actionPlot_Results")
        icon6 = QIcon()
        icon6.addFile(u":/icons/pencil-ruler.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPlot_Results.setIcon(icon6)
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        icon7 = QIcon()
        iconThemeName = u"edit-undo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon7 = QIcon.fromTheme(iconThemeName)
        else:
            icon7.addFile(u"../../../../../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        self.actionUndo.setIcon(icon7)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        icon8 = QIcon()
        iconThemeName = u"edit-redo"
        if QIcon.hasThemeIcon(iconThemeName):
            icon8 = QIcon.fromTheme(iconThemeName)
        else:
            icon8.addFile(u"../../../../../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        self.actionRedo.setIcon(icon8)
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        icon9 = QIcon()
        icon9.addFile(u":/icons/disk--plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveAs.setIcon(icon9)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.Species = QWidget()
        self.Species.setObjectName(u"Species")
        self.Species.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.Species)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget_7 = QWidget(self.Species)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 0, 1, 1)
        self.sys_opt_label = QLabel(self.widget_7)
        self.sys_opt_label.setObjectName(u"sys_opt_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sys_opt_label.sizePolicy().hasHeightForWidth())
        self.sys_opt_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.sys_opt_label)

        self.frame_5 = QFrame(self.widget_7)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.frame_5)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy3)
        self.formLayout_3 = QFormLayout(self.widget_8)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.comp_label = QLabel(self.widget_8)
        self.comp_label.setObjectName(u"comp_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comp_label.sizePolicy().hasHeightForWidth())
        self.comp_label.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.comp_label)

        self.numComp = QSpinBox(self.widget_8)
        self.numComp.setObjectName(u"numComp")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.numComp.sizePolicy().hasHeightForWidth())
        self.numComp.setSizePolicy(sizePolicy5)
        self.numComp.setMinimum(1)
        self.numComp.setMaximum(999)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.numComp)

        self.species_label = QLabel(self.widget_8)
        self.species_label.setObjectName(u"species_label")
        sizePolicy4.setHeightForWidth(self.species_label.sizePolicy().hasHeightForWidth())
        self.species_label.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.species_label)

        self.numSpecies = QSpinBox(self.widget_8)
        self.numSpecies.setObjectName(u"numSpecies")
        sizePolicy5.setHeightForWidth(self.numSpecies.sizePolicy().hasHeightForWidth())
        self.numSpecies.setSizePolicy(sizePolicy5)
        self.numSpecies.setMinimum(1)
        self.numSpecies.setMaximum(999)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.numSpecies)

        self.phases_label = QLabel(self.widget_8)
        self.phases_label.setObjectName(u"phases_label")
        sizePolicy4.setHeightForWidth(self.phases_label.sizePolicy().hasHeightForWidth())
        self.phases_label.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.phases_label)

        self.numPhases = QSpinBox(self.widget_8)
        self.numPhases.setObjectName(u"numPhases")
        sizePolicy5.setHeightForWidth(self.numPhases.sizePolicy().hasHeightForWidth())
        self.numPhases.setSizePolicy(sizePolicy5)
        self.numPhases.setMinimum(0)
        self.numPhases.setMaximum(999)
        self.numPhases.setValue(0)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.numPhases)

        self.line_7 = QFrame(self.widget_8)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.formLayout_3.setWidget(3, QFormLayout.SpanningRole, self.line_7)

        self.line = QFrame(self.widget_8)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout_3.setWidget(8, QFormLayout.SpanningRole, self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ionic_strength_info = QToolButton(self.widget_8)
        self.ionic_strength_info.setObjectName(u"ionic_strength_info")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.ionic_strength_info.sizePolicy().hasHeightForWidth())
        self.ionic_strength_info.setSizePolicy(sizePolicy6)
        icon10 = QIcon()
        icon10.addFile(u":/icons/information-frame.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ionic_strength_info.setIcon(icon10)

        self.gridLayout.addWidget(self.ionic_strength_info, 0, 2, 1, 1)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.imode_label = QLabel(self.widget_8)
        self.imode_label.setObjectName(u"imode_label")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.imode_label)

        self.imode = CustomComboBox(self.widget_8)
        self.imode.addItem("")
        self.imode.addItem("")
        self.imode.setObjectName(u"imode")
        sizePolicy3.setHeightForWidth(self.imode.sizePolicy().hasHeightForWidth())
        self.imode.setSizePolicy(sizePolicy3)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.imode)


        self.gridLayout.addLayout(self.formLayout_6, 0, 0, 1, 2)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.refIonicStr_label = QLabel(self.widget_8)
        self.refIonicStr_label.setObjectName(u"refIonicStr_label")
        self.refIonicStr_label.setEnabled(False)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.refIonicStr_label)

        self.refIonicStr = CustomSpinBox(self.widget_8)
        self.refIonicStr.setObjectName(u"refIonicStr")
        self.refIonicStr.setEnabled(False)
        self.refIonicStr.setDecimals(5)
        self.refIonicStr.setMaximum(999.000000000000000)
        self.refIonicStr.setSingleStep(0.050000000000000)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.refIonicStr)

        self.A_label = QLabel(self.widget_8)
        self.A_label.setObjectName(u"A_label")
        self.A_label.setEnabled(False)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.A_label)

        self.A = CustomSpinBox(self.widget_8)
        self.A.setObjectName(u"A")
        self.A.setEnabled(False)
        self.A.setDecimals(4)
        self.A.setMinimum(-999.000000000000000)
        self.A.setMaximum(999.000000000000000)
        self.A.setSingleStep(0.050000000000000)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.A)

        self.B_label = QLabel(self.widget_8)
        self.B_label.setObjectName(u"B_label")
        self.B_label.setEnabled(False)

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.B_label)

        self.B = CustomSpinBox(self.widget_8)
        self.B.setObjectName(u"B")
        self.B.setEnabled(False)
        self.B.setDecimals(4)
        self.B.setMinimum(-999.000000000000000)
        self.B.setMaximum(999.000000000000000)
        self.B.setSingleStep(0.050000000000000)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.B)

        self.c0_label = QLabel(self.widget_8)
        self.c0_label.setObjectName(u"c0_label")
        self.c0_label.setEnabled(False)

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.c0_label)

        self.c0 = CustomSpinBox(self.widget_8)
        self.c0.setObjectName(u"c0")
        self.c0.setEnabled(False)
        self.c0.setDecimals(4)
        self.c0.setMinimum(-999.000000000000000)
        self.c0.setMaximum(999.000000000000000)
        self.c0.setSingleStep(0.050000000000000)

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.c0)

        self.c1_label = QLabel(self.widget_8)
        self.c1_label.setObjectName(u"c1_label")
        self.c1_label.setEnabled(False)

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.c1_label)

        self.c1 = CustomSpinBox(self.widget_8)
        self.c1.setObjectName(u"c1")
        self.c1.setEnabled(False)
        self.c1.setDecimals(4)
        self.c1.setMinimum(-999.000000000000000)
        self.c1.setMaximum(999.000000000000000)
        self.c1.setSingleStep(0.050000000000000)

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.c1)

        self.d0_label = QLabel(self.widget_8)
        self.d0_label.setObjectName(u"d0_label")
        self.d0_label.setEnabled(False)

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.d0_label)

        self.d0 = CustomSpinBox(self.widget_8)
        self.d0.setObjectName(u"d0")
        self.d0.setEnabled(False)
        self.d0.setDecimals(4)
        self.d0.setMinimum(-999.000000000000000)
        self.d0.setMaximum(999.000000000000000)
        self.d0.setSingleStep(0.050000000000000)

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.d0)

        self.d1_label = QLabel(self.widget_8)
        self.d1_label.setObjectName(u"d1_label")
        self.d1_label.setEnabled(False)

        self.formLayout_7.setWidget(6, QFormLayout.LabelRole, self.d1_label)

        self.d1 = CustomSpinBox(self.widget_8)
        self.d1.setObjectName(u"d1")
        self.d1.setEnabled(False)
        self.d1.setDecimals(4)
        self.d1.setMinimum(-999.000000000000000)
        self.d1.setMaximum(999.000000000000000)
        self.d1.setSingleStep(0.050000000000000)

        self.formLayout_7.setWidget(6, QFormLayout.FieldRole, self.d1)

        self.e0_label = QLabel(self.widget_8)
        self.e0_label.setObjectName(u"e0_label")
        self.e0_label.setEnabled(False)

        self.formLayout_7.setWidget(7, QFormLayout.LabelRole, self.e0_label)

        self.e0 = CustomSpinBox(self.widget_8)
        self.e0.setObjectName(u"e0")
        self.e0.setEnabled(False)
        self.e0.setDecimals(4)
        self.e0.setMinimum(-999.000000000000000)
        self.e0.setMaximum(999.000000000000000)
        self.e0.setSingleStep(0.050000000000000)

        self.formLayout_7.setWidget(7, QFormLayout.FieldRole, self.e0)

        self.e1_label = QLabel(self.widget_8)
        self.e1_label.setObjectName(u"e1_label")
        self.e1_label.setEnabled(False)

        self.formLayout_7.setWidget(8, QFormLayout.LabelRole, self.e1_label)

        self.e1 = CustomSpinBox(self.widget_8)
        self.e1.setObjectName(u"e1")
        self.e1.setEnabled(False)
        self.e1.setDecimals(4)
        self.e1.setMinimum(-999.000000000000000)
        self.e1.setMaximum(999.000000000000000)
        self.e1.setSingleStep(0.050000000000000)

        self.formLayout_7.setWidget(8, QFormLayout.FieldRole, self.e1)


        self.gridLayout.addLayout(self.formLayout_7, 1, 0, 1, 3)

        self.gridLayout.setRowStretch(0, 1)

        self.formLayout_3.setLayout(10, QFormLayout.SpanningRole, self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.uncertainty_info = QToolButton(self.widget_8)
        self.uncertainty_info.setObjectName(u"uncertainty_info")
        self.uncertainty_info.setIcon(icon10)

        self.gridLayout_2.addWidget(self.uncertainty_info, 0, 1, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.uncertaintyMode = QCheckBox(self.widget_8)
        self.uncertaintyMode.setObjectName(u"uncertaintyMode")
        self.uncertaintyMode.setChecked(True)

        self.formLayout_4.setWidget(0, QFormLayout.SpanningRole, self.uncertaintyMode)


        self.gridLayout_2.addLayout(self.formLayout_4, 0, 0, 1, 1)


        self.formLayout_3.setLayout(7, QFormLayout.SpanningRole, self.gridLayout_2)


        self.horizontalLayout_6.addWidget(self.widget_8)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.Species)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy4.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy4)
        self.verticalLayout_8 = QVBoxLayout(self.widget_6)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tab_comp_label = QLabel(self.widget_6)
        self.tab_comp_label.setObjectName(u"tab_comp_label")
        sizePolicy4.setHeightForWidth(self.tab_comp_label.sizePolicy().hasHeightForWidth())
        self.tab_comp_label.setSizePolicy(sizePolicy4)

        self.verticalLayout_8.addWidget(self.tab_comp_label)

        self.horizontalFrame_2 = QFrame(self.widget_6)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy4.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy4)
        self.horizontalFrame_2.setFrameShape(QFrame.Box)
        self.horizontalFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 2, 0, 2)
        self.insert_above_comp_button = QToolButton(self.horizontalFrame_2)
        self.insert_above_comp_button.setObjectName(u"insert_above_comp_button")
        icon11 = QIcon()
        icon11.addFile(u":/icons/table-insert-row-before.png", QSize(), QIcon.Normal, QIcon.Off)
        self.insert_above_comp_button.setIcon(icon11)
        self.insert_above_comp_button.setIconSize(QSize(18, 18))
        self.insert_above_comp_button.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.insert_above_comp_button)

        self.insert_below_comp_button = QToolButton(self.horizontalFrame_2)
        self.insert_below_comp_button.setObjectName(u"insert_below_comp_button")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.insert_below_comp_button.sizePolicy().hasHeightForWidth())
        self.insert_below_comp_button.setSizePolicy(sizePolicy7)
        icon12 = QIcon()
        icon12.addFile(u":/icons/table-insert-row-after.png", QSize(), QIcon.Normal, QIcon.Off)
        self.insert_below_comp_button.setIcon(icon12)
        self.insert_below_comp_button.setIconSize(QSize(18, 18))
        self.insert_below_comp_button.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.insert_below_comp_button)

        self.remove_comp_button = QToolButton(self.horizontalFrame_2)
        self.remove_comp_button.setObjectName(u"remove_comp_button")
        icon13 = QIcon()
        icon13.addFile(u":/icons/table-delete-row.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_comp_button.setIcon(icon13)
        self.remove_comp_button.setIconSize(QSize(18, 18))
        self.remove_comp_button.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.remove_comp_button)

        self.line_5 = QFrame(self.horizontalFrame_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)

        self.move_up_comp_button = QToolButton(self.horizontalFrame_2)
        self.move_up_comp_button.setObjectName(u"move_up_comp_button")
        icon14 = QIcon()
        icon14.addFile(u":/icons/row_up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.move_up_comp_button.setIcon(icon14)
        self.move_up_comp_button.setIconSize(QSize(18, 18))
        self.move_up_comp_button.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.move_up_comp_button)

        self.move_down_comp_button = QToolButton(self.horizontalFrame_2)
        self.move_down_comp_button.setObjectName(u"move_down_comp_button")
        icon15 = QIcon()
        icon15.addFile(u":/icons/row_down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.move_down_comp_button.setIcon(icon15)
        self.move_down_comp_button.setIconSize(QSize(18, 18))
        self.move_down_comp_button.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.move_down_comp_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addWidget(self.horizontalFrame_2)

        self.compView = QTableView(self.widget_6)
        self.compView.setObjectName(u"compView")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.compView.sizePolicy().hasHeightForWidth())
        self.compView.setSizePolicy(sizePolicy8)
        self.compView.setMaximumSize(QSize(180, 16777215))
        self.compView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.compView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.compView.setProperty("showDropIndicator", False)
        self.compView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.compView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.compView.setTextElideMode(Qt.ElideNone)
        self.compView.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.compView)


        self.horizontalLayout.addWidget(self.widget_6)

        self.widget_2 = QWidget(self.Species)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.tab_comp_label_2 = QLabel(self.widget_2)
        self.tab_comp_label_2.setObjectName(u"tab_comp_label_2")
        sizePolicy4.setHeightForWidth(self.tab_comp_label_2.sizePolicy().hasHeightForWidth())
        self.tab_comp_label_2.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.tab_comp_label_2)

        self.horizontalFrame = QFrame(self.widget_2)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy9)
        self.horizontalFrame.setFrameShape(QFrame.Box)
        self.horizontalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 2, 0, 2)
        self.select_all_button = QToolButton(self.horizontalFrame)
        self.select_all_button.setObjectName(u"select_all_button")
        icon16 = QIcon()
        icon16.addFile(u":/icons/ui-check-box.png", QSize(), QIcon.Normal, QIcon.Off)
        self.select_all_button.setIcon(icon16)
        self.select_all_button.setIconSize(QSize(18, 18))
        self.select_all_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.select_all_button)

        self.deselect_all_button = QToolButton(self.horizontalFrame)
        self.deselect_all_button.setObjectName(u"deselect_all_button")
        icon17 = QIcon()
        icon17.addFile(u":/icons/ui-check-box-uncheck.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deselect_all_button.setIcon(icon17)
        self.deselect_all_button.setIconSize(QSize(18, 18))
        self.deselect_all_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.deselect_all_button)

        self.line_6 = QFrame(self.horizontalFrame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_6)

        self.insert_above_species_button = QToolButton(self.horizontalFrame)
        self.insert_above_species_button.setObjectName(u"insert_above_species_button")
        self.insert_above_species_button.setIcon(icon11)
        self.insert_above_species_button.setIconSize(QSize(18, 18))
        self.insert_above_species_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.insert_above_species_button)

        self.insert_below_species_button = QToolButton(self.horizontalFrame)
        self.insert_below_species_button.setObjectName(u"insert_below_species_button")
        sizePolicy7.setHeightForWidth(self.insert_below_species_button.sizePolicy().hasHeightForWidth())
        self.insert_below_species_button.setSizePolicy(sizePolicy7)
        self.insert_below_species_button.setIcon(icon12)
        self.insert_below_species_button.setIconSize(QSize(18, 18))
        self.insert_below_species_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.insert_below_species_button)

        self.remove_species_button = QToolButton(self.horizontalFrame)
        self.remove_species_button.setObjectName(u"remove_species_button")
        self.remove_species_button.setIcon(icon13)
        self.remove_species_button.setIconSize(QSize(18, 18))
        self.remove_species_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.remove_species_button)

        self.line_4 = QFrame(self.horizontalFrame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_4)

        self.move_up_species_button = QToolButton(self.horizontalFrame)
        self.move_up_species_button.setObjectName(u"move_up_species_button")
        self.move_up_species_button.setIcon(icon14)
        self.move_up_species_button.setIconSize(QSize(18, 18))
        self.move_up_species_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.move_up_species_button)

        self.move_down_species_button = QToolButton(self.horizontalFrame)
        self.move_down_species_button.setObjectName(u"move_down_species_button")
        self.move_down_species_button.setIcon(icon15)
        self.move_down_species_button.setIconSize(QSize(18, 18))
        self.move_down_species_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.move_down_species_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.edit_column_button = QToolButton(self.horizontalFrame)
        self.edit_column_button.setObjectName(u"edit_column_button")
        icon18 = QIcon()
        icon18.addFile(u":/icons/table--pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_column_button.setIcon(icon18)
        self.edit_column_button.setIconSize(QSize(18, 18))
        self.edit_column_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.edit_column_button)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.tablesTab = QTabWidget(self.widget_2)
        self.tablesTab.setObjectName(u"tablesTab")
        self.tablesTab.setUsesScrollButtons(False)
        self.species = QWidget()
        self.species.setObjectName(u"species")
        self.verticalLayout_3 = QVBoxLayout(self.species)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.speciesView = QTableView(self.species)
        self.speciesView.setObjectName(u"speciesView")
        self.speciesView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.speciesView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.speciesView.setProperty("showDropIndicator", False)
        self.speciesView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.speciesView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.speciesView.setTextElideMode(Qt.ElideNone)
        self.speciesView.horizontalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_3.addWidget(self.speciesView)

        icon19 = QIcon()
        icon19.addFile(u":/icons/flask.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tablesTab.addTab(self.species, icon19, "")
        self.solidspecies = QWidget()
        self.solidspecies.setObjectName(u"solidspecies")
        self.verticalLayout_12 = QVBoxLayout(self.solidspecies)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.solidSpeciesView = QTableView(self.solidspecies)
        self.solidSpeciesView.setObjectName(u"solidSpeciesView")
        self.solidSpeciesView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.solidSpeciesView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.solidSpeciesView.setProperty("showDropIndicator", False)
        self.solidSpeciesView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.solidSpeciesView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.solidSpeciesView.horizontalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_12.addWidget(self.solidSpeciesView)

        icon20 = QIcon()
        icon20.addFile(u":/icons/beaker-empty.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tablesTab.addTab(self.solidspecies, icon20, "")

        self.verticalLayout.addWidget(self.tablesTab)


        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 5)
        self.tabWidget.addTab(self.Species, "")
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.Settings.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy1)
        self.verticalLayout_7 = QVBoxLayout(self.Settings)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.dmodeSelector = QWidget(self.Settings)
        self.dmodeSelector.setObjectName(u"dmodeSelector")
        sizePolicy6.setHeightForWidth(self.dmodeSelector.sizePolicy().hasHeightForWidth())
        self.dmodeSelector.setSizePolicy(sizePolicy6)
        self.horizontalLayout_2 = QHBoxLayout(self.dmodeSelector)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dmode_label = QLabel(self.dmodeSelector)
        self.dmode_label.setObjectName(u"dmode_label")
        sizePolicy6.setHeightForWidth(self.dmode_label.sizePolicy().hasHeightForWidth())
        self.dmode_label.setSizePolicy(sizePolicy6)

        self.horizontalLayout_2.addWidget(self.dmode_label)

        self.dmode = CustomComboBox(self.dmodeSelector)
        self.dmode.addItem("")
        self.dmode.addItem("")
        self.dmode.addItem("")
        self.dmode.setObjectName(u"dmode")
        sizePolicy7.setHeightForWidth(self.dmode.sizePolicy().hasHeightForWidth())
        self.dmode.setSizePolicy(sizePolicy7)

        self.horizontalLayout_2.addWidget(self.dmode)


        self.verticalLayout_7.addWidget(self.dmodeSelector)

        self.mode_views = QStackedWidget(self.Settings)
        self.mode_views.setObjectName(u"mode_views")
        self.pyes_modes = QWidget()
        self.pyes_modes.setObjectName(u"pyes_modes")
        self.horizontalLayout_7 = QHBoxLayout(self.pyes_modes)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.dmode0Input = QWidget(self.pyes_modes)
        self.dmode0Input.setObjectName(u"dmode0Input")
        sizePolicy9.setHeightForWidth(self.dmode0Input.sizePolicy().hasHeightForWidth())
        self.dmode0Input.setSizePolicy(sizePolicy9)
        self.horizontalLayout_3 = QHBoxLayout(self.dmode0Input)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 100, 0)
        self.dmode_inputs = QStackedWidget(self.dmode0Input)
        self.dmode_inputs.setObjectName(u"dmode_inputs")
        sizePolicy4.setHeightForWidth(self.dmode_inputs.sizePolicy().hasHeightForWidth())
        self.dmode_inputs.setSizePolicy(sizePolicy4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy4.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy4)
        self.horizontalLayout_9 = QHBoxLayout(self.page)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.page)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy10)
        self.widget_3.setMinimumSize(QSize(263, 287))
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 25, 0, 0)
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setMinimumSize(QSize(280, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 0, -1, 6)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_3)

        self.v0_label = QLabel(self.frame)
        self.v0_label.setObjectName(u"v0_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.v0_label)

        self.v0 = CustomSpinBox(self.frame)
        self.v0.setObjectName(u"v0")
        self.v0.setDecimals(3)
        self.v0.setMaximum(900.000000000000000)
        self.v0.setSingleStep(0.050000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.v0)

        self.initv_label = QLabel(self.frame)
        self.initv_label.setObjectName(u"initv_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.initv_label)

        self.initv = CustomSpinBox(self.frame)
        self.initv.setObjectName(u"initv")
        self.initv.setDecimals(3)
        self.initv.setMaximum(900.000000000000000)
        self.initv.setSingleStep(0.050000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.initv)

        self.vinc_label = QLabel(self.frame)
        self.vinc_label.setObjectName(u"vinc_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.vinc_label)

        self.vinc = CustomSpinBox(self.frame)
        self.vinc.setObjectName(u"vinc")
        self.vinc.setDecimals(3)
        self.vinc.setMaximum(900.000000000000000)
        self.vinc.setSingleStep(0.050000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.vinc)

        self.nop_label = QLabel(self.frame)
        self.nop_label.setObjectName(u"nop_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.nop_label)

        self.nop = CustomSpinBox(self.frame)
        self.nop.setObjectName(u"nop")
        self.nop.setDecimals(0)
        self.nop.setMinimum(1.000000000000000)
        self.nop.setMaximum(9000.000000000000000)
        self.nop.setSingleStep(1.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.nop)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.line_2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.label_4)

        self.c0back_label = QLabel(self.frame)
        self.c0back_label.setObjectName(u"c0back_label")
        self.c0back_label.setEnabled(False)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.c0back_label)

        self.ctback_label = QLabel(self.frame)
        self.ctback_label.setObjectName(u"ctback_label")
        self.ctback_label.setEnabled(False)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.ctback_label)

        self.c0back = CustomSpinBox(self.frame)
        self.c0back.setObjectName(u"c0back")
        self.c0back.setEnabled(False)
        self.c0back.setDecimals(5)
        self.c0back.setMaximum(900.000000000000000)
        self.c0back.setSingleStep(0.050000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.c0back)

        self.ctback = CustomSpinBox(self.frame)
        self.ctback.setObjectName(u"ctback")
        self.ctback.setEnabled(False)
        self.ctback.setDecimals(5)
        self.ctback.setMaximum(900.000000000000000)
        self.ctback.setSingleStep(0.050000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.ctback)


        self.verticalLayout_9.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.horizontalLayout_9.addWidget(self.widget_3)

        self.dmode_inputs.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy4.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy4)
        self.horizontalLayout_10 = QHBoxLayout(self.page_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.page_2)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy10.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy10)
        self.widget_11.setMinimumSize(QSize(263, 287))
        self.verticalLayout_11 = QVBoxLayout(self.widget_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 25, 0, 0)
        self.frame_2 = QFrame(self.widget_11)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(284, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(-1, 0, -1, 6)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.label_9)

        self.initialLog_label = QLabel(self.frame_2)
        self.initialLog_label.setObjectName(u"initialLog_label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.initialLog_label)

        self.initialLog = CustomSpinBox(self.frame_2)
        self.initialLog.setObjectName(u"initialLog")
        self.initialLog.setDecimals(3)
        self.initialLog.setMaximum(900.000000000000000)
        self.initialLog.setSingleStep(0.050000000000000)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.initialLog)

        self.finalLog_label = QLabel(self.frame_2)
        self.finalLog_label.setObjectName(u"finalLog_label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.finalLog_label)

        self.finalLog = CustomSpinBox(self.frame_2)
        self.finalLog.setObjectName(u"finalLog")
        self.finalLog.setDecimals(3)
        self.finalLog.setMaximum(900.000000000000000)
        self.finalLog.setSingleStep(0.050000000000000)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.finalLog)

        self.logInc_label = QLabel(self.frame_2)
        self.logInc_label.setObjectName(u"logInc_label")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.logInc_label)

        self.logInc = CustomSpinBox(self.frame_2)
        self.logInc.setObjectName(u"logInc")
        self.logInc.setDecimals(3)
        self.logInc.setMaximum(900.000000000000000)
        self.logInc.setSingleStep(0.050000000000000)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.logInc)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.formLayout_2.setWidget(5, QFormLayout.SpanningRole, self.line_3)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(6, QFormLayout.SpanningRole, self.label_16)

        self.cback_label = QLabel(self.frame_2)
        self.cback_label.setObjectName(u"cback_label")
        self.cback_label.setEnabled(False)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.cback_label)

        self.cback = CustomSpinBox(self.frame_2)
        self.cback.setObjectName(u"cback")
        self.cback.setEnabled(False)
        self.cback.setDecimals(5)
        self.cback.setMaximum(900.000000000000000)
        self.cback.setSingleStep(0.050000000000000)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.cback)

        self.indComp_label = QLabel(self.frame_2)
        self.indComp_label.setObjectName(u"indComp_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.indComp_label)

        self.indComp = CustomComboBox(self.frame_2)
        self.indComp.setObjectName(u"indComp")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.indComp)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)


        self.horizontalLayout_10.addWidget(self.widget_11)

        self.dmode_inputs.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.dmode_inputs)

        self.widget = QWidget(self.dmode0Input)
        self.widget.setObjectName(u"widget")
        sizePolicy9.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy9)
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.concView = QTableView(self.widget)
        self.concView.setObjectName(u"concView")
        self.concView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_4.addWidget(self.concView)


        self.horizontalLayout_3.addWidget(self.widget)


        self.horizontalLayout_7.addWidget(self.dmode0Input)

        self.mode_views.addWidget(self.pyes_modes)
        self.bstac_modes = QWidget()
        self.bstac_modes.setObjectName(u"bstac_modes")
        self.verticalLayout_10 = QVBoxLayout(self.bstac_modes)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.bstac_modes)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.add_titration = QToolButton(self.frame_3)
        self.add_titration.setObjectName(u"add_titration")
        icon21 = QIcon()
        icon21.addFile(u":/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_titration.setIcon(icon21)
        self.add_titration.setIconSize(QSize(18, 18))
        self.add_titration.setAutoRaise(True)

        self.horizontalLayout_11.addWidget(self.add_titration)

        self.remove_titration = QToolButton(self.frame_3)
        self.remove_titration.setObjectName(u"remove_titration")
        icon22 = QIcon()
        icon22.addFile(u":/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_titration.setIcon(icon22)
        self.remove_titration.setIconSize(QSize(18, 18))
        self.remove_titration.setAutoRaise(True)

        self.horizontalLayout_11.addWidget(self.remove_titration)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_11.addWidget(self.pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.label_7 = QLabel(self.bstac_modes)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_13.addWidget(self.label_7)

        self.label = QLabel(self.bstac_modes)
        self.label.setObjectName(u"label")

        self.verticalLayout_13.addWidget(self.label)

        self.listWidget = QListWidget(self.bstac_modes)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setCheckState(Qt.Unchecked);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setCheckState(Qt.Unchecked);
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setCheckState(Qt.Unchecked);
        __qlistwidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setCheckState(Qt.Unchecked);
        __qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_13.addWidget(self.listWidget)

        self.label_5 = QLabel(self.bstac_modes)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_13.addWidget(self.label_5)

        self.listWidget_2 = QListWidget(self.bstac_modes)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_13.addWidget(self.listWidget_2)

        self.label_6 = QLabel(self.bstac_modes)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_13.addWidget(self.label_6)

        self.listWidget_3 = QListWidget(self.bstac_modes)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.verticalLayout_13.addWidget(self.listWidget_3)

        self.verticalLayout_13.setStretch(2, 2)
        self.verticalLayout_13.setStretch(4, 1)
        self.verticalLayout_13.setStretch(6, 1)

        self.horizontalLayout_13.addLayout(self.verticalLayout_13)

        self.titration_tabs = QTabWidget(self.bstac_modes)
        self.titration_tabs.setObjectName(u"titration_tabs")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy11)
        self.horizontalLayout_12 = QHBoxLayout(self.tab)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_5 = inputTitrationOpt(self.tab)
        self.widget_5.setObjectName(u"widget_5")

        self.horizontalLayout_12.addWidget(self.widget_5)

        self.titration_tabs.addTab(self.tab, "")

        self.horizontalLayout_13.addWidget(self.titration_tabs)

        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.mode_views.addWidget(self.bstac_modes)

        self.verticalLayout_7.addWidget(self.mode_views)

        self.tabWidget.addTab(self.Settings, "")
        self.Calc = QWidget()
        self.Calc.setObjectName(u"Calc")
        self.verticalLayout_2 = QVBoxLayout(self.Calc)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.debug = QCheckBox(self.Calc)
        self.debug.setObjectName(u"debug")

        self.verticalLayout_2.addWidget(self.debug)

        self.consoleOutput = QTextEdit(self.Calc)
        self.consoleOutput.setObjectName(u"consoleOutput")
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(11)
        self.consoleOutput.setFont(font)
        self.consoleOutput.setUndoRedoEnabled(False)
        self.consoleOutput.setLineWrapMode(QTextEdit.NoWrap)
        self.consoleOutput.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.consoleOutput)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setSizeConstraint(QLayout.SetNoConstraint)
        self.formLayout_8.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_8.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.maxNewtonRaphsonIterationsLabel = QLabel(self.Calc)
        self.maxNewtonRaphsonIterationsLabel.setObjectName(u"maxNewtonRaphsonIterationsLabel")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.maxNewtonRaphsonIterationsLabel)

        self.maxNewtonRaphsonIterationsSpinBox = QSpinBox(self.Calc)
        self.maxNewtonRaphsonIterationsSpinBox.setObjectName(u"maxNewtonRaphsonIterationsSpinBox")
        self.maxNewtonRaphsonIterationsSpinBox.setMinimum(1)
        self.maxNewtonRaphsonIterationsSpinBox.setMaximum(999999)
        self.maxNewtonRaphsonIterationsSpinBox.setValue(200)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.maxNewtonRaphsonIterationsSpinBox)

        self.jacobianModeLabel = QLabel(self.Calc)
        self.jacobianModeLabel.setObjectName(u"jacobianModeLabel")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.jacobianModeLabel)

        self.jacobianModeComboBox = QComboBox(self.Calc)
        self.jacobianModeComboBox.addItem("")
        self.jacobianModeComboBox.addItem("")
        self.jacobianModeComboBox.addItem("")
        self.jacobianModeComboBox.setObjectName(u"jacobianModeComboBox")
        sizePolicy3.setHeightForWidth(self.jacobianModeComboBox.sizePolicy().hasHeightForWidth())
        self.jacobianModeComboBox.setSizePolicy(sizePolicy3)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.jacobianModeComboBox)


        self.verticalLayout_2.addLayout(self.formLayout_8)

        self.calcButton = QPushButton(self.Calc)
        self.calcButton.setObjectName(u"calcButton")
        sizePolicy3.setHeightForWidth(self.calcButton.sizePolicy().hasHeightForWidth())
        self.calcButton.setSizePolicy(sizePolicy3)
        self.calcButton.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.calcButton)

        self.widget_4 = QWidget(self.Calc)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.exportButton = QPushButton(self.widget_4)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setEnabled(False)
        self.exportButton.setIcon(icon5)

        self.horizontalLayout_5.addWidget(self.exportButton)

        self.plotDistButton = QPushButton(self.widget_4)
        self.plotDistButton.setObjectName(u"plotDistButton")
        self.plotDistButton.setEnabled(False)
        self.plotDistButton.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.plotDistButton)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.tabWidget.addTab(self.Calc, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1283, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(18, 18))
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionWebsite)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCalculate)
        self.toolBar.addAction(self.actionExport_Results)
        self.toolBar.addAction(self.actionPlot_Results)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.calcButton.clicked.connect(MainWindow.calculate)
        self.exportButton.clicked.connect(MainWindow.exportDist)
        self.plotDistButton.clicked.connect(MainWindow.plotDist)
        self.v0.valueChanged.connect(MainWindow.v0Updater)
        self.numComp.valueChanged.connect(MainWindow.updateComp)
        self.numSpecies.valueChanged.connect(MainWindow.updateSpecies)
        self.speciesView.clicked.connect(self.speciesView.edit)
        self.numPhases.valueChanged.connect(MainWindow.updateSolid)
        self.insert_above_species_button.clicked.connect(MainWindow.insertSpeciesAbove)
        self.insert_below_species_button.clicked.connect(MainWindow.insertSpeciesBelow)
        self.remove_species_button.clicked.connect(MainWindow.removeSpecies)
        self.move_up_species_button.clicked.connect(MainWindow.moveSpeciesUp)
        self.move_down_species_button.clicked.connect(MainWindow.moveSpeciesDown)
        self.insert_above_comp_button.clicked.connect(MainWindow.insertCompAbove)
        self.insert_below_comp_button.clicked.connect(MainWindow.insertCompBelow)
        self.remove_comp_button.clicked.connect(MainWindow.removeComp)
        self.move_up_comp_button.clicked.connect(MainWindow.moveCompUp)
        self.move_down_comp_button.clicked.connect(MainWindow.moveCompDown)
        self.uncertainty_info.clicked.connect(MainWindow.displayUncertaintyInfo)
        self.ionic_strength_info.clicked.connect(MainWindow.displayIonicStrengthInfo)
        self.select_all_button.clicked.connect(MainWindow.checkAll)
        self.deselect_all_button.clicked.connect(MainWindow.uncheckAll)
        self.edit_column_button.clicked.connect(MainWindow.massEditColumn)
        self.add_titration.clicked.connect(MainWindow.addTitration)
        self.remove_titration.clicked.connect(MainWindow.removeTitration)
        self.pushButton.clicked.connect(MainWindow.test)

        self.tabWidget.setCurrentIndex(2)
        self.tablesTab.setCurrentIndex(0)
        self.dmode.setCurrentIndex(0)
        self.mode_views.setCurrentIndex(0)
        self.dmode_inputs.setCurrentIndex(0)
        self.titration_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyES", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save Project", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About PyES", None))
#if QT_CONFIG(tooltip)
        self.actionAbout.setToolTip(QCoreApplication.translate("MainWindow", u"About PyES", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionWebsite.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.actionCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
#if QT_CONFIG(tooltip)
        self.actionCalculate.setToolTip(QCoreApplication.translate("MainWindow", u"Launch the calculation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionCalculate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionExport_Results.setText(QCoreApplication.translate("MainWindow", u"Export Results", None))
#if QT_CONFIG(tooltip)
        self.actionExport_Results.setToolTip(QCoreApplication.translate("MainWindow", u"Export Results", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionExport_Results.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionPlot_Results.setText(QCoreApplication.translate("MainWindow", u"Plot Results", None))
#if QT_CONFIG(tooltip)
        self.actionPlot_Results.setToolTip(QCoreApplication.translate("MainWindow", u"Plot Results", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPlot_Results.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"Save Project As...", None))
#if QT_CONFIG(tooltip)
        self.actionSaveAs.setToolTip(QCoreApplication.translate("MainWindow", u"Save Project As...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSaveAs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.sys_opt_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Options</span></p></body></html>", None))
        self.comp_label.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Components", None))
#if QT_CONFIG(statustip)
        self.numComp.setStatusTip(QCoreApplication.translate("MainWindow", u"Number of components present.", None))
#endif // QT_CONFIG(statustip)
        self.species_label.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Species", None))
#if QT_CONFIG(statustip)
        self.numSpecies.setStatusTip(QCoreApplication.translate("MainWindow", u"Number of species to be considered.", None))
#endif // QT_CONFIG(statustip)
        self.phases_label.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Solid Species", None))
#if QT_CONFIG(statustip)
        self.numPhases.setStatusTip(QCoreApplication.translate("MainWindow", u"Number of solid phases to be considered.", None))
#endif // QT_CONFIG(statustip)
        self.ionic_strength_info.setText("")
        self.imode_label.setText(QCoreApplication.translate("MainWindow", u"Ionic Strength", None))
        self.imode.setItemText(0, QCoreApplication.translate("MainWindow", u"Const.", None))
        self.imode.setItemText(1, QCoreApplication.translate("MainWindow", u"Var.", None))

#if QT_CONFIG(statustip)
        self.imode.setStatusTip(QCoreApplication.translate("MainWindow", u"Constant/variable ionic strength.", None))
#endif // QT_CONFIG(statustip)
        self.refIonicStr_label.setText(QCoreApplication.translate("MainWindow", u"Ref. Ionic Strength", None))
#if QT_CONFIG(statustip)
        self.refIonicStr.setStatusTip(QCoreApplication.translate("MainWindow", u"Reference Ionic Strength to be used (if no other ionic strengths are being explicited).", None))
#endif // QT_CONFIG(statustip)
        self.A_label.setText(QCoreApplication.translate("MainWindow", u"A", None))
#if QT_CONFIG(statustip)
        self.A.setStatusTip(QCoreApplication.translate("MainWindow", u"\"A\" term of the Debye-H\u00fcckel equation.", None))
#endif // QT_CONFIG(statustip)
        self.B_label.setText(QCoreApplication.translate("MainWindow", u"B", None))
#if QT_CONFIG(statustip)
        self.B.setStatusTip(QCoreApplication.translate("MainWindow", u"\"B\" term of the Debye-H\u00fcckel equation.", None))
#endif // QT_CONFIG(statustip)
        self.c0_label.setText(QCoreApplication.translate("MainWindow", u"c0", None))
#if QT_CONFIG(statustip)
        self.c0.setStatusTip(QCoreApplication.translate("MainWindow", u"\"c0\" term of the Debye-H\u00fcckel equation.", None))
#endif // QT_CONFIG(statustip)
        self.c1_label.setText(QCoreApplication.translate("MainWindow", u"c1", None))
#if QT_CONFIG(statustip)
        self.c1.setStatusTip(QCoreApplication.translate("MainWindow", u"\"c1\" term of the Debye-H\u00fcckel equation.", None))
#endif // QT_CONFIG(statustip)
        self.d0_label.setText(QCoreApplication.translate("MainWindow", u"d0", None))
#if QT_CONFIG(statustip)
        self.d0.setStatusTip(QCoreApplication.translate("MainWindow", u"\"d0\" term of the Debye-H\u00fcckel equation.", None))
#endif // QT_CONFIG(statustip)
        self.d1_label.setText(QCoreApplication.translate("MainWindow", u"d1", None))
#if QT_CONFIG(statustip)
        self.d1.setStatusTip(QCoreApplication.translate("MainWindow", u"\"d1\" term of the Debye-H\u00fcckel equation.", None))
#endif // QT_CONFIG(statustip)
        self.e0_label.setText(QCoreApplication.translate("MainWindow", u"e0", None))
#if QT_CONFIG(statustip)
        self.e0.setStatusTip(QCoreApplication.translate("MainWindow", u"\"e0\" term of the Debye-H\u00fcckel equation.", None))
#endif // QT_CONFIG(statustip)
        self.e1_label.setText(QCoreApplication.translate("MainWindow", u"e1", None))
#if QT_CONFIG(statustip)
        self.e1.setStatusTip(QCoreApplication.translate("MainWindow", u"\"e1\" term of the Debye-H\u00fcckel equation.", None))
#endif // QT_CONFIG(statustip)
        self.uncertainty_info.setText("")
        self.uncertaintyMode.setText(QCoreApplication.translate("MainWindow", u"Uncertainty Estimation", None))
        self.tab_comp_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Components</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.insert_above_comp_button.setToolTip(QCoreApplication.translate("MainWindow", u"Add Component Above", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.insert_above_comp_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Add Component Above", None))
#endif // QT_CONFIG(statustip)
        self.insert_above_comp_button.setText("")
#if QT_CONFIG(tooltip)
        self.insert_below_comp_button.setToolTip(QCoreApplication.translate("MainWindow", u"Add Component Below", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.insert_below_comp_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Add Component Below", None))
#endif // QT_CONFIG(statustip)
        self.insert_below_comp_button.setText("")
#if QT_CONFIG(tooltip)
        self.remove_comp_button.setToolTip(QCoreApplication.translate("MainWindow", u"Remove Component", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.remove_comp_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Remove Component", None))
#endif // QT_CONFIG(statustip)
        self.remove_comp_button.setText("")
#if QT_CONFIG(tooltip)
        self.move_up_comp_button.setToolTip(QCoreApplication.translate("MainWindow", u"Move Component Up", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.move_up_comp_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Move Component Up", None))
#endif // QT_CONFIG(statustip)
        self.move_up_comp_button.setText("")
#if QT_CONFIG(tooltip)
        self.move_down_comp_button.setToolTip(QCoreApplication.translate("MainWindow", u"Move Component Down", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.move_down_comp_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Move Component Down", None))
#endif // QT_CONFIG(statustip)
        self.move_down_comp_button.setText("")
        self.tab_comp_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Species</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.select_all_button.setToolTip(QCoreApplication.translate("MainWindow", u"Ignore all species", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.select_all_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Ignore all species", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.deselect_all_button.setToolTip(QCoreApplication.translate("MainWindow", u"Consider all species", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.deselect_all_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Consider all species", None))
#endif // QT_CONFIG(statustip)
        self.deselect_all_button.setText("")
#if QT_CONFIG(tooltip)
        self.insert_above_species_button.setToolTip(QCoreApplication.translate("MainWindow", u"Add Species Above", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.insert_above_species_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Add Species Above", None))
#endif // QT_CONFIG(statustip)
        self.insert_above_species_button.setText("")
#if QT_CONFIG(tooltip)
        self.insert_below_species_button.setToolTip(QCoreApplication.translate("MainWindow", u"Add Species Below", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.insert_below_species_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Add Species Below", None))
#endif // QT_CONFIG(statustip)
        self.insert_below_species_button.setText("")
#if QT_CONFIG(tooltip)
        self.remove_species_button.setToolTip(QCoreApplication.translate("MainWindow", u"Remove Species", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.remove_species_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Remove Species", None))
#endif // QT_CONFIG(statustip)
        self.remove_species_button.setText("")
#if QT_CONFIG(tooltip)
        self.move_up_species_button.setToolTip(QCoreApplication.translate("MainWindow", u"Move Species Up", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.move_up_species_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Move Species Up", None))
#endif // QT_CONFIG(statustip)
        self.move_up_species_button.setText("")
#if QT_CONFIG(tooltip)
        self.move_down_species_button.setToolTip(QCoreApplication.translate("MainWindow", u"Move Species Down", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.move_down_species_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Move Species Down", None))
#endif // QT_CONFIG(statustip)
        self.move_down_species_button.setText("")
#if QT_CONFIG(tooltip)
        self.edit_column_button.setToolTip(QCoreApplication.translate("MainWindow", u"Edit whole column", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.edit_column_button.setStatusTip(QCoreApplication.translate("MainWindow", u"Edit whole column", None))
#endif // QT_CONFIG(statustip)
        self.edit_column_button.setText("")
        self.tablesTab.setTabText(self.tablesTab.indexOf(self.species), QCoreApplication.translate("MainWindow", u"Solution Species", None))
        self.tablesTab.setTabText(self.tablesTab.indexOf(self.solidspecies), QCoreApplication.translate("MainWindow", u"Solid Species", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Species), QCoreApplication.translate("MainWindow", u"Species", None))
        self.dmode_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Work Mode:</span></p></body></html>", None))
        self.dmode.setItemText(0, QCoreApplication.translate("MainWindow", u"Titration", None))
        self.dmode.setItemText(1, QCoreApplication.translate("MainWindow", u"Distribution", None))
        self.dmode.setItemText(2, QCoreApplication.translate("MainWindow", u"Refine Potentiometric", None))

#if QT_CONFIG(statustip)
        self.dmode.setStatusTip(QCoreApplication.translate("MainWindow", u"Select operation mode.", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Volume Settings:</span></p></body></html>", None))
        self.v0_label.setText(QCoreApplication.translate("MainWindow", u"Initial Volume:", None))
#if QT_CONFIG(statustip)
        self.v0.setStatusTip(QCoreApplication.translate("MainWindow", u"Initial volume in the titration vessel.", None))
#endif // QT_CONFIG(statustip)
        self.v0.setSuffix(QCoreApplication.translate("MainWindow", u" ml", None))
        self.initv_label.setText(QCoreApplication.translate("MainWindow", u"First Point Volume:", None))
#if QT_CONFIG(statustip)
        self.initv.setStatusTip(QCoreApplication.translate("MainWindow", u"Volume in the vessel at the first titration point.", None))
#endif // QT_CONFIG(statustip)
        self.initv.setSuffix(QCoreApplication.translate("MainWindow", u" ml", None))
        self.vinc_label.setText(QCoreApplication.translate("MainWindow", u"Volume Increments:", None))
#if QT_CONFIG(statustip)
        self.vinc.setStatusTip(QCoreApplication.translate("MainWindow", u"Increment in volume for each titration point.", None))
#endif // QT_CONFIG(statustip)
        self.vinc.setSuffix(QCoreApplication.translate("MainWindow", u" ml", None))
        self.nop_label.setText(QCoreApplication.translate("MainWindow", u"Number of points:", None))
#if QT_CONFIG(statustip)
        self.nop.setStatusTip(QCoreApplication.translate("MainWindow", u"Number of titration points.", None))
#endif // QT_CONFIG(statustip)
        self.nop.setSuffix("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Background Ions Settings:</span></p></body></html>", None))
        self.c0back_label.setText(QCoreApplication.translate("MainWindow", u"Initial C:", None))
        self.ctback_label.setText(QCoreApplication.translate("MainWindow", u"Titrant C:", None))
#if QT_CONFIG(statustip)
        self.c0back.setStatusTip(QCoreApplication.translate("MainWindow", u"Initial concentration of background ions in titration vessel.", None))
#endif // QT_CONFIG(statustip)
        self.c0back.setSuffix(QCoreApplication.translate("MainWindow", u" mol/l", None))
#if QT_CONFIG(statustip)
        self.ctback.setStatusTip(QCoreApplication.translate("MainWindow", u"Concentration of background ions in the titrant.", None))
#endif // QT_CONFIG(statustip)
        self.ctback.setSuffix(QCoreApplication.translate("MainWindow", u" mol/l", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Indipendent Component Settings:</span></p></body></html>", None))
        self.initialLog_label.setText(QCoreApplication.translate("MainWindow", u"Initial -log[A]:", None))
#if QT_CONFIG(statustip)
        self.initialLog.setStatusTip(QCoreApplication.translate("MainWindow", u"Initial Log value of the indipendent component.", None))
#endif // QT_CONFIG(statustip)
        self.finalLog_label.setText(QCoreApplication.translate("MainWindow", u"Final -log[A]", None))
#if QT_CONFIG(statustip)
        self.finalLog.setStatusTip(QCoreApplication.translate("MainWindow", u"Final Log value of the indipendent component.", None))
#endif // QT_CONFIG(statustip)
        self.logInc_label.setText(QCoreApplication.translate("MainWindow", u"-log[A] Increment:", None))
#if QT_CONFIG(statustip)
        self.logInc.setStatusTip(QCoreApplication.translate("MainWindow", u"Log increment of the indipendent component at each point.", None))
#endif // QT_CONFIG(statustip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Background Ions Settings:</span></p></body></html>", None))
        self.cback_label.setText(QCoreApplication.translate("MainWindow", u"Concentration:", None))
#if QT_CONFIG(tooltip)
        self.cback.setToolTip(QCoreApplication.translate("MainWindow", u"Sum of the concentrations of ionic species that do not take part in the reactions.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.cback.setStatusTip(QCoreApplication.translate("MainWindow", u"Sum of the concentrations of ionic species that do not take part in the reactions.", None))
#endif // QT_CONFIG(statustip)
        self.cback.setSuffix(QCoreApplication.translate("MainWindow", u" mol/l", None))
        self.indComp_label.setText(QCoreApplication.translate("MainWindow", u"Indipendent Comp:", None))
#if QT_CONFIG(statustip)
        self.indComp.setStatusTip(QCoreApplication.translate("MainWindow", u"Component to be considered indipendent.", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Analytical Concentrations:</span></p></body></html>", None))
        self.add_titration.setText("")
        self.remove_titration.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"TEST", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Parameters to refine</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Constants", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"test1", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"test2", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"test3", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"test4", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Parameters 2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Parameters 3", None))
        self.titration_tabs.setTabText(self.titration_tabs.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(statustip)
        self.debug.setStatusTip(QCoreApplication.translate("MainWindow", u"Create a Debug Log to file.", None))
#endif // QT_CONFIG(statustip)
        self.debug.setText(QCoreApplication.translate("MainWindow", u"Debug to file", None))
        self.maxNewtonRaphsonIterationsLabel.setText(QCoreApplication.translate("MainWindow", u"Max Newton-Raphson iterations", None))
        self.jacobianModeLabel.setText(QCoreApplication.translate("MainWindow", u"Jacobian Mode", None))
        self.jacobianModeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal mode", None))
        self.jacobianModeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Mixed mode", None))
        self.jacobianModeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Log mode", None))

#if QT_CONFIG(statustip)
        self.calcButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Launch the calculation routine.", None))
#endif // QT_CONFIG(statustip)
        self.calcButton.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
#if QT_CONFIG(statustip)
        self.exportButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Export the results in various formats.", None))
#endif // QT_CONFIG(statustip)
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export Results", None))
#if QT_CONFIG(statustip)
        self.plotDistButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Plot the results and export the graphs.", None))
#endif // QT_CONFIG(statustip)
        self.plotDistButton.setText(QCoreApplication.translate("MainWindow", u"Plot Results", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Calc), QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"?", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

