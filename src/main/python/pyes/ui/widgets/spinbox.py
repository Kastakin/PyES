from PySide6.QtWidgets import QDoubleSpinBox, QWidget


class CustomSpinBox(QDoubleSpinBox):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.previous_value = self.value()

    def focusInEvent(self, event):
        self.previous_value = self.value()
        QDoubleSpinBox.focusInEvent(self, event)
