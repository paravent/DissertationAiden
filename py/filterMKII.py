from ast import NodeVisitor
from zlib import DEF_BUF_SIZE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import mysql
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import linear_kernel
from pathlib import Path 
import sys
import time
from sys import argv

movie_list = sys.argv[1]
print(movie_list)
time.sleep(1)
movie_list = movie_list.split(",")

print(movie_list)
#Initialise mysql connection 
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='diss')
#Open connection cursor
cursor = cnx.cursor()

#   ___ _ _ _             __  __ _  _____ ___ 
#  | __(_) | |_ ___ _ _  |  \/  | |/ /_ _|_ _|
#  | _|| | |  _/ -_) '_| | |\/| | ' < | | | | 
#  |_| |_|_|\__\___|_|   |_|  |_|_|\_\___|___|

with open('py/outfile.txt', 'w') as f:
  print('Movie recommender', file=f)

df_collection = {}
df_list = []
#imdb_dataset = pd.read_csv('./dataset/movie_metadata.csv', low_memory=False)

imdb_dataset1 = pd.read_csv('dataset/split_csv/IMDb movies-1.csv', low_memory=False)
df_list.append(imdb_dataset1)
imdb_dataset2 = pd.read_csv('dataset/split_csv/IMDb movies-2.csv', low_memory=False)
df_list.append(imdb_dataset2)
imdb_dataset3 = pd.read_csv('dataset/split_csv/IMDb movies-3.csv', low_memory=False)
df_list.append(imdb_dataset3)
imdb_dataset4 = pd.read_csv('dataset/split_csv/IMDb movies-4.csv', low_memory=False)
df_list.append(imdb_dataset4)
imdb_dataset5 = pd.read_csv('dataset/split_csv/IMDb movies-5.csv', low_memory=False)
df_list.append(imdb_dataset5)
imdb_dataset6 = pd.read_csv('dataset/split_csv/IMDb movies-6.csv', low_memory=False)
df_list.append(imdb_dataset6)
imdb_dataset7 = pd.read_csv('dataset/split_csv/IMDb movies-7.csv', low_memory=False)
df_list.append(imdb_dataset7)
imdb_dataset8 = pd.read_csv('dataset/split_csv/IMDb movies-8.csv', low_memory=False)
df_list.append(imdb_dataset8)
imdb_dataset9 = pd.read_csv('dataset/split_csv/IMDb movies-9.csv', low_memory=False)
df_list.append(imdb_dataset9)
imdb_dataset10 = pd.read_csv('dataset/split_csv/IMDb movies-10.csv', low_memory=False)
df_list.append(imdb_dataset10)
imdb_dataset11 = pd.read_csv('dataset/split_csv/IMDb movies-11.csv', low_memory=False)
df_list.append(imdb_dataset11)
imdb_dataset12 = pd.read_csv('dataset/split_csv/IMDb movies-12.csv', low_memory=False)
df_list.append(imdb_dataset12)
imdb_dataset13 = pd.read_csv('dataset/split_csv/IMDb movies-13.csv', low_memory=False)
df_list.append(imdb_dataset13)
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


for i in range(len(df_list)):
  print(df_list[i])
  find_missing_values(df_list[i])

var_holder = {}
 
for i in range(10):
    var_holder['my_var_' + str(i)] = "iterationNumber=="+str(i)
 
locals().update(var_holder)
 
print(my_var_0)


new_frame_list = []


    
# plot_occurences(new_data_frame)

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

# language_vector = TfidfVectorizer(stop_words='english') #Vectoriser object
# genres_matrix = language_vector.fit_transform(new_data_frame['genre']) #apply language object to genres column
# print(list(enumerate(language_vector.get_feature_names())))
# # First value in indices is the movie in the dataframe
# # Second value is the genres
# # For example the if a value was (0,17) ~ 0.91 means 'movie 0' has a genres 'scifi' and a 'tf-idf value of 0.91'
# print(genres_matrix[:100])


