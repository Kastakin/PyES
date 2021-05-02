# This script handles all the models used by the UI
# to display tabular data

import re

import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from PyQt5.QtGui import QColor


class PreviewModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self._data = pd.DataFrame([[0, 0]])

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

    def rowCount(self, index=QModelIndex()):
        return self._data.shape[0]

    def columnCount(self, index=QModelIndex()):
        return self._data.shape[1]


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
        """ Insert a row into the model. """
        self.beginInsertRows(index, position, position + rows - 1)

        for row in range(rows):
            empty_row = pd.DataFrame(
                [[0.0 for x in range(4)]],
                columns=["C0", "CT", "Sigma C0", "Sigma CT"],
                index=["COMP" + str(position + row + 1)],
            )
            self._data = self._data.append(empty_row, ignore_index=False)

        self.endInsertRows()
        self.layoutChanged.emit()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """ Remove a row from the model. """
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
        """ Insert a row into the model. """
        self.beginInsertRows(index, position, position + rows - 1)

        for row in range(rows):
            empty_row = pd.DataFrame(
                [["COMP" + str(position + row + 1)] + [0]],
                columns=[
                    "Name",
                    "Charge",
                ],
            )
            self._data = self._data.append(empty_row, ignore_index=True)

        self.endInsertRows()
        self.layoutChanged.emit()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """ Remove a row from the model. """
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
                return QVariant("{0}".format(value))
            else:
                return QVariant(value)

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def updateHeader(self, new_header):
        self._data.columns = [
            "Ignored",
            "LogB",
            "Sigma",
            "Ref. Ionic Str.",
            "CG",
            "DG",
            "EG",
        ] + new_header
        self.layoutChanged.emit()

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled
        else:
            value = self._data.iloc[index.row(), 0]
            if value == False:
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
            # The following 6 columns are float values
            elif index.column() < 7:
                try:
                    self._data.iloc[index.row(), index.column()] = float(value)
                except:
                    return False
            # All the other columns hold stechiometric coeff. as int
            else:
                try:
                    self._data.iloc[index.row(), index.column()] = int(value)
                except:
                    return False
            self.dataChanged.emit(index, index)
        return True

    def insertRows(self, position, rows=1, index=QModelIndex()):
        """ Insert a row into the model. """
        self.beginInsertRows(index, position, position + rows - 1)

        empty_row = pd.DataFrame(
            [
                [False]
                + [0.0 for x in range(6)]
                + [0 for x in range(self.columnCount(index) - 7)],
            ],
            columns=self._data.columns,
        )

        for row in range(rows):
            self._data = self._data.append(empty_row, ignore_index=True)

        self.endInsertRows()
        self.layoutChanged.emit()

        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """ Remove rows from the model. """
        self.beginRemoveRows(index, position, position + rows - 1)

        self._data = self._data.drop(
            self._data.index[position - rows : position], axis=0
        )

        self.endRemoveRows()
        self.layoutChanged.emit()

        return True

    def insertColumns(self, position, columns=1, index=QModelIndex()):
        """ Add columns to the model """
        self.beginInsertColumns(index, position, position + columns - 1)

        for column in range(columns):
            self._data.insert(position + column, "COMP" + str(position + column), 0)

        self.endInsertColumns()
        self.layoutChanged.emit()

        return True

    def removeColumns(self, position, columns=1, index=QModelIndex()):
        """ Remove columns from the model. """
        self.beginRemoveColumns(index, position, position + columns - 1)

        self._data = self._data.drop(
            self._data.columns[position - columns : position], axis=1
        )

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
                return QVariant("{0}".format(value))
            else:
                return QVariant(value)

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def updateHeader(self, new_header):
        self._data.columns = [
            "Ignored",
            "LogKs",
            "Sigma",
            "Ref. Ionic Str.",
            "CGF",
            "DGF",
            "EGF",
        ] + new_header
        self.layoutChanged.emit()

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled
        else:
            value = self._data.iloc[index.row(), 0]
            if value == False:
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
            # The following 6 columns are float values
            elif index.column() < 7:
                try:
                    self._data.iloc[index.row(), index.column()] = float(value)
                except:
                    return False
            # All the other columns hold stechiometric coeff. as int
            else:
                try:
                    self._data.iloc[index.row(), index.column()] = int(value)
                except:
                    return False
            self.dataChanged.emit(index, index)
        return True

    def insertRows(self, position, rows=1, index=QModelIndex()):
        """ Insert a row into the model. """
        self.beginInsertRows(index, position, position + rows - 1)

        empty_row = pd.DataFrame(
            [
                [False]
                + [0.0 for x in range(6)]
                + [0 for x in range(self.columnCount(index) - 7)]
            ],
            columns=self._data.columns,
        )

        for row in range(rows):
            self._data = self._data.append(empty_row, ignore_index=True)

        self.endInsertRows()
        self.layoutChanged.emit()

        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """ Remove rows from the model. """
        self.beginRemoveRows(index, position, position + rows - 1)

        self._data = self._data.drop(
            self._data.index[position - rows : position], axis=0
        )

        self.endRemoveRows()
        self.layoutChanged.emit()

        return True

    def insertColumns(self, position, columns=1, index=QModelIndex()):
        """ Add columns to the model """
        self.beginInsertColumns(index, position, position + columns - 1)

        for column in range(columns):
            self._data.insert(position + column, "COMP" + str(position + column), 0)

        self.endInsertColumns()
        self.layoutChanged.emit()

        return True

    def removeColumns(self, position, columns=1, index=QModelIndex()):
        """ Remove columns from the model. """
        self.beginRemoveColumns(index, position, position + columns - 1)

        self._data = self._data.drop(
            self._data.columns[position - columns : position], axis=1
        )

        self.endRemoveColumns()
        self.layoutChanged.emit()

        return True

    def rowCount(self, index=QModelIndex()):
        return self._data.shape[0]

    def columnCount(self, index=QModelIndex()):
        return self._data.shape[1]
