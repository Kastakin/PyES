from PySide6.QtWidgets import QComboBox, QWidget


class CustomComboBox(QComboBox):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.previous_index = self.currentIndex()

    def focusInEvent(self, event):
        self.previous_index = self.currentIndex()
        QComboBox.focusInEvent(self, event)