# confusion_matrix = linear_kernel(genres_matrix,genres_matrix) # create the cosine similarity matrix
# print(confusion_matrix)

# the function to convert from index to title_year
def get_title_from_index(index_list, dataframe):
 
  return dataframe.loc[index_list,'title']

# the function to convert from title to index
def get_index_from_title(title, dataframe):
  
  print(dataframe.loc[dataframe['title'].str.contains(title)], 'not hard coded')


  #Get index of movie we're looking for to plug into similarity matrix 
  return dataframe.loc[dataframe['title'].str.contains(title)].index.values[0]



def run_recommender(movie, number_to_recommend, dataframe, confusion_matrix): 

    movie_index = get_index_from_title(movie, dataframe) #171
    movie_list = list(enumerate(confusion_matrix[int(movie_index)]))
    similar_list = list(filter(lambda x:x[0] != int(movie_index), sorted(movie_list,key=lambda x:x[1], reverse=True)))

    print('Movies ~ '+'\033[1m'+str(movie)+'\033[91m'+'.\n')
    
    with open('py/outfile.txt', 'a') as f:
      print(movie, file=f)
      for i,s in similar_list[:number_to_recommend]: 
        print(get_title_from_index(i, dataframe))
        print('       ', get_title_from_index(i, dataframe), file=f)
      

def send_it(movie):
  for i in range(len(df_list)):
    try:
      df_list[i].drop(df_list[i][df_list[i]['year'].astype(int) < 1970].index, inplace = True)
    except ValueError:
      print('')
    try:
      df_list[i].drop(df_list[i][df_list[i]['language'].astype(str) != 'English'].index, inplace = True ) 
    except ValueError:
      continue
    # df_list[i].drop(df_list[i][df_list[i]['language'].astype(str) != 'English'].index, inplace = True)
    
    # indexNames = df_list[i][(df_list[i]['language'] != 'English')].index
    # df_list[i].drop(indexNames , inplace=True)
    # dfgroup=df_list[i].groupby(['language']).describe()
  
    # try:
    #   df_list[i].drop(df_list[i][df_list[i]['language'] != 'English'].index, inplace = True)
    # except ValueError:
    #   continue


    new_frame_list.append(df_list[i].dropna(axis = 0, how='all'))
    #print(new_frame_list[i].head(5)['title'])
    #print(new_frame_list[i].shape)

    #print(find_missing_values(new_frame_list[i]))
    #print(len(new_frame_list), "you are here---------------------------------")
    new_frame_list[i]['genre'] = new_frame_list[i]['genre'].str.replace('|','')
    new_frame_list[i].columns = new_frame_list[i].columns.str.strip()
    new_frame_list[i]['genre'] = new_frame_list[i]['genre'].str.replace('Sci-Fi', 'SciFi')
    language_vector = TfidfVectorizer(stop_words='english') #Vectoriser object
    genres_matrix = language_vector.fit_transform(new_frame_list[i]['genre']) #apply language object to genres column
    #print(list(enumerate(language_vector.get_feature_names())))
    # First value in indices is the movie in the dataframe
    # Second value is the genres
    # For example the if a value was (0,17) ~ 0.91 means 'movie 0' has a genres 'scifi' and a 'tf-idf value of 0.91'
    #print(genres_matrix[:100], "call number--------------------------------------- ", i)
    confusion_matrix = linear_kernel(genres_matrix,genres_matrix) # create the cosine similarity matrix
    try:
      run_recommender(movie, 15, new_frame_list[i], confusion_matrix)
    except: 
      IndexError: print("Movie not found")

send_it('The Nun')
send_it('Hot Fuzz')
send_it('Shaun of the Dead')
send_it('Deadpool')
send_it('Avengers: Endgame')
send_it('The Conjuring 2')
send_it('Before I Wake')
send_it('Scott Pilgrim vs. the World')
send_it('Shrek')
send_it('Cars')
for i in movie_list:
  print(movie_list)



