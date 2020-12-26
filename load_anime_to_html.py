# this contains all the function that will be used for html update and format


import os
import pandas as pd
import time
#from app import User
import app
import math
import json
import numpy as np




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





# the pandas dataframe that contains all anime basic data information
all_shows_list = pd.read_json(os.path.join(os.getcwd(), "data_collection", "all_shows.json"), lines=True)


print(all_shows_list)
# the following is returning different sub pandas dataframe of all_shows_list according to each alphabetical
def return_a_list_panda():
    # generate all a list
    a_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "A") | (all_shows_list["showName"].str[0] == "a" )]
    return a_category_panda


def return_other_list_panda():
    a_category_panda = all_shows_list.loc[
    (all_shows_list["showName"].str[0] == "A") | (all_shows_list["showName"].str[0] == "a")]


    # generate the all other list
    #   all other list will be everything before the first index of a list
    first_a_index = a_category_panda.head(1).index


    other_category_panda = (all_shows_list.iloc[: first_a_index[0]])
    return other_category_panda


def return_b_list_panda():
    # generate all b list
    b_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "B") | (all_shows_list["showName"].str[0] == "b" )]
    return b_category_panda


def return_c_list_panda():
    # generate all c list
    c_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "C") | (all_shows_list["showName"].str[0] == "c" )]
    return c_category_panda


def return_d_list_panda():

    # generate all d list
    d_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "D") | (all_shows_list["showName"].str[0] == "d" )]
    return d_category_panda


def return_e_list_panda():
    # generate all e list
    e_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "E") | (all_shows_list["showName"].str[0] == "e" )]
    return e_category_panda


def return_f_list_panda():
    # generate all f list
    f_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "F") | (all_shows_list["showName"].str[0] == "f" )]
    return f_category_panda


def return_g_list_panda():
    # generate all g list
    g_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "G") | (all_shows_list["showName"].str[0] == "g" )]
    return g_category_panda


def return_h_list_panda():
    # generate all h list
    h_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "H") | (all_shows_list["showName"].str[0] == "h" )]
    return h_category_panda


def return_i_list_panda():

    # generate all i list
    i_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "I") | (all_shows_list["showName"].str[0] == "i" )]
    return i_category_panda


def return_j_list_panda():
    # generate all j list
    j_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "J") | (all_shows_list["showName"].str[0] == "j" )]
    return j_category_panda


def return_k_list_panda():
    # generate all k list
    k_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "K") | (all_shows_list["showName"].str[0] == "k" )]
    return k_category_panda


def return_l_list_panda():

    # generate all l list
    l_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "L") | (all_shows_list["showName"].str[0] == "l" )]
    return l_category_panda


def return_m_list_panda():
    # generate all m list
    m_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "M") | (all_shows_list["showName"].str[0] == "m" )]
    return m_category_panda


def return_n_list_panda():
    # generate all n list
    n_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "N") | (all_shows_list["showName"].str[0] == "n" )]
    return n_category_panda


def return_o_list_panda():
    # generate all o list
    o_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "O") | (all_shows_list["showName"].str[0] == "o" )]
    return o_category_panda


def return_p_list_panda():
    # generate all p list
    p_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "P") | (all_shows_list["showName"].str[0] == "p" )]
    return p_category_panda


def return_q_list_panda():
    # generate all q list
    q_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "Q") | (all_shows_list["showName"].str[0] == "q" )]
    return q_category_panda


def return_r_list_panda():
    # generate all r list
    r_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "R") | (all_shows_list["showName"].str[0] == "r" )]
    return r_category_panda


def return_s_list_panda():

    # generate all s list
    s_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "S") | (all_shows_list["showName"].str[0] == "s" )]
    return s_category_panda


def return_t_list_panda():
    # generate all t list
    t_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "T") | (all_shows_list["showName"].str[0] == "t" )]
    return t_category_panda


def return_u_list_panda():

    # generate all u list
    u_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "U") | (all_shows_list["showName"].str[0] == "u" )]
    return u_category_panda


def return_v_list_panda():
    # generate all v list
    v_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "V") | (all_shows_list["showName"].str[0] == "v" )]
    return v_category_panda


def return_w_list_panda():
    # generate all w list
    w_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "W") | (all_shows_list["showName"].str[0] == "w" )]
    return w_category_panda


def return_x_list_panda():
    # generate all x list
    x_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "X") | (all_shows_list["showName"].str[0] == "x" )]
    return x_category_panda


def return_y_list_panda():
    # generate all Y list
    y_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "Y") | (all_shows_list["showName"].str[0] == "y" )]
    return y_category_panda


