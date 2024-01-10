from PySide6.QtGui import QUndoCommand
from PySide6.QtWidgets import QHBoxLayout, QTabBar, QTabWidget, QWidget
from ui.widgets import inputTitrationOpt


class AddTab(QUndoCommand):
    def __init__(self, tab_widget: QTabWidget):
        QUndoCommand.__init__(self)
        self.tab_widget = tab_widget

    def undo(self) -> None:
        idx_to_remove = self.tab_widget.count() - 1
        removed_widget = self.tab_widget.widget(idx_to_remove)
        self.tab_widget.removeTab(idx_to_remove)
        removed_widget.setParent(None)

    def redo(self) -> None:
        new_widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(inputTitrationOpt())
        new_widget.setLayout(layout)

        self.tab_widget.addTab(
            new_widget, str(self.tab_widget.findChild(QTabBar).count() + 1)
        )


class RemoveTab(QUndoCommand):
    def __init__(self, tab_widget: QTabWidget):
        QUndoCommand.__init__(self)
        self.tab_widget = tab_widget
        self.idx_to_remove = self.tab_widget.currentIndex()
        self.removed_widget = self.tab_widget.currentWidget()
        self.old_parent = self.removed_widget.parent()

    def undo(self) -> None:
        self.tab_widget.insertTab(
            self.idx_to_remove,
            self.removed_widget,
            str(self.idx_to_remove + 1),
        )
        self.removed_widget.setParent(self.old_parent)
        for i in range(self.tab_widget.count()):
            self.tab_widget.setTabText(i, f"{i+1}")
        self.tab_widget.setCurrentIndex(self.idx_to_remove)

    def redo(self) -> None:
        self.tab_widget.removeTab(self.idx_to_remove)
        self.removed_widget.setParent(None)
        for i in range(self.tab_widget.count()):
            self.tab_widget.setTabText(i, f"{i+1}")
