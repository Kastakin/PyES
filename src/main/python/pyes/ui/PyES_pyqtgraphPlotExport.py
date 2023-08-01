# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyES_pyqtgraphPlotExport.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from pyqtgraph import PlotWidget
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
    QAbstractItemView,
    QApplication,
    QCheckBox,
    QComboBox,
    QFormLayout,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLayout,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QTableView,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        if not PlotWindow.objectName():
            PlotWindow.setObjectName("PlotWindow")
        PlotWindow.resize(800, 600)
        PlotWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(PlotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 5, 2, 2)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.deselect_all = QPushButton(self.widget_2)
        self.deselect_all.setObjectName("deselect_all")

        self.gridLayout.addWidget(self.deselect_all, 3, 1, 1, 1)

        self.regions_check = QCheckBox(self.widget_2)
        self.regions_check.setObjectName("regions_check")

        self.gridLayout.addWidget(self.regions_check, 1, 0, 1, 2)

        self.tabWidget_2 = QTabWidget(self.widget_2)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy1)
        self.species = QWidget()
        self.species.setObjectName("species")
        self.horizontalLayout_4 = QHBoxLayout(self.species)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.speciesView = QTableView(self.species)
        self.speciesView.setObjectName("speciesView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.speciesView.sizePolicy().hasHeightForWidth())
        self.speciesView.setSizePolicy(sizePolicy2)
        self.speciesView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.speciesView.setAlternatingRowColors(True)
        self.speciesView.horizontalHeader().setVisible(False)

        self.horizontalLayout_4.addWidget(self.speciesView)

        self.tabWidget_2.addTab(self.species, "")
        self.solids = QWidget()
        self.solids.setObjectName("solids")
        self.horizontalLayout_3 = QHBoxLayout(self.solids)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.solidsView = QTableView(self.solids)
        self.solidsView.setObjectName("solidsView")
        sizePolicy2.setHeightForWidth(self.solidsView.sizePolicy().hasHeightForWidth())
        self.solidsView.setSizePolicy(sizePolicy2)
        self.solidsView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.solidsView.setAlternatingRowColors(True)
        self.solidsView.horizontalHeader().setVisible(False)

        self.horizontalLayout_3.addWidget(self.solidsView)

        self.tabWidget_2.addTab(self.solids, "")

        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 2)

        self.filter = QPushButton(self.widget_2)
        self.filter.setObjectName("filter")

        self.gridLayout.addWidget(self.filter, 4, 0, 1, 2)

        self.select_all = QPushButton(self.widget_2)
        self.select_all.setObjectName("select_all")

        self.gridLayout.addWidget(self.select_all, 3, 0, 1, 1)

        self.errors_check = QCheckBox(self.widget_2)
        self.errors_check.setObjectName("errors_check")

        self.gridLayout.addWidget(self.errors_check, 2, 0, 1, 2)

        self.verticalLayout.addWidget(self.widget_2)

        self.horizontalLayout.addWidget(self.widget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.conc_tab = QWidget()
        self.conc_tab.setObjectName("conc_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.conc_tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.conc_graph = PlotWidget(self.conc_tab)
        self.conc_graph.setObjectName("conc_graph")

        self.horizontalLayout_2.addWidget(self.conc_graph)

        self.tabWidget.addTab(self.conc_tab, "")
        self.perc_tab = QWidget()
        self.perc_tab.setObjectName("perc_tab")
        self.verticalLayout_2 = QVBoxLayout(self.perc_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.perc_graph = PlotWidget(self.perc_tab)
        self.perc_graph.setObjectName("perc_graph")

        self.verticalLayout_2.addWidget(self.perc_graph)

        self.verticalLayout_2.setStretch(0, 1)
        self.tabWidget.addTab(self.perc_tab, "")
        self.titration_tab = QWidget()
        self.titration_tab.setObjectName("titration_tab")
        self.verticalLayout_3 = QVBoxLayout(self.titration_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.titration_graph = PlotWidget(self.titration_tab)
        self.titration_graph.setObjectName("titration_graph")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.titration_graph.sizePolicy().hasHeightForWidth()
        )
        self.titration_graph.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.titration_graph)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.componentLabel = QLabel(self.titration_tab)
        self.componentLabel.setObjectName("componentLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.componentLabel)

        self.componentComboBox = QComboBox(self.titration_tab)
        self.componentComboBox.setObjectName("componentComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.componentComboBox)

        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalLayout_3.setStretch(0, 1)
        self.tabWidget.addTab(self.titration_tab, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.exportButton = QPushButton(self.centralwidget)
        self.exportButton.setObjectName("exportButton")

        self.verticalLayout_4.addWidget(self.exportButton)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        PlotWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlotWindow)
        self.deselect_all.clicked.connect(PlotWindow.deselectAll)
        self.select_all.clicked.connect(PlotWindow.selectAll)
        self.filter.clicked.connect(PlotWindow.filterSpecies)
        self.regions_check.clicked.connect(PlotWindow.changeSolidsGraphics)
        self.errors_check.clicked.connect(PlotWindow.changeErrorsGraphics)

        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(PlotWindow)

    # setupUi

    def retranslateUi(self, PlotWindow):
        PlotWindow.setWindowTitle(
            QCoreApplication.translate("PlotWindow", "Export Plot", None)
        )
        self.deselect_all.setText(
            QCoreApplication.translate("PlotWindow", "Deselect All", None)
        )
        self.regions_check.setText(
            QCoreApplication.translate("PlotWindow", "Solids as regions", None)
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.species),
            QCoreApplication.translate("PlotWindow", "Species", None),
        )
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.solids),
            QCoreApplication.translate("PlotWindow", "Solids", None),
        )
        self.filter.setText(QCoreApplication.translate("PlotWindow", "Filter", None))
        self.select_all.setText(
            QCoreApplication.translate("PlotWindow", "Select All", None)
        )
        self.errors_check.setText(
            QCoreApplication.translate("PlotWindow", "Plot error bars", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.conc_tab),
            QCoreApplication.translate("PlotWindow", "Concentrations", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.perc_tab),
            QCoreApplication.translate("PlotWindow", "Percentages", None),
        )
        self.componentLabel.setText(
            QCoreApplication.translate("PlotWindow", "Component:", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.titration_tab),
            QCoreApplication.translate("PlotWindow", "Titration Curve", None),
        )
        self.exportButton.setText(
            QCoreApplication.translate("PlotWindow", "Export Graph", None)
        )

    # retranslateUi
