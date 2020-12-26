"""
Sketchfab supports the Oauth2 protocol for authentication and authorization
### Introduction
- Please refer to the manual for missing/relevant information : https://tools.ietf.org/html/draft-ietf-oauth-v2-31
- This code sample does not work such as it is, it is a template that roughly shows how the token exchange works.
- This code sample is written in python but the same logic applies for every other language
### Requirements
To begin, obtain Oauth2 credentials from support@sketchfab.com.
You must provide us a redirect uri to which we can redirect your calls
### Implementation
The protocol works as follow:
1. You ask for an authorization code from the Sketchfab server with a supplied `redirect_uri`
2. Sketchfab asks permission to your user
3. A successful authorization will pass the client the authorization code in the URL via the supplied `redirect_uri`
4. You exchange this authorization code with an access token from the Sketchfab server
5. You use the access token to authenticate and authorize your user
"""
import pickle
import requests
import secrets
import json
import os
import pandas as pd
import numpy as np
import total_number_anime


def get_new_code_verifier() -> str:
    token = secrets.token_urlsafe(100)
    return token[:128]


code_verifier = code_challenge = get_new_code_verifier()

CLIENT_ID = "443541e57017cdbfa0fa3bde18c237dd"
CLIENT_SECRET = "67f520bc015bea4797d3bb1cbb04481968b813a614351aabc872569659db773e"

REDIRECT_URI = 'https://www.animerecommendation.cf/'
AUTHORIZE_URL = "https://myanimelist.net/v1/oauth2/authorize"
ACCESS_TOKEN_URL = "https://myanimelist.net/v1/oauth2/token"

with open(os.path.join(os.getcwd(), "initalize_data.json"), "r") as f:
    file_info = json.loads(f.read())

access_token = file_info['access_token']
refresh_token = file_info['refresh_token']
print(access_token)
print(refresh_token)

