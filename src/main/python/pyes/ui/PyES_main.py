# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyES_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
    QAction,
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
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLayout,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QStatusBar,
    QTableView,
    QTabWidget,
    QTextEdit,
    QToolBar,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1283, 778)
        MainWindow.setMinimumSize(QSize(1204, 778))
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.setEnabled(True)
        icon = QIcon()
        icon.addFile(":/icons/document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        icon1 = QIcon()
        icon1.addFile(
            ":/icons/folder-open-document.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionOpen.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        icon2 = QIcon()
        icon2.addFile(":/icons/disk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        icon3 = QIcon()
        icon3.addFile(":/icons/question-frame.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionWebsite = QAction(MainWindow)
        self.actionWebsite.setObjectName("actionWebsite")
        self.actionCalculate = QAction(MainWindow)
        self.actionCalculate.setObjectName("actionCalculate")
        icon4 = QIcon()
        icon4.addFile(":/icons/control.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCalculate.setIcon(icon4)
        self.actionExport_Results = QAction(MainWindow)
        self.actionExport_Results.setObjectName("actionExport_Results")
        icon5 = QIcon()
        icon5.addFile(
            ":/icons/application-export.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionExport_Results.setIcon(icon5)
        self.actionPlot_Results = QAction(MainWindow)
        self.actionPlot_Results.setObjectName("actionPlot_Results")
        icon6 = QIcon()
        icon6.addFile(":/icons/pencil-ruler.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPlot_Results.setIcon(icon6)
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.Species = QWidget()
        self.Species.setObjectName("Species")
        self.Species.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.Species)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget_7 = QWidget(self.Species)
        self.widget_7.setObjectName("widget_7")
        self.widget_7.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 0, 1, 1)
        self.sys_opt_label = QLabel(self.widget_7)
        self.sys_opt_label.setObjectName("sys_opt_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.sys_opt_label.sizePolicy().hasHeightForWidth()
        )
        self.sys_opt_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.sys_opt_label)

        self.frame_5 = QFrame(self.widget_7)
        self.frame_5.setObjectName("frame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.frame_5)
        self.widget_8.setObjectName("widget_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy3)
        self.formLayout_3 = QFormLayout(self.widget_8)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.comp_label = QLabel(self.widget_8)
        self.comp_label.setObjectName("comp_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comp_label.sizePolicy().hasHeightForWidth())
        self.comp_label.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.comp_label)

        self.numComp = QSpinBox(self.widget_8)
        self.numComp.setObjectName("numComp")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.numComp.sizePolicy().hasHeightForWidth())
        self.numComp.setSizePolicy(sizePolicy5)
        self.numComp.setMinimum(1)
        self.numComp.setMaximum(999)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.numComp)

        self.species_label = QLabel(self.widget_8)
        self.species_label.setObjectName("species_label")
        sizePolicy4.setHeightForWidth(
            self.species_label.sizePolicy().hasHeightForWidth()
        )
        self.species_label.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.species_label)

        self.numSpecies = QSpinBox(self.widget_8)
        self.numSpecies.setObjectName("numSpecies")
        sizePolicy5.setHeightForWidth(self.numSpecies.sizePolicy().hasHeightForWidth())
        self.numSpecies.setSizePolicy(sizePolicy5)
        self.numSpecies.setMinimum(1)
        self.numSpecies.setMaximum(999)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.numSpecies)

        self.phases_label = QLabel(self.widget_8)
        self.phases_label.setObjectName("phases_label")
        sizePolicy4.setHeightForWidth(
            self.phases_label.sizePolicy().hasHeightForWidth()
        )
        self.phases_label.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.phases_label)

        self.numPhases = QSpinBox(self.widget_8)
        self.numPhases.setObjectName("numPhases")
        sizePolicy5.setHeightForWidth(self.numPhases.sizePolicy().hasHeightForWidth())
        self.numPhases.setSizePolicy(sizePolicy5)
        self.numPhases.setMinimum(0)
        self.numPhases.setMaximum(999)
        self.numPhases.setValue(0)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.numPhases)

        self.line_7 = QFrame(self.widget_8)
        self.line_7.setObjectName("line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.formLayout_3.setWidget(3, QFormLayout.SpanningRole, self.line_7)

        self.uncertaintyMode_label = QLabel(self.widget_8)
        self.uncertaintyMode_label.setObjectName("uncertaintyMode_label")

        self.formLayout_3.setWidget(
            6, QFormLayout.LabelRole, self.uncertaintyMode_label
        )

        self.uncertaintyMode = QComboBox(self.widget_8)
        self.uncertaintyMode.addItem("")
        self.uncertaintyMode.addItem("")
        self.uncertaintyMode.setObjectName("uncertaintyMode")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.uncertaintyMode)

        self.line = QFrame(self.widget_8)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout_3.setWidget(8, QFormLayout.SpanningRole, self.line)

        self.imode_label = QLabel(self.widget_8)
        self.imode_label.setObjectName("imode_label")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.imode_label)

        self.imode = QComboBox(self.widget_8)
        self.imode.addItem("")
        self.imode.addItem("")
        self.imode.setObjectName("imode")
        sizePolicy3.setHeightForWidth(self.imode.sizePolicy().hasHeightForWidth())
        self.imode.setSizePolicy(sizePolicy3)

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.imode)

        self.refIonicStr_label = QLabel(self.widget_8)
        self.refIonicStr_label.setObjectName("refIonicStr_label")
        self.refIonicStr_label.setEnabled(False)

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.refIonicStr_label)

        self.refIonicStr = QDoubleSpinBox(self.widget_8)
        self.refIonicStr.setObjectName("refIonicStr")
        self.refIonicStr.setEnabled(False)
        self.refIonicStr.setDecimals(5)
        self.refIonicStr.setMaximum(999.000000000000000)
        self.refIonicStr.setSingleStep(0.050000000000000)

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.refIonicStr)

        self.A_label = QLabel(self.widget_8)
        self.A_label.setObjectName("A_label")
        self.A_label.setEnabled(False)

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.A_label)

        self.A = QDoubleSpinBox(self.widget_8)
        self.A.setObjectName("A")
        self.A.setEnabled(False)
        self.A.setDecimals(4)
        self.A.setMinimum(-999.000000000000000)
        self.A.setMaximum(999.000000000000000)
        self.A.setSingleStep(0.050000000000000)

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.A)

        self.B_label = QLabel(self.widget_8)
        self.B_label.setObjectName("B_label")
        self.B_label.setEnabled(False)

        self.formLayout_3.setWidget(12, QFormLayout.LabelRole, self.B_label)

        self.B = QDoubleSpinBox(self.widget_8)
        self.B.setObjectName("B")
        self.B.setEnabled(False)
        self.B.setDecimals(4)
        self.B.setMinimum(-999.000000000000000)
        self.B.setMaximum(999.000000000000000)
        self.B.setSingleStep(0.050000000000000)

        self.formLayout_3.setWidget(12, QFormLayout.FieldRole, self.B)

        self.c0_label = QLabel(self.widget_8)
        self.c0_label.setObjectName("c0_label")
        self.c0_label.setEnabled(False)

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.c0_label)

        self.c0 = QDoubleSpinBox(self.widget_8)
        self.c0.setObjectName("c0")
        self.c0.setEnabled(False)
        self.c0.setDecimals(4)
        self.c0.setMinimum(-999.000000000000000)
        self.c0.setMaximum(999.000000000000000)
        self.c0.setSingleStep(0.050000000000000)

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.c0)

        self.c1_label = QLabel(self.widget_8)
        self.c1_label.setObjectName("c1_label")
        self.c1_label.setEnabled(False)

        self.formLayout_3.setWidget(14, QFormLayout.LabelRole, self.c1_label)

        self.c1 = QDoubleSpinBox(self.widget_8)
        self.c1.setObjectName("c1")
        self.c1.setEnabled(False)
        self.c1.setDecimals(4)
        self.c1.setMinimum(-999.000000000000000)
        self.c1.setMaximum(999.000000000000000)
        self.c1.setSingleStep(0.050000000000000)

        self.formLayout_3.setWidget(14, QFormLayout.FieldRole, self.c1)

        self.d0_label = QLabel(self.widget_8)
        self.d0_label.setObjectName("d0_label")
        self.d0_label.setEnabled(False)

        self.formLayout_3.setWidget(15, QFormLayout.LabelRole, self.d0_label)

        self.d0 = QDoubleSpinBox(self.widget_8)
        self.d0.setObjectName("d0")
        self.d0.setEnabled(False)
        self.d0.setDecimals(4)
        self.d0.setMinimum(-999.000000000000000)
        self.d0.setMaximum(999.000000000000000)
        self.d0.setSingleStep(0.050000000000000)

        self.formLayout_3.setWidget(15, QFormLayout.FieldRole, self.d0)

        self.d1_label = QLabel(self.widget_8)
        self.d1_label.setObjectName("d1_label")
        self.d1_label.setEnabled(False)

        self.formLayout_3.setWidget(16, QFormLayout.LabelRole, self.d1_label)

        self.d1 = QDoubleSpinBox(self.widget_8)
        self.d1.setObjectName("d1")
        self.d1.setEnabled(False)
        self.d1.setDecimals(4)
        self.d1.setMinimum(-999.000000000000000)
        self.d1.setMaximum(999.000000000000000)
        self.d1.setSingleStep(0.050000000000000)

        self.formLayout_3.setWidget(16, QFormLayout.FieldRole, self.d1)

        self.e0_label = QLabel(self.widget_8)
        self.e0_label.setObjectName("e0_label")
        self.e0_label.setEnabled(False)

        self.formLayout_3.setWidget(17, QFormLayout.LabelRole, self.e0_label)

        self.e0 = QDoubleSpinBox(self.widget_8)
        self.e0.setObjectName("e0")
        self.e0.setEnabled(False)
        self.e0.setDecimals(4)
        self.e0.setMinimum(-999.000000000000000)
        self.e0.setMaximum(999.000000000000000)
        self.e0.setSingleStep(0.050000000000000)

        self.formLayout_3.setWidget(17, QFormLayout.FieldRole, self.e0)

        self.e1_label = QLabel(self.widget_8)
        self.e1_label.setObjectName("e1_label")
        self.e1_label.setEnabled(False)

        self.formLayout_3.setWidget(18, QFormLayout.LabelRole, self.e1_label)

        self.e1 = QDoubleSpinBox(self.widget_8)
        self.e1.setObjectName("e1")
        self.e1.setEnabled(False)
        self.e1.setDecimals(4)
        self.e1.setMinimum(-999.000000000000000)
        self.e1.setMaximum(999.000000000000000)
        self.e1.setSingleStep(0.050000000000000)

        self.formLayout_3.setWidget(18, QFormLayout.FieldRole, self.e1)

        self.horizontalLayout_6.addWidget(self.widget_8)

        self.verticalLayout_6.addWidget(self.frame_5)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.Species)
        self.widget_6.setObjectName("widget_6")
        sizePolicy4.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy4)
        self.verticalLayout_8 = QVBoxLayout(self.widget_6)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tab_comp_label = QLabel(self.widget_6)
        self.tab_comp_label.setObjectName("tab_comp_label")
        sizePolicy4.setHeightForWidth(
            self.tab_comp_label.sizePolicy().hasHeightForWidth()
        )
        self.tab_comp_label.setSizePolicy(sizePolicy4)

        self.verticalLayout_8.addWidget(self.tab_comp_label)

        self.horizontalFrame_2 = QFrame(self.widget_6)
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.horizontalFrame_2.sizePolicy().hasHeightForWidth()
        )
        self.horizontalFrame_2.setSizePolicy(sizePolicy6)
        self.horizontalFrame_2.setFrameShape(QFrame.Box)
        self.horizontalFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 2, 0, 2)
        self.insert_above_comp_button = QToolButton(self.horizontalFrame_2)
        self.insert_above_comp_button.setObjectName("insert_above_comp_button")
        icon7 = QIcon()
        icon7.addFile(
            ":/icons/table-insert-row-before.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.insert_above_comp_button.setIcon(icon7)
        self.insert_above_comp_button.setIconSize(QSize(18, 18))
        self.insert_above_comp_button.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.insert_above_comp_button)

        self.insert_below_comp_button = QToolButton(self.horizontalFrame_2)
        self.insert_below_comp_button.setObjectName("insert_below_comp_button")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.insert_below_comp_button.sizePolicy().hasHeightForWidth()
        )
        self.insert_below_comp_button.setSizePolicy(sizePolicy7)
        icon8 = QIcon()
        icon8.addFile(
            ":/icons/table-insert-row-after.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.insert_below_comp_button.setIcon(icon8)
        self.insert_below_comp_button.setIconSize(QSize(18, 18))
        self.insert_below_comp_button.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.insert_below_comp_button)

        self.remove_comp_button = QToolButton(self.horizontalFrame_2)
        self.remove_comp_button.setObjectName("remove_comp_button")
        icon9 = QIcon()
        icon9.addFile(":/icons/table-delete-row.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_comp_button.setIcon(icon9)
        self.remove_comp_button.setIconSize(QSize(18, 18))
        self.remove_comp_button.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.remove_comp_button)

        self.line_5 = QFrame(self.horizontalFrame_2)
        self.line_5.setObjectName("line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)

        self.move_up_comp_button = QToolButton(self.horizontalFrame_2)
        self.move_up_comp_button.setObjectName("move_up_comp_button")
        icon10 = QIcon()
        icon10.addFile(":/icons/row_up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.move_up_comp_button.setIcon(icon10)
        self.move_up_comp_button.setIconSize(QSize(18, 18))
        self.move_up_comp_button.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.move_up_comp_button)

        self.move_down_comp_button = QToolButton(self.horizontalFrame_2)
        self.move_down_comp_button.setObjectName("move_down_comp_button")
        icon11 = QIcon()
        icon11.addFile(":/icons/row_down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.move_down_comp_button.setIcon(icon11)
        self.move_down_comp_button.setIconSize(QSize(18, 18))
        self.move_down_comp_button.setAutoRaise(True)

        self.horizontalLayout_8.addWidget(self.move_down_comp_button)

        self.verticalLayout_8.addWidget(self.horizontalFrame_2)

        self.compView = QTableView(self.widget_6)
        self.compView.setObjectName("compView")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.compView.sizePolicy().hasHeightForWidth())
        self.compView.setSizePolicy(sizePolicy8)
        self.compView.setMaximumSize(QSize(180, 16777215))
        self.compView.setFrameShape(QFrame.StyledPanel)
        self.compView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.compView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.compView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.compView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.compView.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.compView)

        self.horizontalLayout.addWidget(self.widget_6)

        self.widget_2 = QWidget(self.Species)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.tab_comp_label_2 = QLabel(self.widget_2)
        self.tab_comp_label_2.setObjectName("tab_comp_label_2")
        sizePolicy4.setHeightForWidth(
            self.tab_comp_label_2.sizePolicy().hasHeightForWidth()
        )
        self.tab_comp_label_2.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.tab_comp_label_2)

        self.horizontalFrame = QFrame(self.widget_2)
        self.horizontalFrame.setObjectName("horizontalFrame")
        sizePolicy6.setHeightForWidth(
            self.horizontalFrame.sizePolicy().hasHeightForWidth()
        )
        self.horizontalFrame.setSizePolicy(sizePolicy6)
        self.horizontalFrame.setFrameShape(QFrame.Box)
        self.horizontalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 2, 0, 2)
        self.insert_above_species_button = QToolButton(self.horizontalFrame)
        self.insert_above_species_button.setObjectName("insert_above_species_button")
        self.insert_above_species_button.setIcon(icon7)
        self.insert_above_species_button.setIconSize(QSize(18, 18))
        self.insert_above_species_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.insert_above_species_button)

        self.insert_below_species_button = QToolButton(self.horizontalFrame)
        self.insert_below_species_button.setObjectName("insert_below_species_button")
        sizePolicy7.setHeightForWidth(
            self.insert_below_species_button.sizePolicy().hasHeightForWidth()
        )
        self.insert_below_species_button.setSizePolicy(sizePolicy7)
        self.insert_below_species_button.setIcon(icon8)
        self.insert_below_species_button.setIconSize(QSize(18, 18))
        self.insert_below_species_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.insert_below_species_button)

        self.remove_species_button = QToolButton(self.horizontalFrame)
        self.remove_species_button.setObjectName("remove_species_button")
        self.remove_species_button.setIcon(icon9)
        self.remove_species_button.setIconSize(QSize(18, 18))
        self.remove_species_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.remove_species_button)

        self.line_4 = QFrame(self.horizontalFrame)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_4)

        self.move_up_species_button = QToolButton(self.horizontalFrame)
        self.move_up_species_button.setObjectName("move_up_species_button")
        self.move_up_species_button.setIcon(icon10)
        self.move_up_species_button.setIconSize(QSize(18, 18))
        self.move_up_species_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.move_up_species_button)

        self.move_down_species_button = QToolButton(self.horizontalFrame)
        self.move_down_species_button.setObjectName("move_down_species_button")
        self.move_down_species_button.setIcon(icon11)
        self.move_down_species_button.setIconSize(QSize(18, 18))
        self.move_down_species_button.setAutoRaise(True)

        self.horizontalLayout_4.addWidget(self.move_down_species_button)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout.addWidget(self.horizontalFrame)

        self.tablesTab = QTabWidget(self.widget_2)
        self.tablesTab.setObjectName("tablesTab")
        self.tablesTab.setTabPosition(QTabWidget.North)
        self.tablesTab.setTabShape(QTabWidget.Rounded)
        self.tablesTab.setUsesScrollButtons(False)
        self.tablesTab.setTabBarAutoHide(False)
        self.species = QWidget()
        self.species.setObjectName("species")
        self.verticalLayout_3 = QVBoxLayout(self.species)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.speciesView = QTableView(self.species)
        self.speciesView.setObjectName("speciesView")
        self.speciesView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.speciesView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.speciesView.setProperty("showDropIndicator", False)
        self.speciesView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.speciesView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.speciesView.horizontalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_3.addWidget(self.speciesView)

        icon12 = QIcon()
        icon12.addFile(":/icons/flask.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tablesTab.addTab(self.species, icon12, "")
        self.solidspecies = QWidget()
        self.solidspecies.setObjectName("solidspecies")
        self.verticalLayout_12 = QVBoxLayout(self.solidspecies)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.solidSpeciesView = QTableView(self.solidspecies)
        self.solidSpeciesView.setObjectName("solidSpeciesView")
        self.solidSpeciesView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.solidSpeciesView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.solidSpeciesView.setProperty("showDropIndicator", False)
        self.solidSpeciesView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.solidSpeciesView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.solidSpeciesView.horizontalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_12.addWidget(self.solidSpeciesView)

        icon13 = QIcon()
        icon13.addFile(":/icons/beaker-empty.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tablesTab.addTab(self.solidspecies, icon13, "")

        self.verticalLayout.addWidget(self.tablesTab)

        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 5)
        self.tabWidget.addTab(self.Species, "")
        self.Settings = QWidget()
        self.Settings.setObjectName("Settings")
        self.Settings.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy1)
        self.verticalLayout_7 = QVBoxLayout(self.Settings)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.dmodeSelector = QWidget(self.Settings)
        self.dmodeSelector.setObjectName("dmodeSelector")
        sizePolicy9 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(
            self.dmodeSelector.sizePolicy().hasHeightForWidth()
        )
        self.dmodeSelector.setSizePolicy(sizePolicy9)
        self.horizontalLayout_2 = QHBoxLayout(self.dmodeSelector)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dmode_label = QLabel(self.dmodeSelector)
        self.dmode_label.setObjectName("dmode_label")
        sizePolicy9.setHeightForWidth(self.dmode_label.sizePolicy().hasHeightForWidth())
        self.dmode_label.setSizePolicy(sizePolicy9)

        self.horizontalLayout_2.addWidget(self.dmode_label)

        self.dmode = QComboBox(self.dmodeSelector)
        self.dmode.addItem("")
        self.dmode.addItem("")
        self.dmode.setObjectName("dmode")
        sizePolicy7.setHeightForWidth(self.dmode.sizePolicy().hasHeightForWidth())
        self.dmode.setSizePolicy(sizePolicy7)

        self.horizontalLayout_2.addWidget(self.dmode)

        self.verticalLayout_7.addWidget(self.dmodeSelector)

        self.dmode0Input = QWidget(self.Settings)
        self.dmode0Input.setObjectName("dmode0Input")
        sizePolicy4.setHeightForWidth(self.dmode0Input.sizePolicy().hasHeightForWidth())
        self.dmode0Input.setSizePolicy(sizePolicy4)
        self.horizontalLayout_3 = QHBoxLayout(self.dmode0Input)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.dmode0Input)
        self.widget.setObjectName("widget")
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.dmode0_concView = QTableView(self.widget)
        self.dmode0_concView.setObjectName("dmode0_concView")

        self.verticalLayout_4.addWidget(self.dmode0_concView)

        self.horizontalLayout_3.addWidget(self.widget)

        self.widget_3 = QWidget(self.dmode0Input)
        self.widget_3.setObjectName("widget_3")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy10)
        self.widget_3.setMinimumSize(QSize(263, 287))
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 25, 0, 0)
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName("frame")
        sizePolicy9.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy9)
        self.frame.setMinimumSize(QSize(280, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setContentsMargins(-1, 0, -1, 6)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName("label_3")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_3)

        self.v0_label = QLabel(self.frame)
        self.v0_label.setObjectName("v0_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.v0_label)

        self.v0 = QDoubleSpinBox(self.frame)
        self.v0.setObjectName("v0")
        self.v0.setDecimals(3)
        self.v0.setMaximum(900.000000000000000)
        self.v0.setSingleStep(0.050000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.v0)

        self.initv_label = QLabel(self.frame)
        self.initv_label.setObjectName("initv_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.initv_label)

        self.initv = QDoubleSpinBox(self.frame)
        self.initv.setObjectName("initv")
        self.initv.setDecimals(3)
        self.initv.setMaximum(900.000000000000000)
        self.initv.setSingleStep(0.050000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.initv)

        self.vinc_label = QLabel(self.frame)
        self.vinc_label.setObjectName("vinc_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.vinc_label)

        self.vinc = QDoubleSpinBox(self.frame)
        self.vinc.setObjectName("vinc")
        self.vinc.setDecimals(3)
        self.vinc.setMaximum(900.000000000000000)
        self.vinc.setSingleStep(0.050000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.vinc)

        self.nop_label = QLabel(self.frame)
        self.nop_label.setObjectName("nop_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.nop_label)

        self.nop = QDoubleSpinBox(self.frame)
        self.nop.setObjectName("nop")
        self.nop.setDecimals(0)
        self.nop.setMinimum(1.000000000000000)
        self.nop.setMaximum(9000.000000000000000)
        self.nop.setSingleStep(1.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.nop)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.line_2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName("label_4")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.label_4)

        self.c0back_label = QLabel(self.frame)
        self.c0back_label.setObjectName("c0back_label")
        self.c0back_label.setEnabled(False)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.c0back_label)

        self.ctback_label = QLabel(self.frame)
        self.ctback_label.setObjectName("ctback_label")
        self.ctback_label.setEnabled(False)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.ctback_label)

        self.c0back = QDoubleSpinBox(self.frame)
        self.c0back.setObjectName("c0back")
        self.c0back.setEnabled(False)
        self.c0back.setDecimals(5)
        self.c0back.setMaximum(900.000000000000000)
        self.c0back.setSingleStep(0.050000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.c0back)

        self.ctback = QDoubleSpinBox(self.frame)
        self.ctback.setObjectName("ctback")
        self.ctback.setEnabled(False)
        self.ctback.setDecimals(5)
        self.ctback.setMaximum(900.000000000000000)
        self.ctback.setSingleStep(0.050000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.ctback)

        self.verticalLayout_9.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3.addWidget(self.widget_3)

        self.verticalLayout_7.addWidget(self.dmode0Input)

        self.dmode1Input = QWidget(self.Settings)
        self.dmode1Input.setObjectName("dmode1Input")
        sizePolicy4.setHeightForWidth(self.dmode1Input.sizePolicy().hasHeightForWidth())
        self.dmode1Input.setSizePolicy(sizePolicy4)
        self.horizontalLayout_7 = QHBoxLayout(self.dmode1Input)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.dmode1Input)
        self.widget_5.setObjectName("widget_5")
        sizePolicy4.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy4)
        self.verticalLayout_10 = QVBoxLayout(self.widget_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName("label_8")

        self.verticalLayout_10.addWidget(self.label_8)

        self.dmode1_concView = QTableView(self.widget_5)
        self.dmode1_concView.setObjectName("dmode1_concView")

        self.verticalLayout_10.addWidget(self.dmode1_concView)

        self.horizontalLayout_7.addWidget(self.widget_5)

        self.widget_11 = QWidget(self.dmode1Input)
        self.widget_11.setObjectName("widget_11")
        sizePolicy10.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy10)
        self.widget_11.setMinimumSize(QSize(263, 287))
        self.verticalLayout_11 = QVBoxLayout(self.widget_11)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 25, 0, 0)
        self.frame_2 = QFrame(self.widget_11)
        self.frame_2.setObjectName("frame_2")
        sizePolicy9.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy9)
        self.frame_2.setMinimumSize(QSize(284, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout_2.setContentsMargins(-1, 0, -1, 6)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.label_9)

        self.initialLog_label = QLabel(self.frame_2)
        self.initialLog_label.setObjectName("initialLog_label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.initialLog_label)

        self.initialLog = QDoubleSpinBox(self.frame_2)
        self.initialLog.setObjectName("initialLog")
        self.initialLog.setDecimals(3)
        self.initialLog.setMaximum(900.000000000000000)
        self.initialLog.setSingleStep(0.050000000000000)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.initialLog)

        self.finalLog_label = QLabel(self.frame_2)
        self.finalLog_label.setObjectName("finalLog_label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.finalLog_label)

        self.finalLog = QDoubleSpinBox(self.frame_2)
        self.finalLog.setObjectName("finalLog")
        self.finalLog.setDecimals(3)
        self.finalLog.setMaximum(900.000000000000000)
        self.finalLog.setSingleStep(0.050000000000000)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.finalLog)

        self.logInc_label = QLabel(self.frame_2)
        self.logInc_label.setObjectName("logInc_label")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.logInc_label)

        self.logInc = QDoubleSpinBox(self.frame_2)
        self.logInc.setObjectName("logInc")
        self.logInc.setDecimals(3)
        self.logInc.setMaximum(900.000000000000000)
        self.logInc.setSingleStep(0.050000000000000)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.logInc)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.formLayout_2.setWidget(5, QFormLayout.SpanningRole, self.line_3)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName("label_16")

        self.formLayout_2.setWidget(6, QFormLayout.SpanningRole, self.label_16)

        self.cback_label = QLabel(self.frame_2)
        self.cback_label.setObjectName("cback_label")
        self.cback_label.setEnabled(False)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.cback_label)

        self.cback = QDoubleSpinBox(self.frame_2)
        self.cback.setObjectName("cback")
        self.cback.setEnabled(False)
        self.cback.setDecimals(5)
        self.cback.setMaximum(900.000000000000000)
        self.cback.setSingleStep(0.050000000000000)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.cback)

        self.indComp_label = QLabel(self.frame_2)
        self.indComp_label.setObjectName("indComp_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.indComp_label)

        self.indComp = QComboBox(self.frame_2)
        self.indComp.setObjectName("indComp")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.indComp)

        self.verticalLayout_11.addWidget(self.frame_2)

        self.verticalSpacer_6 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.horizontalLayout_7.addWidget(self.widget_11)

        self.verticalLayout_7.addWidget(self.dmode1Input)

        self.tabWidget.addTab(self.Settings, "")
        self.Calc = QWidget()
        self.Calc.setObjectName("Calc")
        self.verticalLayout_2 = QVBoxLayout(self.Calc)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.debug = QCheckBox(self.Calc)
        self.debug.setObjectName("debug")

        self.verticalLayout_2.addWidget(self.debug)

        self.consoleOutput = QTextEdit(self.Calc)
        self.consoleOutput.setObjectName("consoleOutput")
        font = QFont()
        font.setFamilies(["Courier New"])
        font.setPointSize(11)
        self.consoleOutput.setFont(font)
        self.consoleOutput.setUndoRedoEnabled(False)
        self.consoleOutput.setLineWrapMode(QTextEdit.NoWrap)
        self.consoleOutput.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.consoleOutput)

        self.calcButton = QPushButton(self.Calc)
        self.calcButton.setObjectName("calcButton")
        sizePolicy3.setHeightForWidth(self.calcButton.sizePolicy().hasHeightForWidth())
        self.calcButton.setSizePolicy(sizePolicy3)
        self.calcButton.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.calcButton)

        self.widget_4 = QWidget(self.Calc)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.exportButton = QPushButton(self.widget_4)
        self.exportButton.setObjectName("exportButton")
        self.exportButton.setEnabled(False)
        self.exportButton.setIcon(icon5)

        self.horizontalLayout_5.addWidget(self.exportButton)

        self.plotDistButton = QPushButton(self.widget_4)
        self.plotDistButton.setObjectName("plotDistButton")
        self.plotDistButton.setEnabled(False)
        self.plotDistButton.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.plotDistButton)

        self.verticalLayout_2.addWidget(self.widget_4)

        self.tabWidget.addTab(self.Calc, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1283, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(18, 18))
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionWebsite)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
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
        self.dmode.currentIndexChanged.connect(MainWindow.dmodeUpdater)
        self.indComp.currentIndexChanged.connect(MainWindow.indipendentUpdater)
        self.v0.valueChanged.connect(MainWindow.v0Updater)
        self.uncertaintyMode.currentIndexChanged.connect(MainWindow.relErrorsUpdater)
        self.imode.currentIndexChanged.connect(MainWindow.imodeUpdater)
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

        self.tabWidget.setCurrentIndex(0)
        self.tablesTab.setCurrentIndex(0)
        self.dmode.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "PyES", None)
        )
        self.actionNew.setText(
            QCoreApplication.translate("MainWindow", "New Project", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+N", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(
            QCoreApplication.translate("MainWindow", "Open Project", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+O", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSave.setText(
            QCoreApplication.translate("MainWindow", "Save Project", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", "About", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+H", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        self.actionWebsite.setText(
            QCoreApplication.translate("MainWindow", "Website", None)
        )
        self.actionCalculate.setText(
            QCoreApplication.translate("MainWindow", "Calculate", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionCalculate.setToolTip(
            QCoreApplication.translate("MainWindow", "Launch the calculation", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.actionCalculate.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+R", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionExport_Results.setText(
            QCoreApplication.translate("MainWindow", "Export Results", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionExport_Results.setToolTip(
            QCoreApplication.translate("MainWindow", "Export Results", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.actionExport_Results.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+E", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionPlot_Results.setText(
            QCoreApplication.translate("MainWindow", "Plot Results", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionPlot_Results.setToolTip(
            QCoreApplication.translate("MainWindow", "Plot Results", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.actionPlot_Results.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+P", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionAbout_Qt.setText(
            QCoreApplication.translate("MainWindow", "About Qt", None)
        )
        self.sys_opt_label.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Options</span></p></body></html>',
                None,
            )
        )
        self.comp_label.setText(
            QCoreApplication.translate("MainWindow", "N\u00b0 Comp.", None)
        )
        # if QT_CONFIG(statustip)
        self.numComp.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Number of components present.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.species_label.setText(
            QCoreApplication.translate("MainWindow", "N\u00b0 Species", None)
        )
        # if QT_CONFIG(statustip)
        self.numSpecies.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Number of species to be considered.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.phases_label.setText(
            QCoreApplication.translate("MainWindow", "N\u00b0 Solid Species", None)
        )
        # if QT_CONFIG(statustip)
        self.numPhases.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Number of solid phases to be considered.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.uncertaintyMode_label.setText(
            QCoreApplication.translate("MainWindow", "Uncertainty Estimation", None)
        )
        self.uncertaintyMode.setItemText(
            0, QCoreApplication.translate("MainWindow", "Yes", None)
        )
        self.uncertaintyMode.setItemText(
            1, QCoreApplication.translate("MainWindow", "No", None)
        )

        self.imode_label.setText(
            QCoreApplication.translate("MainWindow", "Ionic Strength", None)
        )
        self.imode.setItemText(
            0, QCoreApplication.translate("MainWindow", "Const.", None)
        )
        self.imode.setItemText(
            1, QCoreApplication.translate("MainWindow", "Var.", None)
        )

        # if QT_CONFIG(statustip)
        self.imode.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Constant/variable ionic strength.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.refIonicStr_label.setText(
            QCoreApplication.translate("MainWindow", "Ref. Ionic Strength", None)
        )
        # if QT_CONFIG(statustip)
        self.refIonicStr.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Reference Ionic Strength to be used (if no other ionic strengths are being explicited).",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.A_label.setText(QCoreApplication.translate("MainWindow", "A", None))
        # if QT_CONFIG(statustip)
        self.A.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", '"A" term of the Debye-H\u00fcckel equation.', None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.B_label.setText(QCoreApplication.translate("MainWindow", "B", None))
        # if QT_CONFIG(statustip)
        self.B.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", '"B" term of the Debye-H\u00fcckel equation.', None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.c0_label.setText(QCoreApplication.translate("MainWindow", "c0", None))
        # if QT_CONFIG(statustip)
        self.c0.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", '"c0" term of the Debye-H\u00fcckel equation.', None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.c1_label.setText(QCoreApplication.translate("MainWindow", "c1", None))
        # if QT_CONFIG(statustip)
        self.c1.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", '"c1" term of the Debye-H\u00fcckel equation.', None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.d0_label.setText(QCoreApplication.translate("MainWindow", "d0", None))
        # if QT_CONFIG(statustip)
        self.d0.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", '"d0" term of the Debye-H\u00fcckel equation.', None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.d1_label.setText(QCoreApplication.translate("MainWindow", "d1", None))
        # if QT_CONFIG(statustip)
        self.d1.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", '"d1" term of the Debye-H\u00fcckel equation.', None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.e0_label.setText(QCoreApplication.translate("MainWindow", "e0", None))
        # if QT_CONFIG(statustip)
        self.e0.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", '"e0" term of the Debye-H\u00fcckel equation.', None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.e1_label.setText(QCoreApplication.translate("MainWindow", "e1", None))
        # if QT_CONFIG(statustip)
        self.e1.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", '"e1" term of the Debye-H\u00fcckel equation.', None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.tab_comp_label.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Components</span></p></body></html>',
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.insert_above_comp_button.setToolTip(
            QCoreApplication.translate("MainWindow", "Add Component Above", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.insert_above_comp_button.setStatusTip(
            QCoreApplication.translate("MainWindow", "Add Component Above", None)
        )
        # endif // QT_CONFIG(statustip)
        self.insert_above_comp_button.setText("")
        # if QT_CONFIG(tooltip)
        self.insert_below_comp_button.setToolTip(
            QCoreApplication.translate("MainWindow", "Add Component Below", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.insert_below_comp_button.setStatusTip(
            QCoreApplication.translate("MainWindow", "Add Component Below", None)
        )
        # endif // QT_CONFIG(statustip)
        self.insert_below_comp_button.setText("")
        # if QT_CONFIG(tooltip)
        self.remove_comp_button.setToolTip(
            QCoreApplication.translate("MainWindow", "Remove Component", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.remove_comp_button.setStatusTip(
            QCoreApplication.translate("MainWindow", "Remove Component", None)
        )
        # endif // QT_CONFIG(statustip)
        self.remove_comp_button.setText("")
        # if QT_CONFIG(tooltip)
        self.move_up_comp_button.setToolTip(
            QCoreApplication.translate("MainWindow", "Move Component Up", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.move_up_comp_button.setStatusTip(
            QCoreApplication.translate("MainWindow", "Move Component Up", None)
        )
        # endif // QT_CONFIG(statustip)
        self.move_up_comp_button.setText("")
        # if QT_CONFIG(tooltip)
        self.move_down_comp_button.setToolTip(
            QCoreApplication.translate("MainWindow", "Move Component Down", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.move_down_comp_button.setStatusTip(
            QCoreApplication.translate("MainWindow", "Move Component Down", None)
        )
        # endif // QT_CONFIG(statustip)
        self.move_down_comp_button.setText("")
        self.tab_comp_label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Species</span></p></body></html>',
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.insert_above_species_button.setToolTip(
            QCoreApplication.translate("MainWindow", "Add Species Above", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.insert_above_species_button.setStatusTip(
            QCoreApplication.translate("MainWindow", "Add Species Above", None)
        )
        # endif // QT_CONFIG(statustip)
        self.insert_above_species_button.setText("")
        # if QT_CONFIG(tooltip)
        self.insert_below_species_button.setToolTip(
            QCoreApplication.translate("MainWindow", "Add Species Below", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.insert_below_species_button.setStatusTip(
            QCoreApplication.translate("MainWindow", "Add Species Below", None)
        )
        # endif // QT_CONFIG(statustip)
        self.insert_below_species_button.setText("")
        # if QT_CONFIG(tooltip)
        self.remove_species_button.setToolTip(
            QCoreApplication.translate("MainWindow", "Remove Species", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.remove_species_button.setStatusTip(
            QCoreApplication.translate("MainWindow", "Remove Species", None)
        )
        # endif // QT_CONFIG(statustip)
        self.remove_species_button.setText("")
        # if QT_CONFIG(tooltip)
        self.move_up_species_button.setToolTip(
            QCoreApplication.translate("MainWindow", "Move Species Up", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.move_up_species_button.setStatusTip(
            QCoreApplication.translate("MainWindow", "Move Species Up", None)
        )
        # endif // QT_CONFIG(statustip)
        self.move_up_species_button.setText("")
        # if QT_CONFIG(tooltip)
        self.move_down_species_button.setToolTip(
            QCoreApplication.translate("MainWindow", "Move Species Down", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.move_down_species_button.setStatusTip(
            QCoreApplication.translate("MainWindow", "Move Species Down", None)
        )
        # endif // QT_CONFIG(statustip)
        self.move_down_species_button.setText("")
        self.tablesTab.setTabText(
            self.tablesTab.indexOf(self.species),
            QCoreApplication.translate("MainWindow", "Solution Species", None),
        )
        self.tablesTab.setTabText(
            self.tablesTab.indexOf(self.solidspecies),
            QCoreApplication.translate("MainWindow", "Solid Species", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Species),
            QCoreApplication.translate("MainWindow", "Species", None),
        )
        self.dmode_label.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Work Mode:</span></p></body></html>',
                None,
            )
        )
        self.dmode.setItemText(
            0, QCoreApplication.translate("MainWindow", "Titration", None)
        )
        self.dmode.setItemText(
            1, QCoreApplication.translate("MainWindow", "Distribution", None)
        )

        # if QT_CONFIG(statustip)
        self.dmode.setStatusTip(
            QCoreApplication.translate("MainWindow", "Select operation mode.", None)
        )
        # endif // QT_CONFIG(statustip)
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Initial and Titrant concentration:</span></p></body></html>',
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Volume Settings:</span></p></body></html>',
                None,
            )
        )
        self.v0_label.setText(
            QCoreApplication.translate("MainWindow", "Initial Volume:", None)
        )
        # if QT_CONFIG(statustip)
        self.v0.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Initial volume in the titration vessel.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.v0.setSuffix(QCoreApplication.translate("MainWindow", " ml", None))
        self.initv_label.setText(
            QCoreApplication.translate("MainWindow", "First Point Volume:", None)
        )
        # if QT_CONFIG(statustip)
        self.initv.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Volume in the vessel at the first titration point.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.initv.setSuffix(QCoreApplication.translate("MainWindow", " ml", None))
        self.vinc_label.setText(
            QCoreApplication.translate("MainWindow", "Volume Increments:", None)
        )
        # if QT_CONFIG(statustip)
        self.vinc.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Increment in volume for each titration point.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.vinc.setSuffix(QCoreApplication.translate("MainWindow", " ml", None))
        self.nop_label.setText(
            QCoreApplication.translate("MainWindow", "Number of points:", None)
        )
        # if QT_CONFIG(statustip)
        self.nop.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Number of titration points.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.nop.setSuffix("")
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Background Ions Settings:</span></p></body></html>',
                None,
            )
        )
        self.c0back_label.setText(
            QCoreApplication.translate("MainWindow", "Initial C:", None)
        )
        self.ctback_label.setText(
            QCoreApplication.translate("MainWindow", "Titrant C:", None)
        )
        # if QT_CONFIG(statustip)
        self.c0back.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Initial concentration of background ions in titration vessel.",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.c0back.setSuffix(QCoreApplication.translate("MainWindow", " mol/l", None))
        # if QT_CONFIG(statustip)
        self.ctback.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Concentration of background ions in the titrant.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.ctback.setSuffix(QCoreApplication.translate("MainWindow", " mol/l", None))
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Analytical concentration:</span></p></body></html>',
                None,
            )
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Indipendent Component Settings:</span></p></body></html>',
                None,
            )
        )
        self.initialLog_label.setText(
            QCoreApplication.translate("MainWindow", "Initial -log[A]:", None)
        )
        # if QT_CONFIG(statustip)
        self.initialLog.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Initial Log value of the indipendent component.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.finalLog_label.setText(
            QCoreApplication.translate("MainWindow", "Final -log[A]", None)
        )
        # if QT_CONFIG(statustip)
        self.finalLog.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Final Log value of the indipendent component.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.logInc_label.setText(
            QCoreApplication.translate("MainWindow", "-log[A] Increment:", None)
        )
        # if QT_CONFIG(statustip)
        self.logInc.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Log increment of the indipendent component at each point.",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.label_16.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">Background Ions Settings:</span></p></body></html>',
                None,
            )
        )
        self.cback_label.setText(
            QCoreApplication.translate("MainWindow", "Concentration:", None)
        )
        # if QT_CONFIG(tooltip)
        self.cback.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Sum of the concentrations of ionic species that do not take part in the reactions.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.cback.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Sum of the concentrations of ionic species that do not take part in the reactions.",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.cback.setSuffix(QCoreApplication.translate("MainWindow", " mol/l", None))
        self.indComp_label.setText(
            QCoreApplication.translate("MainWindow", "Indipendent Comp:", None)
        )
        # if QT_CONFIG(statustip)
        self.indComp.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Component to be considered indipendent.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Settings),
            QCoreApplication.translate("MainWindow", "Settings", None),
        )
        # if QT_CONFIG(statustip)
        self.debug.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Create a Debug Log to file.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.debug.setText(
            QCoreApplication.translate("MainWindow", "Debug to file", None)
        )
        # if QT_CONFIG(statustip)
        self.calcButton.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Launch the calculation routine.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.calcButton.setText(
            QCoreApplication.translate("MainWindow", "Calculate", None)
        )
        # if QT_CONFIG(statustip)
        self.exportButton.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Export the results in various formats.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.exportButton.setText(
            QCoreApplication.translate("MainWindow", "Export Results", None)
        )
        # if QT_CONFIG(statustip)
        self.plotDistButton.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Plot the results and export the graphs.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.plotDistButton.setText(
            QCoreApplication.translate("MainWindow", "Plot Results", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.Calc),
            QCoreApplication.translate("MainWindow", "Calculate", None),
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "?", None))
        self.toolBar.setWindowTitle(
            QCoreApplication.translate("MainWindow", "toolBar", None)
        )

    # retranslateUi
