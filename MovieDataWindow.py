from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class imdbGUIMovieWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Movie Data Window")
        self.setGeometry(0, 0, 400, 400)