# access_toke = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU5NWYwNDk3NTFiNTJmNzcyZDBiZTcwMzI4N2EyNjg0MTJiYWE5ZGE2ODQ2MDI1NDg2ZDg4Zjg5YzUwMzBhM2Q0ODZkOWM2NmUyMjc4OGRlIn0.eyJhdWQiOiI0NDM1NDFlNTcwMTdjZGJmYTBmYTNiZGUxOGMyMzdkZCIsImp0aSI6IjU5NWYwNDk3NTFiNTJmNzcyZDBiZTcwMzI4N2EyNjg0MTJiYWE5ZGE2ODQ2MDI1NDg2ZDg4Zjg5YzUwMzBhM2Q0ODZkOWM2NmUyMjc4OGRlIiwiaWF0IjoxNjA4NTcyODg1LCJuYmYiOjE2MDg1NzI4ODUsImV4cCI6MTYxMTI1MTI4NSwic3ViIjoiMTA5NjM5ODYiLCJzY29wZXMiOltdfQ.Ic8ubYWDoyflOYDacE3c77DmprM8lKG22rXzAmBhLOAoKABb_W4xfErYuCPhFOyMq0YMZJyk_5ZoDWqXhU3I1XXykZ0SHQw38IYa8nwyT_-LRPgM-IB1HFv4uVwDNiNrPpN-dssff0O4SWsWtdh-kp2istI_CfmWiHr2qPdsGCQcbaEOcRcJoZ1Dehk7oYu6w8yNP-tPyVZbv_p8LRrZ7gBDpCkACejS47vI0dEcZvYTbkXpMQZabh0UjE68Pp8evdTlktaDE2jWes7xE-xCcVSadaWx5KJUyzF-kWCLay4p2D55u0BQ5_F4Y0gnSgflhm7s0nrW2gvZk4jhLw-KwQ'
# 1. Ask for an authorization code\
# print(code_challenge) #4J8CS7CdupXixj_IYoh36_kOs9-xi6mYeGXVMt5HeRfRPNIDSQxg5H4NFB2VPxS2wO99j58vMtxEeXy388_AoMLvbdkptx3UE4EG_gmAhUTu4VfcaZmHWaEbJApvWR_m
# print('{}?response_type=code&client_id={}&code_challenge={}&state=RequestID42'.format(AUTHORIZE_URL, CLIENT_ID, code_challenge, REDIRECT_URI))
# response = requests.get('{}?response_type=code&client_id={}&code_challenge={}&state=RequestID42'.format(AUTHORIZE_URL, CLIENT_ID, code_challenge, REDIRECT_URI))
# after response https://www.google.com/?code=def502001cc550aadaf3fb69a2d74996127d2c2008251f031e2628ae83c44d2f7d5c5c393aa31470b023c96a056256983f3f549f217ff94369ed2dec616c62ac3a753a6b2b4819d28ebd9118dfaca148c6b9d198cbc7d68bf3c6c5b32241850a9eefc6d7db9a5ce19775d362b13dec0d12546c764dc763c15d0230be8a3b2f070d24dbfc7c8d53f6c71a7947f5adc26e09832791f0391bbc13498bd85890d51bf25d6ed7fea4ed4d524a90c6f629cf6fce38eaa7d11e4b8c962881173fdf90fcd4e335c51a4e111012e98aa3530c82e8953489a6315981d861cbae978b5d22f0c0c358bcc13780aada5fb1d3115ce785537f86900752cad37b524c43372e233c9e908e8aa64a23114086445df38ff94fb979b2f1b591e1076434767f2f2de9806a682475fe4da50f044c4e0e3ca899f434f86af3887352b227103be61afdaa8c47f6d656ee223ec67242ac632a66ee4f8fdb597132d9d841f969fd1cc7a0fdd2a14f4d50ffac11ab2207361ff68e3553fc85f3f57504a0c2c610687ae4e30ba460f45a102d367e77054f52b1a034fd87e29bb66625857e76d64a39f50e6fb56f40bc85d48de0a83d1843bbe44080fcb080ef7aa7ea8e3d4846dc52069787b0ca19ebbbea2721fdc50afaf6b4e5b80c37d73532d9171d43277e47dcd96b700442a7039e1df8a7c5a62b80&state=RequestID42
# print(response.status_code)
# print(response.status_code)
"""
response = requests.post(
    ACCESS_TOKEN_URL,
    data={
        'client_id': CLIENT_ID,
        'client_secret' : CLIENT_SECRET,
        'code': 'def502001cc550aadaf3fb69a2d74996127d2c2008251f031e2628ae83c44d2f7d5c5c393aa31470b023c96a056256983f3f549f217ff94369ed2dec616c62ac3a753a6b2b4819d28ebd9118dfaca148c6b9d198cbc7d68bf3c6c5b32241850a9eefc6d7db9a5ce19775d362b13dec0d12546c764dc763c15d0230be8a3b2f070d24dbfc7c8d53f6c71a7947f5adc26e09832791f0391bbc13498bd85890d51bf25d6ed7fea4ed4d524a90c6f629cf6fce38eaa7d11e4b8c962881173fdf90fcd4e335c51a4e111012e98aa3530c82e8953489a6315981d861cbae978b5d22f0c0c358bcc13780aada5fb1d3115ce785537f86900752cad37b524c43372e233c9e908e8aa64a23114086445df38ff94fb979b2f1b591e1076434767f2f2de9806a682475fe4da50f044c4e0e3ca899f434f86af3887352b227103be61afdaa8c47f6d656ee223ec67242ac632a66ee4f8fdb597132d9d841f969fd1cc7a0fdd2a14f4d50ffac11ab2207361ff68e3553fc85f3f57504a0c2c610687ae4e30ba460f45a102d367e77054f52b1a034fd87e29bb66625857e76d64a39f50e6fb56f40bc85d48de0a83d1843bbe44080fcb080ef7aa7ea8e3d4846dc52069787b0ca19ebbbea2721fdc50afaf6b4e5b80c37d73532d9171d43277e47dcd96b700442a7039e1df8a7c5a62b80',
        'code_verifier' : '4J8CS7CdupXixj_IYoh36_kOs9-xi6mYeGXVMt5HeRfRPNIDSQxg5H4NFB2VPxS2wO99j58vMtxEeXy388_AoMLvbdkptx3UE4EG_gmAhUTu4VfcaZmHWaEbJApvWR_m',
        'grant_type': 'authorization_code'

    }
)
"""


# expire in 31 days
# print(response)
# print(response.json())

