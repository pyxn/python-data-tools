import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SAGA Data Tools")
        self.setFixedWidth(724)
        self.setFixedHeight(300)
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
