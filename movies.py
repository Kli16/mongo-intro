'''
American Movies Scraped from Wikipedia: contains American Movies by name, director, genre, year, and cast
Link: https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json
I connected to homer, created a db called movies, and created a collection
'''
from pymongo import MongoClient
import json

connection = MongoClient('homer.stuy.edu')
db = connection.liK
collection = db.movies

filename = "movies.json"
movielist = open(filename, "r")
movies = json.load(movielist)

collection.insert_many(movies)

def get_movie_by_genre(genre):
    return collection.find({'genre': genre})

def get_movie_by_title(title):
    return collection.find({'title': title})

def get_movie_by_year(year):
    return collection.find({'year': year})

def get_movie_by_year_director(year, director):
    return collection.find({'year': year, 'director': director})

def get_movie_by_year_genre(year, genre):
    return collection.find({'year': year, 'genre': genre})

def display_movies(collection):
    for i in collection:
        print i['title']

#print "-----MOVIES IN COMEDY----\n"
#display_movies(get_movie_by_genre("Comedy"))

#print "-----MOVIES IN 2015 BY ----\n"
#display_movies(get_movie_by_year_director(2015, "Rob Cohen"))

print "-----ACTION MOVIES IN 2007----\n"
display_movies(get_movie_by_year_genre(2007, "Action"))

movielist.close()