# result {'token_type': 'Bearer', 'expires_in': 2678400, 'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU5NWYwNDk3NTFiNTJmNzcyZDBiZTcwMzI4N2EyNjg0MTJiYWE5ZGE2ODQ2MDI1NDg2ZDg4Zjg5YzUwMzBhM2Q0ODZkOWM2NmUyMjc4OGRlIn0.eyJhdWQiOiI0NDM1NDFlNTcwMTdjZGJmYTBmYTNiZGUxOGMyMzdkZCIsImp0aSI6IjU5NWYwNDk3NTFiNTJmNzcyZDBiZTcwMzI4N2EyNjg0MTJiYWE5ZGE2ODQ2MDI1NDg2ZDg4Zjg5YzUwMzBhM2Q0ODZkOWM2NmUyMjc4OGRlIiwiaWF0IjoxNjA4NTcyODg1LCJuYmYiOjE2MDg1NzI4ODUsImV4cCI6MTYxMTI1MTI4NSwic3ViIjoiMTA5NjM5ODYiLCJzY29wZXMiOltdfQ.Ic8ubYWDoyflOYDacE3c77DmprM8lKG22rXzAmBhLOAoKABb_W4xfErYuCPhFOyMq0YMZJyk_5ZoDWqXhU3I1XXykZ0SHQw38IYa8nwyT_-LRPgM-IB1HFv4uVwDNiNrPpN-dssff0O4SWsWtdh-kp2istI_CfmWiHr2qPdsGCQcbaEOcRcJoZ1Dehk7oYu6w8yNP-tPyVZbv_p8LRrZ7gBDpCkACejS47vI0dEcZvYTbkXpMQZabh0UjE68Pp8evdTlktaDE2jWes7xE-xCcVSadaWx5KJUyzF-kWCLay4p2D55u0BQ5_F4Y0gnSgflhm7s0nrW2gvZk4jhLw-KwQ', 'refresh_token': 'def502008d3a4e8f275ca4f7d4a54887a3b361e75806407656e22ee84169c1b3664c22f3cae1f0f3d4f4e2ead5d4ed2c8e75f490a857ee013d981b8e733ea50fd1814ac6a19b3c23968c1172453461d5e18e88de918790ced821c153f61bf40baded44f1c038982b7d9a11df5813ef970b7cc07ee7c03922a63ff3084b79690042ff794614121db7281b54f2b13f606fe43d4a3bb7f347d7309ca07c721008e2e56976dd7cce8537fa254cfbe689053dd415a82b820827045665a7776de724b085deb512142d620de5f4cb06b80f06073db182bc5b216e091eef114ea49a4b50bbf2d5c0b3921c97caf709b25a78264824efc110827ab4d227fb794d3cdf161903f76191d40179a6fe4afa48dbdea524f469f38c8464d04eab929cf7a428c71377b7759321663e3c2aaca2f5bc44e8914027a9880b71242278f83f989a94ba3a8b2474b845b4bb12cf47694f5a7ebd0fb0d4041271ddcd47a9483e7f7fcc7ace597970e16636715885f34d2200003e0dbfbc71ac6bc58847a6c03a6b35a1f987992a29cc119839b31a'}
# {'token_type': 'Bearer', 'expires_in': 2678400, 'access_token':         'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjNiMTZmNmUwZTgwMmU5YjgwOGM2ZTFiZDlhM2M5ODE5OGEzZmIwN2VhNGU5MGRjNThkZGM0MWM1MTkyYmYxZjViNTIxODdkM2MxNTdjNmNmIn0.eyJhdWQiOiI0NDM1NDFlNTcwMTdjZGJmYTBmYTNiZGUxOGMyMzdkZCIsImp0aSI6IjNiMTZmNmUwZTgwMmU5YjgwOGM2ZTFiZDlhM2M5ODE5OGEzZmIwN2VhNGU5MGRjNThkZGM0MWM1MTkyYmYxZjViNTIxODdkM2MxNTdjNmNmIiwiaWF0IjoxNjA4NTczNzg5LCJuYmYiOjE2MDg1NzM3ODksImV4cCI6MTYxMTI1MjE4OSwic3ViIjoiMTA5NjM5ODYiLCJzY29wZXMiOltdfQ.a538gry2obc98d4HzfajkSwVjC_dWufbIqx2AmvQbEedafC2xsFBrWvliM67BvhDUzHt1ib0O9KGETpGkUpAYgHIZld6KNlGXG8PENzTFNE3FpKOVR4thhwIoSGOyEeOyscSipOBvp9JZlq3Qk97v_cnp8EHrcrTAfCTg7faICCeqIKTEYBynkVl8iD4-Le5PZp1RMzGZW71ojIpw_6xj0PaJGxORoTKXG_F-RXNFQrct7e5jb_XEjDre98J3dBZyGIeADnDe094Kq3K2l7HFr2Up_-USJDAjb_pLEh1SXpH7BqKGkuESrOKijhhS_o9uRa-stNCE51vwortEpxHlw', 'refresh_token': 'def502003a2d1f19d1defc608439b5da39ef7db64f1511c64e4d4fe176b3cf64530184119a37ce60a36db2372bf638a1210956e7404cb5f8fcec1155bed0067ca1e30c2c850f75f36ab667c3a71f4ae2cf1d94dfeb279aa78c449a137f5c73937f6282be1197d79481964eb2427e9aa441582cbe8b1f7e235404313da841254b0850ef86be0f55f32144a76dd32c7fa26f8e9f2469e0cbe5a5b09a305f90e8ba063e870605538b86ac83e57c6ad47214dae151dc7d39e4b2ec8e2bce4a4068a107edfe805fa0df0a8f10341e1d60b3510d0b594cea2a2421d4029626afba260207ae977bbc8c2bd786bff40f419044bebf67e87f9b3f73d5cd1cd6ef41f6505489e8cf513d6e48e869c0efb3e1dac2e1272c25cc740ab080f44bc1c1ad350ac6a3032a27d493b118108afa8ebb543c64e1aa3637c3c3c80670f24b94330abbedf6e12bbf6367f2ee33c3517d2ffb4dbf0d01f33ee27cdbfe7a14af08152c45b541573c09fc901a69a4ac7523cb904db1a2de5ca65b5433271c31bdf46fb052e377a746f3747f0493c2'}


