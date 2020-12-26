import os
import pickle

path = os.path.join(os.getcwd(), "data_collection", "animeGenres.pickle")

with open(path, "rb") as file:
    info = pickle.load(file)

print(info)