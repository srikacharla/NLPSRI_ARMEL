# NLP for music lyrics analysis

Github repository: https://github.com/srikacharla/NLPSRI_ARMEL

# Project title : NLP for music lyrics analysis.

# 1. Description of project

- Through this project we aim to build and train models to classify songs into respective genres through their lyrics. We performed similarity analysis of songs of various genres over different periods. We also looked at how accurate models can be when they are trained on lyrics data and how the models perform when we throw different kinds of data at them. We also gained insight on what goes on inside a model and how obvious things about a dataset don’t actually play a significant role in the prediction process. We also performed sentiment analysis on these genres to gauge which genres had the most positive songs and what happens to existing sentiment analysis tools when we input non english data. 

- Final report + all expected output:
https://drive.google.com/file/d/1SpkxsUd5abPvv-wVoAq4NN445LPyGAce/view?usp=sharing

- The project proposal document can be found here:
 https://drive.google.com/file/d/1AkYhyl_e4zvuJhIQGskBdHTiJN4tN9eC/view?usp=sharing

# 2. Team Members
- Armel Nsinagani
- Sri Harsha Kacharla

# 3. Dependencies used

The dependencies used to execute every Python scripts are the following ones:
- Pandas (For more information, click [here](https://pandas.pydata.org/))
- NumPy (For more information, click [here](https://numpy.org/))
- Nltk (For more information, click [here](https://www.nltk.org/))
- Os (For more information, click [here](https://docs.python.org/3/library/os.html))
- Re (For more information, click [here](https://docs.python.org/3/library/re.html))
- Csv (For more information, click [here](https://docs.python.org/3/library/csv.html))
- PyTorch (For more information, click [here](https://pytorch.org/))
- Transformers (For more information, click [here](https://huggingface.co/transformers/installation.html))
- Scikit Learn (For more information, click [here](https://scikit-learn.org/stable/))
- matplotlib  (For more information, click [here](https://matplotlib.org/))
- Pickle (For more information, click [here](https://docs.python.org/3/library/pickle.html))
- lyrics genius (For more information, click [here](https://pypi.org/project/lyricsgenius/))
- json (For more information, click [here](https://docs.python.org/3/library/json.html))
- seaborn (For more information, click [here](https://seaborn.pydata.org/))
- pygoogletranslation (For more information, click [here](https://pypi.org/project/pygoogletranslation/))
- googletrans (For more information, click [here](https://pypi.org/project/googletrans/))


While some Python modules are already installed by default,some are not. 
For this reason, requirements.txt file was created to install the remaining modules. 
Missing modules must be installed before running all code.


```python
pip install -r requirements.txt
```

***requirements.txt*** is found [here](https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/requirements.txt). 

# 4. How to build project
Clone this repository using `git clone: https://github.com/srikacharla/NLPSRI_ARMEL.git 
Follow steps #5 (how to run project)


# 5. How to run project
Create a virtual environment using: `python3 -m venv env` 
Activate the virtual environment
Install all required packages using the following command:
```python
pip install -r requirements.txt
```
** Note: Make sure all working directories are in root folder.


## 5.1
Data scraping

Song lyrics were extracted using Lyrics genius database. The algorithm for extraction can be found in file (https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/DateDataRetrieval.py). Note that the files: List_of_artists.csv is required to retrieve that data. It contains the list of artists used to extract lyrics from the Genius Database. It can be found [here](https://github.com/srikacharla/NLPSRI_ARMEL/tree/main/Datasets)
To download only lyrics data, run this file(https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/LyricsDataRetieval.py) 

To download lyrics data with date information, run this file (https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/DateDataRetrieval.py) 

To download Bollywood songs, run this file (https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/BollywoodSongsRetrieval.py) 

To translate the Bollywood lyrics and save this data, run this file (https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/BollywoodSongsTranslate.py) 

*** Note: In order to process through the project without extracting the data from Database (which is time-consuming) every time, all extracted data necessary for the project has been stored and can be found in [here](https://github.com/srikacharla/NLPSRI_ARMEL/tree/main/Datasets). 

** Important note** 
In order to run any other files, you first need to have the data in the Datasets folder. 
Link to download Datasets data: https://1drv.ms/u/s!AiZZze8uHoL6kRLJxuTefXUZCZzz?e=o3eO1b

## 5.2 
Similarity within same music genre

Run file: sim_within.py, found here (https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/sim_within.py)  

Output is similarity matrices between song lyrics of the same music genres. See final report Fig. 6 for expected outcome & detailed explanation. 

## 5.3 
Similarity between different genre of music

Run file: sim_between.py, found here (https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/sim_between.py)

Output is similarity matrices between different music genres. See final report Fig. 7 for expected outcome & detailed explanation.

## 5.4 
Change of music genres similarity across time  

Run file: sim_by_years.py, found here (https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/sim_by_years.py)    

Output is plot change of similarity score between each music genre against others. It shows how the lyrical dependency between song lyrics has evolved across time. See final report Fig. 8 for expected outcome & detailed explanation.

*** Input here is similarity matrices built here: (https://github.com/srikacharla/NLPSRI_ARMEL/blob/extract_year_sim.py). Results were saved here (https://github.com/srikacharla/NLPSRI_ARMEL/blob/similarity_analysis), and were used in sim_by_years.py

## 5.5 
Training
Run file: ModelTraining.py, found here (https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/ModelTraining.py)

Output is the confusion matrix of all three models. This file also saves the RandomForest model for further use.

## 5.6 
Prediction 
Run file1: BollywoodSongPredictionFile.py found here 
(https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/BollywoodSongPredictionFile.py)
Output is the graph showing the predicted labels for bollywood songs. 

Run file2: BollywoodSongsPredictionAfterTranslation.py found here (https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/BollywoodSongsPredictionAfterTranslation.py)

Output is the graph showing the predicted labels for bollywood songs.

## 5.7 
Sentiment Analysis
Run file1: GenreSentimentAnalysis.py found here (https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/GenreSentimentAnalysis.py)

Output is the graph showing the % of songs in each genre with their respective sentiments.

Run file2: BollywoodSongsSentiment.py found here
(https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/BollywoodSongsSentiment.py)

Output is the graph showing the % of Bollywood songs in their respective sentiments.

Run file3: BollywoodSongsSentimentAnalysisAfterTranslation.py found here (https://github.com/srikacharla/NLPSRI_ARMEL/blob/main/BollywoodSongsSentimentAnalysisAfterTranslation.py)
