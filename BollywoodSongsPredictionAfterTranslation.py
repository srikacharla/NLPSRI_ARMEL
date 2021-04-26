import pickle
from matplotlib import pyplot as plt
BollywoodLyrics = pickle.load(open("Datasets/translated_lyrics_combined","rb"))

model_rfAll = pickle.load(open("Datasets/RFModel","rb"))

labelBollywood = model_rfAll.predict(BollywoodLyrics)
count1Bollywood = 0
count2Bollywood = 0
count3Bollywood = 0
count4Bollywood = 0
count5Bollywood = 0
count6Bollywood = 0
count7Bollywood = 0
for x in labelBollywood:
  if x == 1:
    count1Bollywood+=1
  if x == 2:
    count2Bollywood+=1
  if x == 3:
    count3Bollywood+=1
  if x == 4:
    count4Bollywood+=1
  if x == 5:
    count5Bollywood+=1
  if x == 6:
    count6Bollywood+=1
  if x == 7:
    count7Bollywood+=1

print("POP")
print(count1Bollywood/len(BollywoodLyrics))
print("\nROCK")
print(count2Bollywood/len(BollywoodLyrics))
print("\nLATIN")
print(count3Bollywood/len(BollywoodLyrics))
print("\nR&B")
print(count4Bollywood/len(BollywoodLyrics))
print("\nEDM")
print(count5Bollywood/len(BollywoodLyrics))
print("\nCountry")
print(count6Bollywood/len(BollywoodLyrics))
print("\nGospel")
print(count7Bollywood/len(BollywoodLyrics))


Columns = ["POP","ROCK","LATIN","R&B","EDM","Country","Gospel"]
New_Colors = ['green','blue','purple','brown','teal','grey','red']
COLOR = 'black'
plt.rcParams['text.color'] = COLOR
plt.rcParams['axes.labelcolor'] = COLOR
plt.rcParams['xtick.color'] = COLOR
plt.rcParams['ytick.color'] = COLOR
plt.bar(Columns,[count1Bollywood/len(BollywoodLyrics),count2Bollywood/len(BollywoodLyrics),count3Bollywood/len(BollywoodLyrics),count4Bollywood/len(BollywoodLyrics),count5Bollywood/len(BollywoodLyrics),count6Bollywood/len(BollywoodLyrics),count7Bollywood/len(BollywoodLyrics)],color = New_Colors)
plt.title('Bollywood Music similarity with different genres')
plt.xlabel('Genre')
plt.ylabel('Similarity')
plt.show()