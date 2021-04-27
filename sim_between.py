import pickle
import nltk
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
nltk.download('stopwords')

# ------------------------------------------------------| Functions
# Function 1: similarity matrix of n-array
def returnSimilarityMatrix(doc,bit):
    '''
    :param doc: n-by-1 Array where each item is lyrics of 1 song
    :param bit: Enter 1 (english) or 0 (spanish)
    :return: n-by-n array with cosine similarity of each pair
    '''
    if bit == 1:
        stopWords = stopwords.words('english')
    else:
        stopWords = stopwords.words('spanish')
    vect = TfidfVectorizer(min_df=1, stop_words = stopWords)
    tfidf = vect.fit_transform(doc)
    pair_similarity = sklearn.metrics.pairwise.cosine_similarity(tfidf)
    return pair_similarity

# Function 2: combine all songs of genre
def combineSongs(L):
    '''
    :param L: n-by-1 Array where each item is lyrics of 1 song
    :return: string with all combined song lyrics
    '''
    s = L[0]
    for i in range(1,len(L)):
        s += L[i]
    return s

# ------------------------------------------------------| Loading data
# Downloading the Lyrics - only
L1 = pickle.load( open( "NLP_project/L1", "rb" ) )
L2 = pickle.load( open( "NLP_project/L2", "rb" ) )
L3 = pickle.load( open( "NLP_project/L3", "rb" ) )
L4 = pickle.load( open( "NLP_project/L4", "rb" ) )
L5 = pickle.load( open( "NLP_project/L5", "rb" ) )
L6 = pickle.load( open( "NLP_project/L6", "rb" ) )
L7 = pickle.load( open( "NLP_project/L7", "rb" ) )

# ------------------------------------------------------| Analysis
# --------------- | Similarity between music genres
# Combining all songs in genre
L1_combined = combineSongs(L1)
L2_combined = combineSongs(L2)
L3_combined = combineSongs(L3)
L4_combined = combineSongs(L4)
L5_combined = combineSongs(L5)
L6_combined = combineSongs(L6)
L7_combined = combineSongs(L7)
# Create dictionary with genre in column
# 1: With Latin
all_songs = [L1_combined,
             L2_combined,
             L3_combined,
             L4_combined,
             L5_combined,
             L6_combined,
             L7_combined]
# 1: Without Latin
all_songs_2 = [L1_combined,
               L2_combined,
               L4_combined,
               L5_combined,
               L6_combined,
               L7_combined]

sim_all = returnSimilarityMatrix(all_songs,1)
sim_all_ = returnSimilarityMatrix(all_songs_2,1)

# Plotting
# All
plt.figure(8)
x_axis = [0,1,2,3,4,5,6]
plt.imshow(sim_all)
my_yticks = ['Pop','Latin','Rock','R&B/Hip Hop','EDM/Electro','Country','Christian/Gospel']
my_xticks = ['Pop','Latin','Rock','R&B/HH','EDM','Country','Christ.']
plt.xticks(x_axis, my_xticks)
plt.yticks(x_axis, my_yticks)
plt.grid(False)
plt.set_cmap('viridis')
plt.colorbar(orientation='vertical')
plt.clim(0, 1)
plt.title('Cosine similarity between categories')
plt.show()

# Without Latin
plt.figure(9)
x_axis = [0,1,2,3,4,5]
plt.imshow(sim_all_)
my_yticks = ['Pop','Rock','R&B/Hip Hop','EDM/Electro','Country','Christian/Gospel']
my_xticks = ['Pop','Rock','R&B/HH','EDM','Country','Christ.']
plt.xticks(x_axis, my_xticks)
plt.yticks(x_axis, my_yticks)
plt.grid(False)
plt.set_cmap('viridis')
plt.colorbar(orientation='vertical')
plt.clim(0, 1)
plt.title('Cosine similarity between categories - without Latin')
plt.show()

