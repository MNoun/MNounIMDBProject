import sqlite3
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import main


class imdbGUIGraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Graph Window")
        self.setGeometry(0, 0, 800, 800)
        self.graph_setup()
        self.show()

    def count_tvup(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        cursor.execute('SELECT rankUpDown FROM popular_tv_data '
                       'WHERE rankUpDown > 0')
        result = cursor.fetchall()
        count = len(result)
        return count

    def count_tvdown(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        cursor.execute('SELECT rankUpDown FROM popular_tv_data '
                       'WHERE rankUpDown < 0')
        result = cursor.fetchall()
        count = len(result)
        return count

    def count_movieup(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        cursor.execute('SELECT rankUpDown FROM popular_movie_data '
                       'WHERE rankUpDown > 0')
        result = cursor.fetchall()
        count = len(result)
        return count

    def count_moviedown(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        cursor.execute('SELECT rankUpDown FROM popular_movie_data '
                       'WHERE rankUpDown < 0')
        result = cursor.fetchall()
        count = len(result)
        return count

    def graph_setup(self):
        name = 'show_data.db'
        connection, cursor = main.db_open(name)
        counttvup = self.count_tvup(connection, cursor)
        counttvdown = self.count_tvup(connection, cursor)
        countmovieup = self.count_tvup(connection, cursor)
        countmoviedown = self.count_tvup(connection, cursor)

        set0 = QBarSet("Rank Up")
        set1 = QBarSet("Rank Down")

        set0 << counttvup << countmovieup
        set1 << counttvdown << countmoviedown

        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Popular Ranking Data")
        categories = ["TV", "Movies"]
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chartView)
        return