def print_user_info(access_token: str):
    url = 'https://api.myanimelist.net/v2/users/@me'
    response = requests.get(url, headers={
        'Authorization': f'Bearer {access_token}'
    })

    response.raise_for_status()
    user = response.json()
    response.close()

    print(f"\n>>> Greetings {user['name']}! <<<")


# refresh token
def refresh(refresh_token: str):
    response = requests.post(
        ACCESS_TOKEN_URL,
        data={
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }
    )

    with open("initalize_data.json", "w") as file:
        file.write(json.dumps(response.json()))


def anime_info(access_token: str, animeId: int):
    url = 'https://api.myanimelist.net/v2/anime/{}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics, opening_themes, ending_themes'.format(
        animeId)
    response = requests.get(url, headers={
        'Authorization': f'Bearer {access_token}'
    })

    # response.raise_for_status()

    # response.close()
    if response.status_code == 404:
        return "end"
    elif response.status_code == 503:
        return "busy"  # means the server is busy
    elif response.status_code == 200:
        print("send info")
        return response.json()
    else:
        return "unknow error"


print(anime_info(access_token, 1))
print(anime_info(access_token, 1689))
print(anime_info(access_token, 15583))


# here initalize anime begin

# got inside first, then get info

def createFolder(directory):
    # create windows file
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def total_number_of_show():
    # use try and error method to see how many anime are in the myanimelist

    end = False
    currentAnimeNumber = 17380  # start with a sure number

    result = requests.get('https://myanimelist.net/topanime.php?limit={}'.format(currentAnimeNumber))
    while result.status_code != 404:
        if result.status_code == 503:
            # means the server is busy
            continue
        currentAnimeNumber += 1
        result = requests.get('https://myanimelist.net/topanime.php?limit={}'.format(currentAnimeNumber))

        # means still exist

    return currentAnimeNumber - 1  # this should be all number of anime


def search_result(webId):
    global  allAnimeDataFile
    return allAnimeDataFile.loc[allAnimeDataFile["websiteId"] == webId]

