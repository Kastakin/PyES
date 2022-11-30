from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox
from pytest import MonkeyPatch, fixture
from pytestqt.qtbot import QtBot

from src.main.python.pyes.main import MainWindow


@fixture
def window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    return window


class TestMainWindow:
    def test_init(self, window: MainWindow):
        assert window.relErrorMode.currentIndex() == 1
        assert window.imode.currentIndex() == 0

        assert window.compProxy.sourceModel() is window.compModel
        assert window.compView.model() is window.compProxy

        assert window.speciesProxy.sourceModel() is window.speciesModel
        assert window.speciesView.model() is window.speciesProxy

        assert window.solidSpeciesProxy.sourceModel() is window.solidSpeciesModel
        assert window.solidSpeciesView.model() is window.solidSpeciesProxy

        assert window.numComp.value() == 1
        assert window.numSpecies.value() == 1
        assert window.numPhases.value() == 0

        assert window.speciesView.model().rowCount() == 1
        assert window.compView.model().rowCount() == 1
        assert window.solidSpeciesView.model().rowCount() == 0

    def test_add_comp_above_unselected(self, window: MainWindow, qtbot: QtBot):
        qtbot.mouseClick(window.insert_above_comp_button, Qt.MouseButton.LeftButton)

        assert window.numComp.value() == 2
        assert window.compView.model().rowCount() == 2

        assert (
            window.compView.model().data(window.compView.model().index(0, 0)) == "COMP0"
        )

    def test_add_comp_below_unselected(self, window: MainWindow, qtbot: QtBot):
        qtbot.mouseClick(window.insert_below_comp_button, Qt.MouseButton.LeftButton)

        assert window.numComp.value() == 2
        assert window.compView.model().rowCount() == 2

        assert (
            window.compView.model().data(window.compView.model().index(1, 0)) == "COMP2"
        )

    def test_add_comp_above_selected(self, window: MainWindow, qtbot: QtBot):
        window.numComp.setValue(2)
        window.compView.selectRow(2)
        qtbot.mouseClick(window.insert_above_comp_button, Qt.MouseButton.LeftButton)

        assert window.numComp.value() == 3
        assert window.compView.model().rowCount() == 3

        assert (
            window.compView.model().data(window.compView.model().index(1, 0)) == "COMP1"
        )

    def test_add_comp_below_selected(self, window: MainWindow, qtbot: QtBot):
        window.numComp.setValue(3)
        window.compView.selectRow(1)
        qtbot.mouseClick(window.insert_below_comp_button, Qt.MouseButton.LeftButton)

        assert window.numComp.value() == 4
        assert window.compView.model().rowCount() == 4

        assert (
            window.compView.model().data(window.compView.model().index(2, 0)) == "COMP2"
        )

    def test_increase_comp_key(self, window: MainWindow, qtbot: QtBot):
        qtbot.keyClick(window.numComp, Qt.Key.Key_Up)

        assert window.numComp.value() == 2
        assert (
            window.compView.model().data(
                window.compView.model().index(window.compView.model().rowCount() - 1, 0)
            )
            == "COMP2"
        )

    def test_decrease_comp_key(self, window: MainWindow, qtbot: QtBot):
        qtbot.keyClick(window.numComp, Qt.Key.Key_Down)
        assert window.numComp.value() == 1

        window.numComp.setValue(2)

        qtbot.keyClick(window.numComp, Qt.Key.Key_Down)
        assert window.numComp.value() == 1

    def test_remove_comp(
        self, window: MainWindow, qtbot: QtBot, monkeypatch: MonkeyPatch
    ):
        window.numComp.setValue(3)
        window.compView.selectRow(1)

        monkeypatch.setattr(QMessageBox, "question", lambda *args: QMessageBox.Yes)
        qtbot.mouseClick(window.remove_comp_button, Qt.MouseButton.LeftButton)

        assert window.numComp.value() == 2
        assert (
            window.compView.model().data(
                window.compView.model().index(window.compView.model().rowCount() - 1, 0)
            )
            == "COMP3"
        )

    def test_abort_remove_comp(
        self, window: MainWindow, qtbot: QtBot, monkeypatch: MonkeyPatch
    ):
        window.numComp.setValue(3)
        window.compView.selectRow(1)

        monkeypatch.setattr(QMessageBox, "question", lambda *args: QMessageBox.No)
        qtbot.mouseClick(window.remove_comp_button, Qt.MouseButton.LeftButton)

        assert window.numComp.value() == 3
        assert (
            window.compView.model().data(
                window.compView.model().index(window.compView.model().rowCount() - 1, 0)
            )
            == "COMP3"
        )
