# MNounIMDBProject
Created by: Mitchell Noun
Created on: 1/29/22
Class: COMP490

Install Instructions:
  - Two text files: RawData.txt and ShowData.txt
  - Requirements.txt
  - Secrets.py to hold apiKey variable
  - Import requests and Secrets
  - sqlite
  - PyQt5
  - PyQtCharts

Description:
  This program uses IMDb API to retrieve data from the top 250 tv shows, user ratings from the tv shows ranked 1, 50, 100, 200, and The Wheel of Time, the most popular shows, the most popular movies, and the top 250 movies. This data is exported to text files and inserted into two sqlite databases. This data is visualized through an interactive GUI that allows the user to see specific data. This program includes:
   - main.py: retrieves and formats data, exports and inserts data into text files and an sqlite database
   - show_data.db: database for official show and movie data
   - tests.py: automated tests for functions in main.py, creates and uses a test database
   - test_db.db: test database
   - GUI
   
   Databases:
   - show_data.db
      - Includes six tables: show_data, ratings_data for sprint 2, and popular_movie_data, popular_tv_data, rank_updown_data, top250_movie_data for sprint 3
      - Each table is the official data from the API
   - test_db.db
      - Includes six tables: show_data, ratings_data for sprint 2, and popular_movie_data, popular_tv_data, rank_updown_data, top250_movie_data for sprint 3
      - Each table is filled with a minumum amount of data during the tests for the tests to work
   
   GUI:
   - Detailed GUI description and testing available in GUIDescription.pdf

To Do:
  - Fix flake8
