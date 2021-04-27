import numpy as np
import pickle
import nltk
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
nltk.download('stopwords')

'''
In this file, we get the similarity matrix between genres, after songs lyrics have been grouped in
5 groups: <2000, 2000 - 2005, 2005 - 2010, 2010 - 2015, >2015

Input: extracting lyrics + dates
Output: 5 similarity matrix | 1 per year group
Function: Output used in sim_by_years.py

'''

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

# Function 3: Get release dates
def extractDate(stack):
    '''
    :param stack: n-by-2 Array with songs lyrics & dates
    :return: n-by-1 array with song release dates
    '''
    date_extracted = []
    for i in range(0,len(stack[1])):
        d = stack[1][i][:4]
        date_extracted.append(int(d))
    return date_extracted

#----------------- Load lyrics + Dates
Lyr_1 = pickle.load( open( "finallyrics/finalLyrics1", "rb" ) )
Lyr_2 = pickle.load( open( "finallyrics/finalLyrics2", "rb" ) )
Lyr_3 = pickle.load( open( "finallyrics/finalLyrics3", "rb" ) )
Lyr_4 = pickle.load( open( "finallyrics/finalLyrics4", "rb" ) )
Lyr_5 = pickle.load( open( "finallyrics/finalLyrics5", "rb" ) )
Lyr_6 = pickle.load( open( "finallyrics/finalLyrics6", "rb" ) )
Lyr_7 = pickle.load( open( "finallyrics/finalLyrics7", "rb" ) )


#-----------------------------/ Computation
# Getting the dates
d_1 = extractDate(Lyr_1)
d_2 = extractDate(Lyr_2)
d_3 = extractDate(Lyr_3)
d_4 = extractDate(Lyr_4)
d_5 = extractDate(Lyr_5)
d_6 = extractDate(Lyr_6)
d_7 = extractDate(Lyr_7)

# ----------------------------/ Get & save similarity matrix by years
# < 2000
L1 = np.array(Lyr_1[0])[np.array(d_1) < 2000]
L2 = np.array(Lyr_2[0])[np.array(d_2) < 2000]
L3 = np.array(Lyr_3[0])[np.array(d_3) < 2000]
L4 = np.array(Lyr_4[0])[np.array(d_4) < 2000]
L5 = np.array(Lyr_5[0])[np.array(d_5) < 2000]
L6 = np.array(Lyr_6[0])[np.array(d_6) < 2000]
L7 = np.array(Lyr_7[0])[np.array(d_7) < 2000]

L1_combined = combineSongs(L1.tolist())
L2_combined = combineSongs(L2.tolist())
L3_combined = combineSongs(L3.tolist())
L4_combined = combineSongs(L4.tolist())
L5_combined = combineSongs(L5.tolist())
L6_combined = combineSongs(L6.tolist())
L7_combined = combineSongs(L7.tolist())

all_songs = [L1_combined,
                L2_combined,
                L4_combined,
                L5_combined,
                L6_combined,
                L7_combined]

sim_1 = returnSimilarityMatrix(all_songs,1)

# 2000 - 2005
L1 = np.array(Lyr_1[0])[(np.array(d_1) > 2000) & (np.array(d_1) < 2005)]
L2 = np.array(Lyr_2[0])[(np.array(d_1) > 2000) & (np.array(d_1) < 2005)]
L3 = np.array(Lyr_3[0])[(np.array(d_1) > 2000) & (np.array(d_1) < 2005)]
L4 = np.array(Lyr_4[0])[(np.array(d_1) > 2000) & (np.array(d_1) < 2005)]
L5 = np.array(Lyr_5[0])[(np.array(d_1) > 2000) & (np.array(d_1) < 2005)]
L6 = np.array(Lyr_6[0])[(np.array(d_1) > 2000) & (np.array(d_1) < 2005)]
L7 = np.array(Lyr_7[0])[(np.array(d_1) > 2000) & (np.array(d_1) < 2005)]

L1_combined = combineSongs(L1.tolist())
L2_combined = combineSongs(L2.tolist())
L3_combined = combineSongs(L3.tolist())
L4_combined = combineSongs(L4.tolist())
L5_combined = combineSongs(L5.tolist())
L6_combined = combineSongs(L6.tolist())
L7_combined = combineSongs(L7.tolist())

