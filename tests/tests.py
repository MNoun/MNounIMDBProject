import main
import pytest
import requests
import Secrets
import sqlite3


def test_show_data():  # test 1: retrieves 250
    imdburl = f"https://imdb-api.com/en/API/Top250TVs/{Secrets.API_KEY}"
    response = requests.get(imdburl)  # gets a response from imDb
    data = response.json()
    datalist = data['items']  # makes a list of dict
    length = len(datalist)  # gets length of dictionary
    assert length == 250


# test 2: database
def test_database():
    testdict = {"items": [{"id": "test", "title": "test", "fullTitle": "test",
                "crew": "test", "year": 0, "imDbRating": 0, "imDbRatingCount": 0}]}  # test data for test database
    datalist = testdict['items']
    name = 'test_db.db'
    connection, cursor = main.db_open(name)
    main.db_setup(cursor)  # database setup function
    main.db_populate_top250(connection, cursor, datalist)  # database populate function, using test data
    cursor.execute("SELECT title FROM show_data")  # selects test title and compares it to correct title
    res = cursor.fetchall()
    result = res[0]
    assert result[0] == "test"
