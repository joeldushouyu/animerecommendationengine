from load_anime_to_html import all_shows_list
import pandas as pd

result = all_shows_list.loc[0:2]
print(result)

for index, row in all_shows_list.iterrows():
    print(row["genre"])
    if row["genre"] == "":
        print("here")
        result = result.append(row)

print(result)

result.to_json('missinggenre.json', orient='records', lines=True)