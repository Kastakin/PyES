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
        self.signals.log.emit(r"Beginning optimization routine...")
        start_time = time.time()
        self.signals.log.emit("--" * 40)

        # use the provided model to optimize required parameters, store the results
        try:
            results = optimizer.predict()
            # Calculate elapsed time between start to finish
            elapsed_time = round((time.time() - start_time), 5)
        except Exception as e:
            self.signals.aborted.emit(str(e))
            return None

        self.signals.log.emit("\n".join(results[0]))
        self.signals.log.emit("--" * 40)
        self.signals.log.emit(results[1].to_string())

        # Plot the species distribution using the optimized parameters
        self.signals.result.emit(results[1])

        self.signals.log.emit("--" * 40)
        self.signals.log.emit("Elapsed Time: %s s" % elapsed_time)

        self.signals.log.emit("### FINISHED ###")
        self.signals.finished.emit()