def return_z_list_panda():
    # generate all Z list
    z_category_panda = all_shows_list.loc[(all_shows_list["showName"].str[0] == "Z") | (all_shows_list["showName"].str[0] == "z" )]
    return z_category_panda


def add_hightlight(showName:str, searchKey=""):
    if searchKey == "":
        return "<mark>"+showName+"</mark>"
    else:
        searchKeyIndex = showName.find(searchKey)
        print(searchKeyIndex)
        return showName[0:searchKeyIndex] + "<mark>" + showName[searchKeyIndex:] + "</mark>"

def write_html_click(animeId:int, showname:str, ):
    # the function help to generate the clickable button in the encyclopedia page
    # html format of encyclopedia list
    # putting the id of each show in the panda dataframe

    return """
                <i><form  action="/viewdetail/{}" method="POST">
                        
                <button class="HOVERLINE" type="submit"><font color="#0000ff">{}</font></button>
                </form></i>
    
                """.format(animeId, showname)


def write_to_html_form(anime_list_panda, type="", searchKey=""):
    # used for the encyclopedia and search page
    # anime_list_panda is a pandas dataframe contains basic information of anime
    #
    # this function is going to call write_htl_click() to generate a list of clickable buttom by the show_name in anime_list_panda
    # This is used to the encyclopedia page of html
    html_message = ""
    if type == "search":
        for index, rows in anime_list_panda.iterrows():
            html_message += write_html_click(str(rows["animeId"]), rows["showName"],type, searchKey)
            # html_message += write_html_click( str(rows["show_name"]).replace(" ", "%20"), rows["show_name"])
    else:
        for index, rows in anime_list_panda.iterrows():

            html_message += write_html_click(str(rows["animeId"]), rows["showName"])
            #html_message += write_html_click( str(rows["show_name"]).replace(" ", "%20"), rows["show_name"])
                                                                 # replace // with space, since query cannot have space inside
    return html_message

def load_viewdetail_file(animeId:int):
    # this is for the detail view of this specific anime
    # return the path of this anime data

    # remember, all anime folder and information is named with its id

    # getting the name of this anime correspond to this id,

    if all_shows_list.loc[all_shows_list.animeId == animeId].empty:
        # means when this path is not exist in the system, means this anime id is not exist
        return "error"
    else:

        path = os.path.join(os.getcwd(), "anime_data",
                            str(animeId),
                            "{}.json".format(animeId))
        return path


def write_to_detailview_htmlform(path:str, userId:int, animeId:int):
    # this function is generate and return all different part of detailview html page in html
    with open(path, "r") as file:
        fileInfo = json.loads(file.read())

    return fileInfo["show_name"], image_htmlformat(fileInfo["image"]), alternativetitle_htmlform(fileInfo["other_title"]), genres_htmlform(fileInfo['genre']),  plot_htmlform(fileInfo["plot"]), rating_htmlform(userId, animeId), episodeAndRunningtime_htmlform(fileInfo["episode"]), vintage_htmlform(fileInfo["vintage"]),  openingTheme_htmlform(fileInfo["opening_theme"]), endingTheme_htmlform(fileInfo["ending_theme"]), type_htmlform(fileInfo['type'])


def image_htmlformat(image_url:str):
    # the image part of detailview html
    return """
<div id="infotype-19" class="encyc-info-type same-width-as-main">
    <div class="fright"><div>
        <img src="{}" style="border: 1px solid black"></a><br>
</div></div>
</div>
    """.format(image_url)


def alternativetitle_htmlform(other_title:list):
    #the alternative title part of detailview html
    if len(other_title) == 0:
        print("here")
        return ""
    else:
        return_message =  """
<div id="infotype-2" class="encyc-info-type same-width-as-main">
<strong>Alternative title:</strong>"""

        for value in other_title:
            return_message += """
    <div class="tab">{}</div>""".format(value)

        return_message += """
</div>"""
        return return_message


def genres_htmlform(genres:list):
    # the genere type of detailview html
    # mayshould update more variety of genre
    return_message = """
<div id="infotype-30" class="encyc-info-type br same-width-as-main">
<strong>Genres:</strong>\n"""
    if len(genres) == 0:
        return ""
    else:
        return_message += ",\n".join(["""		<span><a href="/genre/{0}" class="discreet">{0}</a></span>""".format(genre) for genre in genres])
        return_message += "\n</div>"
        return return_message


