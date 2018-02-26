from pymongo import MongoClient

connection = MongoClient('homer.stuy.edu')
db = connection.test
collection = db.restaurants

#All restaurants in a specified borough.
def get_borough(borough):
    return collection.find( {'borough': borough} )

#All restaurants in a specified zip code.
def get_zipcode(zipcode):
    return collection.find( {'address.zipcode': zipcode} )
#All restaurants in a specified zip code and with a specified grade.
def get_zip_grade(zipcode, grade):
    return collection.find( {'address.zipcode': zipcode, 'grades.grade': grade} )

#All restaurants in a specified zip code with a score below a specified threshold.
def get_zip_score(zipcode, score):
    return collection.find( {'address.zipcode': zipcode, 'grades.score': {'$lt': score} } )

#Something more clever.
def get_zip_cuisine(zipcode, cuisine):
    return collection.find({'address.zipcode': zipcode, 'cuisine': cuisine})

def display_restaurants(collection):
    for i in collection:
        print i['name']

print "-----RESTAURANTS IN QUEENS-----\n"
display_restaurants(get_borough("Queens"))

print "-----RESTAURANTS IN 11101----\n"
display_restaurants(get_zipcode("11101"))

print "-----RESTAURANTS IN 11101 WITH GRADE A----\n"
display_restaurants(get_zip_grade("11101", "A"))

print "-----RESTAURANTS IN 11101 WITH SCORE LOWER THAN 7----\n"
display_restaurants(get_zip_score("11101", 7))

print "-----RESTAURANTS IN 11101 WITH CHINESE CUISINE----\n"
display_restaurants(get_zip_cuisine('11101','Chinese'))
