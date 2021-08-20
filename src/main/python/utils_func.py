import numpy as np
import pandas as pd
from openpyxl.utils import get_column_letter


# TODO: has to be updated from legacy code
def returnDataDict(self, saving=True):
    """
    Returns a dict containing the relevant data extracted from the form.

    If saving is True dataframes/tables are returned as dictionaries for ease of storage reasons.
    Otherwise dictionay will simply hold the dataframes as they are.
    """
    data_list = {
        "nc": self.numComp.value(),
        "ns": self.numSpecies.value(),
        "np": self.numPhases.value(),
        "emode": self.relErrorMode.currentIndex(),
        "imode": self.imode.currentIndex(),
        "ris": self.refIonicStr.value(),
        "a": self.A.value(),
        "b": self.B.value(),
        "c0": self.c0.value(),
        "c1": self.c1.value(),
        "d0": self.d0.value(),
        "d1": self.d1.value(),
        "e0": self.e0.value(),
        "e1": self.e1.value(),
        "dmode": self.dmode.currentIndex(),
        "v0": self.v0.value(),
        "initv": self.initv.value(),
        "vinc": self.vinc.value(),
        "nop": self.nop.value(),
        "c0back": self.c0back.value(),
        "ctback": self.ctback.value(),
        "ind_comp": self.indComp.currentIndex(),
        "initialLog": self.initialLog.value(),
        "finalLog": self.finalLog.value(),
        "logInc": self.logInc.value(),
        "cback": self.cback.value(),
    }

    if saving:
        data_models = {
            "compModel": self.compModel._data.to_dict(),
            "concModel": self.concModel._data.to_dict(),
        }
        if self.numSpecies.value() > 0:
            data_models["speciesModel"] = self.speciesModel._data.to_dict()
        if self.numPhases.value() > 0:
            data_models["solidSpeciesModel"] = self.solidSpeciesModel._data.to_dict()
    else:
        data_models = {
            "compModel": self.compModel._data,
            "speciesModel": self.speciesModel._data,
            "solidSpeciesModel": self.solidSpeciesModel._data,
            "concModel": self.concModel._data,
        }

    data_list = {**data_list, **data_models}

    return data_list


def indCompUpdater(self):
    """
    Update the selected indipendent component, tries to preserve the last one picked.
    """
    old_selected = self.indComp.currentIndex()
    if old_selected < 0:
        old_selected = 0
    self.indComp.clear()
    self.indComp.addItems(self.compModel._data["Name"])
    num_elements = self.indComp.count()
    if num_elements >= old_selected:
        self.indComp.setCurrentIndex(old_selected)
    else:
        self.indComp.setCurrentIndex(num_elements)


def cleanData():
    """
    Returns clean data to be used in the initialization
    of the software
    """

    conc_data = pd.DataFrame(
        [[0.0 for x in range(4)]],
        columns=["C0", "CT", "Sigma C0", "Sigma CT"],
        index=["COMP1"],
    )
    comp_data = pd.DataFrame(
        [["COMP1", 0]],
        columns=[
            "Name",
            "Charge",
        ],
    )
    species_data = pd.DataFrame(
        [[False] + [""] + [0.0 for x in range(6)] + [0] + ["COMP1"]],
        columns=[
            "Ignored",
            "Name",
            "LogB",
            "Sigma",
            "Ref. Ionic Str.",
            "CG",
            "DG",
            "EG",
            "COMP1",
            "Comp. %",
        ],
    )
    solid_species_data = pd.DataFrame(
        [[False] + [""] + [0.0 for x in range(6)] + [0] + ["COMP1"]],
        columns=[
            "Ignored",
            "Name",
            "LogB",
            "Sigma",
            "Ref. Ionic Str.",
            "CG",
            "DG",
            "EG",
            "COMP1",
            "Comp. %",
        ],
    ).drop(0)

    return conc_data, comp_data, species_data, solid_species_data


def getName(vector):
    """
    Get name of species given their coefficients.
    """
    comps = vector.index.to_numpy(copy=True)
    coeff = vector.to_numpy(copy=True)
    comps = comps[coeff != 0]
    coeff = coeff[coeff != 0]
    comps = np.where(coeff < 0, "OH", comps)
    coeff = np.abs(coeff)
    comps = np.where(
        coeff > 1, "(" + comps + ")" + coeff.astype(str), "(" + comps + ")"
    )
    return comps.sum()


def getColWidths(dataframe):
    """
    Function to be used in conjuction with openpyxl to adjust width to tontent of a dataframe.
    """
    # Find the maximum length for the index
    idx_max = [len(str(dataframe.index.name)) + 5]

    cols_max = [(len(col) + 5) for col in dataframe.columns]
    # Concatenate the two
    return idx_max + cols_max


def adjustWidths(ws, widths):
    """
    Given a worksheet apply the desired withs to all the columns
    """
    for i, column_width in enumerate(widths):
        ws.column_dimensions[get_column_letter(i + 1)].width = column_width