def theme_htmlform(themes:list):
    # the theme part of detailview html
    if len(themes) == 0:
        return ""
    else:
        return_message = """
<div id="infotype-31" class="encyc-info-type same-width-as-main">
<strong>Themes:</strong>\n"""
        return_message += ",\n".join([ """	<span><a class="discreet">{}</a></span>""".format(theme) for theme in themes])
        return_message += "\n</div>"
        return return_message


def plot_htmlform(description:str):
    # the plot part of detailview html
    if description == "":
        return description
    else:
        return """
<div id="infotype-12" class="encyc-info-type br same-width-as-main">
<strong>Plot Summary:</strong>
	<span>{}</span>
</div>
        """.format(description)


def episodeAndRunningtime_htmlform(runningtime:str):
    # the running time/episode part of viewdetail html
    print(runningtime)
    if str(runningtime).isdigit() and int(runningtime) == 0:
        # means there is no available data, the program automatically sets to 0
        # for it is impossible to have any running time to be 0
        return ""
    elif str(runningtime).isdigit():
        # means this is a tv show, contain number of episode
        return """
<div id="infotype-3" class="encyc-info-type br same-width-as-main">
<strong>Number of episodes:</strong>
	<span>{}</span>
</div>""".format(runningtime)

    elif runningtime == "":
        return ""
    else:
        # means this is a movive, a total running time
        return """
<div id="infotype-4" class="encyc-info-type br same-width-as-main">
<strong>Running time:</strong> 
	<span>{}</span>
</div>
        """.format(runningtime)


def vintage_htmlform(vintage:list):
    # the vintage part of viewdetail html
    if len(vintage) == 0:
        # the vintage part should be a data, therefore should contain something
        # if len(vintage) == 0, means this data was not availabe when the system generat the file
        return ""
    else:
        return_message = """
<div id="infotype-7" class="encyc-info-type br same-width-as-main">
<strong>Vintage:</strong>
        <span>{}</span>
  """.format(vintage)
        return_message +="""\n</div>"""
        return return_message


def officialWebsite_htmlform(url:str):
    if url == "":
        return ""
    else:
        return """
<div id="infotype-10" class="encyc-info-type br same-width-as-main">
<strong>Official website:</strong>
	<div class="tab"><a target="_blank" rel="nofollow" href="{}">Click here</a> </div>
</div>""".format(url)

def type_htmlform(types:str):
    if types == "":
        return ''
    else:
        return """
        ({})
                """.format(types)

def openingTheme_htmlform(op:list):
    # the opening theme part of this anime
    if len(op) == 0:
        return ""
    else:
        return_message = """
<div id="infotype-11" class="encyc-info-type br same-width-as-main">
<strong>Opening Theme:</strong>"""

        for i in range(len(op)):
            return_message += """
    <div class="tab">#{}: {} </div>""".format(i+1, op[i])
        return_message += """\n</div>"""
        return return_message


def endingTheme_htmlform(ed:list):
    # the ending part of this anime
    if len(ed) == 0:
        return ""
    else:
        return_message = """
<div id="infotype-24" class="encyc-info-type br same-width-as-main">
<strong>Ending Theme:</strong>"""

        for i in range(len(ed)):
            return_message += """
            <div class="tab">#{}: {} </div>""".format(i + 1, ed[i])
        return_message += """\n</div>"""
        return return_message


def insertSong_htmlform(insertSong:list):
    # the inserting song part of this anime
    if len(insertSong) == 0:
        # when not song is available
        return ""
    else:
        return_message = """
<div id="infotype-35" class="encyc-info-type br same-width-as-main">
<strong>Insert Song:</strong>"""

        for i in range(len(insertSong)):
            return_message += """
                    <div class="tab">#{}: {} </div>""".format(i + 1, insertSong[i])
        return_message += """\n</div>"""
        return return_message

# a unused function

def search_by_genre(searchGenre:str):


    result = pd.DataFrame(columns=["show_name", "genre", "file_category"])
    for row in all_shows_list.itertuples(index=False):
        if searchGenre in row[1]:
            result = result.append({'show_name':row[0], 'genre':row[1], 'file_category':row[2]}, ignore_index=True)
    return result


# used when user returned a rating
def update_userRating(userId:int, animeId:int, rating:int, comment:str, time, ):
    # open the rating file data tha contains all the ratings
    filePath = os.path.join(os.getcwd(), "data_collection", "rating_data.json")
    # load to pandas dataframe
    userRating = pd.read_json(filePath, lines=True)

    if ( userRating.loc[(userRating["userId"] == userId) & (userRating["animeId"] == animeId)].empty ) and rating != "":
        # when is not find, means this user has not rate this anime

        newRow = pd.DataFrame([{"userId":userId, "animeId":animeId, "rating":rating, "comment":comment, "time":time}])

        userRating = userRating.append(newRow, ignore_index=True)
        #print(userRating)

        # write back to the file
        userRating.to_json(filePath, orient="records", lines=True)
    else:
        # to prevent the repeat rating when user refresh the page
        #print("rated")
        pass


