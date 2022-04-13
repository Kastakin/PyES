# This script handles all the models used by the UI
# to display tabular data

import re

import pandas as pd
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QColorConstants
from utils_func import getName


class TitrationComponentsModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def updateIndex(self, new_index):
        self._data.index = new_index
        self.layoutChanged.emit()

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            try:
                self._data.iloc[index.row(), index.column()] = float(value)
            except:
                return False
            self.dataChanged.emit(index, index)
        return True

    def insertRows(self, position, rows=1, index=QModelIndex()):
        """Insert a row into the model."""
        self.beginInsertRows(index, position, position + rows - 1)

        empty_rows = pd.DataFrame(
            [[0.0 for x in range(4)] for row in range(rows)],
            columns=["C0", "CT", "Sigma C0", "Sigma CT"],
            index=["COMP" + str(position + row + 1) for row in range(rows)],
        )
        self._data = pd.concat([self._data, empty_rows], ignore_index=True)

        self.endInsertRows()
        self.layoutChanged.emit()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """Remove a row from the model."""
        self.beginRemoveRows(index, position, position + rows - 1)

        self._data = self._data.drop(
            self._data.index[position - rows : position], axis=0
        )

        self.endRemoveRows()
        self.layoutChanged.emit()
        return True

    def rowCount(self, index=QModelIndex()):
        return self._data.shape[0]

    def columnCount(self, index=QModelIndex()):
        return self._data.shape[1]


class ComponentsModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            # First column must contain non-empty strings
            if index.column() == 0:
                if re.match(r"^\S+$", value):
                    self._data.iloc[index.row(), index.column()] = value
                else:
                    return False
            # The other column can accept only int values
            else:
                try:
                    self._data.iloc[index.row(), index.column()] = int(value)
                except:
                    return False
            self.dataChanged.emit(index, index)
        return True

    def insertRows(self, position, rows=1, index=QModelIndex()):
        """Insert a row into the model."""
        self.beginInsertRows(index, position, position + rows - 1)

        empty_rows = pd.DataFrame(
            [["COMP" + str(position + row + 1)] + [0] for row in range(rows)],
            columns=[
                "Name",
                "Charge",
            ],
        )
        self._data = pd.concat([self._data, empty_rows], ignore_index=True)

        self.endInsertRows()
        self.layoutChanged.emit()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """Remove a row from the model."""
        self.beginRemoveRows(index, position, position + rows - 1)

        self._data = self._data.drop(
            self._data.index[position - rows : position], axis=0
        )

        self.endRemoveRows()
        self.layoutChanged.emit()
        return True

    def rowCount(self, index=QModelIndex()):
        return self._data.shape[0]

    def columnCount(self, index=QModelIndex()):
        return self._data.shape[1]


class SpeciesModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            if index.column() != 0:
                return str("{}".format(value))
            else:
                return bool(value)

        if role == Qt.BackgroundRole:
            if (index.column() >= 8) & (index.column() < self.columnCount() - 1):
                return QColorConstants.LightGray
            elif index.column() == 2:
                return QColorConstants.DarkCyan
            elif index.column() == 3:
                return QColorConstants.LightGray
            elif index.column() == self.columnCount() - 1:
                return False
            else:
                return QColorConstants.White

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def updateCompName(self, new_comp):
        if self._data["Comp. %"].isin(new_comp).all() == False:
            self._data["Comp. %"] = self._data["Comp. %"].where(
                self._data["Comp. %"].isin(new_comp),
                new_comp[0],
            )
            return True
        else:
            return False

    def updateHeader(self, new_header):
        self._data.columns = (
            [
                "Ignored",
                "Name",
                "LogB",
                "Sigma",
                "Ref. Ionic Str.",
                "CG",
                "DG",
                "EG",
            ]
            + new_header
            + ["Comp. %"]
        )

        for row in self._data.index:
            self._data.iloc[row, 1] = str(getName(self._data.iloc[row, 8:-1]))
            if self._data.iloc[row, 1] == "0":
                self._data.iloc[row, 1] = ""

        self.layoutChanged.emit()

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled
        elif index.column() == 1:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        else:
            value = self._data.iloc[index.row(), 0]
            if value == False:
                if index.column() == self.columnCount() - 1:
                    return Qt.ItemIsEditable | Qt.ItemIsEnabled
                else:
                    return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
            else:
                return Qt.NoItemFlags

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            # The frist column holds the ignore flag
            if index.column() == 0:
                try:
                    self._data.iloc[index.row(), index.column()] = value
                    self.layoutChanged.emit()
                except:
                    return False
            # The second column holds the species name as a string
            elif index.column() == 1:
                self._data.iloc[index.row(), index.column()] = str(value)
            # Columns before the coeff. holds floating point values
            elif index.column() < 8:
                try:
                    self._data.iloc[index.row(), index.column()] = float(value)
                except:
                    return False
            # Last column always stores the info relative to % calculations
            elif index.column() == self.columnCount() - 1:
                self._data.iloc[index.row(), index.column()] = value
            # All the other columns hold stechiometric coeff. as int
            else:
                try:
                    self._data.iloc[index.row(), index.column()] = int(value)
                except:
                    return False
                # Updating coeff. should update the corresponding species name
                self._data.iloc[index.row(), 1] = str(
                    getName(self._data.iloc[index.row(), 8:-1])
                )
            self.dataChanged.emit(index, index)
        return True

    def insertRows(self, position, rows=1, index=QModelIndex()):
        """Insert a row into the model."""
        self.beginInsertRows(index, position, position + rows - 1)

        empty_rows = pd.DataFrame(
            [
                [False]
                + [""]
                + [0.0 for x in range(6)]
                + [int(0) for x in range(self.columnCount(index) - 9)]
                + [self._data.columns[8]]
                for row in range(rows)
            ],
            columns=self._data.columns,
        )

        # for row in range(rows):
        self._data = pd.concat([self._data, empty_rows], ignore_index=True)

        self.endInsertRows()
        self.layoutChanged.emit()

        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """Remove rows from the model."""
        self.beginRemoveRows(index, position, position + rows - 1)

        self._data = self._data.drop(
            self._data.index[position - rows : position], axis=0
        )

        self.endRemoveRows()
        self.layoutChanged.emit()

        return True

    def insertColumns(self, position, columns=1, index=QModelIndex()):
        """Add columns to the model"""
        start = position + 1
        finish = position + columns
        self.beginInsertColumns(index, position, position + columns - 1)

        for column in range(columns):
            self._data.insert(position + column, "COMP" + str(position + column), 0)

        self.endInsertColumns()
        self.layoutChanged.emit()

        return True

    def removeColumns(self, position, columns=1, index=QModelIndex()):
        """Remove columns from the model."""
        start = position - columns
        finish = position
        self.beginRemoveColumns(index, start, finish)

        self._data = self._data.drop(self._data.columns[start:finish], axis=1)

        self.endRemoveColumns()
        self.layoutChanged.emit()

        return True

    def rowCount(self, index=QModelIndex()):
        return self._data.shape[0]

    def columnCount(self, index=QModelIndex()):
        return self._data.shape[1]


class SolidSpeciesModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            if index.column() != 0:
                return str("{}".format(value))
            else:
                return bool(value)

        if role == Qt.BackgroundRole:
            if (index.column() >= 8) & (index.column() < self.columnCount() - 1):
                return QColorConstants.LightGray
            elif index.column() == 2:
                return QColorConstants.DarkCyan
            elif index.column() == 3:
                return QColorConstants.LightGray
            elif index.column() == self.columnCount() - 1:
                return False
            else:
                return QColorConstants.White

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def updateCompName(self, new_comp):
        if self._data["Comp. %"].isin(new_comp).all() == False:
            self._data["Comp. %"] = self._data["Comp. %"].where(
                self._data["Comp. %"].isin(new_comp),
                new_comp[0],
            )
            return True
        else:
            return False

    def updateHeader(self, new_header):
        self._data.columns = (
            [
                "Ignored",
                "Name",
                "LogKs",
                "Sigma",
                "Ref. Ionic Str.",
                "CGF",
                "DGF",
                "EGF",
            ]
            + new_header
            + ["Comp. %"]
        )

        for row in self._data.index:
            self._data.iloc[row, 1] = str(getName(self._data.iloc[row, 8:-1]))
            if self._data.iloc[row, 1] == "0":
                self._data.iloc[row, 1] = ""

        self.layoutChanged.emit()

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled
        elif index.column() == 1:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        else:
            value = self._data.iloc[index.row(), 0]
            if value == False:
                if index.column() == self.columnCount() - 1:
                    return Qt.ItemIsEditable | Qt.ItemIsEnabled
                else:
                    return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
            else:
                return Qt.NoItemFlags

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            # The frist column holds the ignore flag
            if index.column() == 0:
                try:
                    self._data.iloc[index.row(), index.column()] = value
                    self.layoutChanged.emit()
                except:
                    return False
            # The second column holds the species name as a string
            elif index.column() == 1:
                self._data.iloc[index.row(), index.column()] = str(value)
            # Columns before the coeff. holds floating point values
            elif index.column() < 8:
                try:
                    self._data.iloc[index.row(), index.column()] = float(value)
                except:
                    return False
            # Last column always stores the info relative to % calculations
            elif index.column() == self.columnCount() - 1:
                self._data.iloc[index.row(), index.column()] = value
            # All the other columns hold stechiometric coeff. as int
            else:
                try:
                    self._data.iloc[index.row(), index.column()] = int(value)
                except:
                    return False
                # Updating coeff. should update the corresponding species name
                self._data.iloc[index.row(), 1] = str(
                    getName(self._data.iloc[index.row(), 8:-1])
                )
            self.dataChanged.emit(index, index)
        return True

    def insertRows(self, position, rows=1, index=QModelIndex()):
        """Insert a row into the model."""
        self.beginInsertRows(index, position, position + rows - 1)

        empty_rows = pd.DataFrame(
            [
                [False]
                + [""]
                + [0.0 for x in range(6)]
                + [int(0) for x in range(self.columnCount(index) - 9)]
                + [self._data.columns[8]]
                for row in range(rows)
            ],
            columns=self._data.columns,
        )

        self._data = pd.concat([self._data, empty_rows], ignore_index=True)

        self.endInsertRows()
        self.layoutChanged.emit()

        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """Remove rows from the model."""
        self.beginRemoveRows(index, position, position + rows - 1)

        self._data = self._data.drop(
            self._data.index[position - rows : position], axis=0
        )

        self.endRemoveRows()
        self.layoutChanged.emit()

        return True

    def insertColumns(self, position, columns=1, index=QModelIndex()):
        """Add columns to the model"""
        start = position + 1
        finish = position + columns
        self.beginInsertColumns(index, position, position + columns - 1)

        for column in range(columns):
            self._data.insert(position + column, "COMP" + str(position + column), 0)

        self.endInsertColumns()
        self.layoutChanged.emit()

        return True

    def removeColumns(self, position, columns=1, index=QModelIndex()):
        """Remove columns from the model."""
        start = position - columns
        finish = position
        self.beginRemoveColumns(index, start, finish)

        self._data = self._data.drop(self._data.columns[start:finish], axis=1)

        self.endRemoveColumns()
        self.layoutChanged.emit()

        return True

    def rowCount(self, index=QModelIndex()):
        return self._data.shape[0]

    def columnCount(self, index=QModelIndex()):
        return self._data.shape[1]
