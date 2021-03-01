from PyQt5.QtCore import QIdentityProxyModel, Qt


class ProxyModel(QIdentityProxyModel):
    def __init__(self, parent=None):
        super(ProxyModel, self).__init__(parent)
        self._columns = set()
        self._rows = set()

    def columnReadOnly(self, column):
        return column in self._columns

    def setColumnReadOnly(self, columns, readonly=True):
        for column in columns:
            if readonly:
                self._columns.add(column)
                self.layoutChanged.emit()
            else:
                self._columns.discard(column)
                self.layoutChanged.emit()

    def rowReadOnly(self, row):
        return row in self._rows

    def setRowReadOnly(self, rows, readonly=True):
        for row in rows:
            if readonly:
                self._rows.add(row)
                self.layoutChanged.emit()
            else:
                self._rows.discard(row)
                self.layoutChanged.emit()

    def flags(self, index):
        flags = super(ProxyModel, self).flags(index)
        if self.columnReadOnly(index.column()):
            flags &= ~Qt.ItemIsEditable
            flags &= ~Qt.ItemIsEnabled
        if self.rowReadOnly(index.row()):
            flags &= ~Qt.ItemIsEditable
            flags &= ~Qt.ItemIsEnabled
        return flags