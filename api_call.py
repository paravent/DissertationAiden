#! /usr/local/bin/python3

import requests 
import json
import mysql.connector
import sys
from sys import argv

username = sys.argv[1]
#Initialise mysql connection 
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='diss')
#Open connection cursor
cursor = cnx.cursor()

api_genre_path = 'genres.json'
#Receiving API call data
trending = (requests.get("https://api.themoviedb.org/3/trending/all/week?api_key=60273795ce17f499171c35b57865cfc0"))
trending_movie = (requests.get("https://api.themoviedb.org/3/trending/movie/week?api_key=60273795ce17f499171c35b57865cfc0"))
trending_tv = (requests.get("https://api.themoviedb.org/3/trending/tv/week?api_key=60273795ce17f499171c35b57865cfc0"))
trending_person = (requests.get("https://api.themoviedb.org/3/trending/person/week?api_key=60273795ce17f499171c35b57865cfc0"))


genreRequest = (requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=60273795ce17f499171c35b57865cfc0&language=en-US"))

#Parse api call to json file
def parse_json(json_file, path_to_json, api_request):
    jsonFile = open(json_file, "w")
    with open(path_to_json, 'w') as outfile:
        outfile.truncate(0)
        json.dump(api_request, outfile, indent=4, sort_keys=True)
    return 0

def find_genre_in_trending(json_file, genre_id):
    f = open(json_file)
    success_message = "Movie identified : "
    fail_message = "Incorrect title field"
    matched_media = [] 
    #return json object as dictionary
    data = json.load(f)
    #iterate over dictionary
    for i in data['results']:
        dict_to_string = json.dumps(i)
        jsonObject = json.loads(dict_to_string)
        if "genre_ids" in jsonObject:
            for i in jsonObject["genre_ids"]:
                 #print(i)
                if i == genre_id:
                    try:
                        movie_title = jsonObject["title"] 
                        matched_media.append(movie_title)
                        print(success_message, movie_title)
                    except Exception:
                        print(fail_message)
                    try:
                        movie_title = jsonObject["name"] 
                        matched_media.append(movie_title)
                        print(success_message, movie_title)
                    except Exception:
                        print(fail_message)
                    try:
                        movie_title = jsonObject["original_name"] 
                        matched_media.append(movie_title)
                        print(success_message, movie_title)
                    except Exception:
                        print(fail_message)
        else:
            print("cant find original title") 
            
    #close file
    f.close()

    return matched_media

def parse_genre_id(json_file, genre_name): 
    f = open(json_file)

    #return json object as dictionary
    data = json.load(f)
    #iterate over dict
    for i in data['genres']:
        dict_to_string = json.dumps(i)
        json_object = json.loads(dict_to_string)
        if "name" in json_object:
            if json_object["name"] == genre_name:
                genre_id = json_object["id"]
                print("Genre : ", json_object["name"], ": id:", json_object["id"])
        else:
            print("Key does not exist")
            
    #close file
    f.close()

    return genre_id
     
def split_user_genres(user_trend_genres):
    # split the text
    words = user_trend_genres.split("''")
    # for each word in the line:
    return words

def convert(lst):
    return (lst[0].split())


parse_json("all_trending.json", 'all_trending.json', trending.json())
parse_json("movie_trend.json", 'movie_trend.json', trending.json())
parse_json("tv_trend.json", 'tv_trend.json', trending.json())
parse_json("person_trend.json", 'person_trend.json', trending.json())
parse_json("genres.json", api_genre_path, genreRequest.json())
genres = parse_genre_id('genres.json', "Horror")

cursor.execute("SELECT userTrendGenre FROM users WHERE (%(username)s) IN (userUsername) ", {'username': username})
for (userUsername) in cursor:
    # print("User: {name}".format(name = userUsername))
    genres = ','.join(userUsername)
    split = split_user_genres(genres)
    convert_str = convert(split)



#Match user trending genre to its API genre ID
matched_list = []
for i in convert_str:
    parse_genre_id(api_genre_path, i)
    
    test = find_genre_in_trending('all_trending.json', parse_genre_id(api_genre_path, i))
    print(test)
    for x in test:
        
        matched_list.append(x)
    

#Remove duplicates
matched_list = list(dict.fromkeys(matched_list))

val_string = ' , '.join(matched_list)

cursor.execute("UPDATE `users` SET `userLiked` = (%(movie)s) WHERE `users`.`userID` = 1;", {'movie': val_string} )
# cursor.execute(sql, val_string)
cnx.commit()

#Close mysql connection 
cnx.close()