from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class imdbGUIGraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Graph Window")
        self.setGeometry(0, 0, 400, 400)