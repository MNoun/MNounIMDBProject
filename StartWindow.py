from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import DataVisualWindow


class imdbGUIStartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.data_window = None

    def setup_window(self):
        self.setWindowTitle("Start Window")
        self.setGeometry(0, 0, 400, 400)
        # button opens update data
        update_button = QPushButton("Update Data", self)
        #update_button.clicked.connect()
        update_button.move(150, 0)
        # button opens DataVisualWindow
        data_button = QPushButton("Visualization", self)
        data_button.clicked.connect(lambda: self.setup_data_window())
        data_button.move(150, 50)
        # button quits the application
        quit_button = QPushButton("Quit Now", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.move(150, 100)
        self.show()

    def setup_data_window(self):
        self.data_window = DataVisualWindow.imdbGUIDataWindow()
        self.data_window.show()