def rating_htmlform(userId:int, animeId:int):
    # return the rating information,  after and before rated in viewdetail part
    ratingFile = pd.read_json(os.path.join(os.getcwd(), "data_collection", "rating_data.json"), lines=True)

    df = (ratingFile.loc[(ratingFile["userId"] == userId) & (ratingFile["animeId"] == animeId)])

    return_html = ""
    if df.empty:
        # means is has not been rated by current user
        # return a extra rating form
        # this is the rating form with 1 to 5 stars of rating
        return_html += """
            <div class="container">
                <h3>Rating</h3>
                <h5>1(low) to 5(high)</h5>
                <div class="pt-3">
                    <form action="/viewdetail/{}" method="POST">
                        <input id="input-2" name="ratingScore" class="rating rating-loading" data-min="0" data-max="5" data-step="1" value="0" data-size="md">
                        <strong>Comment</strong>
                        <input type="text"  name="comment" placeholder="leave your comment here" value="" size="100">
                        <button class="btn btn-primary" type="submit" >rate</button>
                    </form>
                </div>
            </div>
        """.format(animeId)

    # rating info of this animeId
    # a pandas dataframe
    animeRatingInfo = ratingFile.loc[ratingFile["animeId"] == animeId]
    #print(animeRatingInfo)
    return_html += """\
        
        
    <div class="container">

        {}
		<div class="row">
			<div class="col-sm-7">
				<hr/>
				<div class="review-block">
					

				{}
				</div>
			</div>
		</div>
    </div> 
         
        """.format(generate_general_review_form(animeId), generate_detail_review_form(animeRatingInfo))

    return return_html

def generate_average_rating_score(animeId:int):

    # this function generate the average rating score and each number of 5,4,3,2,1 start rating with bar size of rating form in html
    ratingFile = pd.read_json(os.path.join(os.getcwd(), "data_collection", "rating_data.json"), lines=True)
    animeRatingInfo = ratingFile.loc[ratingFile["animeId"] == animeId]
    # this return the general rating information of this anime
    totalRatingNumber = len(animeRatingInfo)
    fiveStarRatingNumber = len(animeRatingInfo.loc[animeRatingInfo["rating"] == 5])
    fourStarRatingNumber = len(animeRatingInfo.loc[animeRatingInfo["rating"] == 4])
    threeStarRatingNumber = len(animeRatingInfo.loc[animeRatingInfo["rating"] == 3])
    twoStarRatingNumber = len(animeRatingInfo.loc[animeRatingInfo["rating"] == 2])
    oneStarRatingNumber = len(animeRatingInfo.loc[animeRatingInfo["rating"] == 1])
    #print(fiveStarRatingNumber, twoStarRatingNumber, "here")

    if totalRatingNumber != 0:
        averageRating = (5*fiveStarRatingNumber + 4*fourStarRatingNumber + 3*threeStarRatingNumber + 2*twoStarRatingNumber + 1*oneStarRatingNumber)/totalRatingNumber
        averageRating = round(averageRating,2)
        fiveStarRatingBarPercentage = (fiveStarRatingNumber/totalRatingNumber) * 100
        fiveStarRatingBarPercentage = round(fiveStarRatingBarPercentage,2)
        fourStarRatingBarPercentage = (fourStarRatingNumber/totalRatingNumber) * 100
        fourStarRatingBarPercentage = round(fourStarRatingBarPercentage, 2)
        threeStarRatingBarPercentage = (threeStarRatingNumber/totalRatingNumber) * 100
        threeStarRatingBarPercentage = round(threeStarRatingBarPercentage, 2)
        twoStarRatingBarPercentage = (twoStarRatingNumber / totalRatingNumber) * 100
        twoStarRatingBarPercentage = round(twoStarRatingBarPercentage, 2)
        oneStarRatingBarPercentage = (oneStarRatingNumber / totalRatingNumber) * 100
        oneStarRatingBarPercentage = round(oneStarRatingBarPercentage, 2)
    else:
        # means no user has rate this anime yet
        # means need to set all things to zero, avoid zerodivision error
        averageRating = 0
        fiveStarRatingBarPercentage = 0
        fourStarRatingBarPercentage = 0
        threeStarRatingBarPercentage = 0
        twoStarRatingBarPercentage = 0
        oneStarRatingBarPercentage = 0

    return averageRating, fiveStarRatingBarPercentage, fiveStarRatingNumber, fourStarRatingBarPercentage, fourStarRatingNumber, threeStarRatingBarPercentage,threeStarRatingNumber, twoStarRatingBarPercentage, twoStarRatingNumber, oneStarRatingBarPercentage, oneStarRatingNumber
