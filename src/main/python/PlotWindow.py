from ui.sssc_plotExport import Ui_plotWindow

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QSizePolicy


class PlotWindow(QWidget, Ui_plotWindow):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)

        self.result = parent.result

        self.plot.plot(
            [self.result.index for i in range(self.result.shape[1])],
            [self.result[i] for i in self.result.columns],
            self.result.columns,
            "Titrant Volume [ml]",
            "Concentration [mol/L]",
            "Titration Curve",
            new=True,
        )

    def exportPlot(self):
        self.plot.canvas.figure.savefig("/home/lorenzo/test.png", dpi=300)

    def closeEvent(self, event):
        pass
