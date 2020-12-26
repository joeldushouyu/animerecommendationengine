import pandas as pd
import requests



#df.loc[df.username == 'jack'].food
s = requests.get("https://www.animenewsnetwork.com/encyclopedia/anime.php?id=19743")
print(s.status_code)