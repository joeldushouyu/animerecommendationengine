from bs4 import BeautifulSoup
import requests
import os
import json
import html5lib
import lxml
import pandas as pd
import json


# name str              error
# genre list            []
# theme list            []
# episode list          0
# vintage list [[]]     [[]]
# plot str              ""
# opening list []       []
# ending  list []       []
# insert song[]         []
# image str             ""


other_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=9"
a_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=A"
b_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=B"
c_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=C"
d_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=D"
e_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=E"
f_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=F"
g_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=G"
h_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=H"
i_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=I"
j_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=J"
k_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=K"
l_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=L"
m_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=M"
n_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=N"
o_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=O"
p_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=P"
q_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=Q"
r_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=R"
s_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=S"
t_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=T"
u_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=U"
v_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=V"
w_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=W"
x_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=X"
y_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=Y"
z_url = "https://www.animenewsnetwork.com/encyclopedia/anime.php?list=Z"

def createFolder(directory):
    # create windows file
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def other_titles(other_title)->list:
    other_title_result = []
    lens = len(other_title[0])

    for i in range(0, lens, 2):
        if i > 2:
            # change to binary unicode
            other_title_result.append(str(other_title[0].contents[i - 1].text))
            #print(other_title[0].contents[i-1].text)

    return other_title_result[:]


def genres_result(genres):
    generes_list = []
    x = genres[0].find_all(class_="discreet")  # give a deeper search  genres[0], should only have 1
    for i in range(len(x)):
        generes_list.append(x[i].text)
    return generes_list[:]

def theme_result(theme):
    all_list = []
    x = theme[0].find_all(class_="discreet")
    for i in range(len(x)):
        all_list.append(x[i].text)

    return all_list[:]


def plot_result(plot):
    plot_text = ""
    if len(plot[0].find_all("span")) == 1:
        #print(type(plot[0].find_all("span")[0].text))
        return plot[0].find_all("span")[0].text
    else:
        # when more than one paragraph present
        if len(plot[0].find_all("div", class_="tab")) > 0:

            for texts in plot[0].find_all("div",class_ = "tab"):
                plot_text += texts.text
        return plot_text
        #print(plot_text)

def episode_result(episode):
    #print(episode)


    if len(episode[0].find_all("span")) == 1:

        return episode[0].find_all("span")[0].text
    elif len(episode[0].find_all("span")) > 1:
        # means there is a suspicious answer
        # will use the first (current) number
        st = str(episode[0].find_all("span")[0])
        beg = int(st.find(">") + 1)
        end = int(st.find("<", beg))
        #print(st[beg : end])
        return st[beg : end]

    else:
        # when there are more than one, we choose the last number
        st = str(episode[0].find_all(class_="tab")[-1])
        beg = int(st.find(">")+1)
        end = int(st.find("<", beg))
        #print(beg, end)
        return (st[beg : end])

        #print(st[st.find(">")+1 : st.find("<")])
        #print(episode[0].find_all(class_="tab")[-1])


def vintage_result(vintage)->list:
    x = str((vintage[0].text))
    x = x.split("\n")
    del x[0]  # delete first empty line
    del x[0]    # delete title vintage
    del x[-1]   # delete last empyt line

    return x[:]

def website_result(website)->list:

    x = (website[0].find_all("a"))
    #print(x)
    return_website = []
    # return_website a double array, 0 for url, 1 for name
    for value in x:
        #print(value["href"])
        """
        location_of_biggersign = str(value).find(">")
        name = (str(value)[location_of_biggersign + 1: -4])
        print(name)
        return_website.append([value["href"], name])
        """
        #print(value)

        #return_website[:]
        # get the first link available
        return value["href"]

def opening_theme_result(opening_theme):
    list_of_op = []
    x = (opening_theme[0].find_all("div", class_="tab"))
    for value in x:
        if "#" in value.text:
            list_of_op.append(value.text[4:].strip())
        else:
            list_of_op.append(value.text[:].strip())
    return list_of_op[:]

def ending_theme_result(ending_theme):
    list_of_ed = []
    x = (ending_theme[0].find_all("div", class_="tab"))

    for value in x:
        if "#" in value.text:
            list_of_ed.append(value.text[4:].strip())
        else:
            list_of_ed.append(value.text[:].strip())
    return list_of_ed

