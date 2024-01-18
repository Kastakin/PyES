import numpy as np
import pandas as pd
from openpyxl.utils import get_column_letter
from PySide6.QtCore import QAbstractItemModel
from PySide6.QtWidgets import QComboBox, QTableView
from viewmodels.delegate import ComboBoxDelegate


def addSpeciesComp(position: int, added_rows: int, view: QTableView, comp_names):
    view.setItemDelegateForColumn(view.model().columnCount() - 1, None)
    view.model().insertColumns(position, added_rows)
    view.setItemDelegateForColumn(
        view.model().columnCount() - 1,
        ComboBoxDelegate(view, comp_names),
    )


def removeSpeciesComp(position: int, removed_rows: int, view: QTableView, comp_names):
    view.setItemDelegateForColumn(view.model().columnCount() - 1, None)
    view.model().removeColumns(position, removed_rows)
    view.setItemDelegateForColumn(
        view.model().columnCount() - 1,
        ComboBoxDelegate(view, comp_names),
    )

def updateCompNames(
    comp_model: QAbstractItemModel,
    species_table: QTableView,
    solids_table: QTableView,
    conc_model: QAbstractItemModel,
    ind_comp: QComboBox,
):
    """
    Handles the displayed names in the species table when edited in the components one
    """
    species_tables = [species_table, solids_table]
    species_models = [table.model() for table in species_tables]

    updated_comps = comp_model._data["Name"].tolist()

    for table, model in zip(species_tables, species_models):
        table.setItemDelegateForColumn(
            model.columnCount() - 1,
            ComboBoxDelegate(table, updated_comps),
        )
        model.updateHeader(updated_comps)
        model.updateCompName(updated_comps)

    conc_model.updateIndex(updated_comps)

    updateIndComponent(comp_model, ind_comp)


def updateIndComponent(comp_model: QAbstractItemModel, components_combobox: QComboBox):
    """
    Update the selected indipendent component, tries to preserve the last one picked.
    """
    old_selected = components_combobox.currentIndex()
    if old_selected < 0:
        old_selected = 0

    components_combobox.blockSignals(True)
    components_combobox.clear()
    components_combobox.addItems(comp_model._data["Name"])
    components_combobox.blockSignals(False)

    num_elements = components_combobox.count()
    if num_elements > old_selected:
        components_combobox.setCurrentIndex(old_selected)
    else:
        components_combobox.setCurrentIndex(num_elements - 1)


def cleanData():
    """
    Returns clean data to be used in the initialization
    of the software
    """

    conc_data = pd.DataFrame(
        [[0.0 for x in range(4)]],
        columns=["C0", "CT", "Sigma C0", "Sigma CT"],
        index=["A"],
    )
    comp_data = pd.DataFrame(
        [["A", 0]],
        columns=[
            "Name",
            "Charge",
        ],
    )
    species_data = pd.DataFrame(
        [[False] + [""] + [0.0 for x in range(6)] + [int(0)] + ["A"]],
        columns=[
            "Ignored",
            "Name",
            "LogB",
            "Sigma",
            "Ref. Ionic Str.",
            "CG",
            "DG",
            "EG",
            "A",
            "Ref. Comp.",
        ],
    )
    solid_species_data = pd.DataFrame(
        [[False] + [""] + [0.0 for x in range(6)] + [int(0)] + ["A"]],
        columns=[
            "Ignored",
            "Name",
            "LogKs",
            "Sigma",
            "Ref. Ionic Str.",
            "CG",
            "DG",
            "EG",
            "A",
            "Ref. Comp.",
        ],
    ).drop(0)

    return conc_data, comp_data, species_data, solid_species_data


def getName(vector):
    """
    Get name of species given their coefficients.
    """
    # TODO: rewrite, this is garbage and difficult to understand, maybe refactor
    comps = vector.index.to_numpy(copy=True)
    coeff = vector.to_numpy(copy=True)
    comps = comps[coeff != 0]
    coeff = coeff[coeff != 0]
    comps = np.where(coeff < 0, "OH", comps)
    coeff = np.abs(coeff)
    comps = np.where(
        coeff > 1, "(" + comps + ")" + coeff.astype(str), "(" + comps + ")"
    )
    return "".join(comps)


def getColWidths(dataframe):
    """
    Function to be used in conjuction with openpyxl to adjust width to tontent of a dataframe.
    """
    # Find the maximum length for the index
    idx_max = [len(str(dataframe.index.name)) + 5]

    cols_max = [(len(col) + 5) for col in dataframe.columns]
    # Concatenate the two
    return idx_max + cols_max


def adjustColumnWidths(wb, ws_name, data):
    """
    Given a worksheet apply the desired widths to all the columns
    """
    ws = wb[ws_name]
    widths = getColWidths(data)

    for i, column_width in enumerate(widths):
        ws.column_dimensions[get_column_letter(i + 1)].width = column_width