def generate_general_review_form(animeId):
    # this return the general rating information of this anime
    # means the total average rating and each 5,4,3,2,1, star rating's bar size
    """
    totalRatingNumber = len(animeRatingInfo)
    fiveStarRatingNumber = len(animeRatingInfo.loc[animeRatingInfo["rating"] == 5])
    fourStarRatingNumber = len(animeRatingInfo.loc[animeRatingInfo["rating"] == 4])
    threeStarRatingNumber = len(animeRatingInfo.loc[animeRatingInfo["rating"] == 3])
    twoStarRatingNumber = len(animeRatingInfo.loc[animeRatingInfo["rating"] == 2])
    oneStarRatingNumber = len(animeRatingInfo.loc[animeRatingInfo["rating"] == 1])
    #print(fiveStarRatingNumber, twoStarRatingNumber, "here")

    if totalRatingNumber != 0:
        averageRating = (5*fiveStarRatingNumber + 4*fourStarRatingNumber + 3*threeStarRatingNumber + 2*twoStarRatingNumber + 1*oneStarRatingNumber)/totalRatingNumber
        averageRating = round(averageRating,2)
        fiveStarRatingBarPercentage = (fiveStarRatingNumber/totalRatingNumber) * 100
        fiveStarRatingBarPercentage = round(fiveStarRatingBarPercentage,2)
        fourStarRatingBarPercentage = (fourStarRatingNumber/totalRatingNumber) * 100
        fourStarRatingBarPercentage = round(fourStarRatingBarPercentage, 2)
        threeStarRatingBarPercentage = (threeStarRatingNumber/totalRatingNumber) * 100
        threeStarRatingBarPercentage = round(threeStarRatingBarPercentage, 2)
        twoStarRatingBarPercentage = (twoStarRatingNumber / totalRatingNumber) * 100
        twoStarRatingBarPercentage = round(twoStarRatingBarPercentage, 2)
        oneStarRatingBarPercentage = (oneStarRatingNumber / totalRatingNumber) * 100
        oneStarRatingBarPercentage = round(oneStarRatingBarPercentage, 2)
    else:
        # means no user has rate this anime yet
        # means need to set all things to zero, avoid zerodivision error
        averageRating = 0
        fiveStarRatingBarPercentage = 0
        fourStarRatingBarPercentage = 0
        threeStarRatingBarPercentage = 0
        twoStarRatingBarPercentage = 0
        oneStarRatingBarPercentage = 0
    """
    averageRating, fiveStarRatingBarPercentage, fiveStarRatingNumber, fourStarRatingBarPercentage, fourStarRatingNumber, threeStarRatingBarPercentage, threeStarRatingNumber, twoStarRatingBarPercentage, twoStarRatingNumber, oneStarRatingBarPercentage, oneStarRatingNumber = generate_average_rating_score(animeId)

    return_html = """
		<div class="row">
			<div class="col-sm-3">
				<div class="rating-block">
					<h4>Average user rating</h4>
					<h2 class="bold padding-bottom-7">{} <small>/ 5</small></h2>
				</div>
			</div>
			<div class="col-sm-3">
				<h4>Rating breakdown</h4>
				<div class="pull-left">
					<div class="pull-left" style="width:35px; line-height:1;">
						<div style="height:9px; margin:5px 0;">5 <span class="glyphicon glyphicon-star"></span></div>
					</div>
					<div class="pull-left" style="width:180px;">
						<div class="progress" style="height:9px; margin:8px 0;">
						  <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="5" aria-valuemin="0" aria-valuemax="5" style="width: {}%">
							<span class="sr-only">80% Complete (danger)</span>
						  </div>
						</div>
					</div>
					<div class="pull-right" style="margin-left:10px;">{}</div>
				</div>
				<div class="pull-left">
					<div class="pull-left" style="width:35px; line-height:1;">
						<div style="height:9px; margin:5px 0;">4 <span class="glyphicon glyphicon-star"></span></div>
					</div>
					<div class="pull-left" style="width:180px;">
						<div class="progress" style="height:9px; margin:8px 0;">
						  <div class="progress-bar progress-bar-primary" role="progressbar" aria-valuenow="4" aria-valuemin="0" aria-valuemax="5" style="width: {}%">
							<span class="sr-only">80% Complete (danger)</span>
						  </div>
						</div>
					</div>
					<div class="pull-right" style="margin-left:10px;">{}</div>
				</div>
				<div class="pull-left">
					<div class="pull-left" style="width:35px; line-height:1;">
						<div style="height:9px; margin:5px 0;">3 <span class="glyphicon glyphicon-star"></span></div>
					</div>
					<div class="pull-left" style="width:180px;">
						<div class="progress" style="height:9px; margin:8px 0;">
						  <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="3" aria-valuemin="0" aria-valuemax="5" style="width: {}%">
							<span class="sr-only">80% Complete (danger)</span>
						  </div>
						</div>
					</div>
					<div class="pull-right" style="margin-left:10px;">{}</div>
				</div>
				<div class="pull-left">
					<div class="pull-left" style="width:35px; line-height:1;">
						<div style="height:9px; margin:5px 0;">2 <span class="glyphicon glyphicon-star"></span></div>
					</div>
					<div class="pull-left" style="width:180px;">
						<div class="progress" style="height:9px; margin:8px 0;">
						  <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="2" aria-valuemin="0" aria-valuemax="5" style="width: {}%">
							<span class="sr-only">80% Complete (danger)</span>
						  </div>
						</div>
					</div>
					<div class="pull-right" style="margin-left:10px;">{}</div>
				</div>
				<div class="pull-left">
					<div class="pull-left" style="width:35px; line-height:1;">
						<div style="height:9px; margin:5px 0;">1 <span class="glyphicon glyphicon-star"></span></div>
					</div>
					<div class="pull-left" style="width:180px;">
						<div class="progress" style="height:9px; margin:8px 0;">
						  <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="1" aria-valuemin="0" aria-valuemax="5" style="width: {}%">
							<span class="sr-only">80% Complete (danger)</span>
						  </div>
						</div>
					</div>
					<div class="pull-right" style="margin-left:10px;">{}</div>
				</div>
			</div>
		</div>    
    """.format(averageRating,
               fiveStarRatingBarPercentage, fiveStarRatingNumber,
               fourStarRatingBarPercentage, fourStarRatingNumber,
               threeStarRatingBarPercentage, threeStarRatingNumber,
               twoStarRatingBarPercentage, twoStarRatingNumber,
               oneStarRatingBarPercentage, oneStarRatingNumber)

    return return_html