def search_list(showName: str):
    global allAnimeDataFile
    # print(allAnimeDataFile)
    all_shows_list = allAnimeDataFile

    def return_a_list_panda():
        # generate all a list
        a_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "A") | (all_shows_list["showName"].str[0] == "a")]
        return a_category_panda

    def return_other_list_panda():
        a_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "A") | (all_shows_list["showName"].str[0] == "a")]

        # generate the all other list
        #   all other list will be everything before the first index of a list

        if len(a_category_panda) == 0:
            # means contain nothing, just return all_shows_lists
            return all_shows_list

        first_a_index = a_category_panda.head(1).index

        other_category_panda = (all_shows_list.iloc[: first_a_index[0]])
        return other_category_panda

    def return_b_list_panda():
        # generate all b list
        b_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "B") | (all_shows_list["showName"].str[0] == "b")]

        return b_category_panda

    def return_c_list_panda():
        # generate all c list
        c_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "C") | (all_shows_list["showName"].str[0] == "c")]

        return c_category_panda

    def return_d_list_panda():
        # generate all d list
        d_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "D") | (all_shows_list["showName"].str[0] == "d")]

        return d_category_panda

    def return_e_list_panda():
        # generate all e list
        e_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "E") | (all_shows_list["showName"].str[0] == "e")]

        return e_category_panda

    def return_f_list_panda():
        # generate all f list
        f_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "F") | (all_shows_list["showName"].str[0] == "f")]

        return f_category_panda

    def return_g_list_panda():
        # generate all g list
        g_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "G") | (all_shows_list["showName"].str[0] == "g")]

        return g_category_panda

    def return_h_list_panda():
        # generate all h list
        h_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "H") | (all_shows_list["showName"].str[0] == "h")]

        return h_category_panda

    def return_i_list_panda():
        # generate all i list
        i_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "I") | (all_shows_list["showName"].str[0] == "i")]

        return i_category_panda

    def return_j_list_panda():
        # generate all j list
        j_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "J") | (all_shows_list["showName"].str[0] == "j")]

        return j_category_panda

    def return_k_list_panda():
        # generate all k list
        k_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "K") | (all_shows_list["showName"].str[0] == "k")]

        return k_category_panda

    def return_l_list_panda():
        # generate all l list
        l_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "L") | (all_shows_list["showName"].str[0] == "l")]

        return l_category_panda

    def return_m_list_panda():
        # generate all m list
        m_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "M") | (all_shows_list["showName"].str[0] == "m")]

        return m_category_panda

    def return_n_list_panda():
        # generate all n list
        n_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "N") | (all_shows_list["showName"].str[0] == "n")]

        return n_category_panda

    def return_o_list_panda():
        # generate all o list
        o_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "O") | (all_shows_list["showName"].str[0] == "o")]
        return o_category_panda

    def return_p_list_panda():
        # generate all p list
        p_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "P") | (all_shows_list["showName"].str[0] == "p")]
        return p_category_panda

    def return_q_list_panda():
        # generate all q list
        q_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "Q") | (all_shows_list["showName"].str[0] == "q")]
        return q_category_panda

    def return_r_list_panda():
        # generate all r list
        r_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "R") | (all_shows_list["showName"].str[0] == "r")]
        return r_category_panda

    def return_s_list_panda():
        # generate all s list
        s_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "S") | (all_shows_list["showName"].str[0] == "s")]
        return s_category_panda

    def return_t_list_panda():
        # generate all t list
        t_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "T") | (all_shows_list["showName"].str[0] == "t")]
        return t_category_panda

    def return_u_list_panda():
        # generate all u list
        u_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "U") | (all_shows_list["showName"].str[0] == "u")]
        return u_category_panda

    def return_v_list_panda():
        # generate all v list
        v_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "V") | (all_shows_list["showName"].str[0] == "v")]
        return v_category_panda

    def return_w_list_panda():
        # generate all w list
        w_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "W") | (all_shows_list["showName"].str[0] == "w")]
        return w_category_panda

    def return_x_list_panda():
        # generate all x list
        x_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "X") | (all_shows_list["showName"].str[0] == "x")]

        return x_category_panda

    def return_y_list_panda():
        # generate all Y list
        y_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "Y") | (all_shows_list["showName"].str[0] == "y")]
        return y_category_panda

    def return_z_list_panda():
        # generate all Z list
        z_category_panda = all_shows_list.loc[
            (all_shows_list["showName"].str[0] == "Z") | (all_shows_list["showName"].str[0] == "z")]
        return z_category_panda

    firstLetter = showName[0]
    firstLetter = firstLetter.lower()

    if firstLetter == "a":
        return return_a_list_panda()
    elif firstLetter == "b":
        return return_b_list_panda()
    elif firstLetter == "c":
        return return_c_list_panda()
    elif firstLetter == "d":
        return return_d_list_panda()
    elif firstLetter == "e":
        return return_e_list_panda()
    elif firstLetter == "f":
        return return_f_list_panda()
    elif firstLetter == "g":
        return return_g_list_panda()
    elif firstLetter == "h":
        return return_h_list_panda()
    elif firstLetter == "i":
        return return_i_list_panda()
    elif firstLetter == "j":
        return return_j_list_panda()
    elif firstLetter == "k":
        return return_k_list_panda()
    elif firstLetter == "l":
        return return_l_list_panda()
    elif firstLetter == "m":
        return return_m_list_panda()
    elif firstLetter == "n":
        return return_n_list_panda()
    elif firstLetter == "o":
        return return_o_list_panda()
    elif firstLetter == "p":
        return return_p_list_panda()
    elif firstLetter == "q":
        return return_q_list_panda()
    elif firstLetter == "r":
        return return_r_list_panda()
    elif firstLetter == "s":
        return return_s_list_panda()
    elif firstLetter == "t":
        return return_t_list_panda()
    elif firstLetter == "u":
        return return_u_list_panda()
    elif firstLetter == "v":
        return return_v_list_panda()
    elif firstLetter == "w":
        return return_w_list_panda()
    elif firstLetter == "x":
        return return_x_list_panda()
    elif firstLetter == "y":
        return return_y_list_panda()
    elif firstLetter == "z":
        return return_z_list_panda()
    else:
        return return_other_list_panda()


