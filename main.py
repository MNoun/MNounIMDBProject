# Created by: Mitchell Noun
# Date created: 1/29/22
# Class: COMP490 Senior Design and Development
# Assignment: Project 1 Sprint 1
import requests
import Secrets


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


def get_ratings():  # gets the required user ratings and writes them to ShowData.txt
    rank1 = f"https://imdb-api.com/en/API/UserRatings/{Secrets.apiKey}/tt5491994"  # getting data from rank 1 show
    response1 = requests.get(rank1)
    data1 = response1.json()
    datalist1 = data1['ratings']
    rank50 = f"https://imdb-api.com/en/API/UserRatings/{Secrets.apiKey}/tt2297757"  # getting data from rank 50 show
    response2 = requests.get(rank50)
    data2 = response2.json()
    datalist2 = data2['ratings']
    rank100 = f"https://imdb-api.com/en/API/UserRatings/{Secrets.apiKey}/tt0286486"  # getting data from rank 100 show
    response3 = requests.get(rank100)
    data3 = response3.json()
    datalist3 = data3['ratings']
    rank200 = f"https://imdb-api.com/en/API/UserRatings/{Secrets.apiKey}/tt1492966"  # getting data from rank 200 show
    response4 = requests.get(rank200)
    data4 = response4.json()
    datalist4 = data4['ratings']
    rankwot = f"https://imdb-api.com/en/API/UserRatings/{Secrets.apiKey}/tt7462410"  # getting data from Wheel of Time show
    response5 = requests.get(rankwot)
    data5 = response5.json()
    datalist5 = data5['ratings']
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
    get_ratings()
    write_data(datalist)
    return


if __name__ == '__main__':
    main()
