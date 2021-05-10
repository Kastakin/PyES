import math
import time
import logging
from datetime import datetime

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot

from optimizers.titration import Titration
from optimizers.distribution import Distribution


# Main optimization routine worker and signals
class optimizeSignal(QObject):
    log = pyqtSignal(str)
    aborted = pyqtSignal(str)
    finished = pyqtSignal()
    result = pyqtSignal(object)


class optimizeWorker(QRunnable):
    def __init__(self, data_list, debug):
        super().__init__()
        self.signals = optimizeSignal()
        self.data = data_list
        self.debug = debug

    @pyqtSlot()
    def run(self):
        # If run with debug enabled create the logging istance
        if self.debug:
            date_time = datetime.now()
            log_file = "logs/" + date_time.strftime("%d_%m_%Y-%H:%M:%S") + "_logS4.log"
            filehandler = logging.FileHandler(log_file)
            formatter = logging.Formatter("%(levelname)s:%(message)s")
            filehandler.setFormatter(formatter)
            log = logging.getLogger()  # root logger - Good to get it only once.
            for hdlr in log.handlers[:]:  # remove the existing file handlers
                if isinstance(hdlr, logging.FileHandler):
                    log.removeHandler(hdlr)
            log.addHandler(filehandler)
            log.setLevel(logging.DEBUG)

        if self.data["dmode"] == 0:
            ## TITRATION MODE ##
            # TODO: Error handling is still a bit weak, need testing
            optimizer = Titration()
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
            self.signals.log.emit(r"Simulating titration curve...")
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
        else:
            ## DISTRIBUTION MODE ##
            # TODO: Error handling is still a bit weak, need testing
            optimizer = Distribution()
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

        return None
