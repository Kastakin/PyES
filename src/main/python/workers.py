import math
import time

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot

from optimizer import Optimizer


# Main optimization routine worker and signals
class optimizeSignal(QObject):
    log = pyqtSignal(str)
    aborted = pyqtSignal(str)
    finished = pyqtSignal()
    result = pyqtSignal(object)


class optimizeWorker(QRunnable):
    def __init__(self, data_list):
        super().__init__()
        self.signals = optimizeSignal()
        self.data = data_list

    @pyqtSlot()
    def run(self):
        # TODO: Error handling is still a bit weak, need testing
        optimizer = Optimizer()
        # Start timer to time entire process
        start_time = time.time()

        self.signals.log.emit(r"### Beginning Optimization ###")
        self.signals.log.emit(r"Loading data...")

        # load the data into the optimizer, catch errors that might invalidate the output
        try:
            optimizer.fit(self.data)
        except Exception as e:
            self.signals.aborted.emit(str(e))
            return None

        self.signals.log.emit(r"DATA LOADED!")
        self.signals.log.emit(r"Calculating distribution of the species...")
        start_time = time.time()
        self.signals.log.emit("--" * 40)

        # predict species distribution 
        try:
            optimizer.predict()
            # Calculate elapsed time between start to finish
            elapsed_time = round((time.time() - start_time), 5)
        except Exception as e:
            self.signals.aborted.emit(str(e))
            return None

        distribution = optimizer.distribution()

        # Print species distribution as text in the log console
        self.signals.log.emit(distribution.to_string())

        # Plot the species distribution using the optimized parameters
        self.signals.result.emit(distribution)

        self.signals.log.emit("--" * 40)
        self.signals.log.emit("Elapsed Time: %s s" % elapsed_time)

        self.signals.log.emit("### FINISHED ###")
        self.signals.finished.emit()

# TODO: worker for exporting calculated data

# TODO: worker for exporting plot