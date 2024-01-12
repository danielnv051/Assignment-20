from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from game_file import Ui_MainWindow


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.game_count = 0
        self.winner = ""


app = QApplication()
window = Game()
window.show()
app.exec()
