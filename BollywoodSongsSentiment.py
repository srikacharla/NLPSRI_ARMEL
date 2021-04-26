import pickle
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia = SIA()
import matplotlib.pyplot as plt

BollywoodLyrics = pickle.load(open("Datasets/BollywoodLyrics","rb"))

vader_labelsBollywood = []
positiveBollywood = 0
negativeBollywood = 0
neutralBollyood = 0
for lyrics in BollywoodLyrics:
  sentiment_scores = (sia.polarity_scores(lyrics))
  if sentiment_scores['compound']>=0.05:
    vader_labelsBollywood.append(1)
    positiveBollywood+=1
  elif sentiment_scores['compound'] >-0.05 and sentiment_scores['compound'] < 0.05:
    vader_labelsBollywood.append(2)
    neutralBollyood+=1
  else:
    vader_labelsBollywood.append(0)
    negativeBollywood+=1

Columns = ["positive","neutral","negative"]
New_Colors = ['green','blue','purple','brown','teal','grey','red']
COLOR = 'black'
plt.rcParams['text.color'] = COLOR
plt.rcParams['axes.labelcolor'] = COLOR
plt.rcParams['xtick.color'] = COLOR
plt.rcParams['ytick.color'] = COLOR
plt.bar(Columns,[positiveBollywood/(positiveBollywood+negativeBollywood+neutralBollyood),neutralBollyood/(positiveBollywood+negativeBollywood+neutralBollyood),negativeBollywood/(negativeBollywood+positiveBollywood+neutralBollyood)],color = New_Colors)
plt.title('% of bollywood music and their sentiment')
plt.xlabel('')
plt.show()