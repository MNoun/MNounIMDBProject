import DataGraphWindow
import StartWindow
import main
import pytest
import requests
import Secrets
import sqlite3


# Sprint 2 test 1: assure that method retrieves 250 pieces of data
def test_show_data():
    imdburl = f"https://imdb-api.com/en/API/Top250TVs/{Secrets.API_KEY}"
    response = requests.get(imdburl)  # gets a response from imDb
    data = response.json()
    datalist = data['items']  # makes a list of dict
    length = len(datalist)  # gets length of dictionary
    assert length == 250


# Sprint 2 test 2: assure that database is created and populated correctly
def test_database_data():
    testdict = {"items": [{"id": "test1", "title": "test", "fullTitle": "test",
                           "crew": "test", "year": 0, "imDbRating": 0,
                           "imDbRatingCount": 0}]}  # test data for test database
    datalist = testdict['items']
    name = 'test_db.db'
    connection, cursor = main.db_open(name)
    main.db_setup(cursor)  # database setup function
    main.db_populate_top250(connection, cursor, datalist)  # database populate function, using test data
    cursor.execute("SELECT title FROM show_data")  # selects test title and compares it to correct title
    res = cursor.fetchall()
    result = res[0]
    assert result[0] == "test"


# Sprint 3 test 1: new table is there
def test_updown_table():
    name = 'test_db.db'
    connection, cursor = main.db_open(name)
    main.db_setup2(cursor)
    cursor.execute('SELECT count(*) FROM main.sqlite_master WHERE type= ? AND name= ?', ('table', 'rank_updown_data'))
    result = cursor.fetchall()
    count = result[0]
    assert count[0] == 1


# Sprint 3 test 2: assure that get_rank_updown works properly
def test_updown_data():
    # add more test data
    testdict1 = {"items": [{"id": "test1", "rank": 0, "rankUpDown": 2, "title": "test", "fullTitle": "test",
                            "crew": "test", "year": 0, "imDbRating": 0, "imDbRatingCount": 0}]}
    datalist1 = testdict1['items']
    testdict2 = {"items": [{"id": "test2", "rank": 0, "rankUpDown": 8, "title": "test2", "fullTitle": "test",
                            "crew": "test", "year": 0, "imDbRating": 0, "imDbRatingCount": 0}]}
    datalist2 = testdict2['items']
    testdict3 = {"items": [{"id": "test3", "rank": 0, "rankUpDown": -3, "title": "test3", "fullTitle": "test",
                            "crew": "test", "year": 0, "imDbRating": 0, "imDbRatingCount": 0}]}
    datalist3 = testdict3['items']
    testdict4 = {"items": [{"id": "test4", "rank": 0, "rankUpDown": 10, "title": "test4", "fullTitle": "test",
                            "crew": "test", "year": 0, "imDbRating": 0, "imDbRatingCount": 0}]}
    datalist4 = testdict4['items']

    name = 'test_db.db'
    connection, cursor = main.db_open(name)
    main.db_setup2(cursor)  # make sure databases are set up
    # populate table with test data
    main.db_populate_popular_movies(connection, cursor, datalist1)
    main.db_populate_popular_movies(connection, cursor, datalist2)
    main.db_populate_popular_movies(connection, cursor, datalist3)
    main.db_populate_popular_movies(connection, cursor, datalist4)

    main.get_rank_updown(connection, cursor)  # test get_rank_updown
    cursor.execute("SELECT id FROM rank_updown_data")  # selects test title and compares it to correct title
    res = cursor.fetchall()
    result = res[0]
    assert result[0] == "test4"


# Sprint 3 test 3: assures new populate functions work
def test_database_data2():
    testdict = {"items": [{"id": "test1", "rank": 0, "rankUpDown": 1, "title": "test", "fullTitle": "test",
                           "crew": "test", "year": 0, "imDbRating": 0, "imDbRatingCount": 0}]}
    datalist = testdict['items']
    name = 'test_db.db'
    connection, cursor = main.db_open(name)
    main.db_setup2(cursor)
    # populate test databases new tables
    main.db_populate_top250_movies(connection, cursor, datalist)
    main.db_populate_popular_tv(connection, cursor, datalist)
    cursor.execute("SELECT title FROM popular_movie_data")  # selects test title and compares it to correct title
    res = cursor.fetchall()
    result = res[0]
    assert result[0] == "test"


# Sprint 3 test 4: tests new create table function and foreign key
def test_database_creation():
    name = 'test_db.db'
    connection, cursor = main.db_open(name)
    main.db_setup2(cursor)
    cursor.execute('SELECT popular_movie_data.id FROM popular_movie_data INNER JOIN rank_updown_data '
                   'ON popular_movie_data.id = rank_updown_data.id WHERE rank_updown_data.rankUpDown = 8')
    res = cursor.fetchall()
    result = res[0]
    assert result[0] == "test2"


# Sprint 4 test 1: tests tv up and down counters for graph
def test_tvupdowncount():
    name = 'test_db.db'
    connection, cursor = main.db_open(name)
    result1 = DataGraphWindow.imdbGUIGraphWindow.count_tvup(DataGraphWindow.imdbGUIGraphWindow, connection, cursor)
    result2 = DataGraphWindow.imdbGUIGraphWindow.count_tvdown(DataGraphWindow.imdbGUIGraphWindow, connection, cursor)
    assert result1 == 1
    assert result2 == 0


# Sprint 4 test 2: tests movie up and down counters for graph
def test_movieupdowncount():
    name = 'test_db.db'
    connection, cursor = main.db_open(name)
    result1 = DataGraphWindow.imdbGUIGraphWindow.count_movieup(DataGraphWindow.imdbGUIGraphWindow, connection, cursor)
    result2 = DataGraphWindow.imdbGUIGraphWindow.count_moviedown(DataGraphWindow.imdbGUIGraphWindow, connection, cursor)
    assert result1 == 3
    assert result2 == 1


# Sprint 4 test 3: tests the table crossover
def test_guicrossover():
    name = 'test_db.db'
    connection, cursor = main.db_open(name)
    cursor.execute('SELECT show_data.title FROM show_data '
                   'INNER JOIN popular_movie_data ON show_data.id = popular_movie_data.id')
    res = cursor.fetchall()
    result = res[0]
    assert result[0] == "test"