def check_exist(showName: str, webId: int):
    # check if this anime already initalized
    #searchList = search_list(showName)
    "##############3333"
    # print(searchList)
    """
    for index, row in searchList.iterrows():
        print(row["websiteId"])
        if row["showName"] == showName and int(webId) == row["websiteId"]:
            # print(row["showName"])
            return True
    """
    searchResult = search_result(webId)
    if len(searchResult ) == 0:
        return False
    else:
        return  True


def correspond_animeId_with_webId(webId):
    global allAnimeDataFile
    return allAnimeDataFile.loc[allAnimeDataFile["websiteId"] == webId]["animeId"].values[0]

def alternative_title(animeData):
    # print(animeData["alternative_titles"])
    other_title = []
    for name in animeData["alternative_titles"].values():
        if type(name) == list:
            # used for synonymf
            for nam in name:
                if nam != "":
                    other_title.append(nam)
        elif name != "":
            other_title.append(name)
    return other_title


def genres(animeData):
    animeGenre = []
    if 'genres' not in animeData.keys():
        return []
    genre_list = animeData["genres"]
    for genre in genre_list:
        animeGenre.append(genre["name"])
    return animeGenre


def types(animeData):
    return (animeData['media_type'])


def plot(animeData):
    if 'plot' not in animeData.keys():
        return ''
    return animeData['synopsis']


def episode(animeData):
    return animeData['num_episodes']


def vintage(animeData):
    if animeData["status"] == "currently_airing":
        return "currently airing"
    elif animeData['status'] == 'not_yet_aired':
        return "not yet aired"
    elif 'start_date' not in animeData.keys() and 'end_date' not in animeData.keys():
        return "? - ?"
    if 'end_date' not in animeData.keys():
        return str(animeData['start_date'] + " - " + "?")
    if "start_date" not in animeData.keys():
        return str("?" + " - " + animeData['end_date'])

    return str(animeData["start_date"] + " - " + animeData["end_date"])


def opening_themes(animeData):
    anime_op = []
    if "opening_themes" not in animeData.keys():
        # when no opening themes exist
        return []
    op = animeData["opening_themes"]
    for dicty in op:
        anime_op.append(dicty['text'])
    return anime_op


def ending_themes(animeData):
    anime_ed = []

    if "ending_themes" not in animeData.keys():
        return []

    ed = animeData["ending_themes"]
    for dicty in ed:
        anime_ed.append(dicty['text'])
    return anime_ed


def picture_url(animeData):
    if 'main_picture' not in animeData.keys():
        return ""
    return animeData["main_picture"]["medium"]


