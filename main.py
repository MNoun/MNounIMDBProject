# Created by: Mitchell Noun
# Date created: 1/29/22
# Class: COMP490 Senior Design and Development
# Assignment: Project 1 Sprint 1
import json
import requests
import Secrets


def get_data(data):  # gets data from top 250
    with open("RawData.txt", "w") as rawData:  # writes all data to RawData.txt
        for item in data:
            rawData.write("id:%s, rank:%s, title:%s, fullTitle:%s, year:%s, image:%s, crew:%s, imDbRating:%s, "
                          "imDbRatingCount:%s \n" % (item['id'],item['rank'],item['title'],item['fullTitle'],
                                                     item['year'],item['image'],item['crew'],item['imDbRating'],
                                                     item['imDbRatingCount']))
    rawData.close()
    return


def write_data():  # writes data in readable format in ShowData.txt

    return


def get_ratings():  # gets the required user ratings and writes them to ShowData.txt
    return


def main():  # main function
    imdburl = f"https://imdb-api.com/en/API/Top250TVs/{Secrets.apiKey}"
    response = requests.get(imdburl)  # gets a response from imDb
    if response.status_code != 200:  # error code
        print("Error!")
        return
    data = response.json()
    datalist = data['items']  # makes a list of dict

    # function calls
    get_data(datalist)
    #get_ratings()
    #write_data()
    return


if __name__ == '__main__':
    main()