def generate_detail_review_form(animeRatingInfo):
    return_html = ""
    for id in list(animeRatingInfo["userId"].values):
        # user id start with 1


        currentUser = animeRatingInfo.loc[animeRatingInfo["userId"] == id]

        if currentUser.empty:
            # means this user has not rate this anime yet
            continue
        user = app.User.query.filter_by(id=int(id)).first()
        if user.iconUrl == "":
            # means no image url
            iconUrl = "data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw=="
        else:
            iconUrl - user.iconUrl
        return_html += """
					<div class="row">
						<div class="col-sm-3">
							<img src="{}" width="200" height="200" class="img-responsive" >
							<div class="review-block-name">{}</a></div>
							<div class="review-block-date">{}</div>
						</div>
						<div class="col-sm-9">
						    <div class="review-block-rate">
            """.format(iconUrl, user.username ,currentUser["time"].values[0])

        # here is for the number of star rating icon that user give to this anime
        for x in range(1,5+1):
            # start with 1, since 1 is the lowest score one can give
            if x <= int(currentUser["rating"].values[0]):
                # button with yellow color
                return_html += """
								<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
                """
            else:
                # rating button with gray color
                return_html += """
								<button type="button" class="btn btn-default btn-grey btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
                """

        return_html += """
                            </div>

							<div class="review-block-description">{}</div>
						</div>
					</div>
					<hr/>
        """.format(currentUser["comment"].values[0])

    return return_html



