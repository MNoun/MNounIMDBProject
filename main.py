# Created by: Mitchell Noun
# Date created: 1/29/22
# Class: COMP490 Senior Design and Development
# Assignment: Project 1
import sys
import requests
import Secrets
import sqlite3
from typing import Tuple
from PyQt5.QtWidgets import QApplication, QMainWindow


# ------------------------------------ Sprint 1 ------------------------------------------ #
import StartWindow


def get_data(datalist):  # gets raw data from top 250
    with open("RawData.txt", "w") as rawData:  # writes all data to RawData.txt
        for item in datalist:
            rawData.write("id:%s, rank:%s, title:%s, fullTitle:%s, year:%s, image:%s, crew:%s, imDbRating:%s, "
                          "imDbRatingCount:%s \n" % (item['id'], item['rank'], item['title'], item['fullTitle'],
                                                     item['year'], item['image'], item['crew'], item['imDbRating'],
                                                     item['imDbRatingCount']))
    rawData.close()
    return


def write_data(datalist):  # writes data in readable format in ShowData.txt
    with open("ShowData.txt", "a") as ShowData:
        for item in datalist:
            ShowData.write("Title:%s, Rank:%s \n" % (item['title'], item['rank']))
    ShowData.close()
    return


def get_ratings(datalist1, datalist2, datalist3, datalist4, datalist5):
    # gets the required user ratings and writes them to ShowData.txt
    with open("ShowData.txt", "w") as ShowData:
        for ratings in datalist1:
            ShowData.write("Rank 1: Rating:%s, Percent:%s, Votes:%s \n" % (ratings['rating'], ratings['percent'],
                                                                           ratings['votes']))
        for ratings in datalist2:
            ShowData.write("Rank 50: Rating:%s, Percent:%s, Votes:%s \n" % (ratings['rating'], ratings['percent'],
                                                                            ratings['votes']))
        for ratings in datalist3:
            ShowData.write("Rank 100: Rating:%s, Percent:%s, Votes:%s \n" % (ratings['rating'], ratings['percent'],
                                                                             ratings['votes']))
        for ratings in datalist4:
            ShowData.write("Rank 200: Rating:%s, Percent:%s, Votes:%s \n" % (ratings['rating'], ratings['percent'],
                                                                             ratings['votes']))
        for ratings in datalist5:
            ShowData.write("Wheel of Time: Rating:%s, Percent:%s, Votes:%s \n" % (ratings['rating'], ratings['percent'],
                                                                                  ratings['votes']))
    return


# ------------------------------------ Sprint 2 ------------------------------------------ #


def db_setup(cursor: sqlite3.Cursor):  # sets up the two needed databases
    # creates database for top250 data
    cursor.execute('''CREATE TABLE IF NOT EXISTS show_data(
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    fullTitle TEXT NOT NULL,
    crew TEXT NOT NULL,
    showYear INTEGER NOT NULL,
    imdbRating FLOAT NOT NULL,
    imdbRatingCount FLOAT NOT NULL
    );''')
    # creates database for ratings data
    cursor.execute('''CREATE TABLE IF NOT EXISTS ratings_data(
    imdbID TEXT DEFAULT '',
    totalRating FLOAT DEFAULT 0,
    totalVotes INTEGER DEFAULT 0,
    tenRating FLOAT NOT NULL ,
    tenVotes INTEGER NOT NULL ,
    nineRating FLOAT NOT NULL ,
    nineVotes INTEGER NOT NULL ,
    eightRating FLOAT NOT NULL ,
    eightVotes INTEGER NOT NULL ,
    sevenRating FLOAT NOT NULL ,
    sevenVotes INTEGER NOT NULL ,
    sixRating FLOAT NOT NULL ,
    sixVotes INTEGER NOT NULL ,
    fiveRating FLOAT NOT NULL ,
    fiveVotes INTEGER NOT NULL ,
    fourRating FLOAT NOT NULL ,
    fourVotes INTEGER NOT NULL ,
    threeRating FLOAT NOT NULL ,
    threeVotes INTEGER NOT NULL ,
    twoRating FLOAT NOT NULL ,
    twoVotes INTEGER NOT NULL ,
    oneRating FLOAT NOT NULL ,
    oneVotes INTEGER NOT NULL , 
    FOREIGN KEY (imdbID) REFERENCES show_data (id)
    ON DELETE CASCADE ON UPDATE NO ACTION
    );''')
    return


