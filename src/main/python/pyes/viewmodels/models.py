# This script handles all the models used by the UI
# to display tabular data

import re

import pandas as pd
from commands import ComponentsCellEdit, SpeciesCellEdit
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QColorConstants, QPalette, QUndoStack
from utils_func import getName


class GenericModel(QAbstractTableModel):
    def __init__(
        self, data: pd.DataFrame | None = None, undo_stack: QUndoStack | None = None
    ) -> None:
        super().__init__()
        self._data = data
        self.undostack = undo_stack

        self.readonly_columns = set()
        self.readonly_rows = set()

    def insertRows(
        self, empty_rows: pd.DataFrame, position: int, rows: int, index=QModelIndex()
    ) -> bool:
        self.beginInsertRows(
            index, (0 if position == -1 else position), position + rows - 1
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

    def headerData(
        self, section, orientation, role: Qt.ItemDataRole = Qt.ItemDataRole.DisplayRole
    ):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])

    def updateFlags(self, flags: Qt.ItemFlag, index: QModelIndex):
        if self.columnReadOnly(index.column()):
            flags &= ~Qt.ItemFlag.ItemIsEditable
            flags &= ~Qt.ItemFlag.ItemIsEnabled
        if self.rowReadOnly(index.row()):
            flags &= ~Qt.ItemFlag.ItemIsEditable
            flags &= ~Qt.ItemFlag.ItemIsEnabled

        return flags

    def columnReadOnly(self, column):
        return column in self.readonly_columns

    def setColumnReadOnly(self, columns, readonly=True):
        for column in columns:
            if readonly:
                self.readonly_columns.add(column)
                self.layoutChanged.emit()
            else:
                self.readonly_columns.discard(column)
                self.layoutChanged.emit()

    def rowReadOnly(self, row):
        return row in self.readonly_rows

    def setRowReadOnly(self, rows, readonly=True):
        for row in rows:
            if readonly:
                self.readonly_rows.add(row)
                self.layoutChanged.emit()
            else:
                self.readonly_rows.discard(row)
                self.layoutChanged.emit()

    def showAllRows(self):
        self.readonly_rows = set()

    def showAllColumns(self):
        self.readonly_columns = set()

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


class ConcentrationsModel(GenericModel):
    def __init__(self, data: pd.DataFrame, undo_stack: QUndoStack):
        super().__init__(data, undo_stack)
        self.previous_ind_comp = 0

    def data(self, index, role: Qt.ItemDataRole = Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

        if role == Qt.ItemDataRole.UserRole:
            value = self._data.iloc[index.row(), index.column()]
            return value

    def updateIndex(self, new_index):
        self._data.index = new_index
        self.layoutChanged.emit()

    def flags(self, index):
        flags = (
            Qt.ItemFlag.ItemIsEditable
            | Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsSelectable
        )
        return self.updateFlags(flags, index)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            try:
                self.undostack.push(ComponentsCellEdit(self, index, float(value)))
                print("edited")
            except:
                return False
            self.dataChanged.emit(index, index)
            return True

    def insertRows(self, position, rows=1, index=QModelIndex()) -> bool:
        """Insert a row into the model."""
        empty_rows = pd.DataFrame(
            [[0.0 for x in range(4)] for row in range(rows)],
            columns=["C0", "CT", "Sigma C0", "Sigma CT"],
            index=["COMP" + str(position + row + 1) for row in range(rows)],
        )
        super().insertRows(empty_rows, position, rows, index)

    def setPreviousIndependentComponent(self, index: int):
        self.previous_ind_comp = index


class ComponentsModel(GenericModel):
    def __init__(self, data: pd.DataFrame, undo_stack: QUndoStack):
        super().__init__(data, undo_stack)

    def data(self, index, role: Qt.ItemDataRole = Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

        if role == Qt.ItemDataRole.UserRole:
            value = self._data.iloc[index.row(), index.column()]
            return value

    def flags(self, index):
        flags = (
            Qt.ItemFlag.ItemIsEditable
            | Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsSelectable
        )

        return self.updateFlags(flags, index)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            # First column must contain non-empty strings
            if index.column() == 0:
                if re.match(r"^\S+$", value):
                    self.undostack.push(ComponentsCellEdit(self, index, value))
                else:
                    return False
            # The other column can accept only int values
            else:
                try:
                    self.undostack.push(ComponentsCellEdit(self, index, int(value)))
                except:
                    return False
            self.dataChanged.emit(index, index)
        return True

    def insertRows(self, position, rows=1, index=QModelIndex()) -> bool:
        """Insert a row into the model."""
        empty_rows = pd.DataFrame(
            [["COMP" + str(position + row + 1)] + [0] for row in range(rows)],
            columns=self._data.columns,
        )

        super().insertRows(empty_rows, position, rows, index)


class GenericSpeciesModel(GenericModel):
    def __init__(
        self, data: pd.DataFrame, undo_stack: QUndoStack, template_header: list[str]
    ):
        super().__init__(data, undo_stack)
        self.template_header = template_header

    def data(
        self, index: QModelIndex, role: Qt.ItemDataRole = Qt.ItemDataRole.DisplayRole
    ):
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
        if index.column() == 0:
            flags = Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled
        elif index.column() == 1:
            flags = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
        else:
            value = self._data.iloc[index.row(), 0]
            if value == False:
                if index.column() == self.columnCount() - 1:
                    flags = Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled
                else:
                    flags = (
                        Qt.ItemFlag.ItemIsEditable
                        | Qt.ItemFlag.ItemIsEnabled
                        | Qt.ItemFlag.ItemIsSelectable
                    )
            else:
                flags = Qt.ItemFlag.NoItemFlags

        return self.updateFlags(flags, index)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
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

    def insertRows(self, position: int, rows: int = 1, index=QModelIndex()) -> bool:
        """Insert a row into the model."""
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
        super().insertRows(empty_rows, position, rows, index)

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


class SolubleSpeciesModel(GenericSpeciesModel):
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


class SolidSpeciesModel(GenericSpeciesModel):
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
