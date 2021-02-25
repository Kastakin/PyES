import numpy as np


def returnDataDict(self, saving=True):
    """
    Returns a dict containing the relevant data extracted from the form.

    If saving is True dataframes/tables are returned as dictionaries for ease of storage reasons.
    Otherwise dictionay will simply hold the dataframes as they are.
    """
    if saving:
        data_list = {
            "wmode": self.wmode.currentIndex(),
            "nc": self.numComp.value(),
            "ns": self.numSpecies.value(),
            "v0": self.vesselVolume.value(),
            "sv": self.sd_v.value(),
            "ph_range": [self.initialph.value(), self.finalph.value()],
            "std_pot": self.electrodeSP.value(),
            "se": self.sd_e.value(),
            "comp_pot": self.potComp.currentIndex(),
            "compModel": self.compModel._data.to_dict(),
            "speciesModel": self.speciesModel._data.to_dict(),
            "tritModel": self.tritModel._data.to_dict(),
            "tritCompModel": self.tritCompModel._data.to_dict(),
        }
    else:
        data_list = {
            "wmode": self.wmode.currentIndex(),
            "nc": self.numComp.value(),
            "ns": self.numSpecies.value(),
            "v0": self.vesselVolume.value(),
            "sv": self.sd_v.value(),
            "ph_range": [self.initialph.value(), self.finalph.value()],
            "std_pot": self.electrodeSP.value(),
            "se": self.sd_e.value(),
            "comp_pot": self.potComp.currentIndex(),
            "compModel": self.compModel._data,
            "speciesModel": self.speciesModel._data,
            "tritModel": self.tritModel._data,
            "tritCompModel": self.tritCompModel._data,
        }
    return data_list


def potCompUpdater(self):
    """
    Update the selected electroactive component, tries to preserve the last one picked.
    """
    old_selected = self.potComp.currentIndex()
    if old_selected < 0:
        old_selected = 0
    self.potComp.clear()
    self.potComp.addItems(self.compModel._data["Name"])
    num_elements = self.potComp.count()
    if num_elements >= old_selected:
        self.potComp.setCurrentIndex(old_selected)
    else:
        self.potComp.setCurrentIndex(num_elements)
