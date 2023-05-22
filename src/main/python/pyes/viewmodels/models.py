# This script handles all the models used by the UI
# to display tabular data

import re

import pandas as pd
from commands import SpeciesCellEdit
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QColorConstants, QPalette, QUndoStack
from utils_func import getName


class TitrationComponentsModel(QAbstractTableModel):
    def __init__(self, data: pd.DataFrame):
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
        self.beginInsertRows(
            index, (0 if position == -1 else position), position + rows - 1
        )

        empty_rows = pd.DataFrame(
            [[0.0 for x in range(4)] for row in range(rows)],
            columns=["C0", "CT", "Sigma C0", "Sigma CT"],
            index=["COMP" + str(position + row + 1) for row in range(rows)],
        )

        if position == -1:
            self._data = pd.concat(
                [empty_rows, self._data],
                ignore_index=True,
            )
        else:
            # for row in range(rows):
            self._data = pd.concat(
                [self._data[:position], empty_rows, self._data[position:]],
                ignore_index=True,
            )

        self.endInsertRows()
        self.layoutChanged.emit()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """Remove rows from the model."""
        self.beginRemoveRows(
            index,
            (0 if position == -1 else position),
            (0 if position == -1 else position) + rows - 1,
        )
        self._data = self._data.drop(
            self._data.index[position - rows : position], axis=0
        )

        self.endRemoveRows()
        self.layoutChanged.emit()

        return True

    def swapRows(self, first: int, second: int):
        a, b = self._data.iloc[first, :].copy(), self._data.iloc[second, :].copy()
        self._data.iloc[first, :], self._data.iloc[second, :] = b, a
        self.layoutChanged.emit()

    def swapColumns(self, first: int, second: int):
        a, b = self._data.iloc[:, first].copy(), self._data.iloc[:, second].copy()
        self._data.iloc[:, first], self._data.iloc[:, second] = b, a
        self.layoutChanged.emit()

    def rowCount(self, index=QModelIndex()):
        return self._data.index.size

    def columnCount(self, index=QModelIndex()):
        return self._data.columns.size


class ComponentsModel(QAbstractTableModel):
    def __init__(self, data: pd.DataFrame):
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
        self.beginInsertRows(
            index, (0 if position == -1 else position), position + rows - 1
        )

        empty_rows = pd.DataFrame(
            [["COMP" + str(position + row + 1)] + [0] for row in range(rows)],
            columns=self._data.columns,
        )

        if position == -1:
            self._data = pd.concat(
                [empty_rows, self._data],
                ignore_index=True,
            )
        else:
            # for row in range(rows):
            self._data = pd.concat(
                [self._data[:position], empty_rows, self._data[position:]],
                ignore_index=True,
            )

        self.endInsertRows()
        self.layoutChanged.emit()

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """Remove a row from the model."""
        self.beginRemoveRows(
            index,
            (0 if position == -1 else position),
            (0 if position == -1 else position) + rows - 1,
        )
        self._data = self._data.drop(
            self._data.index[position - rows : position], axis=0
        )

        self.endRemoveRows()
        self.layoutChanged.emit()
        return True

    def swapRows(self, first: int, second: int):
        a, b = self._data.iloc[first, :].copy(), self._data.iloc[second, :].copy()
        self._data.iloc[first, :], self._data.iloc[second, :] = b, a
        self.layoutChanged.emit()

    def swapColumns(self, first: int, second: int):
        a, b = self._data.iloc[:, first].copy(), self._data.iloc[:, second].copy()
        self._data.iloc[:, first], self._data.iloc[:, second] = b, a
        self.layoutChanged.emit()

    def rowCount(self, index=QModelIndex()):
        return self._data.index.size

    def columnCount(self, index=QModelIndex()):
        return self._data.columns.size


