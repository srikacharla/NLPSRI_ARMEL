import numpy as np
import pickle

import sklearn
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
import seaborn as sns

L1 = pickle.load(open("Datasets/L1", "rb"))
L2 = pickle.load(open("Datasets/L2", "rb"))
L3 = pickle.load(open("Datasets/L3", "rb"))
L4 = pickle.load(open("Datasets/L4", "rb"))
L5 = pickle.load(open("Datasets/L5", "rb"))
L6 = pickle.load(open("Datasets/L6", "rb"))
L7 = pickle.load(open("Datasets/L7", "rb"))

L = np.concatenate((L1, L2, L3, L4, L5, L6, L7), axis=None)

CategoriesAll = np.concatenate(
    ([1] * len(L1), [2] * len(L2), [3] * len(L3), [4] * len(L4), [5] * len(L5), [6] * len(L6), [7] * len(L7)),
    axis=None)

xtrain, xtest, ytrain, ytest = train_test_split(L, CategoriesAll, train_size=0.90)

np.random.seed(2361)

model_nbCat = make_pipeline(TfidfVectorizer(), MultinomialNB())
model_nbCat.fit(xtrain, ytrain)

model_svmCat = make_pipeline(TfidfVectorizer(), SVC())
model_svmCat.fit(xtrain, ytrain)

model_rfCat = make_pipeline(TfidfVectorizer(), RandomForestClassifier())
model_rfCat.fit(xtrain, ytrain)

labels_nbCat = model_nbCat.predict(xtest)
svm_labels_nbCat = model_svmCat.predict(xtest)
labels_rfCat = model_rfCat.predict(xtest)

svmPrecisionCat = []
svmRecallCat = []
svmF1ScoreCat = []

svmPrecisionCat.append(sklearn.metrics.precision_score(ytest, svm_labels_nbCat, average='micro'))
svmRecallCat.append(sklearn.metrics.recall_score(ytest, svm_labels_nbCat, average='micro'))
svmF1ScoreCat.append(sklearn.metrics.f1_score(ytest, svm_labels_nbCat, average='macro'))

PrecisionCatNb = []
RecallCatNb = []
F1ScoreCatNb = []

PrecisionCatNb.append(sklearn.metrics.precision_score(ytest, labels_nbCat, average='micro'))
RecallCatNb.append(sklearn.metrics.recall_score(ytest, labels_nbCat, average='micro'))
F1ScoreCatNb.append(sklearn.metrics.f1_score(ytest, labels_nbCat, average='macro'))

PrecisionCatRF = []
RecallCatRF = []
F1ScoreCatRF = []

PrecisionCatRF.append(sklearn.metrics.precision_score(ytest, labels_rfCat, average='micro'))
RecallCatRF.append(sklearn.metrics.recall_score(ytest, labels_rfCat, average='micro'))
F1ScoreCatRF.append(sklearn.metrics.f1_score(ytest, labels_rfCat, average='macro'))

print("Bayes")
print("Precision")
print(PrecisionCatNb)
print("Recall")
print(RecallCatNb)
print("F1 Score")
print(F1ScoreCatNb)

print("\nSVM")
print("Precision")
print(svmPrecisionCat)
print("Recall")
print(svmRecallCat)
print("F1 Score")
print(svmF1ScoreCat)

print("\n Random Forest")
print("Precision")
print(PrecisionCatRF)
print("Recall")
print(RecallCatRF)
print("F1 Score")
print(F1ScoreCatRF)

mat = confusion_matrix(ytest, labels_rfCat)
sns.heatmap(mat.T / 100, square=True,
            xticklabels=["POP", "ROCK", "LATIN", "R&B", "EDM", "Country", "Gospel"],
            yticklabels=["POP", "ROCK", "LATIN", "R&B", "EDM", "Country", "Gospel"], cmap='viridis')
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()

mat = confusion_matrix(ytest, labels_nbCat)
sns.heatmap(mat.T / 100, square=True,
            xticklabels=["POP", "ROCK", "LATIN", "R&B", "EDM", "Country", "Gospel"],
            yticklabels=["POP", "ROCK", "LATIN", "R&B", "EDM", "Country", "Gospel"], cmap='viridis')
plt.xlabel('true label')
plt.ylabel('predicted label')

mat = confusion_matrix(ytest, svm_labels_nbCat)
sns.heatmap(mat.T / 100, square=True,
                  xticklabels=["POP", "ROCK", "LATIN", "R&B", "EDM", "Country", "Gospel"],
                  yticklabels=["POP", "ROCK", "LATIN", "R&B", "EDM", "Country", "Gospel"], cmap='viridis')
plt.xlabel('true label')
plt.ylabel('predicted label')
