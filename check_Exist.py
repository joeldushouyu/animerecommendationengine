import os
import pandas as pd
path = os.path.join(os.getcwd(), "anime_data")
import pickle
import numpy as np

for i in range(1, 17391):
    #print(i)
    current_path = os.path.exists(os.path.join(path, str(i)))
    #print(current_path )
    if os.path.exists(os.path.join(path, str(i))) == False:
        print(i)
"""
all_shows_list = pd.read_json(os.path.join(os.getcwd(), "data_collection", "all_shows.json"), lines=True)
df = all_shows_list.sort_values(by=["animeId"])
df = df.loc[df.animeId < 13541]

df = df.sort_values(by=["showName"])'

df.to_json(os.path.join(os.getcwd(), "data_collection", "all_shows2.json"), orient="records", lines=True)

"""

# access_animeId_list = total_number_anime.webAnimeIdList()
with open("webid.pickle","rb") as f:
    info = pickle.load(f)

print(info[15780])
print(len(info))

with open(os.path.join(os.getcwd(), "data_collection", "animeGenres.pickle"), "rb") as f:
    infos = pickle.load(f)
print(len(infos))