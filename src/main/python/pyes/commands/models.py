from typing import Union

from PySide6.QtCore import QAbstractItemModel
from PySide6.QtGui import QUndoCommand
from PySide6.QtWidgets import QSpinBox


class CellEdit(QUndoCommand):
    def __init__(self, index, value, model):
        QUndoCommand.__init__(self)
        self.index = index
        self.value = value
        self.prev = model.data[index.row()][index.column()]
        self.model = model

    def undo(self):
        self.model.list_data[self.index.row()][self.index.column()] = self.prev

    def redo(self):
        self.model.list_data[self.index.row()][self.index.column()] = self.value


class AddSpeciesRows(QUndoCommand):
    def __init__(
        self,
        model: QAbstractItemModel,
        counter: Union[QSpinBox, None],
        position: int,
        number: int,
        update: bool = True,
    ):
        QUndoCommand.__init__(self)
        self.model = model
        self.counter = counter
        self.position = position
        self.number = number
        self.update = update

    def undo(self) -> None:
        self.model.removeRows(
            position=self.position + self.number + 1, rows=self.number
        )
        self.counter.blockSignals(True)
        self.counter.setValue(self.model.rowCount())
        self.counter.blockSignals(False)

    def redo(self) -> None:
        self.model.insertRows(position=self.position, rows=self.number)
        self.counter.blockSignals(True)
        self.counter.setValue(self.model.rowCount())
        self.counter.blockSignals(False)


class RemoveSpeciesRows(QUndoCommand):
    def __init__(
        self,
        model: QAbstractItemModel,
        counter: Union[QSpinBox, None],
        position: int,
        number: int,
        update: bool = True,
    ):
        QUndoCommand.__init__(self)
        self.model = model
        self.counter = counter
        self.position = position
        self.number = number
        self.removed_row = None
        self.update = update

    def undo(self) -> None:
        self.model.insertRows(position=self.position - 2, rows=self.number)
        self.model._data.iloc[
            (self.position - self.number) : (self.position), :
        ] = self.removed_rows
        self.counter.blockSignals(True)
        self.counter.setValue(self.model.rowCount())
        self.counter.blockSignals(False)

    def redo(self) -> None:
        self.removed_rows = self.model._data.iloc[
            (self.position - self.number) : (self.position), :
        ]
        self.model.removeRows(position=self.position, rows=self.number)
        self.counter.blockSignals(True)
        self.counter.setValue(self.model.rowCount())
        self.counter.blockSignals(False)


class AddComponentsRows(QUndoCommand):
    def __init__(
        self,
        model: QAbstractItemModel,
        counter: Union[QSpinBox, None],
        position: int,
        number: int,
        update: bool = True,
    ):
        QUndoCommand.__init__(self)
        self.model = model
        self.counter = counter
        self.position = position
        self.number = number
        self.update = update

    def undo(self) -> None:
        # self.model.removeRows(
        #     position=self.position + self.number + 1, rows=self.number
        # )
        # self.counter.blockSignals(True)
        # self.counter.setValue(self.model.rowCount())
        # self.counter.blockSignals(False)
        pass

    def redo(self) -> None:
        # self.model.insertRows(position=self.position, rows=self.number)
        # self.counter.blockSignals(True)
        # self.counter.setValue(self.model.rowCount())
        # self.counter.blockSignals(False)
        pass


class RemoveComponentsRows(QUndoCommand):
    def __init__(
        self,
        model: QAbstractItemModel,
        counter: Union[QSpinBox, None],
        position: int,
        number: int,
        update: bool = True,
    ):
        QUndoCommand.__init__(self)
        self.model = model
        self.counter = counter
        self.position = position
        self.number = number
        self.removed_row = None
        self.update = update

    def undo(self) -> None:
        # self.model.insertRows(position=self.position - 2, rows=self.number)
        # self.model._data.iloc[
        #     (self.position - self.number) : (self.position), :
        # ] = self.removed_rows
        # self.counter.blockSignals(True)
        # self.counter.setValue(self.model.rowCount())
        # self.counter.blockSignals(False)
        pass

    def redo(self) -> None:
        # self.removed_rows = self.model._data.iloc[
        #     (self.position - self.number) : (self.position), :
        # ]
        # self.model.removeRows(position=self.position, rows=self.number)
        # self.counter.blockSignals(True)
        # self.counter.setValue(self.model.rowCount())
        # self.counter.blockSignals(False)
        pass