def db_open(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:  # opens database
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()
    return connection, cursor


def db_close(connection: sqlite3.Connection):  # closes database
    connection.commit()
    connection.close()
    return


def db_populate_top250(connection: sqlite3.Connection, cursor: sqlite3.Cursor, datalist):
    # populates show_data
    for item in datalist:
        cursor.execute("""INSERT INTO show_data (id, title, fullTitle, crew, showYear, imdbRating, imdbRatingCount)
        VALUES (?,?,?,?,?,?,?)""",
                       (item['id'], item['title'], item['fullTitle'], item['crew'], item['year'],
                        item['imDbRating'], item['imDbRatingCount']))
    connection.commit()
    return


def db_populate_ratings(connection: sqlite3.Connection, cursor: sqlite3.Cursor,
                        datalist1, iddata1, datalist2, iddata2, datalist3,
                        iddata3, datalist4, iddata4, datalist5, iddata5):
    # populates ratings_data
    for ratings in datalist1:
        cursor.execute("""INSERT INTO ratings_data (imdbID, totalRating, totalVotes, tenRating, tenVotes,
         nineRating, nineVotes, eightRating, eightVotes, sevenRating, sevenVotes, sixRating, sixVotes, 
         fiveRating, fiveVotes, fourRating, fourVotes, threeRating, threeVotes, twoRating, twoVotes,
          oneRating, oneVotes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (iddata1['imDbId'], iddata1['totalRating'], iddata1['totalRatingVotes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes']))

    for ratings in datalist2:
        cursor.execute("""INSERT INTO ratings_data (imdbID, totalRating, totalVotes, tenRating, tenVotes,
         nineRating, nineVotes, eightRating, eightVotes, sevenRating, sevenVotes, sixRating, sixVotes, 
         fiveRating, fiveVotes, fourRating, fourVotes, threeRating, threeVotes, twoRating, twoVotes,
          oneRating, oneVotes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (iddata2['imDbId'], iddata2['totalRating'], iddata2['totalRatingVotes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes']))

    for ratings in datalist3:
        cursor.execute("""INSERT INTO ratings_data (imdbID, totalRating, totalVotes, tenRating, tenVotes,
         nineRating, nineVotes, eightRating, eightVotes, sevenRating, sevenVotes, sixRating, sixVotes, 
         fiveRating, fiveVotes, fourRating, fourVotes, threeRating, threeVotes, twoRating, twoVotes,
          oneRating, oneVotes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (iddata3['imDbId'], iddata3['totalRating'], iddata3['totalRatingVotes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes']))

    for ratings in datalist4:
        cursor.execute("""INSERT INTO ratings_data (imdbID, totalRating, totalVotes, tenRating, tenVotes,
         nineRating, nineVotes, eightRating, eightVotes, sevenRating, sevenVotes, sixRating, sixVotes, 
         fiveRating, fiveVotes, fourRating, fourVotes, threeRating, threeVotes, twoRating, twoVotes,
          oneRating, oneVotes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (iddata4['imDbId'], iddata4['totalRating'], iddata4['totalRatingVotes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes']))

    for ratings in datalist5:
        cursor.execute("""INSERT INTO ratings_data (imdbID, totalRating, totalVotes, tenRating, tenVotes,
         nineRating, nineVotes, eightRating, eightVotes, sevenRating, sevenVotes, sixRating, sixVotes, 
         fiveRating, fiveVotes, fourRating, fourVotes, threeRating, threeVotes, twoRating, twoVotes,
          oneRating, oneVotes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (iddata5['imDbId'], iddata5['totalRating'], iddata5['totalRatingVotes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes']))
    connection.commit()
    return


# ------------------------------------ Sprint 3 ------------------------------------------ #


def db_setup2(cursor: sqlite3.Cursor):  # creates new tables for Sprint 3
    # creates table for most popular tv shows
    cursor.execute('''CREATE TABLE IF NOT EXISTS popular_tv_data(
    id TEXT PRIMARY KEY,
    rank INTEGER NOT NULL,
    rankUpDown FLOAT NOT NULL,
    title TEXT NOT NULL,
    fullTitle TEXT NOT NULL,
    crew TEXT NOT NULL,
    showYear INTEGER NOT NULL,
    imdbRating FLOAT NOT NULL,
    imdbRatingCount FLOAT NOT NULL
    );''')
    # creates table for top 250 movies
    cursor.execute('''CREATE TABLE IF NOT EXISTS top250_movie_data(
    id TEXT PRIMARY KEY,
    rank INTEGER NOT NULL,
    title TEXT NOT NULL,
    fullTitle TEXT NOT NULL,
    crew TEXT NOT NULL,
    movieYear INTEGER NOT NULL,
    imdbRating FLOAT NOT NULL,
    imdbRatingCount FLOAT NOT NULL
    );''')
    # creates table for most popular movies
    cursor.execute('''CREATE TABLE IF NOT EXISTS popular_movie_data(
    id TEXT PRIMARY KEY,
    rank INTEGER NOT NULL,
    rankUpDown FLOAT NOT NULL,
    title TEXT NOT NULL,
    fullTitle TEXT NOT NULL,
    crew TEXT NOT NULL,
    showYear INTEGER NOT NULL,
    imdbRating FLOAT NOT NULL,
    imdbRatingCount FLOAT NOT NULL
    );''')
    # creates table for rank up and down
    cursor.execute('''CREATE TABLE IF NOT EXISTS rank_updown_data(
    id TEXT NOT NULL ,
    title TEXT NOT NULL ,
    rank INTEGER NOT NULL ,
    rankUpDown FLOAT NOT NULL,
    imdbRating FLOAT NOT NULL,
    imdbRatingCount FLOAT NOT NULL,
    FOREIGN KEY (id) REFERENCES popular_movie_data (id)
    ON DELETE CASCADE ON UPDATE NO ACTION
    )''')
    return


# populates popular_tv_data
def db_populate_popular_tv(connection: sqlite3.Connection, cursor: sqlite3.Cursor, datalist_tv):
    for item in datalist_tv:
        cursor.execute("""INSERT INTO popular_tv_data (id, rank, rankUpDown, title, fullTitle,
         crew, showYear, imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?,?,?,?)""",
                       (item['id'], item['rank'], item['rankUpDown'], item['title'], item['fullTitle'],
                        item['crew'], item['year'], item['imDbRating'], item['imDbRatingCount']))
    connection.commit()
    return


# populates top250_movie_data
def db_populate_top250_movies(connection: sqlite3.Connection, cursor: sqlite3.Cursor, datalist_topmovies):
    for item in datalist_topmovies:
        cursor.execute("""INSERT INTO top250_movie_data (id, rank, title, fullTitle,
        crew, movieYear, imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?,?,?)""",
                       (item['id'], item['rank'], item['title'], item['fullTitle'],
                        item['crew'], item['year'], item['imDbRating'], item['imDbRatingCount']))
        connection.commit()
    return


# populates popular_movie_data
def db_populate_popular_movies(connection: sqlite3.Connection, cursor: sqlite3.Cursor, datalist_movies):
    for item in datalist_movies:
        cursor.execute("""INSERT INTO popular_movie_data (id, rank, rankUpDown, title, fullTitle,
        crew, showYear, imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?,?,?,?)""",
                       (item['id'], item['rank'], item['rankUpDown'], item['title'], item['fullTitle'],
                        item['crew'], item['year'], item['imDbRating'], item['imDbRatingCount']))
    connection.commit()
    return


# finds the biggest movers and populates rank_updown_data, 3 positive, 1 negative
def get_rank_updown(connection: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.execute('SELECT MAX(rankUpDown) FROM popular_movie_data')  # first largest rankUpDown
    res1 = cursor.fetchall()
    maxRank1 = res1[0]
    cursor.execute('SELECT rankUpDown FROM popular_movie_data ORDER BY rankUpDown DESC LIMIT 1 OFFSET 1')  # 2nd
    res2 = cursor.fetchall()
    maxRank2 = res2[0]
    cursor.execute('SELECT rankUpDown FROM popular_movie_data ORDER BY rankUpDown DESC LIMIT 1 OFFSET 2')  # 3rd
    res3 = cursor.fetchall()
    maxRank3 = res3[0]
    cursor.execute('SELECT MIN(rankUpDown) FROM popular_movie_data')  # largest negative change
    res4 = cursor.fetchall()
    minRank = res4[0]

    # getting data from the select movies
    cursor.execute('SELECT id, title, rank, imdbRating, imdbRatingCount FROM popular_movie_data '
                   'WHERE rankUpDown = ?', (maxRank1[0],))
    row1 = cursor.fetchall()

    cursor.execute('SELECT id, title, rank, imdbRating, imdbRatingCount FROM popular_movie_data '
                   'WHERE rankUpDown = ?', (maxRank2[0],))
    row2 = cursor.fetchall()

    cursor.execute('SELECT id, title, rank, imdbRating, imdbRatingCount FROM popular_movie_data '
                   'WHERE rankUpDown = ?', (maxRank3[0],))
    row3 = cursor.fetchall()

    cursor.execute('SELECT id, title, rank, imdbRating, imdbRatingCount FROM popular_movie_data '
                   'WHERE rankUpDown = ?', (minRank[0],))
    row4 = cursor.fetchall()

    # populates rank_updown_data table with data
    for item in row1:  # largest positive change data
        cursor.execute("""INSERT INTO rank_updown_data (id, rank, rankUpDown, title,
                        imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?)""",
                       (item[0], item[2], maxRank1[0], item[1],
                        item[3], item[4]))

    for item in row2:  # second largest positive change data
        cursor.execute("""INSERT INTO rank_updown_data (id, rank, rankUpDown, title,
                        imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?)""",
                       (item[0], item[2], maxRank2[0], item[1],
                        item[3], item[4]))

    for item in row3:  # third largest positive change data
        cursor.execute("""INSERT INTO rank_updown_data (id, rank, rankUpDown, title,
                        imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?)""",
                       (item[0], item[2], maxRank3[0], item[1],
                        item[3], item[4]))

    for item in row4:  # largest negative change data
        cursor.execute("""INSERT INTO rank_updown_data (id, rank, rankUpDown, title,
                        imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?)""",
                       (item[0], item[2], minRank[0], item[1],
                        item[3], item[4]))
    connection.commit()
    return


# ------------------------------------ Sprint 4 ------------------------------------------ #


def gui_setup():
    app = QApplication(sys.argv)
    startWindow = StartWindow.imdbGUIStartWindow()
    startWindow.show()
    app.exec()
    return


# ------------------------------------ Main ------------------------------------------ #


def main():  # main function
    imdburl = f"https://imdb-api.com/en/API/Top250TVs/{Secrets.API_KEY}"  # for sprints 1 and 2
    response = requests.get(imdburl)  # gets a response from imDb
    if response.status_code != 200:  # error code
        print("Error!")
        return
    data = response.json()
    datalist = data['items']  # makes a list of dict

    imdburl_tv = f"https://imdb-api.com/en/API/MostPopularTVs/{Secrets.API_KEY}"  # sprint 3 most popular tv shows
    response_tv = requests.get(imdburl_tv)  # gets a response from imDb
    if response_tv.status_code != 200:  # error code
        print("Error!")
        return
    data_tv = response_tv.json()
    datalist_tv = data_tv['items']  # makes a list of dict

    imdburl_topmovies = f"https://imdb-api.com/en/API/Top250Movies/{Secrets.API_KEY}"  # sprint 3 top250 movies
    response_topmovies = requests.get(imdburl_topmovies)  # gets a response from imDb
    if response_topmovies.status_code != 200:  # error code
        print("Error!")
        return
    data_topmovies = response_topmovies.json()
    datalist_topmovies = data_topmovies['items']  # makes a list of dict

    imdburl_movies = f"https://imdb-api.com/en/API/MostPopularMovies/{Secrets.API_KEY}"  # sprint 3 most popular movies
    response_movies = requests.get(imdburl_movies)  # gets a response from imDb
    if response_movies.status_code != 200:  # error code
        print("Error!")
        return
    data_movies = response_movies.json()
    datalist_movies = data_movies['items']  # makes a list of dict

    # gets rating data for required shows
    rank1 = f"https://imdb-api.com/en/API/UserRatings/{Secrets.API_KEY}/tt5491994"  # getting data from rank 1 show
    response1 = requests.get(rank1)
    data1 = response1.json()
    iddata1 = {key: data1[key] for key in data1.keys() & {'imDbId', 'totalRating', 'totalRatingVotes'}}
    datalist1 = data1['ratings']
    rank50 = f"https://imdb-api.com/en/API/UserRatings/{Secrets.API_KEY}/tt2297757"  # getting data from rank 50 show
    response2 = requests.get(rank50)
    data2 = response2.json()
    iddata2 = {key: data2[key] for key in data2.keys() & {'imDbId', 'totalRating', 'totalRatingVotes'}}
    datalist2 = data2['ratings']
    rank100 = f"https://imdb-api.com/en/API/UserRatings/{Secrets.API_KEY}/tt0286486"  # getting data from rank 100 show
    response3 = requests.get(rank100)
    data3 = response3.json()
    iddata3 = {key: data3[key] for key in data3.keys() & {'imDbId', 'totalRating', 'totalRatingVotes'}}
    datalist3 = data3['ratings']
    rank200 = f"https://imdb-api.com/en/API/UserRatings/{Secrets.API_KEY}/tt1492966"  # getting data from rank 200 show
    response4 = requests.get(rank200)
    data4 = response4.json()
    iddata4 = {key: data4[key] for key in data4.keys() & {'imDbId', 'totalRating', 'totalRatingVotes'}}
    datalist4 = data4['ratings']
    rankwot = f"https://imdb-api.com/en/API/UserRatings/{Secrets.API_KEY}/tt7462410"  # getting data from Wheel of
    # Time show
    response5 = requests.get(rankwot)
    data5 = response5.json()
    iddata5 = {key: data5[key] for key in data5.keys() & {'imDbId', 'totalRating', 'totalRatingVotes'}}
    datalist5 = data5['ratings']

    name = 'show_data.db'
    connection, cursor = db_open(name)

    # function calls for sprint 1
    get_data(datalist)
    get_ratings(datalist1, datalist2, datalist3, datalist4, datalist5)
    write_data(datalist)
    # function calls for sprint 2
    db_setup(cursor)
    db_populate_top250(connection, cursor, datalist)
    db_populate_ratings(connection, cursor,
                        datalist1, iddata1, datalist2, iddata2, datalist3, iddata3, datalist4, iddata4, datalist5,
                        iddata5)
    db_close(connection)
    # function calls for sprint 3
    db_setup2(cursor)
    db_populate_popular_tv(connection, cursor, datalist_tv)
    db_populate_top250_movies(connection, cursor, datalist_topmovies)
    db_populate_popular_movies(connection, cursor, datalist_movies)
    get_rank_updown(connection, cursor)
    db_close(connection)

    return


if __name__ == '__main__':
    main()
