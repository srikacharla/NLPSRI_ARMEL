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
# --------------- | Similarity within music genres

# Get similarity score
sim_within_L1 = returnSimilarityMatrix(L1,1)
sim_within_L2 = returnSimilarityMatrix(L2,1)
sim_within_L3 = returnSimilarityMatrix(L3,0)
sim_within_L4 = returnSimilarityMatrix(L4,1)
sim_within_L5 = returnSimilarityMatrix(L5,1)
sim_within_L6 = returnSimilarityMatrix(L6,1)
sim_within_L7 = returnSimilarityMatrix(L7,1)

# Plotting
# 1: Pop
plt.figure(1)
plt.imshow(sim_within_L1)
plt.grid(False)
plt.set_cmap('viridis')
plt.colorbar(orientation='vertical')
plt.clim(0, 1)
plt.title('Pop')
plt.xlabel('')
plt.ylabel('')
plt.show()

# 2: Pop
plt.figure(2)
plt.imshow(sim_within_L2)
plt.grid(False)
plt.set_cmap('viridis')
plt.colorbar(orientation='vertical')
plt.clim(0, 1)
plt.title('Rock')
plt.xlabel('')
plt.ylabel('')
plt.show()

# 3: Latin
plt.figure(3)
plt.imshow(sim_within_L3)
plt.grid(False)
plt.set_cmap('viridis')
plt.colorbar(orientation='vertical')
plt.clim(0, 1)
plt.title('Latin')
plt.xlabel('')
plt.ylabel('')
plt.show()

# 4: R&B/Hip Hop
plt.figure(4)
plt.imshow(sim_within_L4)
plt.grid(False)
plt.set_cmap('viridis')
plt.colorbar(orientation='vertical')
plt.clim(0, 1)
plt.title('R&B/Hip Hop')
plt.xlabel('')
plt.ylabel('')
plt.show()

# 5: EDM/Electro
plt.figure(5)
plt.imshow(sim_within_L5)
plt.grid(False)
plt.set_cmap('viridis')
plt.colorbar(orientation='vertical')
plt.clim(0, 1)
plt.title('EDM/Electro')
plt.xlabel('')
plt.ylabel('')
plt.show()

# 6: Country
plt.figure(6)
plt.imshow(sim_within_L6)
plt.grid(False)
plt.set_cmap('viridis')
plt.colorbar(orientation='vertical')
plt.clim(0, 1)
plt.title('Country')
plt.xlabel('')
plt.ylabel('')
plt.show()

# 7: Christian/Gospel
plt.figure(7)
plt.imshow(sim_within_L7)
plt.grid(False)
plt.set_cmap('viridis')
plt.colorbar(orientation='vertical')
plt.clim(0, 1)
plt.title('Christian/Gospel')
plt.xlabel('')
plt.ylabel('')
plt.show()
