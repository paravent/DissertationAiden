import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import linear_kernel
from pathlib import Path 



imdb_dataset = pd.read_csv('./dataset/movie_metadata.csv', low_memory=False)

#   ____        _         __                               
#  |  _ \  __ _| |_ __ _ / _|_ __ __ _ _ __ ___   ___  ___ 
#  | | | |/ _` | __/ _` | |_| '__/ _` | '_ ` _ \ / _ \/ __|
#  | |_| | (_| | || (_| |  _| | | (_| | | | | | |  __/\__ \
#  |____/ \__,_|\__\__,_|_| |_|  \__,_|_| |_| |_|\___||___/
                                                         

def find_missing_values(dataframe):
  
  missing_index = dataframe.columns.tolist() 
  missing = dataframe.isnull().sum().tolist()
  missing_df = pd.DataFrame({'Missing':missing}, index=missing_index)

  return missing_df

#if anything in dataframe is missing data, delete it
new_data_frame = imdb_dataset.dropna(axis = 0, how='all')
print(find_missing_values(new_data_frame))
print(new_data_frame.head(5)['movie_title'])
print(new_data_frame.shape)

new_data_frame['genres'] = new_data_frame['genres'].str.replace('|',' ')
new_data_frame.columns = new_data_frame.columns.str.strip()
#first we need whole words to use tfidf
new_data_frame['genres'] = new_data_frame['genres'].str.replace('Sci-Fi','SciFi')

 
filepath = Path('./dataset/out.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
new_data_frame.to_csv(filepath)

def plot_occurences(new_data_frame):
    # count the number of occurences for each genres in the data set
    counts = dict()
    for i in new_data_frame.index:
        for g in new_data_frame.loc[i,'genres'].split(' '):
            if g not in counts:
                counts[g] = 1
            else:
                counts[g] = counts[g] + 1

    plt.figure(figsize=(12,6))
    plt.bar(list(counts.keys()), counts.values(), color='b')
    plt.xticks(rotation=45)
    plt.xlabel('genres')
    plt.ylabel('Occurence')
    

plot_occurences(new_data_frame)

#    _____ __      ___ ____  _____ 
#   |_   _/ _|    |_ _|  _ \|  ___|
#    | || |_ _____| || | | | |_   
#    | ||  _|_____| || |_| |  _|  
#    |_||_|      |___|____/|_|    
                                 
# Speak about tf-idf for word item relevance within movies
# Convert a collection of raw documents to a matrix of TF-IDF features
# TF-IDF (term frequency-inverse document frequency) is a 
# statistical measure that evaluates how relevant a word is 
# to a document in a collection of documents.

# This is done by multiplying two metrics: 
# how many times a word appears in a document, 
# and the inverse document frequency of the word across a set of documents.
# We are essentially turning our words into numbers

language_vector = TfidfVectorizer(stop_words='english') #Vectoriser object
genres_matrix = language_vector.fit_transform(new_data_frame['genres']) #apply language object to genres column
print(list(enumerate(language_vector.get_feature_names())))
# First value in indices is the movie in the dataframe
# Second value is the genres
# For example the if a value was (0,17) ~ 0.91 means 'movie 0' has a genres 'scifi' and a 'tf-idf value of 0.91'
print(genres_matrix[:100])


confusion_matrix = linear_kernel(genres_matrix,genres_matrix) # create the cosine similarity matrix
print(confusion_matrix)

# the function to convert from index to title_year
def get_title_from_index(index_list):
 
  return new_data_frame.loc[index_list,'movie_title']

# the function to convert from title to index
def get_index_from_title(title):
  
  print(new_data_frame.loc[new_data_frame['movie_title'].str.contains(title)], 'not hard coded')


  #Get index of movie we're looking for to plug into similarity matrix 
  return new_data_frame.loc[new_data_frame['movie_title'].str.contains(title)].index.values[0]



def run_recommender(movie, number_to_recommend): 

    movie_index = get_index_from_title(movie) #171
    movie_list = list(enumerate(confusion_matrix[int(movie_index)]))
    similar_list = list(filter(lambda x:x[0] != int(movie_index), sorted(movie_list,key=lambda x:x[1], reverse=True)))

    print('Movies ~ '+'\033[1m'+str(movie)+'\033[91m'+'.\n')
    
    for i,s in similar_list[:number_to_recommend]: 
      print(get_title_from_index(i))



run_recommender('The Usual Suspects', 20)