import pandas as pd
import numpy as np
import os
import load_anime_to_html
from animate_initalizing import remove_windows_key_word
import app
import json
import modified_SGD
import heapq
import pickle

def generate_rated_matrix():
    # anime that was not rated will be initalize as 0
    allUserRating = np.zeros(shape=(len(app.User.query.filter(app.User.id).all()), len(load_anime_to_html.all_shows_list)))

    ratingData = pd.read_json(os.path.join(os.getcwd(), "data_collection", "rating_data.json"), lines=True)
    #print(ratingData)
    #print(ratingData)
    for index, row in ratingData.iterrows():
        # both the user id and anime id all start counting from 1,
        # but the index in array start counting from 0
        allUserRating[row["userId"]-1][row["animeId"]-1] = row["rating"]

    return allUserRating

#print(generate_rated_matrix())

def generate_P_matrixold():
    # K = 16, total 16 different type of genre, see genre.json
    # P matrix is user x k
    # example:
    #[[1,2,3,4]
    #[2,3,4,5]]
    # has two user with 4 k(latent feature each)
    k = 43
    allUser = np.zeros(shape=(len(app.User.query.filter(app.User.id).all()), len(load_anime_to_html.all_shows_list)))

    P = np.zeros(shape=(len(allUser), k))
    #print(P)
    for id in range(1, len(allUser)+1):
        # User id start with 1
        with open(os.path.join(os.getcwd(), "user_data", "{}".format(id), "info.json")) as file:
            userK = json.loads(file.read())

            # the id start counting from 1, but index start count from 0, so minus 1
            i = 0
            for key in userK.keys():
                # skip the bias key for now
                if key == "bias":
                    continue
                else:
                    P[id-1][i] = userK[key]
                    i += 1
        """
        # the id start counting from 1, but index start count from 0, so minus 1
        for i in range(userK.shape[1]):
            P[id-1][i] = (userK.iloc[0][i]) # only suppose to have 1 row of data
        """
    return P


def generate_P_matrix():
    # K = 16, total 16 different type of genre, see genre.json
    # P matrix is user x k
    # example:
    #[[1,2,3,4]
    #[2,3,4,5]]
    # has two user with 4 k(latent feature each)
    k = 43
    allUser = np.zeros(shape=(len(app.User.query.filter(app.User.id).all()), len(load_anime_to_html.all_shows_list)))

    P = np.zeros(shape=(len(allUser), k))
    #print(P)
    with open(os.path.join(os.getcwd(), "data_collection", "userGenres.pickle"), "rb") as f:
        userGenres = pickle.load(f)
    for id in range(1, len(allUser)+1):
        # User id start with 1
        userK = userGenres[id -1]

        # the id start counting from 1, but index start count from 0, so minus 1
        i = 0
        for key in userK.keys():
            # skip the bias key for now
            if key == "bias":
                continue
            else:
                P[id-1][i] = userK[key]
                i += 1
        """
        # the id start counting from 1, but index start count from 0, so minus 1
        for i in range(userK.shape[1]):
            P[id-1][i] = (userK.iloc[0][i]) # only suppose to have 1 row of data
        """
    return P


def generate_Q_matrix():
    # k = 16, total 16 different type of genre, see genre.json
    # P matrix is anime show x k
    # example:
    #[[1,2,3,4]
    #[2,3,4,5]]
    # has two anime show with 4 k(latent feature each)

    # all_show_list is a pandas dataframe contain all basic information of each anime
    k = 43
    #print(all_shows_list)
    Q = np.zeros(shape=(len(load_anime_to_html.all_shows_list), k))



    with open(os.path.join(os.getcwd(), "data_collection", "animeGenres.pickle"), "rb") as file:
        animeGenreInfo = pickle.load(file)
    # remove_windows_key_word,
        # replace all the windows reserve key by @, since that is how the program creat all those anime file at first

    for animeId in range(1, len(load_anime_to_html.all_shows_list)+1):
        # all anime id start with 1
        #print(all_shows_list.iloc[id-1][0])
        #print(all_shows_list.iloc[id-1][0])
        """
        path = os.path.join(os.getcwd(), "anime_data", "{}".format(remove_windows_key_word(load_anime_to_html.all_shows_list.iloc[id-1][0],"@")), "data.json")
        with open(path, "r") as file:
            fileInfo = json.loads(file.read())
            #print(fileInfo)
            i = 0
            for key in fileInfo.keys():
                if key == "bias":
                    continue
                else:
                    Q[id-1][i] = fileInfo[key]
                    i += 1
            del i

        """
       # path = os.path.join(os.getcwd(), "anime_data", "{}".format(animeId), "data.json")
        #with open(path, "r") as file:
        #fileInfo = json.loads(file.read())
        fileInfo = animeGenreInfo[animeId-1]
            # print(fileInfo)
        i = 0
        for key in fileInfo.keys():
            if key == "bias":
                continue
            else:
                # the index of array start with 1
                Q[animeId - 1][i] = fileInfo[key]
                i += 1
        del i
        """
        for i in range(animeK.shape[1]):
            Q[id-1][i] = animeK.iloc[0][i]
        """
    return Q