def initalize_anime_data(animeData, accessAnimeId):
    global allAnimeDataFile
    global genre_list_dicty
    dicty_info = {}  # store in each individual file
    animeInfoList = []  # will be store in pandas dataframe
    #print(animeId)
    print(animeData)

    # a fake one

    dicty_info["show_name"] = animeData["title"]
    animeInfoList.append(animeData["title"])

    if check_exist(animeData["title"], accessAnimeId) == False:
        pre_exist = False
        # add from the last anime id we have in the system
        if len(allAnimeDataFile) == 0:
            animeId = 1
        else:
            s = allAnimeDataFile.sort_values(by=["animeId"])
            animeId = s.iloc[-1]["animeId"] + 1
        #animeId = len(allAnimeDataFile)+1
        createFolder(os.path.join(current_direct, "anime_data", str(animeId)))
    else:
        pre_exist = True
        # remember, not all anime id exist in the numerical sequence
        animeId = allAnimeDataFile.loc[allAnimeDataFile["showName"] == animeData["title"]]["animeId"].values[0]
        #animeId = correspond_animeId_with_webId(accessAnimeId)
        #print("heheqqqqq")
    dicty_info["other_title"] = alternative_title(animeData)

    dicty_info["genre"] = genres(animeData)
    animeInfoList.append(dicty_info["genre"])

    # not theme, theme instead of type
    dicty_info["type"] = types(animeData)

    dicty_info['plot'] = plot(animeData)

    dicty_info['episode'] = episode(animeData)

    dicty_info['vintage'] = vintage(animeData)

    # remove official website

    dicty_info['opening_theme'] = opening_themes(animeData)

    dicty_info['ending_theme'] = ending_themes(animeData)

    # not insert song

    dicty_info['image'] = picture_url(animeData)

    # remove category

    filename = str(animeId) + ".json"

    with open(os.path.join(current_direct, 'anime_data', str(animeId), filename), "w") as f:
        f.write(json.dumps(dicty_info))

    if pre_exist == False:
        # with open(os.path.join(current_direct, "anime_data", "{0}_shows".format(catgory), show_title_no_key, "data.json"), "w") as f:
        # the info of each genre used for SGD(stochaastic gradient descent )
        showGenreInfo = {}

        """
        with open(os.path.join(current_direct, "anime_data", str(animeId), "data.json"), "w") as f:
            #
            with open(os.path.join(current_direct, "genres.json"), "r") as genres_file:
                genre_list = json.loads(
                    genres_file.read())  # the list contain all the genres type, or the k of user and movie in matrix factorization

                for genre in list(genre_list):
                    # if the show under this genre, give a inital of 2.5
                    # else give 0, since 0 times anything will go to zero
                    if genre in dicty_info["genre"]:
                        showGenreInfo[genre] = 2.5
                    else:
                        showGenreInfo[genre] = 0
            showGenreInfo["bias"] = 0
            print(showGenreInfo)

            genre_list_dicty.append(showGenreInfo)   # intent to write into 1 file

            f.write(json.dumps(showGenreInfo))  # testing only


            """

        with open(os.path.join(current_direct, "genres.json"), "r") as genres_file:
            genre_list = json.loads(
                genres_file.read())  # the list contain all the genres type, or the k of user and movie in matrix factorization

            for genre in list(genre_list):
                # if the show under this genre, give a inital of 2.5
                # else give 0, since 0 times anything will go to zero
                if genre in dicty_info["genre"]:
                    showGenreInfo[genre] = 2.5
                else:
                    showGenreInfo[genre] = 0
        showGenreInfo["bias"] = 0
        print(showGenreInfo)

        genre_list_dicty.append(showGenreInfo)  # intent to write into 1 file


    else:
        # already exist before
        # so will not try to erase the data inside the file

        # Not all anime contains a genre a first, so check if all k(genre) factor is 0 or not
        # if yes, try to update the information, hope others has already update and add some genres for this show

        """
        with open(os.path.join(current_direct, "anime_data", str(animeId), "data.json"), "r") as file:
            animeGenreK = json.loads(file.read())
            print(animeGenreK)
            # print("test")

        """

        animeGenreK = genre_list_dicty[animeId - 1]  # since the index start with 0

        noGenreContain = True  # use to check if this anime is under any genre category last time,
        genreAdd = False  # use to see if any genre added into this anime since last time update
        genreDelet = False  # use to see if any genre was removed under this anime since last time update
        for key in animeGenreK.keys():
            if key != "bias":

                if animeGenreK[key] != 0:
                    noGenreContain = False
                if key not in dicty_info["genre"]:

                    if animeGenreK[key] != 0:
                        # means this anime is no longer under this genre
                        # value is not 0 means it was under thie category before
                        genreDelet = True
                if key in dicty_info["genre"]:
                    if animeGenreK[key] == 0:
                        # means this genre was not classified under this anime last time
                        genreAdd = True

        if noGenreContain:
            # means all genre k value is 0, the anime is not category under any genre when updating last time
            showGenreInfo = {}
            with open(os.path.join(current_direct, "genres.json"), "r") as genres_file:
                genre_list = json.loads(
                    genres_file.read())  # the list contain all the genres type, or the k of user and movie in matrix factorization

                for genre in list(genre_list):
                    # if the show under this genre, give a inital of 2.5
                    # else give 0, since 0 times anything will go to zero
                    if genre in dicty_info["genre"]:
                        showGenreInfo[genre] = 2.5
                    else:
                        showGenreInfo[genre] = 0

                showGenreInfo["bias"] = 0
            genre_list_dicty[animeId - 1] = showGenreInfo

            """
            with open(os.path.join(current_direct, "anime_data", str(animeId), "data.json"), "w") as file:
                file.write(json.dumps(showGenreInfo))  # testing only
                print("was detect unknow genre last time")
                """
        if genreDelet:

            with open(os.path.join(current_direct, "genres.json"), "r") as genres_file:
                genre_list = json.loads(
                    genres_file.read())  # the list contain all the genres type, or the k of user and movie in matrix factorization

            for genre in list(genre_list):
                if genre not in dicty_info["genre"]:
                    # assign any genre to 0 if is not under this anime
                    # thus the origin genre will also get deleted
                    # print(genre)
                    animeGenreK[genre] = 0
            genre_list_dicty[animeId - 1] = animeGenreK
            # print(animeGenreK)
            # write back to file
            """
            with open(os.path.join(current_direct, "anime_data", str(animeId), "data.json"), "w") as f:
                f.write(json.dumps(animeGenreK))
                """
        if genreAdd:
            with open(os.path.join(current_direct, "genres.json"), "r") as genres_file:
                genre_list = json.loads(
                    genres_file.read())  # the list contain all the genres type, or the k of user and movie in matrix factorization

            for genre in list(genre_list):
                if genre in dicty_info["genre"] and animeGenreK[genre] == 0:
                    # assign any genre that is in the list but is equal to 0
                    # means assign any genre type that was not in the list before
                    animeGenreK[genre] = 2.5
            # update it back
            genre_list_dicty[animeId - 1] = animeGenreK
            # write back to file
            """
            with open(os.path.join(current_direct, "anime_data", str(animeId), "data.json"), "w") as f:
                f.write(json.dumps(animeGenreK))
                """

    if len(allAnimeDataFile) > 0 and (check_exist(dicty_info["show_name"], accessAnimeId) == True):
        print("same ********************")
        pass
    else:

        animeInfoList.append(animeId)
        print("The accesss id is ", accessAnimeId)
        animeInfoList.append(accessAnimeId)  # also put the website's id here
        # print(animeInfoList)
        df = pd.DataFrame([animeInfoList], columns=["showName", "genre", "animeId", "websiteId"])

        allAnimeDataFile = pd.concat([df, allAnimeDataFile])


