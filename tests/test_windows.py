from pytestqt.qtbot import QtBot

from src.main.python.pyes.main import MainWindow


class TestMainWindow:
    def test_init(qtbot: QtBot):
        window = MainWindow()
        window.show()
        qtbot.addWidget(window)
