import os
import pickle
import generate_SGD

path = os.path.join(os.getcwd(), "data_collection", "animeGenres.pickle")
path2 = os.path.join(os.getcwd(), "data_collection", "userGenres.pickle")

with open(path, "rb") as file:
    info = pickle.load(file)
with open(path2, "rb") as f:
    userInfo = pickle.load(f)






#print(generate_SGD.generate_Q_matrix()[0:3])
#print(generate_SGD.generate_anime_bias()[0:3])
#userInfo[0]["bias"] = 2
#print("#######")
#print(userInfo[0])
#print(generate_SGD.generate_P_matrix())
#print(userInfo[0]["bias"])
#print(generate_SGD.generate_user_bias())


"""
info[0]["Action"] = 0
info[0]["Adventure"] = 0
info[0]["Fantasy"] = 0
info[0]["Drama"] = 0
info[0]["Game"] = 0
info[0]["Magic"] = 0
info[0]["Sci-Fi"] = 0
"""

print(info[0])
print(info[1])
"""
info[0]["bias"] =10
info[1]["bias"] = -4
with open(path, "wb") as f:
    pickle.dump(info, f)
"""
"""
with open(path2, "wb") as f:
    pickle.dump(userInfo, f)
"""