def generate_Q_matrix_old():
    # k = 16, total 16 different type of genre, see genre.json
    # P matrix is anime show x k
    # example:
    #[[1,2,3,4]
    #[2,3,4,5]]
    # has two anime show with 4 k(latent feature each)

    # all_show_list is a pandas dataframe contain all basic information of each anime
    k = 43
    #print(all_shows_list)
    Q = np.zeros(shape=(len(load_anime_to_html.all_shows_list), k))

    # remove_windows_key_word,
        # replace all the windows reserve key by @, since that is how the program creat all those anime file at first

    for animeId in range(1, len(load_anime_to_html.all_shows_list)+1):
        # all anime id start with 1
        #print(all_shows_list.iloc[id-1][0])
        #print(all_shows_list.iloc[id-1][0])
        """
        path = os.path.join(os.getcwd(), "anime_data", "{}".format(remove_windows_key_word(load_anime_to_html.all_shows_list.iloc[id-1][0],"@")), "data.json")
        with open(path, "r") as file:
            fileInfo = json.loads(file.read())
            #print(fileInfo)
            i = 0
            for key in fileInfo.keys():
                if key == "bias":
                    continue
                else:
                    Q[id-1][i] = fileInfo[key]
                    i += 1
            del i

        """
        path = os.path.join(os.getcwd(), "anime_data", "{}".format(animeId), "data.json")
        with open(path, "r") as file:
            fileInfo = json.loads(file.read())
            # print(fileInfo)
            i = 0
            for key in fileInfo.keys():
                if key == "bias":
                    continue
                else:
                    # the index of array start with 1
                    Q[animeId - 1][i] = fileInfo[key]
                    i += 1
            del i
        """
        for i in range(animeK.shape[1]):
            Q[id-1][i] = animeK.iloc[0][i]
        """
    return Q



def generate_user_biasold():
    u_b = np.zeros(len(app.User.query.filter(app.User.id).all()))
    #print(u_b)
    for id in range(1, len(u_b)+1):
        # User id start with 1
        with open(os.path.join(os.getcwd(), "user_data", "{}".format(id), "info.json")) as file:
            userBias = json.loads(file.read())

            # the id start counting from 1, but index start count from 0, so minus 1
            #print(userBias["bias"])
            u_b[id-1] = userBias["bias"]
    return u_b


def generate_user_bias():
    u_b = np.zeros(len(app.User.query.filter(app.User.id).all()))
    #print(u_b)
    with open(os.path.join(os.getcwd(), "data_collection", "userGenres.pickle"),"rb") as f:
        userGenres = pickle.load(f)
    for id in range(1, len(u_b)+1):
        # User id start with 1
        userBias = userGenres[id-1]

        # the id start counting from 1, but index start count from 0, so minus 1
        #print(userBias["bias"])
        u_b[id-1] = userBias["bias"]
    return u_b

def generate_anime_biasold():
    anime_b = np.zeros(shape=len(load_anime_to_html.all_shows_list))

    # remove_windows_key_word,
    # replace all the windows reserve key by @, since that is how the program creat all those anime file at first

    for animeId in range(1, len(load_anime_to_html.all_shows_list) + 1):
        # all anime id start with 1

        path = os.path.join(os.getcwd(), "anime_data",
                            "{}".format(animeId), "data.json")
        with open(path, "r") as file:
            fileInfo = json.loads(file.read())

            # the id start counting from 1, but index start count from 0, so minus 1
            anime_b[animeId-1] = fileInfo["bias"]

    return anime_b

def generate_anime_bias():
    anime_b = np.zeros(shape=len(load_anime_to_html.all_shows_list))

    # remove_windows_key_word,
    # replace all the windows reserve key by @, since that is how the program creat all those anime file at first

    for animeId in range(1, len(load_anime_to_html.all_shows_list) + 1):
        # all anime id start with 1
        with open(os.path.join(os.getcwd(), "data_collection", "animeGenres.pickle"), "rb") as file:
            animeGenreInfo = pickle.load(file)


            # the id start counting from 1, but index start count from 0, so minus 1
        anime_b[animeId-1] = animeGenreInfo[animeId-1]["bias"]

    return anime_b