def generate_recommend_carousel(recommendAnimeId):
    # carousel is the slide show at the recommendation html page
    # recommendAnimeId is a pandas datafreame, all anime id that was not view by user
    return_SGDcarousel = ""  # this is for the carousel view, the personalize recommendation
    return_ratingcarousel = "" # this is for the generatl rating form

    animeAverageRating = pd.DataFrame( data=[[generate_average_rating_score(id), id] for id in recommendAnimeId["animeId"]], columns=["averageScore", "animeId"])

    animeAverageRating = animeAverageRating.sort_values(by="averageScore", ascending=False) # a sorted pandas dataframe with highest averageScore


    #for animeId in recommendAnimeId.animeId:
    for i in range(recommendAnimeId.shape[0]):


        animeId_SGD = recommendAnimeId.iloc[i, 1]       # the anime id order for applying SGD
        animeId_averageRating = animeAverageRating.iloc[i,1] # the anime id order for the highest average rating score
        path_SGD = os.path.join(os.getcwd(), "anime_data",
                            str(animeId_SGD),
                            "{}.json".format(animeId_SGD, '@'))
        path_averageRating = os.path.join(os.getcwd(), "anime_data",
                            str(animeId_averageRating),
                            "{}.json".format(animeId_averageRating, '@'))
        #print(path)
        with open(path_SGD) as file:
            animeInfo_SGD = json.loads(file.read())
        with open(path_averageRating) as files:
            animeInfo_averageRating = json.loads(files.read())


        imageUrl_SGD = animeInfo_SGD["image"]
        name_SGD = animeInfo_SGD["show_name"]

        imageUrl_averageRating = animeInfo_averageRating["image"]
        name_averageRating = animeInfo_averageRating["show_name"]


        if imageUrl_averageRating == "":
            # means not picture availabe
            # set to a default picture
            imageUrl_averageRating = "https://causeofaction.org/wp-content/uploads/2013/09/Not-available-300x300.gif"
        if imageUrl_SGD == "":
            # means not picture availabe
            # set to a default picture
            imageUrl_SGD = "https://causeofaction.org/wp-content/uploads/2013/09/Not-available-300x300.gif"

        # the first carousel is different code with the rest
        if return_SGDcarousel == "":
            return_SGDcarousel += """
                <div class="carousel-item col-md-3 active">
                    <div class="panel panel-default">
                      <div class="panel-thumbnail">
                        <div class="card text-dark bg-light mb-3" style="width: 18rem;">

                          <img class="contain" src="{}" class="card-img-top" class="card-img-top" class="thumbnail" width="150px" height="165px" alt="..." >
                            <h5 class="card-header"> Top {} recommendation </h5>
                            <div class="card-body">
                            <h5 class="card-title">{}</h5>
                            <p class="card-text">{}/5</p>
                                    <button class = "btn btn-primary" type="button" onclick="document.location='{}'">Click Me!  </button>
                            </div>
                        </div>

                      </div>
                    </div>
                </div>

            """.format( imageUrl_SGD, i+1, name_SGD, generate_average_rating_score(animeId_SGD)[0], '/viewdetail/{}'.format(animeId_SGD) )

            return_ratingcarousel += """
                <div class="carousel-item col-md-3 active">
                    <div class="panel panel-default">
                      <div class="panel-thumbnail">
                        <div class="card text-dark bg-light mb-3" style="width: 18rem;">

                          <img class="contain" src="{}" class="card-img-top" class="card-img-top" class="thumbnail" width="150px" height="165px" alt="..." >
                            <h5 class="card-header"> Top {} recommendation </h5>
                            <div class="card-body">
                            <h5 class="card-title">{}</h5>
                            <p class="card-text">{}/5</p>
                                    <button class = "btn btn-primary" type="button" onclick="document.location='{}'">Click Me!  </button>
                            </div>
                        </div>

                      </div>
                    </div>
                </div>

            """.format( imageUrl_averageRating, i+1, name_averageRating, generate_average_rating_score(animeId_averageRating)[0], '/viewdetail/{}'.format(animeId_averageRating) )

        # the rest of the code for the carousel slide show
        else:
            return_SGDcarousel += """
                <div class="carousel-item col-md-3">
                    <div class="panel panel-default">
                      <div class="panel-thumbnail">
                        <div class="card text-dark bg-light mb-3" style="width: 18rem;">

                          <img class="contain" src="{}" class="card-img-top" class="card-img-top" class="thumbnail" width="150px" height="165px" alt="..." >
                            <h5 class="card-header"> Top {} recommendation </h5>
                            <div class="card-body">
                            <h5 class="card-title">{}</h5>
                            <p class="card-text">{}/5</p>
                                    <button class = "btn btn-primary" type="button" onclick="document.location='{}'">Click Me!  </button>
                            </div>
                        </div>

                      </div>
                    </div>
                </div>

            """.format( imageUrl_SGD, i+1, name_SGD,  generate_average_rating_score(animeId_SGD)[0], '/viewdetail/{}'.format(animeId_SGD) )

            return_ratingcarousel += """
                <div class="carousel-item col-md-3">
                    <div class="panel panel-default">
                      <div class="panel-thumbnail">
                        <div class="card text-dark bg-light mb-3" style="width: 18rem;">

                          <img class="contain" src="{}" class="card-img-top" class="card-img-top" class="thumbnail" width="150px" height="165px" alt="..." >
                            <h5 class="card-header"> Top {} recommendation </h5>
                            <div class="card-body">
                            <h5 class="card-title">{}</h5>
                            <p class="card-text">{}/5</p>
                                    <button class = "btn btn-primary" type="button" onclick="document.location='{}'">Click Me!  </button>
                            </div>
                        </div>

                      </div>
                    </div>
                </div>

            """.format( imageUrl_averageRating, i+1, name_averageRating,  generate_average_rating_score(animeId_averageRating)[0], '/viewdetail/{}'.format(animeId_averageRating) )

    #print(return_html)
    return return_SGDcarousel, return_ratingcarousel