def insert_song_result(insert_song):
    list_of_insert = []
    x = (insert_song[0].find_all("div", class_="tab"))

    for value in x:
        if "#" in value.text:
            list_of_insert.append(value.text[4:].strip())
        else:
            list_of_insert.append(value.text[:].strip())
    return list_of_insert[:]

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
            #return  show_title
# view test2.py for example

# all format start by a open space, then title and info by each space
def format_of_genre(info:str)->str:
    temp = info.split()
    message = "\n"

    for i in range(0, len(temp)-1):
        message += temp[i]
        message += "\n"
    message += temp[-1]
    return message
def change_quote_in_title(title:str)->str:

    if '"' in title:
        title = title.replace('"', "'")
        return title

all_info = []  # for all categpry



initalize_server = "https://www.animenewsnetwork.com/"
# got inside first, then get info
current_direct = os.getcwd()

def check_exist_in_other_category(showtitle:str):
    # looks like useless
    for dicty in all_info:
        if showtitle == dicty["show_name"]:
            return True
    return False

def what_title_shows(catgory:str, url):



    #createFolder("other_shows")
    all_basic_information = []
    #source = requests.get("https://www.animenewsnetwork.com/encyclopedia/anime.php?list=9").content
    source = requests.get(url).content
    soup = BeautifulSoup(source, 'lxml')
    #print(soup.find_all("class"))
    #print(soup.prettify())
    #x = (soup.find_all(class_="lst"))
    # maybe find all i and b

    # get all possible lins
    first_link = soup.find_all(class_="HOVERLINE")

    #for i in range(len(first_link)):

    #all_info = []   #for each categpry
    previous = ""
    for i in range(0,len(first_link)):

        dicty_info = {}  # store in each individual file
        #basic_information = []   # looks like use less
        #basic_information.append(soup.title.text[:-21])
        pre_exist = False  # check if this exist before

        category_info = {}  # will store in all_info

        #print(first_link[i])
        #print(first_link[i]["href"])
        #source2 = initalize_server + first_link[i]["href"]

        # iterate each link one by one
        get_result = requests.get( initalize_server + first_link[i]["href"])
        print(get_result.status_code)
        while get_result.status_code== 500 or get_result.status_code == 503:
            get_result = requests.get(initalize_server + first_link[i]["href"])
        source2 = get_result.content
        soup2 = BeautifulSoup(source2, "html.parser")
        show_title = (soup2.title.text[:-21])  # use to take out the website indention

        dicty_info["show_name"] = show_title
        category_info['show_name'] = show_title
        print(show_title)  # print the name of the anime
        show_title_no_key = remove_windows_key_word(show_title,"@")  # generate file name, avoid windows reserve key, replace it with @
        #print(show_title_no_key)


        # check if this pre_exist before update
        #if os.path.exists(os.path.join(current_direct,"anime_data", "{0}_shows".format(catgory), show_title_no_key)):
        if os.path.exists(os.path.join(current_direct, "anime_data", show_title_no_key)):
            pre_exist = True
            # check if it exist in other category before:
            #if check_exist_in_other_category(show_title) == False

        # creat individual folder for each shows, if folder exist, it will pass
        createFolder(os.path.join(current_direct, "anime_data", show_title_no_key))
        #createFolder(os.path.join(current_direct, "anime_data", "{0}_shows".format(catgory), show_title_no_key))


        #basic_information += (soup2.find_all("div", id="infotype-2"))  # get the other title
        other_title = (soup2.find_all("div", id="infotype-2"))
        if len(other_title) == 1:   # should only find 1 info on the website area
            dicty_info["other_title"] = other_titles(other_title)
        else:
            dicty_info["other_title"] = []

        #basic_information += (soup2.find_all("div", id="infotype-30"))  # get the type of genre
        genres = (soup2.find_all("div", id="infotype-30"))
        if len(genres) ==1:
            dicty_info["genre"] = genres_result(genres)

            # get all title of genre"""
            #print(dicty_info["genre"])
            """
            for i in dicty_info["genre"]:
                if i not in genre_list:
                    genre_list.append(i)
            """
            category_info["genre"] = genres_result(genres)
        else:
            dicty_info["genre"] = []
            category_info["genre"] = []

        #basic_information += (soup2.find_all("div", id="infotype-31")) # get the type of theme
        theme = (soup2.find_all("div", id="infotype-31"))
        if len(theme) == 1 :
            dicty_info["theme"] = theme_result(theme)
        else:
            dicty_info["theme"] = []


        #basic_information += (soup2.find_all("div", id="infotype-12"))  # plot info
        plot = (soup2.find_all("div", id="infotype-12"))
        if len(plot) == 1:
            dicty_info["plot"] = plot_result(plot)
        else:
            dicty_info["plot"] = ""

        #basic_information += (soup2.find_all("div", id="infotype-3"))  # number of episode
        episode = (soup2.find_all("div", id="infotype-3"))
        if len(episode) == 1:
            dicty_info["episode"] = str(episode_result(episode))
        else:
            # try to see if is a movie, which will be express in minutes
            time_long = soup2.find_all("div", id="infotype-4")
            if len(time_long) == 1:
                if len(time_long[0].find_all("span")) == 1:
                    dicty_info["episode"] = time_long[0].find_all("span")[0].text
                elif len(time_long[0].find_all(class_="tab")) >= 1:
                    dicty_info["episode"] = time_long[0].find_all(class_="tab")[0].text
            else:
                dicty_info["episode"] = 0


        #basic_information += (soup2.find_all("div", id="infotype-7"))  # get the date of publish
        vintage = soup2.find_all("div", id="infotype-7")
        if len(vintage) == 1:
            dicty_info["vintage"] = vintage_result(vintage)
        else:
            dicty_info["vintage"] = []



        # need to fix this bug, and also op, ed, insert song

        #dicty_info["vintageh"]= (soup2.find_all("div", id="infotype-7"))

        #basic_information += (soup2.find_all("div", id="infotype-10")) # get the official website
        website = (soup2.find_all("div", id="infotype-10"))

        if len(website) == 1:
            #print(website[0])
            dicty_info["official_website"] = website_result(website)
        else:
            dicty_info["official_website"] = [[]]
        #dicty_info["official website"] = (soup2.find_all("di
        # v", id="infotype-10"))

        # need open and end theme
        #basic_information += (soup2.find_all("div", id="infotype-11"))  # get the official website
        opening_theme = (soup2.find_all("div", id="infotype-11"))


        if len(opening_theme) == 1:
            dicty_info["opening_theme"] = opening_theme_result(opening_theme)
        else:
            dicty_info["opening_theme"] = []

        #basic_information += (soup2.find_all("div", id="infotype-24"))  # get the ed
        ending_theme = (soup2.find_all("div", id="infotype-24"))
        if len(ending_theme) == 1:
            dicty_info["ending_theme"] = ending_theme_result(ending_theme)
        else:
             dicty_info["ending_theme"] = []

        #basic_information += (soup2.find_all("div", id="infotype-35"))  # get the ed
        insert_song = (soup2.find_all("div", id="infotype-35"))
        if len(insert_song) == 1:
            dicty_info["insert_song"] = insert_song_result(insert_song)

        else:
            dicty_info["insert_song"] = []
        # get the picture download

        picture_url = (soup2.find_all("div", id="infotype-19"))
        if len(picture_url) == 1:
            url = str(picture_url[0].find_all("img"))

            url = url[url.find("src="):].split() # split on space
            #print(url[0][4:])  # avoide the src=
            dicty_info["image"] = str("https:"+url[0][4:]).replace('"',"")
            """
            file = open(str(show_title_no_key + ".png"), "wb")
            file.write(requests.get(str("https:"+url[0][4:]).replace('"',"")).content)
            file.close()"""

        else:

            picture_url = (soup2.find_all("img", id="vid-art"))
            if len(picture_url) == 1:
                #print("hhh")
                url = str(picture_url)[str(picture_url).find("src=")+4:-3]

                dicty_info["image"] = str("https:"+url).replace('"',"")

                #print(url)
                #print("here")
                """
                file = open(str(show_title_no_key + ".png"), "wb")
                file.write(requests.get(str("https:"+url).replace('"',"")).content)
                file.close()"""
            else:
                #print("cannot find")
                dicty_info["image"] = ""

        # add which category file is this anime in
        dicty_info["file_category"] = catgory
        category_info['file_category'] = catgory

        # this indiviual shows
        filename = show_title_no_key + ".json"  # write to file

        # the general shows info
        #with open(os.path.join(current_direct, "anime_data", "{0}_shows".format(catgory), show_title_no_key, filename), "w") as f:
        with open(os.path.join(current_direct, "anime_data", show_title_no_key, filename), "w") as f:
            f.write(json.dumps(dicty_info))

        # the possible data

        if pre_exist == False:
            #with open(os.path.join(current_direct, "anime_data", "{0}_shows".format(catgory), show_title_no_key, "data.json"), "w") as f:
            # the info of each genre used for SGD(stochaastic gradient descent )
            showGenreInfo = {}
            with open(os.path.join(current_direct, "anime_data", show_title_no_key, "data.json"), "w") as f:
                #
                with open(os.path.join(current_direct, "genres.json"),"r") as genres_file:
                    genre_list = json.loads(genres_file.read())  # the list contain all the genres type, or the k of user and movie in matrix factorization

                    for genre in list(genre_list):
                        # if the show under this genre, give a inital of 2.5
                        # else give 0, since 0 times anything will go to zero
                        if genre in dicty_info["genre"]:
                            showGenreInfo[genre] = 2.5
                        else:
                            showGenreInfo[genre] = 0
                showGenreInfo["bias"] = 0
                print(showGenreInfo)
                f.write(json.dumps(showGenreInfo))  # testing only
        else:
            # already exist before
            # so will not try to erase the data inside the file
            pass


            #print(dicty_info)

            # make sure no repeat on all_info
            # most likely useless
        if len(all_info)>0 and ( check_exist_in_other_category(dicty_info["show_name"]) == True or dicty_info["show_name"] == all_info[-1]["show_name"]):
            print("same")
            pass
        else:
            all_info.append(category_info)



    # final written for this category
    """may be is no longer workable here"""
    #with open(os.path.join(current_direct, "data_collection","all_{0}_shows.json".format(catgory)), "w") as file:
        #file.write(json.dumps(all_info))


    #write_title()
    #print(all_info)


    #print(type(first_link[2]["href"]))
    """
    source2 = initalize_server + first_link[2]["href"]
    source2 = requests.get( initalize_server + first_link[2]["href"]).content
    soup2 = BeautifulSoup(source2, "lxml")
    basic_information = (soup2.find_all("div", id="infotype-2"))   # get the other title
    basic_information += (soup2.find_all("div", id="infotype-30"))  # get the type of genre
    basic_information += (soup2.find_all("div", id="infotype-31")) # get the type of theme
    basic_information += (soup2.find_all("div", id="infotype-3"))  # number of episode
    basic_information += (soup2.find_all("div", id="infotype-7"))  # get the date of publish
    basic_information += (soup2.find_all("div", id="infotype-10")) # get the official website
    print(basic_information[-1].text)
    print(basic_information[-1].a["href"])"""


def write_all_info():
    with open(os.path.join(current_direct, "data_collection", "all_shows.json"), "w") as f:
        f.write(json.dumps(all_info))

def update():

    what_title_shows("other",other_url)

    #what_title_shows("a",a_url)

    #what_title_shows("b",b_url)

    #what_title_shows("c",c_url)

    #what_title_shows("d",d_url)

    #what_title_shows("e",e_url)

    #what_title_shows("f",f_url)

    #what_title_shows("g",g_url)

    #what_title_shows("h",h_url)

    #what_title_shows("i",i_url)

    #what_title_shows("j",j_url)

    #what_title_shows("k",k_url)

    #what_title_shows("l",l_url)

    #what_title_shows("m",m_url)

    #what_title_shows("n",n_url)

    #what_title_shows("o",o_url)

    #what_title_shows("p",p_url)

    #what_title_shows("q",q_url)
    #what_title_shows("r",r_url)
    #what_title_shows("s",s_url)
    #what_title_shows("t",t_url)
    #what_title_shows("u",u_url)
    #what_title_shows("v",v_url)
    #what_title_shows("w",w_url)
    #what_title_shows("x",x_url)
    #what_title_shows("y",y_url)
    #what_title_shows("z",z_url)


