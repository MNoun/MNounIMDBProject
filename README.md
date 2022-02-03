# MNounIMDBProject
Created by: Mitchell Noun
Created on: 1/29/22
Class: COMP490

Install Instructions:
  - Two text files: RawData.txt and ShowData.txt
  - Requirements.txt
  - Secrets.py to hold apiKey variable
  - Import requests and Secrets

Description:
  This program uses IMDb API to retrieve data from the top 250 tv shows, and user ratings from the tv shows ranked 1, 50, 100, 200, and The Wheel of Time. This data is exported to text files for easy viewing. This program includes several functions:
   - get_data: retrieves the full raw data of the top 250 tv shows
   - write_data: writes the raw data into ShowData.txt as clean, viewable data
   - get_ratings: retrieves the user rating data from the required shows and writes it to the top of ShowData.txt
   - main: main function
