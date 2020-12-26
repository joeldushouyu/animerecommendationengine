import requests
from bs4 import BeautifulSoup
import numpy as np
import time
import pickle
import json
import os

base_url = 'https://myanimelist.net/anime.php?letter='
alphabeticalList = [".", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]
alphabeticalLists = ["X"]
totalAnimeNumber = 0
animeId = np.array([])

# get a numpy of website anime id,
def webAnimeIdLists():

    global animeId, totalAnimeNumber
    for alphabet in alphabeticalList:
        currentUrl = base_url + alphabet

        accessUrl = currentUrl # used for adding the view show number

        showLimit = 0
        requestResult = requests.get(accessUrl)

        while requestResult.status_code != 404:
            if requestResult.status_code == 503:
                continue
            else:
                source = requestResult.content
                print(accessUrl)
                soup = BeautifulSoup(source, 'lxml')

                animeLinks = soup.find_all(class_="hoverinfo_trigger fw-b fl-l")
                #print(animeLinks[0]["id"].replace("sinfo", ""))
                print(animeLinks)
                for i in range(len(animeLinks)):
                    animeId = np.append(animeId, animeLinks[i]["id"].replace("sinfo", ""))


                totalAnimeNumber += len(animeLinks)

                showLimit += 50
                accessUrl = currentUrl + "&show={}".format(str(showLimit))
                requestResult = requests.get(accessUrl)

            time.sleep(2)

    return animeId
"""
with open("webid.pickle", "wb") as f:
    pickle.dump(webAnimeIdLists(), f)
"""
#webAnimeIdLists()