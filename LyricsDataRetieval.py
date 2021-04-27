import lyricsgenius
import pandas as pd
import numpy as np
import pickle

token = "Bm7Y5dWwnKvgw74jWgdNKtU1_PGwF1tHOHoRb-PA8LAgMJ06I6HGnbg0Adh_2IC0"
genius = lyricsgenius.Genius(token)

link = "Datasets\List_of_artist.csv" # I uploaded the CSV file first

DB_artist = pd.read_csv(link)

categories = np.array(DB_artist.columns.values)

C_1 = DB_artist[categories[0]].values
C_2 = DB_artist[categories[1]].values
C_3 = DB_artist[categories[2]].values
C_4 = DB_artist[categories[3]].values
C_5 = DB_artist[categories[4]].values
C_6 = DB_artist[categories[5]].values
C_7 = DB_artist[categories[6]].values

def populateLyrics(array_artist):
  saved_lyrics = []
  for n in array_artist:
    try:
        genius = lyricsgenius.Genius(token, timeout=20)
    except genius.exceptions.Timeout:
        print("Timeout occurred")
    a = genius.search_artist(n, max_songs=1, sort="title", include_features=True)
    s = a.songs
    for k in range(0,len(s)):
      lrc = s[k].to_text()
      saved_lyrics.append(lrc)
  return saved_lyrics



L1 = np.array(populateLyrics(C_1))
L2 = np.array(populateLyrics(C_2))
L3 = np.array(populateLyrics(C_3))
L4 = np.array(populateLyrics(C_4))
L5 = np.array(populateLyrics(C_5))
L6 = np.array(populateLyrics(C_6))
L7 = np.array(populateLyrics(C_7))

Lyrcs = [L1, L2, L3, L4, L5, L6, L7]


f = open("Datasets/L1",'wb')
pickle.dump(L1,f)

f = open("Datasets/L2",'wb')
pickle.dump(L2,f)

f = open("Datasets/L3",'wb')
pickle.dump(L3,f)

f = open("Datasets/L4",'wb')
pickle.dump(L4,f)

f = open("Datasets/L5",'wb')
pickle.dump(L5,f)

f = open("Datasets/L6",'wb')
pickle.dump(L6,f)

f = open("Datasets/L7",'wb')
pickle.dump(L7,f)

with open('/Datasets/lyrics_combined', 'wb') as f:
  pickle.dump(Lyrcs, f)