all_songs = [L1_combined,
                L2_combined,
                L4_combined,
                L5_combined,
                L6_combined,
                L7_combined]

sim_2 = returnSimilarityMatrix(all_songs,1)


# 2005 - 2010
L1 = np.array(Lyr_1[0])[(np.array(d_1) > 2005) & (np.array(d_1) < 2010)]
L2 = np.array(Lyr_2[0])[(np.array(d_1) > 2005) & (np.array(d_1) < 2010)]
L3 = np.array(Lyr_3[0])[(np.array(d_1) > 2005) & (np.array(d_1) < 2010)]
L4 = np.array(Lyr_4[0])[(np.array(d_1) > 2005) & (np.array(d_1) < 2010)]
L5 = np.array(Lyr_5[0])[(np.array(d_1) > 2005) & (np.array(d_1) < 2010)]
L6 = np.array(Lyr_6[0])[(np.array(d_1) > 2005) & (np.array(d_1) < 2010)]
L7 = np.array(Lyr_7[0])[(np.array(d_1) > 2005) & (np.array(d_1) < 2010)]

L1_combined = combineSongs(L1.tolist())
L2_combined = combineSongs(L2.tolist())
L3_combined = combineSongs(L3.tolist())
L4_combined = combineSongs(L4.tolist())
L5_combined = combineSongs(L5.tolist())
L6_combined = combineSongs(L6.tolist())
L7_combined = combineSongs(L7.tolist())

all_songs = [L1_combined,
                L2_combined,
                L4_combined,
                L5_combined,
                L6_combined,
                L7_combined]

sim_3 = returnSimilarityMatrix(all_songs,1)


# 2010 - 2015
L1 = np.array(Lyr_1[0])[(np.array(d_1) > 2010) & (np.array(d_1) < 2015)]
L2 = np.array(Lyr_2[0])[(np.array(d_1) > 2010) & (np.array(d_1) < 2015)]
L3 = np.array(Lyr_3[0])[(np.array(d_1) > 2010) & (np.array(d_1) < 2015)]
L4 = np.array(Lyr_4[0])[(np.array(d_1) > 2010) & (np.array(d_1) < 2015)]
L5 = np.array(Lyr_5[0])[(np.array(d_1) > 2010) & (np.array(d_1) < 2015)]
L6 = np.array(Lyr_6[0])[(np.array(d_1) > 2010) & (np.array(d_1) < 2015)]
L7 = np.array(Lyr_7[0])[(np.array(d_1) > 2010) & (np.array(d_1) < 2015)]

L1_combined = combineSongs(L1.tolist())
L2_combined = combineSongs(L2.tolist())
L3_combined = combineSongs(L3.tolist())
L4_combined = combineSongs(L4.tolist())
L5_combined = combineSongs(L5.tolist())
L6_combined = combineSongs(L6.tolist())
L7_combined = combineSongs(L7.tolist())

all_songs = [L1_combined,
                L2_combined,
                L4_combined,
                L5_combined,
                L6_combined,
                L7_combined]

sim_4 = returnSimilarityMatrix(all_songs,1)

# > 2015
L1 = np.array(Lyr_1[0])[np.array(d_1) > 2015]
L2 = np.array(Lyr_2[0])[np.array(d_2) > 2015]
L3 = np.array(Lyr_3[0])[np.array(d_3) > 2015]
L4 = np.array(Lyr_4[0])[np.array(d_4) > 2015]
L5 = np.array(Lyr_5[0])[np.array(d_5) > 2015]
L6 = np.array(Lyr_6[0])[np.array(d_6) > 2015]
L7 = np.array(Lyr_7[0])[np.array(d_7) > 2015]

L1_combined = combineSongs(L1.tolist())
L2_combined = combineSongs(L2.tolist())
L3_combined = combineSongs(L3.tolist())
L4_combined = combineSongs(L4.tolist())
L5_combined = combineSongs(L5.tolist())
L6_combined = combineSongs(L6.tolist())
L7_combined = combineSongs(L7.tolist())

all_songs = [L1_combined,
                L2_combined,
                L4_combined,
                L5_combined,
                L6_combined,
                L7_combined]

sim_5 = returnSimilarityMatrix(all_songs,1)