#print(generate_rated_matrix())


def binary_search(searchList:list, searchValue:int):
    if len(searchList) == 1:

        return bool(searchList[0] == searchValue)
    else:
        splitIndex = int(len(searchList)/2)

        if searchValue < searchList[splitIndex]:
            return binary_search(searchList[ : splitIndex], searchValue)
        else:
            return binary_search(searchList[splitIndex :], searchValue)

def recommend_shows(userId:int, mf, N=30):
    # mf is the object of class MF in modified_SGD
    # mf should be already after running of SGD on matrix factorization

    # generate a pandas dataframe with predictscore and id for each anime

    # N is the number of top shows

    # since userid start with 1, but index start with 0
    predictUserRating = pd.DataFrame(mf.full_matrix()[userId-1], columns=["predictScore"])
    #print(predictUserRating)
    # anime id start with 1
    # anime id will be correct, since the program start to itterate from 1 (anime Id) folder
    predictUserRating["animeId"] = predictUserRating.index +1

    # a pandas dataframe of all rating information
    ratingData = pd.read_json(os.path.join(os.getcwd(), "data_collection", "rating_data.json"), lines=True)


    ratedAnimeId = ratingData["animeId"].values
    ratedAnimeId = np.unique(ratedAnimeId)      # a array of all rated anime id by other user

    # a array of anime id rated by this user
    userRatedAnimeId = sorted(ratingData.loc[ratingData["userId"] == userId]["animeId"].values)

    possibleAnimeId = np.setdiff1d(ratedAnimeId, userRatedAnimeId)
    # create a anime id that was rated, but not rated by this user
    # assuming user watched a anime when he gives a rating

    # only recommend anime that has already been rated by at least 1 user
    predictUserRating = predictUserRating.loc[predictUserRating["animeId"].isin(possibleAnimeId) ]

    predictUserRating = predictUserRating.sort_values(by="predictScore", ascending=False)
    #print("testing here")
    #print(predictUserRating)
    return predictUserRating


def update_P_matrixold(mf):
    #print(mf.P)
    userId = 1
    for row in mf.P:
        #print(row)
        with open(os.path.join(os.getcwd(), "user_data", "{}".format(userId), "info.json")) as file:
            userInfo = json.loads(file.read())

            rowIndex = 0
            for key in userInfo.keys():
                if key != "bias":
                    userInfo[key] = row[rowIndex]
                rowIndex += 1

        with open(os.path.join(os.getcwd(), "user_data", "{}".format(userId), "info.json"), "w") as files:
            files.write(json.dumps(userInfo))

        userId += 1


def update_P_matrix(mf):
    #print(mf.P)
    userId = 1
    with open(os.path.join(os.getcwd(), "data_collection", "userGenres.pickle"), "rb") as file:
        userGenres = pickle.load(file)
    for row in mf.P:
        #print(row)
        userInfo = userGenres[userId-1]

        rowIndex = 0
        for key in userInfo.keys():
            if key != "bias":
                userInfo[key] = row[rowIndex]
            rowIndex += 1
        userGenres[userId-1] = userInfo

        userId += 1
    with open(os.path.join(os.getcwd(), "data_collection", "userGenres.pickle"), "wb") as f:
        pickle.dump(userGenres, f)
    #print("#########User genres")
    #print(mf.P[1])



def update_Q_matrixold(mf):
    # still needs test
    #print(mf.Q)
    animeId = 1
    for row in mf.Q:
        #print(row)
        path = os.path.join(os.getcwd(), "anime_data",
                            "{}".format(animeId), "data.json")
        with open(path, "r") as file:
            fileInfo = json.loads(file.read())

            # the id start counting from 1, but index start count from 0, so minus 1

            # skip the bias part
            rowIndex = 0
            for key in fileInfo.keys():
                if key != "bias":
                    fileInfo[key] = row[rowIndex]
                rowIndex += 1
        #print(fileInfo)
                # dump the info
        with open(path, "w") as file:
            file.write(json.dumps(fileInfo))
        animeId += 1

