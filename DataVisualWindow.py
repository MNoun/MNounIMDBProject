from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

import DataGraphWindow
import MovieDataWindow
import TVDataWindow


class imdbGUIDataWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.graph_window = None
        self.tv_window = None
        self.movie_window = None


    def setup_window(self):
        self.setWindowTitle("Data Visualization Window")
        self.setGeometry(0, 0, 400, 400)
        # button opens DataGraphWindow
        graph_button = QPushButton("Graph Data", self)
        graph_button.clicked.connect(lambda: self.setup_graph_window())
        graph_button.move(150, 0)
        # button opens TVDataWindow
        tv_button = QPushButton("TV Data", self)
        tv_button.clicked.connect(lambda: self.setup_tv_window())
        tv_button.move(150, 50)
        # button opens MovieDataWindow
        movie_button = QPushButton("Movie Data", self)
        movie_button.clicked.connect(lambda: self.setup_movie_window())
        movie_button.move(150, 100)
        self.show()

    def setup_graph_window(self):
        self.graph_window = DataGraphWindow.imdbGUIGraphWindow()
        self.graph_window.show()

    def setup_tv_window(self):
        self.tv_window = TVDataWindow.imdbGUITVWindow()
        self.tv_window.show()

    def setup_movie_window(self):
        self.movie_window = MovieDataWindow.imdbGUIMovieWindow()
        self.movie_window.show()