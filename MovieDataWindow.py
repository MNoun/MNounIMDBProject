from PyQt5.QtWidgets import QMainWindow, QPushButton, QListWidget, QLabel, QVBoxLayout
import main

class imdbGUIMovieWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label1 = None
        self.label2 = None
        self.popmovies_list = None
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Movie Data Window")
        self.setGeometry(0, 0, 800, 800)
        self.layout = QVBoxLayout()
        self.label1 = QLabel("Popular Movies")
        self.label1.move(100, 10)
        self.layout.addWidget(self.label1)
        popmovies_list = QListWidget(self)
        popmovies_list.move(50, 20)
        popmovies_list.resize(300, 500)
        self.layout.addWidget(popmovies_list)
        self.label2 = QLabel("Top 250 Movies")
        self.label2.move(500, 100)
        self.layout.addWidget(self.label2)
        top250movies_list = QListWidget(self)
        top250movies_list.move(450, 20)
        top250movies_list.resize(300, 500)
        self.layout.addWidget(top250movies_list)
        crossover_list = QListWidget(self)
        crossover_list.move(250, 600)
        crossover_list.resize(300, 150)
        self.layout.addWidget(crossover_list)

        name = 'show_data.db'
        connection, cursor = main.db_open(name)

        # sorting buttons
        rank_button = QPushButton("Rank", self)
        rank_button.clicked.connect(lambda: self.addlistdata_rank(popmovies_list, cursor))
        rank_button.move(50, 550)
        self.layout.addWidget(rank_button)
        rankupdown_button = QPushButton("UpDown", self)
        rankupdown_button.clicked.connect(lambda: self.addlistdata_rankupdown(popmovies_list, cursor))
        rankupdown_button.move(150, 550)
        clear_button = QPushButton("Clear", self)
        clear_button.clicked.connect(lambda: self.clear_list(popmovies_list))
        clear_button.move(250, 550)
        self.layout.addWidget(rankupdown_button)
        self.setLayout(self.layout)
        self.addlistdata_top250(top250movies_list, cursor)
        self.addlistdata_crossover(crossover_list, cursor)

    # populates popmovies_list ordered by ranking
    def addlistdata_rank(self, popmovies_list, cursor):
        cursor.execute('SELECT title FROM popular_movie_data ORDER BY rank ASC ')
        result1 = cursor.fetchall()

        cursor.execute('SELECT rank FROM popular_movie_data ORDER BY rank ASC ')
        result2 = cursor.fetchall()

        cursor.execute('SELECT rankUpDown FROM popular_movie_data ORDER BY rank ASC')
        result3 = cursor.fetchall()

        result = []
        for count in range(0, len(result1)):
            result.append("Title: " + str(result1[count]) +
                          " Rank: " + str(result2[count]) + " RankUpDown " + str(result3[count]))

        popmovies_list.addItems(result)
        return

    # populates popmovies_list ordered by rankUpDown
    def addlistdata_rankupdown(self, popmovies_list, cursor):
        cursor.execute('SELECT title FROM popular_movie_data ORDER BY rankUpDown DESC ')
        result1 = cursor.fetchall()

        cursor.execute('SELECT rank FROM popular_movie_data ORDER BY rankUpDown DESC ')
        result2 = cursor.fetchall()

        cursor.execute('SELECT rankUpDown FROM popular_movie_data ORDER BY rankUpDown DESC ')
        result3 = cursor.fetchall()

        result = []
        for count in range(0, len(result1)):
            result.append("Title: " + str(result1[count]) +
                          " Rank: " + str(result2[count]) + " RankUpDown " + str(result3[count]))

        popmovies_list.addItems(result)
        return

    # populates top250movies_list
    def addlistdata_top250(self, top250movies_list, cursor):
        cursor.execute('SELECT title FROM main.top250_movie_data ')
        result1 = cursor.fetchall()

        result = []
        for count in range(0, len(result1)):
            result.append("Title: " + str(result1[count]))

        top250movies_list.addItems(result)
        return

    # populates list of shows that appear in both lists
    def addlistdata_crossover(self, crossover_list, cursor):
        cursor.execute('SELECT main.top250_movie_data.title FROM main.top250_movie_data '
                       'INNER JOIN main.popular_movie_data ON top250_movie_data.id = popular_movie_data.id')
        title_list = cursor.fetchall()

        result = []
        for count in range(0, len(title_list)):
            result.append("Title: " + str(title_list[count]))
        crossover_list.addItems(result)
        return

    def clear_list(self, popmovies_list):
        popmovies_list.clear()
        return