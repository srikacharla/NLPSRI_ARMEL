import pickle
import lyricsgenius


token = "Bm7Y5dWwnKvgw74jWgdNKtU1_PGwF1tHOHoRb-PA8LAgMJ06I6HGnbg0Adh_2IC0"

Bollywoodartist = []
BollywoodSongs= []

BollywoodLyrics = pickle.load(open("NLPproject/BollywoodLyrics","rb"))
genius = lyricsgenius.Genius(token, timeout=9999)
BollywoodArtists = ["Arijit Singh","Atif Aslam","Sonu Nigam","Shreya Ghoshal","A.R. Rahman"]
for x in BollywoodArtists:
  Bollywoodartist.append(genius.search_artist(x, max_songs=50, sort="release_date", include_features=True))
for x in Bollywoodartist:
  BollywoodSongs.append(x.songs)
  for y in x.songs:
    BollywoodSongs.append(y.songs)

BollywoodSongs = []
for x in Bollywoodartist:
  for y in x.songs:
    BollywoodSongs.append(y)

for k in range(0,len(BollywoodSongs)):
  BollywoodLyrics.append(BollywoodSongs[k].to_text())

f = open("Datasets/BollywoodLyrics",'wb')
pickle.dump(BollywoodLyrics,f)