def write_all_info():
    global allAnimeDataFile
    global genre_list_dicty, animeGenrePath
    allAnimeDataFileSorted = allAnimeDataFile.sort_values("showName", ignore_index=True)

    allAnimeDataFileSorted.to_json(os.path.join(current_direct, "data_collection", "all_shows.json"), orient="records",
                                   lines=True)

    allAnimeDataFile = allAnimeDataFileSorted
    #print(genre_list_dicty)
    # for the k(genres)
    with open(animeGenrePath, "wb") as wfp:
        pickle.dump(genre_list_dicty, wfp)


current_direct = os.getcwd()

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


# for the general information
allAnimeDataFile = pd.read_json(os.path.join(os.getcwd(), "data_collection", "all_shows.json"), lines=True)

genre_list_dicty = []  # a numpy array of anime website id
# a list of dictionary for each anime

animeGenrePath = os.path.join(os.getcwd(), "data_collection", "animeGenres.pickle")
if os.path.exists(animeGenrePath):
    with open(animeGenrePath, "rb") as rfp:
        genre_list_dicty = pickle.load(rfp)

if allAnimeDataFile.shape[0] == 0:
    # means contain nothing,
    allAnimeDataFile = pd.DataFrame(columns=["showName", "genre", "animeId", "websiteId"])


def update():
    # iteratve over each anime id

    #access_animeId_list = total_number_anime.webAnimeIdLists()


    with open("webid.pickle", "rb") as f:

        access_animeId_list = pickle.load(f)
    print(len(access_animeId_list))
    #totalAnimeNumber = total_number_of_show()
    # print(totalAnimeNumber , "total")


    iteration = 1

    # print(totalAnimeNumber)

    genre_list_dicty = []

    while iteration != len(access_animeId_list) + 1:
        result = anime_info(access_token, access_animeId_list[iteration - 1])
        if result == 'end':
            # a 404 error
            print("error occurs !")
        elif result == 'busy':
            continue
        elif result == 'unknown error':
            print("An error occur at id " + str(access_animeId_list[iteration - 1]))
            break
        else:
            # means get the result already
            print("iteration:  " , iteration)
            initalize_anime_data(result, int(access_animeId_list[iteration - 1]))

            # print(allAnimeDataFile)
            # print(access_animeId_list[currentAnimeId-1], currentAnimeId)
            write_all_info()
            """
            if os.path.exists(os.path.join(os.getcwd(),"anime_data", str(currentAnimeId))) == False:
                print("###################### id", currentAnimeId)
                break
            """
            iteration += 1  # the official anime id in the serve

    refresh(refresh_token)

#print(correspond_animeId_with_webId(29411))