def generate_search_result(searchWord:str):
    # search by anime title
    searchByTitle = all_shows_list.loc[all_shows_list["showName"].str.contains(searchWord, case=False, regex=False)]

    # returned a pandas dataframe with matched anime's basic information
    return searchByTitle

def generate_genre_search_result(genre:str):
    # will use about 6 to 7 seconds
    # returned the pandas dataframe of anime's basic information that matched to this genre type
    searchByGenre = pd.DataFrame(columns=['showName', 'genre', 'category', 'animeId'])

    for index, rows in all_shows_list.iterrows():
        #print(rows["genre"])
        if genre in rows["genre"]:

            searchByGenre = searchByGenre.append(rows)

    return searchByGenre




# all are some test cases

def test_genre_search_result():
    print(generate_genre_search_result("action"))


def test_alternativetitle_htmlform():
    print(alternativetitle_htmlform(["""セブンゴースト (Japanese)""", """神幻拍檔 (Chinese (Taiwan))"""]))

def test_image_htmlform():
    print(image_htmlformat("https://cdn.animenewsnetwork.com/thumbnails/fit200x200/encyc/A792-26.jpg"))

def test_genres_htmlform():
    print(genres_htmlform(["adventure", "horror", "supernatural"]))

def test_theme_htmlform():
    print(theme_htmlform(['amnesia', 'bishounen']))

def test_plot_htmlform():
    print(plot_htmlform("hello"))

def test_episodeAndRunningtime_htmlform():
    print(episodeAndRunningtime_htmlform("26"))
    print(episodeAndRunningtime_htmlform(" 25 minutes"))

def test_vintage_htmlform():
    print(vintage_htmlform(["2007-01-22 (production completed)", "2007-02-16 to 2007-02-19 (ep 1 net premiere to Yahoo! Premium members)", "2018-03-28 (Se\u00f1al Colombia - Colombia)"]))

def test_officialWebsite_htmlform():
    print(officialWebsite_htmlform("http://www.cwfilms.jp/5cm/index.htm"))

def test_openingTheme_htmlform():
    print(openingTheme_htmlform(["\"My Soul, Your Beats!\" by Lia", "\"My Soul, Your Beats! (Gldemo ver.)\" by Girls Dead Monster (ep 4)"]))

def test_endingTheme_htmlform():
    print(endingTheme_htmlform( ["\"Brave Song\" by Aoi Tada", "\"Ichiban no Takaramono ~Yui final ver.~ (\u4e00\u756a\u306e\u5b9d\u7269\uff5eYui final ver.\uff5e)\" by LiSA (ep 10)", "\"Ichiban no Takaramono\" (\u4e00\u756a\u306e\u5b9d\u7269) by Karuta (ep 13)"]))

def test_insertSong_htmlform():
    print(insertSong_htmlform(["\"Kamado Tanjir\u014d no Uta\" (\u7ac8\u9580\u70ad\u6cbb\u90ce\u306e\u3046\u305f) by Go Shiina featuring Nami Nakagawa (ep 19)"]))

def test_search():
    print(generate_search_result("date"))

def test_add_highlight():
    print(add_hightlight("hello", "lo"))

""""
other = return_other_list_panda()
for index, rows in other.iterrows():
    print(rows['file_category'],rows['show_name'])
"""
#print([str(row) for row in all_shows_list["show_name"]])
#all_shows_list["id"] = [i+1 for i in range(len(all_shows_list["show_name"]))]
#for show in all_shows_list["show_name"]:
 #   print(show)
#print(remove_windows_key_word("009 Re:Cyborg (movie)", "@"))
"""
x = (all_shows_list.loc[all_shows_list.id ==3])
print(x.show_name.item())
#print(return_o_list_panda())
rating_htmlform(1,5)
"""
#print(all_shows_list["id"])

print(return_o_list_panda())