from PyQt5.QtCore import QEvent, QPoint, QRect, Qt, QVariant, QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QItemDelegate,
    QStyle,
    QStyledItemDelegate,
    QStyleOptionButton,
    QComboBox,
    QApplication,
    QStyleOptionComboBox,
    QAbstractItemDelegate,
)


class CheckBoxDelegate(QStyledItemDelegate):
    """
    A delegate that places a fully functioning QCheckBox in every
    cell of the column to which it's applied
    """

    def __init__(self, parent):
        QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        """
        Important, otherwise an editor is created if the user clicks in this cell.
        ** Need to hook up a signal to the model
        """
        return None

    def paint(self, painter, option, index):
        """
        Paint a checkbox without the label.
        """
        checked = index.data()
        check_box_style_option = QStyleOptionButton()

        check_box_style_option.state |= QStyle.State_Enabled

        if checked:
            check_box_style_option.state |= QStyle.State_On
        else:
            check_box_style_option.state |= QStyle.State_Off

        check_box_style_option.rect = self.getCheckBoxRect(option)

        check_box_style_option.state |= QStyle.State_Enabled

        QApplication.style().drawControl(
            QStyle.CE_CheckBox, check_box_style_option, painter
        )

    def editorEvent(self, event, model, option, index):
        """
        Change the data in the model and the state of the checkbox
        if the user presses the left mousebutton or presses
        Key_Space or Key_Select and this cell is editable. Otherwise do nothing.
        """
        if event.type() == QEvent.MouseButtonPress:
            return False
        if (
            event.type() == QEvent.MouseButtonRelease
            or event.type() == QEvent.MouseButtonDblClick
        ):
            if event.button() != Qt.LeftButton or not self.getCheckBoxRect(
                option
            ).contains(event.pos()):
                return False
            if event.type() == QEvent.MouseButtonDblClick:
                return True
        elif event.type() == QEvent.KeyPress:
            if event.key() != Qt.Key_Space and event.key() != Qt.Key_Select:
                return False
        else:
            return False

        # Change the checkbox-state
        self.setModelData(None, model, index)
        return True

    def setModelData(self, editor, model, index):
        """
        The user wanted to change the old state in the opposite.
        """
        newValue = not index.data()
        model.setData(index, newValue, Qt.EditRole)

    def getCheckBoxRect(self, option):
        check_box_style_option = QStyleOptionButton()
        check_box_rect = QApplication.style().subElementRect(
            QStyle.SE_CheckBoxIndicator, check_box_style_option, None
        )
        check_box_point = QPoint(
            option.rect.x() + option.rect.width() / 2 - check_box_rect.width() / 2,
            option.rect.y() + option.rect.height() / 2 - check_box_rect.height() / 2,
        )
        return QRect(check_box_point, check_box_rect.size())


class ComboBoxDelegate(QItemDelegate):
    def __init__(self, owner, view, choices):
        super().__init__(owner)
        self.items = choices
        self._view = view

    def createEditor(self, parent, option, index):
        self.editor = QComboBox(parent)
        self.editor.addItems(self.items)

        self.editor.activated.connect(
            lambda index, editor=self.editor: self._view.commitData(editor)
        )
        self.editor.activated.connect(
            lambda index, editor=self.editor: self._view.closeEditor(
                editor, QAbstractItemDelegate.NoHint
            )
        )
        QTimer.singleShot(10, self.editor.showPopup)
        return self.editor

    def paint(self, painter, option, index):
        value = index.data(Qt.DisplayRole)
        style = QApplication.style()
        opt = QStyleOptionComboBox()
        opt.text = str(value)
        opt.rect = option.rect
        style.drawComplexControl(QStyle.CC_ComboBox, opt, painter)
        QItemDelegate.paint(self, painter, option, index)

    def setEditorData(self, editor, index):
        value = index.data(Qt.DisplayRole)
        num = self.items.index(value)
        editor.setCurrentIndex(num)

    def setModelData(self, editor, model, index):
        try:
            value = self.items[editor.currentIndex()]
            model.setData(index, value, Qt.EditRole)
        except:
            pass

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
