import logging
import time
from datetime import datetime

from PySide6.QtCore import QObject, QRunnable, Signal, Slot

from optimizers.distribution import Distribution
from optimizers.titration import Titration


# Main optimization routine worker and signals
class optimizeSignal(QObject):
    log = Signal(str)
    aborted = Signal(str)
    finished = Signal()
    result = Signal(object, str)


class optimizeWorker(QRunnable):
    def __init__(self, data_list, debug):
        super().__init__()
        self.signals = optimizeSignal()
        self.data = data_list
        self.debug = debug

    @Slot()
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
        if self.data["dmode"] == 0:
            self.signals.log.emit(r"Calculating species concentration for the simulated titration...")
            start_time = time.time()
            self.signals.log.emit("--" * 40)
        else:
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

        species_distribution = optimizer.speciesDistribution()
        solid_distribution = optimizer.solidDistribution()
        species_percentages, solid_percentages = optimizer.percentages()
        species_info, solid_info, comp_info = optimizer.parameters()

        # Store input info
        self._storeResult(species_info, "species_info")
        self._storeResult(comp_info, "comp_info")

        # Print and store species results
        self._storeResult(species_distribution, "species_distribution", log=True)

        # Print and store species percentages
        self._storeResult(species_percentages, "species_percentages", log=True)

        if self.data["np"] > 0:
            # Store input info regarding solids
            self._storeResult(solid_info, "solid_info")
            # Print and store solid species results
            self._storeResult(solid_distribution, "solid_distribution", log=True)

            # Print and store solid species percentages
            self._storeResult(solid_percentages, "solid_percentages", log=True)

        # If working at variable ionic strength print and store formation constants/solubility products aswell
        if self.data["imode"] == 1:
            formation_constants = optimizer.formationConstants()
            self._storeResult(formation_constants, "formation_constants", log=True)

            if self.data["np"] > 0:
                solubility_products = optimizer.solubilityProducts()
                self._storeResult(
                    solubility_products, "solubility_products", log=True
                )

        self.signals.log.emit("Elapsed Time: %s s" % elapsed_time)

        self.signals.log.emit("### FINISHED ###")
        self.signals.finished.emit()

        return None

    def _storeResult(self, data, name, log=False):
        self.signals.result.emit(data, name)
        if log == True:
            self.signals.log.emit(data.to_string())
            self.signals.log.emit("--" * 40)
