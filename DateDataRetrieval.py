import json
import os
import re

import lyricsgenius
import numpy as np
import pandas as pd
import pickle


link = "Datasets\List_of_artist.csv"

DB_artist = pd.read_csv(link)

categories = np.array(DB_artist.columns.values)

C_1 = DB_artist[categories[0]].values
C_2 = DB_artist[categories[1]].values
C_3 = DB_artist[categories[2]].values
C_4 = DB_artist[categories[3]].values
C_5 = DB_artist[categories[4]].values
C_6 = DB_artist[categories[5]].values
C_7 = DB_artist[categories[6]].values

token = "Bm7Y5dWwnKvgw74jWgdNKtU1_PGwF1tHOHoRb-PA8LAgMJ06I6HGnbg0Adh_2IC0"
genius = lyricsgenius.Genius(token)

def populateLyrics(array_artist):
  saved_lyrics = []
  saved_years = []
  for n in array_artist:
    try:
        genius = lyricsgenius.Genius(token, timeout=9999)
    except genius.exceptions.Timeout:
        print("Timeout occurred")
    a = genius.search_artist(n, max_songs=50, sort="title", include_features=True)
    s = a.songs
    for k in range(0,len(s)):
      lrc = s[k].to_text()
      import os
      os.getcwd()
      if s[k].title != '.':
        s[k].save_lyrics()
        file = "lyrics_"+re.sub('[\W_]+', '', str(s[k].primary_artist.name).lower())+"_"+re.sub('[\W_]+', '', str(s[k].title).lower())+".json"
        try:
          data = json.load(open(file,encoding="utf8"))
          date = data['release_date']
          saved_years.append(date)
          saved_lyrics.append(lrc)
          dir = "C:/Users/srika/PycharmProjects/pythonProject3"
          for f in os.listdir(dir):
            if ".json" in f:
              os.remove(os.path.join(dir, f))
        except Exception:
            print(file)
  return saved_years,saved_lyrics


years1 , lyrics1 = populateLyrics(C_1)
years2 , lyrics2 = populateLyrics(C_2)
years3 , lyrics3 = populateLyrics(C_3)
years4 , lyrics4 = populateLyrics(C_4)
years5 , lyrics5 = populateLyrics(C_5)
years6 , lyrics6 = populateLyrics(C_6)
years7 , lyrics7 = populateLyrics(C_7)

finalYears = []
finalLyrics = []
for i in range(0,len(years1)):
  if years1[i] is not None:
    finalYears.append(years1[i])
    finalLyrics.append(lyrics1[i])
finalLyrics2 = np.array(finalLyrics)
finalYears2 = np.array(finalYears)
os.getcwd()
f = open("Datasets/finalLyrics1",'wb')
pickle.dump([finalLyrics2,finalYears2],f)

finalYears = []
finalLyrics = []
for i in range(0,len(years2)):
  if years2[i] is not None:
    finalYears.append(years2[i])
    finalLyrics.append(lyrics2[i])
finalLyrics2 = np.array(finalLyrics)
finalYears2 = np.array(finalYears)
os.getcwd()
f = open("Datasets/finalLyrics2",'wb')
pickle.dump([finalLyrics2,finalYears2],f)

finalYears = []
finalLyrics = []
for i in range(0,len(years3)):
  if years3[i] is not None:
    finalYears.append(years3[i])
    finalLyrics.append(lyrics3[i])
finalLyrics2 = np.array(finalLyrics)
finalYears2 = np.array(finalYears)
os.getcwd()
f = open("Datasets/finalLyrics3",'wb')
pickle.dump([finalLyrics2,finalYears2],f)
finalYears = []
finalLyrics = []
for i in range(0,len(years4)):
  if years4[i] is not None:
    finalYears.append(years4[i])
    finalLyrics.append(lyrics4[i])

finalLyrics2 = np.array(finalLyrics)
finalYears2 = np.array(finalYears)
os.getcwd()
f = open("Datasets/finalLyrics4",'wb')
pickle.dump([finalLyrics2,finalYears2],f)

finalYears = []
finalLyrics = []
for i in range(0,len(years5)):
  if years5[i] is not None:
    finalYears.append(years5[i])
    finalLyrics.append(lyrics5[i])
finalLyrics2 = np.array(finalLyrics)
finalYears2 = np.array(finalYears)
os.getcwd()
f = open("Datasets/finalLyrics5",'wb')
pickle.dump([finalLyrics2,finalYears2],f)

finalYears = []
finalLyrics = []
for i in range(0,len(years6)):
  if years6[i] is not None:
    finalYears.append(years6[i])
    finalLyrics.append(lyrics6[i])
finalLyrics2 = np.array(finalLyrics)
finalYears2 = np.array(finalYears)
os.getcwd()
f = open("Datasets/finalLyrics6",'wb')
pickle.dump([finalLyrics2,finalYears2],f)

finalYears = []
finalLyrics = []
for i in range(0,len(years7)):
  if years7[i] is not None:
    finalYears.append(years7[i])
    finalLyrics.append(lyrics7[i])
finalLyrics2 = np.array(finalLyrics)
finalYears2 = np.array(finalYears)
os.getcwd()
f = open("Datasets/finalLyrics7",'wb')
pickle.dump([finalLyrics2,finalYears2],f)