class _SpeciesModel(QAbstractTableModel):
    def __init__(
        self, data: pd.DataFrame, undo_stack: QUndoStack, template_header: list[str]
    ):
        super().__init__()
        self.template_header = template_header
        self._data = data
        self.undostack = undo_stack

    def data(self, index: QModelIndex, role: Qt.ItemDataRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            if index.column() != 0:
                return str(f"{value}")
            else:
                return bool(value)

        if role == Qt.ItemDataRole.UserRole:
            value = self._data.iloc[index.row(), index.column()]
            return value

        if role == Qt.ItemDataRole.BackgroundRole:
            if (index.column() >= 8) & (index.column() < self.columnCount() - 1):
                return QPalette().midlight()
            elif index.column() == 2:
                return QColorConstants.DarkCyan
            elif index.column() == 3:
                return QPalette().midlight()
            else:
                return False

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])

    def updateCompName(self, new_comp: list[str]):
        if self._data["Ref. Comp."].isin(new_comp).all() == False:
            self._data["Ref. Comp."] = self._data["Ref. Comp."].where(
                self._data["Ref. Comp."].isin(new_comp),
                new_comp[0],
            )
            return True
        else:
            return False

    def updateHeader(self, new_header: list[str]):
        self._data.columns = self.template_header + new_header + ["Ref. Comp."]

        for row in self._data.index:
            self._data.iloc[row, 1] = str(getName(self._data.iloc[row, 8:-1]))
            if self._data.iloc[row, 1] == "0":
                self._data.iloc[row, 1] = ""

        self.layoutChanged.emit()

    def flags(self, index: QModelIndex):
        # TODO: check if all these checks are needed
        if index.row() >= 0:
            if index.column() == 0:
                return (
                    Qt.ItemFlag.ItemIsEditable
                    | Qt.ItemFlag.ItemIsEnabled
                    | Qt.ItemFlag.ItemIsSelectable
                )
            elif index.column() == 1:
                return (
                    Qt.ItemFlag.ItemIsSelectable
                    | Qt.ItemFlag.ItemIsEnabled
                    | Qt.ItemFlag.ItemIsSelectable
                )
            else:
                value = self._data.iloc[index.row(), 0]
                if value == False:
                    if index.column() == self.columnCount() - 1:
                        return Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled
                    else:
                        return (
                            Qt.ItemFlag.ItemIsEditable
                            | Qt.ItemFlag.ItemIsEnabled
                            | Qt.ItemFlag.ItemIsSelectable
                        )
                else:
                    return Qt.ItemFlag.NoItemFlags
        else:
            return Qt.ItemFlag.NoItemFlags

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            # The frist column holds the ignore flag
            if index.column() == 0:
                try:
                    self.undostack.push(SpeciesCellEdit(self, index, value))
                    self.layoutChanged.emit()
                except:
                    return False
            # The second column holds the species name as a string
            elif index.column() == 1:
                self.undostack.push(SpeciesCellEdit(self, index, str(value)))
            # Columns before the coeff. holds floating point values
            elif index.column() < 8:
                try:
                    self.undostack.push(SpeciesCellEdit(self, index, float(value)))
                except:
                    return False
            # Last column always stores the info relative to % calculations
            elif index.column() == self.columnCount() - 1:
                self.undostack.push(SpeciesCellEdit(self, index, value))
            # All the other columns hold stechiometric coeff. as int
            else:
                try:
                    self.undostack.push(SpeciesCellEdit(self, index, int(value)))
                except:
                    return False
            self.dataChanged.emit(index, index)
        return True

    def insertRows(self, position: int, rows: int = 1, index=QModelIndex()):
        """Insert a row into the model."""
        self.beginInsertRows(
            index,
            (0 if position == -1 else position),
            position + rows - 1,
        )

        empty_rows = pd.DataFrame(
            [
                [False]
                + [""]
                + [0.0 for param in range(6)]
                + [int(0) for column in range(self.columnCount(index) - 9)]
                + [self._data.columns[8]]
                for row in range(rows)
            ],
            columns=self._data.columns,
        )

        if position == -1:
            self._data = pd.concat(
                [empty_rows, self._data],
                ignore_index=True,
            )
        else:
            # for row in range(rows):
            self._data = pd.concat(
                [self._data[:position], empty_rows, self._data[position:]],
                ignore_index=True,
            )

        self.endInsertRows()
        self.layoutChanged.emit()

        return True

    def removeRows(self, position: int, rows: int = 1, index=QModelIndex()):
        """Remove rows from the model."""
        self.beginRemoveRows(
            index,
            (0 if position == -1 else position),
            (0 if position == -1 else position) + rows - 1,
        )
        self._data = self._data.drop(
            self._data.index[position - rows : position], axis=0
        ).reset_index(drop=True)

        self.endRemoveRows()
        self.layoutChanged.emit()

        return True

    def insertColumns(self, position, columns=1, index=QModelIndex()):
        """Add columns to the model"""
        self.beginInsertColumns(index, position, position + columns - 1)

        for column in range(columns):
            self._data.insert(
                position + column, "COMP" + str(position + column), int(0)
            )

        self.endInsertColumns()
        self.layoutChanged.emit()

        return True

    def removeColumns(self, position: int, columns: int = 1, index=QModelIndex()):
        """Remove columns from the model."""
        start = position - columns
        finish = position
        self.beginRemoveColumns(index, start, finish)

        self._data = pd.concat(
            [self._data.iloc[:, :start], self._data.iloc[:, finish:]],
            axis=1,
        )

        self.endRemoveColumns()
        self.layoutChanged.emit()

        return True

    def swapRows(self, first: int, second: int):
        a, b = self._data.iloc[first, :].copy(), self._data.iloc[second, :].copy()
        self._data.iloc[first, :], self._data.iloc[second, :] = b, a
        self.layoutChanged.emit()

    def swapColumns(self, first: int, second: int):
        a, b = self._data.iloc[:, first].copy(), self._data.iloc[:, second].copy()
        self._data.iloc[:, first], self._data.iloc[:, second] = b, a
        self.layoutChanged.emit()

    def rowCount(self, index=QModelIndex()):
        return self._data.index.size

    def columnCount(self, index=QModelIndex()):
        return self._data.columns.size


class SolubleSpeciesModel(_SpeciesModel):
    def __init__(self, data: pd.DataFrame, undo_stack: QUndoStack):
        template_header = [
            "Ignored",
            "Name",
            "LogKs",
            "Sigma",
            "Ref. Ionic Str.",
            "CGF",
            "DGF",
            "EGF",
        ]
        super().__init__(data, undo_stack, template_header)


class SolidSpeciesModel(_SpeciesModel):
    def __init__(self, data: pd.DataFrame, undo_stack: QUndoStack):
        template_header = [
            "Ignored",
            "Name",
            "LogB",
            "Sigma",
            "Ref. Ionic Str.",
            "CGF",
            "DGF",
            "EGF",
        ]
        super().__init__(data, undo_stack, template_header)
