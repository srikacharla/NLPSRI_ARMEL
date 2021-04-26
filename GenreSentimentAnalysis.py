import nltk
import numpy as np

nltk.download('vader_lexicon')
nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import matplotlib.pyplot as plt

sia = SIA()
import os

os.getcwd()
import pickle

LY1 = pickle.load(open("Datasets/finalLyrics1", "rb"))
LY2 = pickle.load(open("Datasets/finallyrics2", "rb"))
LY3 = pickle.load(open("Datasets/finallyrics3", "rb"))
LY4 = pickle.load(open("Datasets/finallyrics4", "rb"))
LY5 = pickle.load(open("Datasets/finallyrics5", "rb"))
LY6 = pickle.load(open("Datasets/finallyrics6", "rb"))
LY7 = pickle.load(open("Datasets/finallyrics7", "rb"))

vader_labels1 = []
positive1 = 0
negative1 = 0
neutral1 = 0
for lyrics in LY1[0]:
    sentiment_scores = (sia.polarity_scores(lyrics))
    if sentiment_scores['compound'] > 0:
        vader_labels1.append(1)
        positive1 += 1
    elif sentiment_scores['compound'] == 0:
        neutral1 += 1
        vader_labels1.append(2)
    else:
        vader_labels1.append(0)
        negative1 += 1

vader_labels2 = []
positive2 = 0
negative2 = 0
neutral2 = 0
for lyrics in LY2[0]:
    sentiment_scores = (sia.polarity_scores(lyrics))
    if sentiment_scores['compound'] > 0:
        vader_labels2.append(1)
        positive2 += 1
    elif sentiment_scores['compound'] == 0:
        neutral2 += 1
        vader_labels2.append(2)
    else:
        vader_labels2.append(0)
        negative2 += 1

vader_labels3 = []
positive3 = 0
negative3 = 0
neutral3 = 0
for lyrics in LY3[0]:
    sentiment_scores = (sia.polarity_scores(lyrics))
    if sentiment_scores['compound'] > 0:
        vader_labels3.append(1)
        positive3 += 1
    elif sentiment_scores['compound'] == 0:
        neutral3 += 1
        vader_labels3.append(2)
    else:
        vader_labels3.append(0)
        negative3 += 1

vader_labels4 = []
positive4 = 0
negative4 = 0
neutral4 = 0
for lyrics in LY4[0]:
    sentiment_scores = (sia.polarity_scores(lyrics))
    if sentiment_scores['compound'] > 0:
        vader_labels4.append(1)
        positive4 += 1
    elif sentiment_scores['compound'] == 0:
        neutral4 += 1
        vader_labels4.append(2)
    else:
        vader_labels4.append(0)
        negative4 += 1

vader_labels5 = []
positive5 = 0
negative5 = 0
neutral5 = 0
for lyrics in LY5[0]:
    sentiment_scores = (sia.polarity_scores(lyrics))
    if sentiment_scores['compound'] > 0:
        vader_labels5.append(1)
        positive5 += 1
    elif sentiment_scores['compound'] == 0:
        neutral5 += 1
        vader_labels5.append(2)
    else:
        vader_labels5.append(0)
        negative5 += 1

vader_labels6 = []
positive6 = 0
negative6 = 0
neutral6 = 0
for lyrics in LY6[0]:
    sentiment_scores = (sia.polarity_scores(lyrics))
    if sentiment_scores['compound'] > 0:
        vader_labels6.append(1)
        positive6 += 1
    elif sentiment_scores['compound'] == 0:
        neutral6 += 1
        vader_labels6.append(2)
    else:
        vader_labels6.append(0)
        negative6 += 1

vader_labels7 = []
positive7 = 0
negative7 = 0
neutral7 = 0
for lyrics in LY7[0]:
    sentiment_scores = (sia.polarity_scores(lyrics))
    if sentiment_scores['compound'] > 0:
        vader_labels7.append(1)
        positive7 += 1
    elif sentiment_scores['compound'] == 0:
        neutral7 += 1
        vader_labels7.append(2)
    else:
        vader_labels7.append(0)
        negative7 += 1


print("POP")
print("positive")
print(positive1)
print("negative")
print(negative1)
print("positivity ratio")
print(positive1/(positive1+negative1+neutral1))
print("\nROCK")
print("positive")
print(positive2)
print("negative")
print(negative2)
print("positivity ratio")
print(positive2/(positive2+negative2+neutral2))
print("\nLATIN")
print("positive")
print(positive3)
print("negative")
print(negative3)
print("positivity ratio")
print(positive3/(positive3+negative3+neutral3))
print("\nR&B")
print("positive")
print(positive4)
print("negative")
print(negative4)
print("positivity ratio")
print(positive4/(positive4+negative4+neutral4))
print("\nEDM")
print("positive")
print(positive5)
print("negative")
print(negative5)
print("positivity ratio")
print(positive5/(positive5+negative5+neutral5))
print("\nCountry")
print("positive")
print(positive6)
print("negative")
print(negative6)
print("positivity ratio")
print(positive6/(positive6+negative6+neutral6))
print("\nGospel")
print("positive")
print(positive7)
print("negative")
print(negative7)
print("positivity ratio")
print(positive7/(positive7+negative7+neutral7))



positiveFinal = []
positiveFinal.append(round(positive1/(positive1+negative1+neutral1),1))
positiveFinal.append(round(positive2/(positive2+negative2+neutral2),1))
positiveFinal.append(round(positive3/(positive3+negative3+neutral3),1))
positiveFinal.append(round(positive4/(positive4+negative4+neutral4),1))
positiveFinal.append(round(positive5/(positive5+negative5+neutral5),1))
positiveFinal.append(round(positive6/(positive6+negative6+neutral6),1))
positiveFinal.append(round(positive7/(positive7+negative7+neutral7),1))
negativeFinal = []
negativeFinal.append(round(negative1/(positive1+negative1+neutral1),1))
negativeFinal.append(round(negative2/(positive2+negative2+neutral2),1))
negativeFinal.append(round(negative3/(positive3+negative3+neutral3),1))
negativeFinal.append(round(negative4/(positive4+negative4+neutral4),1))
negativeFinal.append(round(negative5/(positive5+negative5+neutral5),1))
negativeFinal.append(round(negative6/(positive6+negative6+neutral6),1))
negativeFinal.append(round(negative7/(positive7+negative7+neutral7),1))
sentiment_final = []
for x in range(0,len(negativeFinal)):
  sentiment_final.append(positiveFinal[x])
  sentiment_final.append(negativeFinal[x])

Columns = ["POP","ROCK","LATIN","R&B","EDM","Country","Gospel"]




x = np.arange(len(Columns))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, positiveFinal, width, label='Positive')
rects2 = ax.bar(x + width/2, negativeFinal, width, label='Negative')

ax.set_ylabel('% of songs')
ax.set_title('% of songs of each genre vs Polarity')
ax.set_xticks(x)
ax.set_xticklabels(Columns)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
