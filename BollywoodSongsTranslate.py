from pygoogletranslation import Translator
import pickle

translator = Translator()

BollywoodLyrics = pickle.load( open( "Datasets/BollywoodLyrics", "rb" ) )

import nltk
nltk.download('punkt')
a = []
count= 0
for x in BollywoodLyrics:
  y = x.split('\n')
  a.append([])
  for z in y:
    if z is not None:
      print(z)
      a[count] =translator.translate(z,dest='en')
  count+=1


f = open("Datasets/translated_lyrics_combined",'wb')
pickle.dump(a,f)