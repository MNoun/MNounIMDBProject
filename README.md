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

Description:
  This program uses IMDb API to retrieve data from the top 250 tv shows, and user ratings from the tv shows ranked 1, 50, 100, 200, and The Wheel of Time. This data is exported to text files for easy viewing. This data is also inserted into two sqlite databases. This program includes:
   - main.py: retrieves and formats data, exports and inserts data into text files and an sqlite database
   - show_data.db: database for show data
   - tests.py: automated tests for functions in main.py, creates and uses a test database
   - test_db.db: test database
   
   Databases:
   - show_data.db
      - Includes two tables: show_data and ratings_data
      - Official data from the top 250 shows and user ratings
      - Ratings_data includes all needed data but should be reformatted to be more clear
   - test_db.db
      - Includes two tables: show_data and ratings_data
      - Show_data only has one entry to use as test data for tests.py
      - ratings_data is empty

To Do:
  - Reformat ratings_data table in show_data.db
  - Fix flake8