def update_Q_matrix(mf):
    # still needs test
    #print(mf.Q)
    animeId = 1
    for row in mf.Q:
        #print(row)
        with open(os.path.join(os.getcwd(), "data_collection", "animeGenres.pickle"), "rb") as file:
            animeGenreInfo = pickle.load(file)

            fileInfo = animeGenreInfo[animeId-1]

            # the id start counting from 1, but index start count from 0, so minus 1

            # skip the bias part
            rowIndex = 0
            for key in fileInfo.keys():
                if key != "bias":
                    fileInfo[key] = row[rowIndex]
                rowIndex += 1
            animeGenreInfo[animeId-1] = fileInfo
        #print(fileInfo)
                # dump the info
        with open(os.path.join(os.getcwd(), "data_collection", "animeGenres.pickle"), "wb") as f:
            pickle.dump(animeGenreInfo, f)
        animeId += 1

    #print("Anime genres")
    #print(mf.Q[1])

def update_user_biasold(mf):
    # assuing the mf.b_u has the correct number of user correspond to each bias
    # example
    # [1,3,4] means there are 3 user bias here
    #print(mf.b_u)
    userId = 1 # since user id start with 1
    for value in mf.b_u:
        with open(os.path.join(os.getcwd(), "user_data", "{}".format(userId), "info.json")) as file:
            userInfo = json.loads(file.read())
            userInfo["bias"] = value
        with open(os.path.join(os.getcwd(), "user_data", "{}".format(userId), "info.json"), "w") as files:
            files.write(json.dumps(userInfo))
        userId += 1



def update_user_bias(mf):
    # assuing the mf.b_u has the correct number of user correspond to each bias
    # example
    # [1,3,4] means there are 3 user bias here
    #print(mf.b_u)
    userId = 1 # since user id start with 1
    with open(os.path.join(os.getcwd(), "data_collection", "userGenres.pickle"), "rb") as file:
        userGenres = pickle.load(file)
    for value in mf.b_u:
        userInfo = userGenres[userId-1]
        userInfo["bias"] = value

        userGenres[userId-1] = userInfo
        userId += 1
    with open(os.path.join(os.getcwd(), "data_collection", "userGenres.pickle"), "wb") as f:
        pickle.dump(userGenres, f)
    #print("user bias ^^^^^^")
    #print(mf.b_u[1])



def update_anime_biasold(mf):
    # assume the mf.b_i has teh correct number of anime show(id)
    #print(mf.b_i)
    animeId = 1
    #print(all_shows_list)

    # 0 is the index of first column in this dataframe
    for value in mf.b_i:
        path = os.path.join(os.getcwd(), "anime_data",
                            "{}".format(animeId), "data.json")
        #print(path)
        with open(path, "r") as file:
            fileInfo = json.loads(file.read())
            fileInfo["bias"] = value
        with open(path, "w") as files:
            files.write(json.dumps(fileInfo))

        animeId += 1



def update_anime_bias(mf):
    # assume the mf.b_i has teh correct number of anime show(id)
    #print(mf.b_i)
    animeId = 1
    #print(all_shows_list)
    with open(os.path.join(os.getcwd(), "data_collection", "animeGenres.pickle"), "rb") as f:
        animeGenres = pickle.load(f)
    # 0 is the index of first column in this dataframe
    for value in mf.b_i:
        path = os.path.join(os.getcwd(), "anime_data",
                            "{}".format(animeId), "data.json")
        #print(path)
        #with open(path, "r") as file:



        fileInfo = animeGenres[animeId-1]       # since the index in the list start with 1
        fileInfo["bias"] = value
        animeGenres[animeId-1] = fileInfo


        animeId += 1
    #print(mf.b_i)
    with open(os.path.join(os.getcwd(), "data_collection", "animeGenres.pickle"), "wb") as files:
        pickle.dump(animeGenres, files)
    #print(mf.b_i)
    #print("anime biase %%%%")
    #print(mf.b_i[1])


def apply_SGD(userId):

    mf = modified_SGD.MF(generate_rated_matrix(), generate_P_matrix(), generate_Q_matrix(), generate_user_bias(), generate_anime_bias(), K=43, alpha=0.01, beta=0.01, iterations=300)
    training_process = mf.train()
    update_Q_matrix(mf)
    update_P_matrix(mf)
    update_anime_bias(mf)
    update_user_bias(mf)

    return recommend_shows(userId, mf)






#print(recommend_shows(1, mf))
#update_user_bias(mf)
#update_anime_bias(mf)
#update_Q_matrix(mf)
#update_P_matrix(mf)



"""
print()
print("Global bias:")
print(mf.b)
print()
print("User bias:")
print(mf.b_u)
print()
print("Item bias:")
print(mf.b_i)
print(mf.R)
"""