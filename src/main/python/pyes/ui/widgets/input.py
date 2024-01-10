from typing import Optional

import PySide6.QtCore
from PySide6.QtWidgets import QLineEdit, QSpinBox, QWidget

from .PyES_inputTitrationOpt import Ui_inputTitrationOpt


class inputTitrationOpt(QWidget, Ui_inputTitrationOpt):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

    def retrive_data(self):
        data = dict()
        children = self.children()
        for c in children:
            if isinstance(c, QLineEdit):
                data[c.objectName()] = c.text()
            elif isinstance(c, QSpinBox):
                data[c.objectName()] = c.value()
            else:
                continue
        return data
