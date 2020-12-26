import pandas as pd
import os
import json

list_of_genre = []

def generate_genre(df):
    for genres in df["genre"]:
        for type in genres:
            #print(type)
            if type not in list_of_genre:
                list_of_genre.append(type)

generate_genre(pd.read_json(os.path.join("data_collection", "all_other_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_a_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_b_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_c_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_d_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_e_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_f_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_g_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_h_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_i_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_j_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_k_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_l_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_m_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_n_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_o_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_p_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_q_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_r_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_s_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_t_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_u_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_v_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_w_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_x_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_y_shows.json")))
generate_genre(pd.read_json(os.path.join("data_collection", "all_z_shows.json")))

print(list_of_genre)
with open("genres.json", 'w') as file:
    file.write(json.dumps(list_of_genre))



"""
genre_list = pd.DataFrame()
genre_list["type"] = []
print(genre_list)


for genres in df["genre"]:
    print(genres)
    genre_list["type"] += pd.DataFrame(genres,)

"""
    #for x in genres:
     #   print(x)
        #genre_list["type"] = list(x)
        #print(genre_list)
        #pass
#print(df["genre"])

"""

for index, item in df.iterrows():
    for value in item["genre"]:
        if value not in all_genre_list:
            all_genre_list.append(value)

"""
