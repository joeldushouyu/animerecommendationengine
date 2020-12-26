import os
import json

class Shows():
    def __init__(self,show_name, other_title, genre, theme, plot, episode, vintage, official_website, opening_theme, ending_theme, insert_song,image):
        self.__show_name = show_name
        self.__other_title = other_title
        self.__genre = genre
        self.__theme = theme
        self.__plot = plot
        self.__episode = episode
        self.__vintage = vintage
        self.__official_website = official_website
        self.__opening_theme = opening_theme
        self.__ending_theme = ending_theme
        self.__insert_song = insert_song
        self.__image = image
    def __str__(self):
        return self.__show_name

def remove_windows_key_word(show_title:str, replace:str) -> str:
    # format is ugly
    condition = True
    while condition:
        if ":" in show_title:
            show_title = show_title[:show_title.index(":")] + replace + show_title[show_title.index(":") + 1:]
        #return show_title

        elif "<" in show_title:
            show_title = show_title[:show_title.index("<")] + replace + show_title[show_title.index("<") + 1:]
            #return show_title

        elif ">" in show_title:
            show_title = show_title[:show_title.index(">")] + replace + show_title[show_title.index(">") + 1:]
            #return show_title

        elif '"' in show_title:
            show_title = show_title[:show_title.index('"')]  + replace + show_title[show_title.index('"') + 1:]
            #return show_title

        elif "/" in show_title:
            show_title = show_title[:show_title.index("/")] + replace + show_title[show_title.index("/") + 1:]
            #return show_title

        elif "\\" in show_title:
            show_title = show_title[:show_title.index("\\")] + replace + show_title[show_title.index("\\") + 1:]
            #return show_title

        elif "|" in show_title:
            show_title = show_title[:show_title.index("|")] + replace + show_title[show_title.index("|") + 1:]
            #return show_title

        elif "?" in show_title:
            show_title = show_title[:show_title.index("?")] + replace + show_title[show_title.index("?") + 1:]
            #return show_title

        elif "*" in show_title:
            show_title = show_title[:show_title.index("*")] + replace + show_title[show_title.index("*") + 1:]
            #return  show_title

        else:
            condition = False
    return show_title

def open_shows(type:str)->list:
    file_name = "all_{0}_shows.json".format(type)
    with open(file_name,"r") as file_object:
        info = json.loads(file_object.read())
    return info


other_list = open_shows("other")
other_list_class = []
current_direct = os.path.curdir
for dicty in other_list:
    show_title_no_key = remove_windows_key_word(dicty["show_name"],"@")
    other_list_class.append(Shows(dicty["show_name"], dicty["other_title"], dicty["genre"], dicty["theme"], dicty["plot"], dicty["episode"], dicty["vintage"], dicty["official_website"], dicty["opening_theme"], dicty["ending_theme"], dicty["insert_song"], dicty["image"]))
    if os.path.exists(os.path.join(current_direct, "{0}_shows".format("other"), show_title_no_key)):
        pass
    else:
        print("error")
        print(os.path.join(current_direct, "{0}_shows".format("other"), show_title_no_key))
print(len(other_list_class))